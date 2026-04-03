#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install --upgrade pip wheel setuptools
python3 -m pip install -r requirements.txt

echo
echo "Environment installed."
echo "Next steps:"
echo "1) Ensure ffmpeg/ffprobe are installed and in PATH."
echo "2) Ensure faster-whisper model cache is available locally."
echo "3) Ensure local backend repos:"
echo "   - models/LatentSync (pinned commit)"
echo "   - models/VideoRetalking (Apache-2.0 build)"
echo "4) Place speaker/background assets in assets/."
