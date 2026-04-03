from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

from .utils import PipelineError, ensure_dir


def transcribe_audio(
    audio_wav: Path,
    stage_dir: Path,
    config: Dict[str, Any],
    logger: logging.Logger,
) -> Tuple[Path, Path]:
    ensure_dir(stage_dir)
    try:
        from faster_whisper import WhisperModel  # MIT
    except Exception as exc:
        raise PipelineError("faster-whisper is not installed") from exc

    sub_cfg = config.get("subtitles", {})
    model_name = str(sub_cfg.get("model_name", "large-v3"))
    device = str(sub_cfg.get("device", "cpu"))
    compute_type = str(sub_cfg.get("compute_type", "int8"))
    beam_size = int(sub_cfg.get("beam_size", 5))
    vad_filter = bool(sub_cfg.get("vad_filter", True))

    logger.info(
        "Transcribing with faster-whisper model=%s device=%s compute_type=%s",
        model_name,
        device,
        compute_type,
    )
    model = WhisperModel(model_name, device=device, compute_type=compute_type)
    segments, info = model.transcribe(
        str(audio_wav),
        language="en",
        task="transcribe",
        beam_size=beam_size,
        vad_filter=vad_filter,
        word_timestamps=True,
    )

    word_rows: List[Dict[str, Any]] = []
    seg_rows: List[Dict[str, Any]] = []
    for seg in segments:
        seg_text = str(getattr(seg, "text", "")).strip()
        seg_start = float(getattr(seg, "start", 0.0))
        seg_end = float(getattr(seg, "end", 0.0))
        if seg_end <= seg_start:
            continue
        seg_rows.append(
            {
                "start": round(seg_start, 3),
                "end": round(seg_end, 3),
                "text": seg_text,
            }
        )
        for w in getattr(seg, "words", []) or []:
            if w.start is None or w.end is None:
                continue
            ws = float(w.start)
            we = float(w.end)
            if we <= ws:
                continue
            word_rows.append(
                {
                    "start": round(ws, 3),
                    "end": round(we, 3),
                    "word": str(getattr(w, "word", "")).strip(),
                    "probability": float(getattr(w, "probability", 0.0)),
                }
            )

    if not word_rows:
        raise PipelineError("Transcription produced no words with timestamps")

    words_path = stage_dir / "transcript_words.json"
    segments_path = stage_dir / "transcript_segments.json"
    words_path.write_text(json.dumps(word_rows, indent=2), encoding="utf-8")
    segments_path.write_text(json.dumps(seg_rows, indent=2), encoding="utf-8")

    logger.info(
        "Transcription complete: language=%s words=%d segments=%d",
        getattr(info, "language", "en"),
        len(word_rows),
        len(seg_rows),
    )
    return words_path, segments_path
