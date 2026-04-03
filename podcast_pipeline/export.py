from __future__ import annotations

import logging
from pathlib import Path

from .utils import PipelineError, ensure_binary, ffprobe_streams, run_command


def burn_subtitles_and_export(
    composited_video: Path,
    subtitles_srt: Path,
    output_path: Path,
    logger: logging.Logger,
) -> Path:
    ensure_binary("ffmpeg")
    if not composited_video.exists():
        raise PipelineError(f"Composited video missing: {composited_video}")
    if not subtitles_srt.exists():
        raise PipelineError(f"SRT file missing: {subtitles_srt}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    subtitle_filter = (
        f"subtitles={_escape_filter_path(subtitles_srt)}:"
        "force_style='FontSize=18,PrimaryColour=&Hffffff,OutlineColour=&H000000,Outline=1,Alignment=2'"
    )
    run_command(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(composited_video),
            "-vf",
            subtitle_filter,
            "-c:v",
            "libx264",
            "-c:a",
            "copy",
            "-movflags",
            "+faststart",
            str(output_path),
        ],
        logger,
        timeout_sec=1800,
    )

    if not output_path.exists() or output_path.stat().st_size <= 0:
        raise PipelineError(f"Final export missing/empty: {output_path}")
    validate_final_video(output_path)
    return output_path


def validate_final_video(video_path: Path) -> None:
    data = ffprobe_streams(video_path)
    streams = data.get("streams", [])
    v = next((s for s in streams if s.get("codec_type") == "video"), None)
    a = next((s for s in streams if s.get("codec_type") == "audio"), None)
    if not v or not a:
        raise PipelineError("Final video must contain video and audio streams.")
    if int(v.get("width", 0)) != 1280 or int(v.get("height", 0)) != 720:
        raise PipelineError(f"Final video resolution invalid: {v.get('width')}x{v.get('height')}")
    if str(v.get("codec_name", "")).lower() != "h264":
        raise PipelineError(f"Final video codec invalid: {v.get('codec_name')}")
    if str(a.get("codec_name", "")).lower() not in {"aac", "mp4a"}:
        raise PipelineError(f"Final audio codec invalid: {a.get('codec_name')}")


def _escape_filter_path(path: Path) -> str:
    value = path.as_posix()
    value = value.replace("\\", "\\\\")
    value = value.replace(":", "\\:")
    value = value.replace("'", "\\'")
    value = value.replace(",", "\\,")
    return value
