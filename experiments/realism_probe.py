#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
from pathlib import Path


DEFAULT_CONFIG = Path("configs/realism_probe.yaml")
DEFAULT_AUDIO = Path("assets/audio/probe_audio.mp3")
DEFAULT_SOURCES = [
    Path("assets/source_footage/ashok_vidyasagar_testimonial.mp4"),
    Path("assets/source_footage/direct_to_camera_indoor.mp4"),
    Path("assets/source_footage/podcast_reference.mp4"),
    Path("assets/source_footage/creator_style_vertical.mp4"),
]


def run(cmd: list[str], timeout: int = 600) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        raise RuntimeError(
            "Command failed:\n"
            + " ".join(cmd)
            + "\n\nstdout:\n"
            + result.stdout
            + "\n\nstderr:\n"
            + result.stderr
        )
    return result


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        import yaml
    except ImportError as exc:
        raise RuntimeError("PyYAML is required when using --config. Install requirements/base.txt.") from exc
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def ffprobe(path: Path) -> dict:
    result = run(
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
        timeout=60,
    )
    return json.loads(result.stdout)


def duration(path: Path) -> float:
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        timeout=60,
    )
    return float(result.stdout.strip())


def slug(path: Path) -> str:
    clean = "".join(c.lower() if c.isalnum() else "_" for c in path.stem)
    return "_".join(part for part in clean.split("_") if part)[:60]


def make_audio_clip(audio: Path, out_dir: Path, seconds: float) -> Path:
    if not audio.exists() or audio.stat().st_size == 0:
        raise FileNotFoundError(f"Probe audio missing or empty: {audio}")
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "probe_audio_16k.wav"
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(audio),
            "-t",
            f"{seconds:.3f}",
            "-af",
            "highpass=f=80,lowpass=f=12000,loudnorm=I=-16:TP=-1.5:LRA=11",
            "-ar",
            "16000",
            "-ac",
            "1",
            str(out),
        ],
        timeout=300,
    )
    return out


def video_size(source: Path) -> tuple[int, int]:
    probe = ffprobe(source)
    for stream in probe["streams"]:
        if stream.get("codec_type") == "video":
            return int(stream["width"]), int(stream["height"])
    raise RuntimeError(f"No video stream found: {source}")


def make_reference_clip(source: Path, out_dir: Path, seconds: float, start: float) -> Path:
    if not source.exists() or source.stat().st_size == 0:
        raise FileNotFoundError(f"Source video missing or empty: {source}")
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "source_15s_original_framing.mp4"
    vf = (
        "scale=900:1600:force_original_aspect_ratio=decrease,"
        "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x101010,"
        "fps=30,format=yuv420p"
    )
    run(
        [
            "ffmpeg",
            "-y",
            "-ss",
            f"{start:.3f}",
            "-stream_loop",
            "-1",
            "-i",
            str(source),
            "-t",
            f"{seconds:.3f}",
            "-vf",
            vf,
            "-an",
            "-c:v",
            "libx264",
            "-crf",
            "18",
            "-preset",
            "slow",
            str(out),
        ],
        timeout=900,
    )
    return out


def make_musetalk_input_clip(source: Path, out_dir: Path, seconds: float, start: float) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "source_15s_musetalk_input.mp4"
    width, height = video_size(source)
    aspect = width / height
    if aspect > 1.25:
        # Wide source footage needs a vertical creator-style crop; padding it
        # makes the face too small and invalidates the realism test.
        vf = (
            "scale=1080:1920:force_original_aspect_ratio=increase,"
            "crop=1080:1920,"
            "fps=30,format=yuv420p"
        )
    else:
        # Portrait/selfie footage often exposes mouth artifacts because the
        # face is huge. Keep it smaller and leave room for captions.
        vf = (
            "scale=820:1458:force_original_aspect_ratio=decrease,"
            "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x101010,"
            "fps=30,format=yuv420p"
        )
    run(
        [
            "ffmpeg",
            "-y",
            "-ss",
            f"{start:.3f}",
            "-stream_loop",
            "-1",
            "-i",
            str(source),
            "-t",
            f"{seconds:.3f}",
            "-vf",
            vf,
            "-an",
            "-c:v",
            "libx264",
            "-crf",
            "18",
            "-preset",
            "slow",
            str(out),
        ],
        timeout=900,
    )
    return out


