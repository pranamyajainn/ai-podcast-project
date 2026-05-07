#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"

printf '[setup] Python: '
"$PYTHON_BIN" --version

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo '[setup] ERROR: ffmpeg is not installed or not on PATH.' >&2
  exit 1
fi

if ! command -v ffprobe >/dev/null 2>&1; then
  echo '[setup] ERROR: ffprobe is not installed or not on PATH.' >&2
  exit 1
fi

"$PYTHON_BIN" -m pip install --upgrade pip
"$PYTHON_BIN" -m pip install -r requirements/base.txt

git submodule update --init --recursive

cat <<'MSG'
[setup] Base repo setup complete.
[setup] For CUDA MuseTalk dependencies, run on the GPU machine:
        python3 -m pip install -r models/MuseTalk/requirements.txt
        bash models/MuseTalk/download_weights.sh
MSG
