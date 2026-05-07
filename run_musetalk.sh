#!/usr/bin/env bash
set -euo pipefail

PROBE_DIR="${1:-}"
PYTHON_BIN="${PYTHON_BIN:-python3}"

if [[ -z "$PROBE_DIR" ]]; then
  echo "Usage: ./run_musetalk.sh outputs/realism_probe/<probe_id>" >&2
  exit 1
fi

if [[ ! -d models/MuseTalk ]]; then
  echo "[run_musetalk] models/MuseTalk missing. Run: git submodule update --init --recursive" >&2
  exit 1
fi

if [[ ! -f models/MuseTalk/models/musetalkV15/unet.pth ]]; then
  echo "[run_musetalk] MuseTalk v1.5 weights missing." >&2
  echo "[run_musetalk] Run: cd models/MuseTalk && bash download_weights.sh" >&2
  exit 1
fi

for cfg in "$PROBE_DIR"/cases/*/musetalk_case.yaml; do
  case_dir="$(dirname "$cfg")"
  echo "[run_musetalk] Case: $case_dir"
  before="$(find "$case_dir" -maxdepth 1 -type f -name '*.mp4' -print | sort || true)"
  (
    cd models/MuseTalk
    "$PYTHON_BIN" -m scripts.inference \
      --inference_config "../../$cfg" \
      --result_dir "../../$case_dir" \
      --unet_model_path models/musetalkV15/unet.pth \
      --unet_config models/musetalkV15/musetalk.json \
      --version v15
  )
  newest="$(find "$case_dir" -maxdepth 1 -type f -name '*.mp4' -print0 | xargs -0 ls -t | head -1 || true)"
  if [[ -n "$newest" && "$(basename "$newest")" != "musetalk_output.mp4" ]]; then
    cp "$newest" "$case_dir/musetalk_output.mp4"
    echo "[run_musetalk] Copied $newest -> $case_dir/musetalk_output.mp4"
  fi
done

"$PYTHON_BIN" experiments/realism_probe.py --compare-only --out "$PROBE_DIR"
