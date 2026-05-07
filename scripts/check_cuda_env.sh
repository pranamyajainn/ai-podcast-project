#!/usr/bin/env bash
set -euo pipefail

python3 --version
ffmpeg -version | head -1
ffprobe -version | head -1

if command -v nvidia-smi >/dev/null 2>&1; then
  nvidia-smi
else
  echo 'FAIL: nvidia-smi not found'
  exit 1
fi

python3 - <<'PY'
import torch
print('torch:', torch.__version__)
print('cuda_available:', torch.cuda.is_available())
if torch.cuda.is_available():
    print('cuda_device:', torch.cuda.get_device_name(0))
else:
    raise SystemExit(1)
PY
