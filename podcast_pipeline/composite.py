from __future__ import annotations

import logging
from pathlib import Path

from .utils import PipelineError, ensure_binary, ensure_dir, probe_audio_duration, run_command


def composite_video(
    host_a_video: Path,
    host_b_video: Path,
    full_audio_wav: Path,
    stage_dir: Path,
    logger: logging.Logger,
) -> Path:
    ensure_binary("ffmpeg")
    ensure_dir(stage_dir)

    for p in (host_a_video, host_b_video, full_audio_wav):
        if not p.exists():
            raise PipelineError(f"Composite input missing: {p}")

    out_path = stage_dir / "composited.mp4"
    target_duration = probe_audio_duration(full_audio_wav)
    filter_complex = (
        "[0:v]scale=640:720:force_original_aspect_ratio=decrease,"
        "pad=640:720:(ow-iw)/2:(oh-ih)/2,setsar=1[left];"
        "[1:v]scale=640:720:force_original_aspect_ratio=decrease,"
        "pad=640:720:(ow-iw)/2:(oh-ih)/2,setsar=1[right];"
        "[left][right]hstack=inputs=2[v]"
    )

    # HOST_B on left, HOST_A on right
    run_command(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(host_b_video),
            "-i",
            str(host_a_video),
            "-i",
            str(full_audio_wav),
            "-filter_complex",
            filter_complex,
            "-map",
            "[v]",
            "-map",
            "2:a",
            "-af",
            "apad",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-r",
            "25",
            "-t",
            f"{target_duration:.3f}",
            str(out_path),
        ],
        logger,
        timeout_sec=3600,
    )

    if not out_path.exists() or out_path.stat().st_size <= 0:
        raise PipelineError(f"Composite output missing/empty: {out_path}")
    return out_path
