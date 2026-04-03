from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Tuple

from .utils import PipelineError, ensure_binary, ensure_dir, probe_audio_duration, run_command


def render_speaker_full_video(
    speaker_label: str,
    source_image: Path,
    speaker_padded_wav: Path,
    original_full_wav: Path,
    diarization_json: Path,
    idle_clip_mp4: Path,
    output_dir: Path,
    config: Dict[str, Any],
    fps: int,
    logger: logging.Logger,
) -> Path:
    ensure_binary("ffmpeg")
    ensure_dir(output_dir)

    if speaker_label not in {"HOST_A", "HOST_B"}:
        raise PipelineError(f"Invalid speaker label: {speaker_label}")
    for p in (source_image, speaker_padded_wav, original_full_wav, diarization_json, idle_clip_mp4):
        if not p.exists():
            raise PipelineError(f"Lipsync input missing: {p}")

    timeline = _build_timeline(
        segments=json.loads(diarization_json.read_text(encoding="utf-8")),
        speaker_label=speaker_label,
        full_duration=probe_audio_duration(original_full_wav),
    )
    if not timeline:
        raise PipelineError(f"No timeline segments built for {speaker_label}")

    tmp_dir = ensure_dir(output_dir / f"tmp_{speaker_label.lower()}")
    parts: List[Path] = []

    for idx, seg in enumerate(timeline):
        seg_dur = seg["end"] - seg["start"]
        if seg_dur <= 0.02:
            continue
        part_path = tmp_dir / f"part_{idx:05d}.mp4"
        if seg["type"] == "speech":
            _render_speech_segment_sadtalker(
                source_image=source_image,
                speaker_padded_wav=speaker_padded_wav,
                start=seg["start"],
                duration=seg_dur,
                out_path=part_path,
                tmp_dir=tmp_dir,
                config=config,
                fps=fps,
                logger=logger,
            )
        else:
            _render_idle_segment(
                idle_clip=idle_clip_mp4,
                duration=seg_dur,
                fps=fps,
                out_path=part_path,
                logger=logger,
            )
        if not part_path.exists() or part_path.stat().st_size <= 0:
            raise PipelineError(f"Failed to render segment {idx} for {speaker_label}")
        parts.append(part_path)

    if not parts:
        raise PipelineError(f"No rendered parts for {speaker_label}")

    concat_list = tmp_dir / "concat.txt"
    concat_list.write_text("\n".join([f"file '{p.as_posix()}'" for p in parts]) + "\n", encoding="utf-8")

    out_name = "host_a_full.mp4" if speaker_label == "HOST_A" else "host_b_full.mp4"
    out_path = output_dir / out_name
    run_command(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(fps),
            str(out_path),
        ],
        logger,
        timeout_sec=7200,
    )
    _validate_duration(out_path, original_full_wav)
    logger.info("Rendered full host video %s -> %s", speaker_label, out_path)
    return out_path


def _render_speech_segment_sadtalker(
    source_image: Path,
    speaker_padded_wav: Path,
    start: float,
    duration: float,
    out_path: Path,
    tmp_dir: Path,
    config: Dict[str, Any],
    fps: int,
    logger: logging.Logger,
) -> None:
    seg_audio = tmp_dir / f"audio_{start:.3f}.wav"
    run_command(
        [
            "ffmpeg",
            "-y",
            "-ss",
            f"{start:.3f}",
            "-t",
            f"{duration:.3f}",
            "-i",
            str(speaker_padded_wav),
            "-ar",
            "16000",
            "-ac",
            "1",
            str(seg_audio),
        ],
        logger,
        timeout_sec=1200,
    )

    lip_cfg = config.get("lipsync", {})
    backend = str(lip_cfg.get("backend", "sadtalker")).lower()
    if backend != "sadtalker":
        raise PipelineError(f"Unsupported lipsync backend on this machine: {backend}")

    repo = Path(str(lip_cfg.get("repo_path", "models/SadTalker")))
    script = repo / "inference.py"
    if not repo.exists() or not script.exists():
        raise PipelineError(f"SadTalker repo missing or incomplete: {repo}")

    stage_out = ensure_dir(tmp_dir / f"sadtalker_{start:.3f}")
    run_command(
        [
            "python",
            "inference.py",
            "--driven_audio",
            str(seg_audio),
            "--source_image",
            str(source_image),
            "--result_dir",
            str(stage_out),
            "--still",
            "--preprocess",
            "full",
        ],
        logger,
        cwd=repo,
        timeout_sec=7200,
    )

    generated = _find_latest_mp4(stage_out)
    run_command(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(generated),
            "-vf",
            f"fps={fps},scale=640:720:force_original_aspect_ratio=decrease,pad=640:720:(ow-iw)/2:(oh-ih)/2",
            "-t",
            f"{duration:.3f}",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            str(out_path),
        ],
        logger,
        timeout_sec=1200,
    )


def _render_idle_segment(idle_clip: Path, duration: float, fps: int, out_path: Path, logger: logging.Logger) -> None:
    run_command(
        [
            "ffmpeg",
            "-y",
            "-stream_loop",
            "-1",
            "-i",
            str(idle_clip),
            "-t",
            f"{duration:.3f}",
            "-vf",
            f"fps={fps},scale=640:720:force_original_aspect_ratio=decrease,pad=640:720:(ow-iw)/2:(oh-ih)/2",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            str(out_path),
        ],
        logger,
        timeout_sec=1200,
    )


def _build_timeline(segments: List[Dict[str, Any]], speaker_label: str, full_duration: float) -> List[Dict[str, float]]:
    segs: List[Tuple[float, float]] = []
    for seg in segments:
        if str(seg.get("speaker")) != speaker_label:
            continue
        s = float(seg.get("start", 0.0))
        e = float(seg.get("end", 0.0))
        if e > s:
            segs.append((max(0.0, s), min(full_duration, e)))
    segs.sort(key=lambda x: x[0])

    timeline: List[Dict[str, float]] = []
    cursor = 0.0
    for s, e in segs:
        if s > cursor:
            timeline.append({"type": "idle", "start": round(cursor, 3), "end": round(s, 3)})
        timeline.append({"type": "speech", "start": round(s, 3), "end": round(e, 3)})
        cursor = max(cursor, e)
    if cursor < full_duration:
        timeline.append({"type": "idle", "start": round(cursor, 3), "end": round(full_duration, 3)})
    return timeline


def _find_latest_mp4(path: Path) -> Path:
    files = sorted(path.rglob("*.mp4"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        raise PipelineError(f"No MP4 output produced in {path}")
    return files[0]


def _validate_duration(video_path: Path, reference_audio: Path) -> None:
    vd = probe_audio_duration(video_path)
    rd = probe_audio_duration(reference_audio)
    if abs(vd - rd) > 0.1:
        raise PipelineError(
            f"Duration mismatch beyond tolerance: video={vd:.3f}s audio={rd:.3f}s path={video_path}"
        )
