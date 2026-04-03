from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

from .utils import PipelineError, ensure_binary, ensure_dir, probe_audio_duration, run_command


def diarize_audio(
    transcript_words_json: Path,
    audio_wav: Path,
    stage_dir: Path,
    config: Dict[str, Any],
    logger: logging.Logger,
) -> Tuple[Path, Path, Path]:
    ensure_binary("ffmpeg")
    ensure_dir(stage_dir)

    if not transcript_words_json.exists():
        raise PipelineError(f"Transcript words JSON missing: {transcript_words_json}")
    words = json.loads(transcript_words_json.read_text(encoding="utf-8"))
    if not isinstance(words, list) or not words:
        raise PipelineError("Transcript words JSON is empty/invalid")

    gap = float(config.get("diarize", {}).get("speaker_change_gap_sec", 0.8))
    segments = _build_turn_segments(words, max_gap=gap)

    diarization_json = stage_dir / "diarization.json"
    diarization_json.write_text(json.dumps(segments, indent=2), encoding="utf-8")

    speaker_a_wav = stage_dir / "speaker_a.wav"
    speaker_b_wav = stage_dir / "speaker_b.wav"
    _render_speaker_masked_wav(audio_wav, speaker_a_wav, _segments_for(segments, "HOST_A"), logger)
    _render_speaker_masked_wav(audio_wav, speaker_b_wav, _segments_for(segments, "HOST_B"), logger)

    for p in (diarization_json, speaker_a_wav, speaker_b_wav):
        if not p.exists() or p.stat().st_size <= 0:
            raise PipelineError(f"Diarization stage output missing/empty: {p}")

    a_time = sum(max(0.0, s[1] - s[0]) for s in _segments_for(segments, "HOST_A"))
    b_time = sum(max(0.0, s[1] - s[0]) for s in _segments_for(segments, "HOST_B"))
    logger.info(
        "Diarization complete: segments=%d HOST_A=%.2fs HOST_B=%.2fs",
        len(segments),
        a_time,
        b_time,
    )
    return diarization_json, speaker_a_wav, speaker_b_wav


def _build_turn_segments(words: Sequence[Dict[str, Any]], max_gap: float) -> List[Dict[str, Any]]:
    parsed: List[Tuple[float, float]] = []
    for w in words:
        ws = float(w.get("start", 0.0))
        we = float(w.get("end", 0.0))
        if we > ws:
            parsed.append((ws, we))
    if not parsed:
        raise PipelineError("No valid timed words for diarization")
    parsed.sort(key=lambda x: x[0])

    turns: List[Tuple[float, float]] = []
    cur_start, cur_end = parsed[0]
    for ws, we in parsed[1:]:
        if ws - cur_end > max_gap:
            turns.append((cur_start, cur_end))
            cur_start, cur_end = ws, we
        else:
            cur_end = max(cur_end, we)
    turns.append((cur_start, cur_end))

    out: List[Dict[str, Any]] = []
    speaker = "HOST_A"
    for s, e in turns:
        out.append({"speaker": speaker, "start": round(max(0.0, s), 3), "end": round(max(s, e), 3)})
        speaker = "HOST_B" if speaker == "HOST_A" else "HOST_A"
    return out


def _segments_for(segments: Sequence[Dict[str, Any]], speaker: str) -> List[Tuple[float, float]]:
    out: List[Tuple[float, float]] = []
    for seg in segments:
        if str(seg.get("speaker")) != speaker:
            continue
        s = float(seg.get("start", 0.0))
        e = float(seg.get("end", 0.0))
        if e > s:
            out.append((s, e))
    return out


def _volume_expr(segments: Sequence[Tuple[float, float]]) -> str:
    if not segments:
        return "0"
    return "+".join([f"between(t,{s:.3f},{e:.3f})" for s, e in segments])


def _render_speaker_masked_wav(
    input_wav: Path,
    output_wav: Path,
    active_segments: Sequence[Tuple[float, float]],
    logger: logging.Logger,
) -> None:
    duration = probe_audio_duration(input_wav)
    expr = _volume_expr(active_segments)
    af = f"volume='if(gt({expr},0),1,0)'"
    run_command(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(input_wav),
            "-af",
            af,
            "-ar",
            "16000",
            "-ac",
            "1",
            "-t",
            f"{duration:.3f}",
            str(output_wav),
        ],
        logger,
        timeout_sec=1200,
    )
