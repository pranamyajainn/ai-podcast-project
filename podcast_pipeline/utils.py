from __future__ import annotations

import copy
import json
import logging
import shutil
import subprocess
import time
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import yaml


DEFAULT_CONFIG: Dict[str, Any] = {
    "project": {
        "name": "english-two-speaker-podcast",
        "seed": 124578,
    },
    "paths": {
        "assets_dir": "assets",
        "models_dir": "models",
        "work_dir": "out",
    },
    "audio": {
        "target_sample_rate": 16000,
        "target_channels": 1,
        "loudnorm": "I=-16:TP=-1.5:LRA=11",
        "denoise": False,
        "denoise_nf": -25,
        "max_duration_sec": 1800,
    },
    "diarize": {
        "model": "base",
        "min_segment_duration": 0.5,
        "speaker_change_gap_sec": 0.8,
    },
    "speakers": {
        "a": {
            "source_image": "assets/speaker_a.jpg",
            "idle_video": "assets/speaker_a_looped.mp4",
            "input_video": "/Users/pranamyajain/Downloads/male podcast studio.mp4",
        },
        "b": {
            "source_image": "assets/speaker_b.jpg",
            "idle_video": "assets/speaker_b_looped.mp4",
            "input_video": "/Users/pranamyajain/Downloads/female podcast studio.mp4",
        },
    },
    "lipsync": {
        "backend": "latentsync",
        "repo_path": "models/LatentSync",
        "fallback_backend": "videoretalking",
    },
    "layout": {
        "type": "split_screen",
        "speaker_a_x": 0,
        "speaker_b_x": 960,
        "width_per_speaker": 960,
        "height": 1080,
    },
    "composite": {
        "background": "assets/background_1920x1080.png",
    },
    "subtitles": {
        "language": "en",
        "model_path": "models/whisper/large-v3",
        "beam_size": 5,
        "vad_filter": True,
        "word_timestamps": False,
        "font_name": "Noto Sans",
        "font_size": 42,
        "margin_v": 60,
        "outline": 2,
        "alignment": 2,
        "output_srt": "transcript_en.srt",
    },
    "export": {
        "fps": 25,
        "crf": 18,
        "audio_bitrate": "192k",
        "audio_sample_rate": 48000,
        "preset": "slow",
        "pix_fmt": "yuv420p",
    },
}


@dataclass
class StageStat:
    name: str
    started_at: float
    ended_at: float
    duration_sec: float
    output: Optional[str] = None


class PipelineError(RuntimeError):
    """Raised when a pipeline stage fails."""


class StageTimer:
    def __init__(self, name: str, stats: List[StageStat]):
        self.name = name
        self.stats = stats
        self.start = 0.0
        self.output: Optional[str] = None

    def __enter__(self) -> "StageTimer":
        self.start = time.time()
        return self

    def mark_output(self, output: Path | str) -> None:
        self.output = str(output)

    def __exit__(self, exc_type, exc, _tb) -> None:
        end = time.time()
        self.stats.append(
            StageStat(
                name=self.name,
                started_at=self.start,
                ended_at=end,
                duration_sec=round(end - self.start, 3),
                output=self.output,
            )
        )


def deep_merge(base: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
    result = dict(base)
    for key, value in update.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def load_config(config_path: Path) -> Dict[str, Any]:
    if not config_path.exists():
        return copy.deepcopy(DEFAULT_CONFIG)
    with config_path.open("r", encoding="utf-8") as f:
        user_cfg = yaml.safe_load(f) or {}
    return deep_merge(copy.deepcopy(DEFAULT_CONFIG), user_cfg)


def setup_logger(log_path: Path, verbose: bool = False) -> logging.Logger:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("podcast_pipeline")
    logger.handlers.clear()
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def ensure_binary(binary_name: str) -> None:
    if shutil.which(binary_name) is None:
        raise PipelineError(f"Required binary not found in PATH: {binary_name}")


def run_command(
    command: Iterable[str],
    logger: logging.Logger,
    cwd: Optional[Path] = None,
    env: Optional[Dict[str, str]] = None,
    timeout_sec: int = 1800,
) -> subprocess.CompletedProcess:
    cmd_list = [str(c) for c in command]
    logger.debug("Running command: %s", " ".join(cmd_list))
    try:
        proc = subprocess.run(
            cmd_list,
            cwd=str(cwd) if cwd else None,
            env=env,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=timeout_sec,
        )
    except subprocess.TimeoutExpired as exc:
        raise PipelineError(
            f"Command timed out after {timeout_sec}s: {' '.join(cmd_list)}"
        ) from exc
    if proc.stdout:
        logger.debug(proc.stdout)
    if proc.returncode != 0:
        tail = "\n".join((proc.stdout or "").splitlines()[-40:])
        raise PipelineError(f"Command failed ({proc.returncode}): {' '.join(cmd_list)}\n{tail}")
    return proc


def ffprobe_streams(path: Path) -> Dict[str, Any]:
    ensure_binary("ffprobe")
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-show_streams",
        "-show_format",
        "-of",
        "json",
        str(path),
    ]
    proc = subprocess.run(
        cmd,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=120,
    )
    return json.loads(proc.stdout)


def probe_audio_duration(path: Path) -> float:
    data = ffprobe_streams(path)
    fmt = data.get("format", {})
    duration = fmt.get("duration")
    if duration is None:
        raise PipelineError(f"Could not determine duration for: {path}")
    return float(duration)


def detect_gpu_vram_gb(logger: logging.Logger) -> float:
    try:
        import torch  # BSD-3-Clause

        if torch.cuda.is_available():
            props = torch.cuda.get_device_properties(0)
            gb = props.total_memory / (1024**3)
            logger.info("Detected GPU: %s (%.2f GB)", props.name, gb)
            return float(round(gb, 2))
    except Exception as exc:
        logger.debug("Torch CUDA detection failed: %s", exc)

    nvidia_smi = shutil.which("nvidia-smi")
    if nvidia_smi:
        try:
            proc = subprocess.run(
                [nvidia_smi, "--query-gpu=memory.total", "--format=csv,noheader,nounits"],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30,
            )
            first_line = proc.stdout.strip().splitlines()[0]
            mb = float(first_line)
            gb = mb / 1024.0
            logger.info("Detected GPU VRAM via nvidia-smi: %.2f GB", gb)
            return float(round(gb, 2))
        except Exception as exc:
            logger.debug("nvidia-smi detection failed: %s", exc)

    raise PipelineError(
        "No CUDA GPU detected. This pipeline requires a local NVIDIA GPU for diarization and lipsync stages."
    )


def bool_from_optional_flag(value: Optional[str], default: bool) -> bool:
    if value is None:
        return default
    normalized = str(value).strip().lower()
    if normalized in {"1", "true", "yes", "on"}:
        return True
    if normalized in {"0", "false", "no", "off"}:
        return False
    return default


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


@contextmanager
def stage_error_boundary(stage_name: str, logger: logging.Logger):
    try:
        yield
    except PipelineError:
        raise
    except Exception as exc:
        logger.exception("Unexpected error at stage '%s': %s", stage_name, exc)
        raise PipelineError(f"Unexpected error at stage '{stage_name}': {exc}") from exc
