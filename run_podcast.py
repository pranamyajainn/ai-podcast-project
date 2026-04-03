#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
import time
from dataclasses import asdict
from pathlib import Path
from typing import List

from podcast_pipeline.audio import preprocess_audio
from podcast_pipeline.composite import composite_video
from podcast_pipeline.diarize import diarize_audio
from podcast_pipeline.export import burn_subtitles_and_export
from podcast_pipeline.lipsync import render_speaker_full_video
from podcast_pipeline.subtitles import generate_srt
from podcast_pipeline.transcribe import transcribe_audio
from podcast_pipeline.utils import (
    PipelineError,
    StageStat,
    StageTimer,
    bool_from_optional_flag,
    ensure_dir,
    load_config,
    probe_audio_duration,
    setup_logger,
    stage_error_boundary,
    write_json,
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Two-host local podcast video generator")
    p.add_argument("--audio", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--config", default="configs/default_config.yaml")
    p.add_argument("--speaker-a-image", default="")
    p.add_argument("--speaker-b-image", default="")
    p.add_argument("--keep-intermediates", nargs="?", const="true", default=None)
    p.add_argument("--verbose", action="store_true")
    return p.parse_args()


def resolve_path(base: Path, value: str) -> Path:
    p = Path(value)
    return p if p.is_absolute() else base / p


def cleanup(paths: List[Path]) -> None:
    for p in paths:
        if p.exists():
            shutil.rmtree(p)


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent
    config = load_config(resolve_path(root, args.config))

    input_audio = Path(args.audio).expanduser().resolve()
    out_dir = ensure_dir(Path(args.out).expanduser().resolve())
    logger = setup_logger(ensure_dir(out_dir / "logs") / "pipeline.log", verbose=args.verbose)

    if not input_audio.exists():
        raise PipelineError(f"Input audio not found: {input_audio}")
    if input_audio.suffix.lower() not in {".mp3", ".wav", ".m4a", ".aac", ".flac"}:
        raise PipelineError("Input audio must be a supported audio format (mp3/wav/m4a/aac/flac).")
    audio_dur = probe_audio_duration(input_audio)
    if not (60 <= audio_dur <= 300):
        raise PipelineError(f"Input audio must be 1-5 minutes. Detected duration: {audio_dur:.2f}s")

    speaker_a_image = Path(args.speaker_a_image).expanduser().resolve() if args.speaker_a_image else resolve_path(root, str(config["speakers"]["a"]["source_image"]))
    speaker_b_image = Path(args.speaker_b_image).expanduser().resolve() if args.speaker_b_image else resolve_path(root, str(config["speakers"]["b"]["source_image"]))
    speaker_a_idle = resolve_path(root, str(config["speakers"]["a"]["idle_video"]))
    speaker_b_idle = resolve_path(root, str(config["speakers"]["b"]["idle_video"]))

    for p in (speaker_a_image, speaker_b_image, speaker_a_idle, speaker_b_idle):
        if not p.exists() or p.stat().st_size <= 0:
            raise PipelineError(f"Required asset missing/empty: {p}")

    stage1 = ensure_dir(out_dir / "stage1_audio")
    stage2 = ensure_dir(out_dir / "stage2_transcription")
    stage3 = ensure_dir(out_dir / "stage3_diarization")
    stage4a = ensure_dir(out_dir / "stage4_host_a")
    stage4b = ensure_dir(out_dir / "stage4_host_b")
    stage5 = ensure_dir(out_dir / "stage5_composite")
    stage6 = ensure_dir(out_dir / "stage6_subtitles")
    stage7 = ensure_dir(out_dir / "stage7_export")

    stats: List[StageStat] = []
    started = time.time()

    with stage_error_boundary("1_preprocess_audio", logger):
        with StageTimer("1_preprocess_audio", stats) as t:
            preprocessed_wav = preprocess_audio(input_audio, stage1, config, logger)
            t.mark_output(preprocessed_wav)

    with stage_error_boundary("2_transcription", logger):
        with StageTimer("2_transcription", stats) as t:
            transcript_words_json, transcript_segments_json = transcribe_audio(preprocessed_wav, stage2, config, logger)
            t.mark_output(transcript_words_json)

    with stage_error_boundary("3_diarization", logger):
        with StageTimer("3_diarization", stats) as t:
            diar_json, speaker_a_wav, speaker_b_wav = diarize_audio(
                transcript_words_json,
                preprocessed_wav,
                stage3,
                config,
                logger,
            )
            t.mark_output(diar_json)

    with stage_error_boundary("4_avatar_host_a", logger):
        with StageTimer("4_avatar_host_a", stats) as t:
            host_a_video = render_speaker_full_video(
                speaker_label="HOST_A",
                source_image=speaker_a_image,
                speaker_padded_wav=speaker_a_wav,
                original_full_wav=preprocessed_wav,
                diarization_json=diar_json,
                idle_clip_mp4=speaker_a_idle,
                output_dir=stage4a,
                config=config,
                fps=int(config["export"].get("fps", 25)),
                logger=logger,
            )
            t.mark_output(host_a_video)

    with stage_error_boundary("4_avatar_host_b", logger):
        with StageTimer("4_avatar_host_b", stats) as t:
            host_b_video = render_speaker_full_video(
                speaker_label="HOST_B",
                source_image=speaker_b_image,
                speaker_padded_wav=speaker_b_wav,
                original_full_wav=preprocessed_wav,
                diarization_json=diar_json,
                idle_clip_mp4=speaker_b_idle,
                output_dir=stage4b,
                config=config,
                fps=int(config["export"].get("fps", 25)),
                logger=logger,
            )
            t.mark_output(host_b_video)

    with stage_error_boundary("5_composite", logger):
        with StageTimer("5_composite", stats) as t:
            composited = composite_video(host_a_video, host_b_video, preprocessed_wav, stage5, logger)
            t.mark_output(composited)

    with stage_error_boundary("6_subtitles", logger):
        with StageTimer("6_subtitles", stats) as t:
            srt = generate_srt(transcript_segments_json, diar_json, stage6, logger)
            t.mark_output(srt)

    final_video = stage7 / "final_720p.mp4"
    with stage_error_boundary("7_export", logger):
        with StageTimer("7_export", stats) as t:
            burn_subtitles_and_export(composited, srt, final_video, logger)
            t.mark_output(final_video)

    final_root = out_dir / "final_720p.mp4"
    shutil.copy2(final_video, final_root)

    if not bool_from_optional_flag(args.keep_intermediates, True):
        cleanup([stage1, stage2, stage3, stage4a, stage4b, stage5, stage6])

    write_json(
        out_dir / "run_report.json",
        {
            "input_duration_sec": round(audio_dur, 3),
            "total_runtime_sec": round(time.time() - started, 3),
            "stages": [asdict(s) for s in stats],
            "final_video": str(final_video),
            "final_video_root": str(final_root),
        },
    )
    logger.info("Pipeline complete. Final video: %s", final_root)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PipelineError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
