# First Run Checklist

## 1. CUDA

```bash
nvidia-smi
./scripts/check_cuda_env.sh
```

Must show an NVIDIA GPU and `cuda_available: True`.

## 2. FFmpeg

```bash
ffmpeg -version
ffprobe -version
```

Both must be on PATH.

## 3. MuseTalk Submodule

```bash
git submodule status
ls models/MuseTalk/scripts/inference.py
```

## 4. MuseTalk Weights

```bash
ls -lh models/MuseTalk/models/musetalkV15/unet.pth
ls -lh models/MuseTalk/models/musetalkV15/musetalk.json
```

## 5. Probe Assets

```bash
ls -lh assets/audio/probe_audio.mp3
ls -lh assets/source_footage/*.mp4
```

## 6. Source-Side Probe

```bash
./run_probe.sh
```

Expected: `outputs/realism_probe/<timestamp>/` with case folders and `MUSE_TALK_COMMANDS.md`.

## 7. MuseTalk Output

```bash
./run_musetalk.sh outputs/realism_probe/<timestamp>
```

Expected per case:

```text
musetalk_output.mp4
comparison_source_vs_lipsync.mp4
difference_heatmap.mp4
```

## 8. Human Review

Open the comparison videos on a phone. Fail the approach if mouth edges, teeth, chin, or temporal flicker are obvious in the first 3-5 seconds.
