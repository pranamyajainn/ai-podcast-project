#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, Tuple

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from podcast_pipeline.utils import PipelineError  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare speaker assets from Veo videos")
    parser.add_argument("--speaker-a", required=True, help="Path to speaker A video")
    parser.add_argument("--speaker-b", required=True, help="Path to speaker B video")
    parser.add_argument("--duration", required=True, type=int, help="Looped duration in seconds")
    return parser.parse_args()


def run_cmd(cmd: list[str], timeout_sec: int) -> str:
    proc = subprocess.run(
        cmd,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=timeout_sec,
    )
    if proc.returncode != 0:
        raise PipelineError(f"Command failed ({proc.returncode}): {' '.join(cmd)}\n{proc.stdout}")
    return proc.stdout


def ffprobe_info(path: Path) -> Dict[str, object]:
    out = run_cmd(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_streams",
            "-show_format",
            "-of",
            "json",
            str(path),
        ],
        timeout_sec=60,
    )
    try:
        return json.loads(out)
    except Exception as exc:
        raise PipelineError(f"ffprobe JSON parse failed for {path}: {exc}") from exc


def probe_resolution_duration(path: Path) -> Tuple[str, float]:
    info = ffprobe_info(path)
    streams = info.get("streams", [])
    v_stream = None
    for s in streams:
        if s.get("codec_type") == "video":
            v_stream = s
            break
    if not v_stream:
        raise PipelineError(f"No video stream found: {path}")
    width = int(v_stream.get("width", 0))
    height = int(v_stream.get("height", 0))
    if width <= 0 or height <= 0:
        raise PipelineError(f"Invalid resolution from ffprobe: {path}")
    duration = float(info.get("format", {}).get("duration", 0.0))
    if duration <= 0:
        raise PipelineError(f"Invalid duration from ffprobe: {path}")
    return f"{width}x{height}", duration


def ensure_nonzero(path: Path) -> None:
    if not path.exists():
        raise PipelineError(f"Missing output file: {path}")
    if path.stat().st_size <= 0:
        raise PipelineError(f"Zero-byte output file: {path}")


def process_speaker(input_video: Path, still_out: Path, looped_out: Path, duration: int) -> None:
    if not input_video.exists():
        raise PipelineError(f"Input video not found: {input_video}")
    res, dur = probe_resolution_duration(input_video)
    print(f"INPUT {input_video} | resolution={res} | duration={dur:.3f}s")

    run_cmd(
        [
            "ffmpeg",
            "-y",
            "-ss",
            "00:00:01",
            "-i",
            str(input_video),
            "-frames:v",
            "1",
            "-q:v",
            "2",
            str(still_out),
        ],
        timeout_sec=300,
    )

    run_cmd(
        [
            "ffmpeg",
            "-y",
            "-stream_loop",
            "-1",
            "-i",
            str(input_video),
            "-f",
            "lavfi",
            "-i",
            "anullsrc=channel_layout=stereo:sample_rate=48000",
            "-t",
            str(duration),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-r",
            "25",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-shortest",
            str(looped_out),
        ],
        timeout_sec=1800,
    )


def format_size(path: Path) -> str:
    return f"{path.stat().st_size}B"


def main() -> int:
    args = parse_args()
    assets_dir = ROOT / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    speaker_a = Path(args.speaker_a).expanduser().resolve()
    speaker_b = Path(args.speaker_b).expanduser().resolve()
    if args.duration <= 0:
        raise PipelineError("--duration must be > 0")

    a_still = assets_dir / "speaker_a.jpg"
    b_still = assets_dir / "speaker_b.jpg"
    a_loop = assets_dir / "speaker_a_looped.mp4"
    b_loop = assets_dir / "speaker_b_looped.mp4"

    process_speaker(speaker_a, a_still, a_loop, args.duration)
    process_speaker(speaker_b, b_still, b_loop, args.duration)

    for out in (a_still, b_still, a_loop, b_loop):
        ensure_nonzero(out)

    a_still_res, _ = probe_resolution_duration(a_still)
    b_still_res, _ = probe_resolution_duration(b_still)
    a_loop_res, a_loop_dur = probe_resolution_duration(a_loop)
    b_loop_res, b_loop_dur = probe_resolution_duration(b_loop)

    print("ASSET MANIFEST")
    print(f"assets/speaker_a.jpg        [{a_still_res}] [{format_size(a_still)}]")
    print(f"assets/speaker_b.jpg        [{b_still_res}] [{format_size(b_still)}]")
    print(f"assets/speaker_a_looped.mp4 [{a_loop_res}] [{a_loop_dur:.3f}s] [{format_size(a_loop)}]")
    print(f"assets/speaker_b_looped.mp4 [{b_loop_res}] [{b_loop_dur:.3f}s] [{format_size(b_loop)}]")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PipelineError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
