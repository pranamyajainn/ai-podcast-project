# CUDA Setup

## Recommended OS

- Ubuntu 22.04 LTS or 24.04 LTS
- NVIDIA GPU with CUDA support
- 8GB VRAM minimum for experimentation; 12GB+ preferred

## System Packages

```bash
sudo apt update
sudo apt install -y git git-lfs ffmpeg python3.10 python3.10-venv python3-pip
```

## NVIDIA Requirements

Verify the driver and CUDA runtime:

```bash
nvidia-smi
```

A modern driver compatible with CUDA 11.8+ is recommended. Use the CUDA/PyTorch combination required by upstream MuseTalk if it differs.

## Repo Setup

```bash
git clone --recurse-submodules https://github.com/pranamyajainn/ai-podcast-project.git
cd ai-podcast-project
bash setup.sh
```

## MuseTalk Setup

```bash
python3 -m pip install -r models/MuseTalk/requirements.txt
cd models/MuseTalk
bash download_weights.sh
cd ../..
```

Expected weight location for v1.5:

```text
models/MuseTalk/models/musetalkV15/unet.pth
models/MuseTalk/models/musetalkV15/musetalk.json
```

Run:

```bash
./scripts/check_cuda_env.sh
```

## Common Failures

- `nvidia-smi not found`: NVIDIA driver is missing or container lacks GPU access.
- `torch.cuda.is_available() == False`: wrong PyTorch wheel or CUDA runtime mismatch.
- `unet.pth missing`: MuseTalk weights were not downloaded.
- FFmpeg errors: install a system FFmpeg build with libx264 support.