def make_cinematic_variant(source_clip: Path, audio_clip: Path, out_dir: Path) -> Path:
    out = out_dir / "source_15s_cinematic_masked.mp4"
    vf = (
        "eq=contrast=0.96:brightness=-0.015:saturation=0.93,"
        "noise=alls=4:allf=t+u,"
        "unsharp=5:5:0.35:3:3:0.15,"
        "fps=30,format=yuv420p"
    )
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(source_clip),
            "-i",
            str(audio_clip),
            "-vf",
            vf,
            "-map",
            "0:v",
            "-map",
            "1:a",
            "-c:v",
            "libx264",
            "-crf",
            "20",
            "-preset",
            "slow",
            "-c:a",
            "aac",
            "-b:a",
            "160k",
            "-movflags",
            "+faststart",
            "-shortest",
            str(out),
        ],
        timeout=900,
    )
    return out


def make_comparison(source_clip: Path, lipsync_clip: Path, out_dir: Path) -> tuple[Path, Path]:
    side_by_side = out_dir / "comparison_source_vs_lipsync.mp4"
    diff = out_dir / "difference_heatmap.mp4"
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(source_clip),
            "-i",
            str(lipsync_clip),
            "-filter_complex",
            "[0:v]scale=540:960:force_original_aspect_ratio=decrease,pad=540:960:(ow-iw)/2:(oh-ih)/2[left];"
            "[1:v]scale=540:960:force_original_aspect_ratio=decrease,pad=540:960:(ow-iw)/2:(oh-ih)/2[right];"
            "[left][right]hstack=inputs=2[v]",
            "-map",
            "[v]",
            "-map",
            "1:a?",
            "-c:v",
            "libx264",
            "-crf",
            "18",
            "-preset",
            "slow",
            "-c:a",
            "aac",
            "-shortest",
            str(side_by_side),
        ],
        timeout=900,
    )
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(source_clip),
            "-i",
            str(lipsync_clip),
            "-filter_complex",
            "[0:v]scale=1080:1920,format=rgb24[a];"
            "[1:v]scale=1080:1920,format=rgb24[b];"
            "[a][b]blend=all_mode=difference,eq=contrast=2.2:brightness=0.02[v]",
            "-map",
            "[v]",
            "-an",
            "-c:v",
            "libx264",
            "-crf",
            "18",
            "-preset",
            "slow",
            str(diff),
        ],
        timeout=900,
    )
    return side_by_side, diff


def write_review_sheet(root: Path, cases: list[dict], audio_clip: Path) -> None:
    lines = [
        "# Realism Probe Review Sheet",
        "",
        "Goal: decide whether fixed realistic source footage plus mouth replacement can pass Instagram believability.",
        "",
        f"Audio clip: `{audio_clip}`",
        "",
        "## Pass/Fail Question",
        "",
        "Would a normal Instagram user identify this as fake within 3-5 seconds on a phone?",
        "",
        "## Score Each Case 1-5",
        "",
        "- Teeth artifacts",
        "- Mouth edge blending",
        "- Chin/jaw motion",
        "- Blinking consistency",
        "- Head-motion preservation",
        "- Temporal stability",
        "- Compression survival",
        "",
        "## Cases",
        "",
    ]
    for case in cases:
        lines.extend(
            [
                f"### {case['id']}",
                "",
                f"- Source: `{case['source']}`",
                f"- Original-framing reference: `{case['reference']}`",
                f"- MuseTalk-ready reel: `{case['raw']}`",
                f"- Cinematic masked: `{case['masked']}`",
                f"- MuseTalk input video: `{case['musetalk_input_video']}`",
                f"- MuseTalk input audio: `{case['musetalk_input_audio']}`",
                f"- Expected MuseTalk output path: `{case['expected_lipsync']}`",
                "",
            ]
        )
    (root / "REVIEW.md").write_text("\n".join(lines), encoding="utf-8")


