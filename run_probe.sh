#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"
CONFIG="${1:-configs/realism_probe.yaml}"

required=(
  "assets/audio/probe_audio.mp3"
  "assets/source_footage/ashok_vidyasagar_testimonial.mp4"
  "assets/source_footage/direct_to_camera_indoor.mp4"
  "assets/source_footage/podcast_reference.mp4"
  "assets/source_footage/creator_style_vertical.mp4"
)

for path in "${required[@]}"; do
  if [[ ! -s "$path" ]]; then
    echo "[run_probe] Missing required asset: $path" >&2
    echo "[run_probe] See assets/README.md for expected filenames." >&2
    exit 1
  fi
done

"$PYTHON_BIN" experiments/realism_probe.py --config "$CONFIG"
