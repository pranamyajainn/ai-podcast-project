from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Sequence

from .utils import PipelineError, ensure_dir


def generate_srt(
    transcript_segments_json: Path,
    diarization_json: Path,
    stage_dir: Path,
    logger: logging.Logger,
) -> Path:
    ensure_dir(stage_dir)
    if not transcript_segments_json.exists():
        raise PipelineError(f"Transcript segments JSON missing: {transcript_segments_json}")
    if not diarization_json.exists():
        raise PipelineError(f"Diarization JSON missing: {diarization_json}")

    segments = json.loads(transcript_segments_json.read_text(encoding="utf-8"))
    diar = json.loads(diarization_json.read_text(encoding="utf-8"))
    if not isinstance(segments, list) or not segments:
        raise PipelineError("Transcript segments are empty")

    tolerance = 0.2
    lines: List[str] = []
    idx = 1
    for seg in segments:
        s = float(seg.get("start", 0.0))
        e = float(seg.get("end", 0.0))
        txt = str(seg.get("text", "")).strip()
        if not txt or e <= s:
            continue
        speaker = _speaker_for_segment(s, e, diar, tolerance)
        label = "[HOST A]" if speaker == "HOST_A" else "[HOST B]"
        lines.append(str(idx))
        lines.append(f"{_fmt(s)} --> {_fmt(e)}")
        lines.append(f"{label} {txt}")
        lines.append("")
        idx += 1

    if idx == 1:
        raise PipelineError("No subtitle cues generated")

    out = stage_dir / "transcript_en.srt"
    out.write_text("\n".join(lines), encoding="utf-8")
    logger.info("Subtitle SRT generated: %s (%d cues)", out, idx - 1)
    return out


def _speaker_for_segment(start: float, end: float, diar: Sequence[Dict[str, Any]], tolerance: float) -> str:
    best = None
    best_overlap = -1.0
    qs = max(0.0, start - tolerance)
    qe = end + tolerance
    for seg in diar:
        ss = float(seg.get("start", 0.0))
        ee = float(seg.get("end", 0.0))
        if ee <= ss:
            continue
        overlap = max(0.0, min(qe, ee) - max(qs, ss))
        if overlap > best_overlap:
            best_overlap = overlap
            best = str(seg.get("speaker", "HOST_A"))
    return best or "HOST_A"


def _fmt(seconds: float) -> str:
    ms_total = int(round(seconds * 1000))
    h = ms_total // 3_600_000
    ms_total -= h * 3_600_000
    m = ms_total // 60_000
    ms_total -= m * 60_000
    s = ms_total // 1000
    ms = ms_total - s * 1000
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