def write_musetalk_commands(root: Path, cases: list[dict]) -> None:
    lines = [
        "# MuseTalk Commands",
        "",
        "Run these on a CUDA machine with MuseTalk 1.5 installed.",
        "Copy each resulting file back to the expected output path, then rerun this script with `--compare-only`.",
        "",
    ]
    for case in cases:
        expected = Path(case["expected_lipsync"])
        result_dir = expected.parent
        lines.extend(
            [
                f"## {case['id']}",
                "",
                "```bash",
                "cd models/MuseTalk",
                "python3 -m scripts.inference \\",
                f"  --inference_config ../../{case['musetalk_config']} \\",
                f"  --result_dir ../../{result_dir} \\",
                "  --unet_model_path models/musetalkV15/unet.pth \\",
                "  --unet_config models/musetalkV15/musetalk.json \\",
                "  --version v15",
                "",
                "# Rename/copy the generated MuseTalk mp4 for the comparison pass:",
                f"# cp <generated_musetalk_result.mp4> ../../{expected}",
                "```",
                "",
            ]
        )
    (root / "MUSE_TALK_COMMANDS.md").write_text("\n".join(lines), encoding="utf-8")


def write_musetalk_case_config(case_dir: Path, video_path: Path, audio_path: Path) -> Path:
    config = case_dir / "musetalk_case.yaml"
    config.write_text(
        "\n".join(
            [
                "task_0:",
                f'  video_path: "../../{video_path}"',
                f'  audio_path: "../../{audio_path}"',
                "  bbox_shift: 0",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return config


def build_probe(args: argparse.Namespace) -> None:
    config = load_config(Path(args.config)) if args.config else {}
    seconds = args.seconds if args.seconds is not None else float(config.get("seconds", 15.0))
    start = args.start if args.start is not None else float(config.get("start", 1.0))
    out_dir = args.out or config.get("output_dir") or "outputs/realism_probe"
    audio = Path(args.audio or config.get("audio") or DEFAULT_AUDIO)
    root = Path(out_dir) / time.strftime("%Y%m%d_%H%M%S")
    audio_clip = make_audio_clip(audio, root / "audio", seconds)
    if args.sources:
        sources = [Path(item) for item in args.sources]
    elif config.get("sources"):
        sources = [Path(item["path"] if isinstance(item, dict) else item) for item in config["sources"]]
    else:
        sources = DEFAULT_SOURCES
    cases = []

    for source in sources:
        if not source.exists():
            print(f"[skip] missing source: {source}")
            continue
        case_id = slug(source)
        case_dir = root / "cases" / case_id
        reference = make_reference_clip(source, case_dir, seconds, start)
        raw = make_musetalk_input_clip(source, case_dir, seconds, start)
        masked = make_cinematic_variant(raw, audio_clip, case_dir)
        lipsync = case_dir / "musetalk_output.mp4"
        musetalk_config = write_musetalk_case_config(case_dir, raw, audio_clip)
        case = {
            "id": case_id,
            "source": str(source),
            "reference": str(reference),
            "raw": str(raw),
            "masked": str(masked),
            "musetalk_input_video": str(raw),
            "musetalk_input_audio": str(audio_clip),
            "musetalk_config": str(musetalk_config),
            "expected_lipsync": str(lipsync),
            "probe": ffprobe(raw),
        }
        if lipsync.exists() and lipsync.stat().st_size > 0:
            comparison, diff = make_comparison(raw, lipsync, case_dir)
            case["comparison"] = str(comparison)
            case["difference"] = str(diff)
        cases.append(case)

    if not cases:
        raise RuntimeError(
            "No source videos were available. Place probe footage under assets/source_footage/ "
            "or pass --sources explicitly."
        )

    (root / "manifest.json").write_text(json.dumps(cases, indent=2), encoding="utf-8")
    write_review_sheet(root, cases, audio_clip)
    write_musetalk_commands(root, cases)
    print(f"REALISM_PROBE_DIR={root}")
    print(f"CASES={len(cases)}")


def compare_only(args: argparse.Namespace) -> None:
    root = Path(args.out)
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    for case in manifest:
        raw = Path(case["raw"])
        lipsync = Path(case["expected_lipsync"])
        if lipsync.exists() and lipsync.stat().st_size > 0:
            comparison, diff = make_comparison(raw, lipsync, lipsync.parent)
            print(f"[compare] {case['id']} -> {comparison}, {diff}")
        else:
            print(f"[missing] {lipsync}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a 10-20s realism probe for source-footage lip sync.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--audio")
    parser.add_argument("--out")
    parser.add_argument("--seconds", type=float)
    parser.add_argument("--start", type=float)
    parser.add_argument("--sources", nargs="*")
    parser.add_argument("--compare-only", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    parsed = parse_args()
    if parsed.compare_only:
        compare_only(parsed)
    else:
        build_probe(parsed)
