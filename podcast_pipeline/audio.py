from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict

from .utils import PipelineError, ensure_binary, ensure_dir, run_command


def preprocess_audio(
    input_audio: Path,
    stage_dir: Path,
    config: Dict[str, Any],
    logger: logging.Logger,
) -> Path:
    ensure_binary("ffmpeg")
    ensure_dir(stage_dir)

    audio_cfg = config["audio"]
    target_sr = int(audio_cfg["target_sample_rate"])
    target_ch = int(audio_cfg["target_channels"])
    loudnorm = str(audio_cfg["loudnorm"])

    normalized_wav = stage_dir / "preprocessed.wav"
    denoised_wav = stage_dir / "preprocessed_denoised.wav"

    # highpass at 20Hz removes most DC components in practice.
    audio_filter = f"highpass=f=20,loudnorm={loudnorm}"
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(input_audio),
        "-af",
        audio_filter,
        "-ar",
        str(target_sr),
        "-ac",
        str(target_ch),
        str(normalized_wav),
    ]
    run_command(cmd, logger)

    if bool(audio_cfg.get("denoise", False)):
        nf = float(audio_cfg.get("denoise_nf", -25))
        denoise_cmd = [
            "ffmpeg",
            "-y",
            "-i",
            str(normalized_wav),
            "-af",
            f"afftdn=nf={nf}",
            str(denoised_wav),
        ]
        run_command(denoise_cmd, logger)
        final_audio = denoised_wav
    else:
        final_audio = normalized_wav

    if not final_audio.exists():
        raise PipelineError(f"Audio preprocessing did not produce output: {final_audio}")

    logger.info("Audio preprocessing complete: %s", final_audio)
    return final_audio
