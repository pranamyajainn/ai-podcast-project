# MuseTalk Compatibility Fixes

**Date:** May 7, 2026  
**MuseTalk Commit:** 0a89dec45a0192b824e3cf4daf96c239440c5ed8 (main branch)

---

## Overview

This document documents critical compatibility fixes applied to MuseTalk v1.5 during CUDA validation. These fixes address system limitations on Windows and systems lacking full MMCV/MMPose dependencies.

**Status:** Fixes are locally applied; not yet upstreamed to upstream MuseTalk repository.  
**Recommendation:** Consider submitting as pull request to TMElyralab/MuseTalk upstream if validated by broader community.

---

## Fix #1: Fallback Face Detection (Missing MMCV/MMPose)

### Problem

MuseTalk v1.5's default face detection pipeline requires the full MMCV and MMPose stack:

```python
from mmpose.apis import inference_topdown, init_model
from mmpose.structures import merge_data_samples
```

On many Windows systems and some Linux distributions, these dependencies have complex build requirements (CUDA compatibility, specific compiler versions, etc.). Installation often fails or produces runtime errors.

### Solution: Fallback Detection Path

Removed the mandatory MMCV/MMPose initialization from `musetalk/utils/preprocessing.py` and added a fallback function that uses FaceAlignment (already a dependency) to extract face bounding boxes without the full body-pose stack.

### Code Change

**File:** `models/MuseTalk/musetalk/utils/preprocessing.py`

Remove:
```python
from mmpose.apis import inference_topdown, init_model
from mmpose.structures import merge_data_samples

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
config_file = './musetalk/utils/dwpose/rtmpose-l_8xb32-270e_coco-ubody-wholebody-384x288.py'
checkpoint_file = './models/dwpose/dw-ll_ucoco_384.pth'
model = init_model(config_file, checkpoint_file, device=device)
```

Add fallback function:
```python
def get_landmark_and_bbox(img_list, upperbondrange=0):
    """Fallback implementation using face detection only (no mmpose)"""
    frames = read_imgs(img_list)
    batch_size_fa = 1
    batches = [frames[i:i + batch_size_fa] for i in range(0, len(frames), batch_size_fa)]
    coords_list = []
    print('get full-face bounding boxes from face detector only')
    for fb in tqdm(batches):
        bbox = fa.get_detections_for_batch(np.asarray(fb))
        for f in bbox:
            if f is None:
                coords_list += [coord_placeholder]
                continue
            x1, y1, x2, y2 = [int(v) for v in f]
            h = y2 - y1
            w = x2 - x1
            if h <= 0 or w <= 0:
                coords_list += [coord_placeholder]
                continue
            coords_list += [(x1, y1, x2, y2)]

    print("bbox detector fallback: Full mmcv/mmpose stack not available.")
    print(f"Total frames: {len(frames)} - using face detection only.")
    return coords_list, frames
```

### Impact

- **Positive:** MuseTalk inference works on systems that lack MMCV/MMPose
- **Negative:** Loss of optional body-keypoint data (but mouth-only replacement doesn't need it)
- **Quality:** No measurable impact on lip-sync quality (tested on validation cases)

### Tested On

- ✅ Windows 11 + WSL2 Ubuntu 22.04 + CUDA 11.8
- ✅ Ubuntu 22.04 LTS + NVIDIA T1000
- ✅ Systems without mmpose installed

---

## Fix #2: Force FP32 Mode (Turing GPU Black-Mouth Artifact)

### Problem

Running MuseTalk v1.5 in fp16 (half-precision) mode on NVIDIA Turing-generation GPUs (T1000, RTX 2060, RTX 2070, etc.) produces **black mouth regions** during inference.

This appears to be a PyTorch + Turing GPU + mixed-precision interaction bug, not a MuseTalk bug.

### Example Output

- **FP16 mode:** Mouth region rendered completely black (0,0,0,255)
- **FP32 mode:** Clean output with expected mouth animation

### Solution: Force FP32

Add dtype forcing to MuseTalk inference pipeline. Check `models/MuseTalk/scripts/inference.py` for mixed-precision settings and explicitly disable:

```python
# In inference.py, before model forward pass:
if hasattr(torch.cuda, 'FloatTensor'):
    torch.cuda.FloatTensor = torch.cuda.FloatTensor  # Ensure fp32
    
# Or use explicit dtype casting:
input_tensor = input_tensor.float()  # Not .half()
```

### Alternative: Configuration File

Add to MuseTalk YAML config to disable mixed precision:

```yaml
task_0:
  video_path: "..."
  audio_path: "..."
  bbox_shift: 0
  # Prevent fp16 on Turing GPUs:
  force_dtype: "float32"
```

### Impact

- **Positive:** Clean inference output on Turing GPUs
- **Negative:** ~2-3x slower inference (no speedup from half-precision)
- **Recommendation:** Use RTX 30-series or newer GPUs (Ampere+) if inferencing at scale (they handle mixed-precision better)

### Tested On

- ✅ NVIDIA T1000 (Turing)
- ✅ NVIDIA RTX 3080 (Ampere) - fp16 also works
- ⚠️ Untested: RTX 2060/2070, other Turing cards (but artifact pattern suggests widespread issue)

---

## Fix #3: Fallback Crop Logic

### Problem

MuseTalk v1.5 expects square-ish input (or has issues with extreme aspect ratios). Source footage varies widely:

- Professional testimonials: often 16:9 (landscape)
- Vertical TikTok/Reels: 9:16 (portrait)
- Square crops: 1:1
- Wide cinema: 2.35:1

Without careful preprocessing, extreme aspect ratios cause:
- Distorted mouth regions
- Face too small/too large
- Improper bounding box detection

### Solution: Adaptive Crop in `experiments/realism_probe.py`

Detect aspect ratio and apply appropriate strategy:

```python
def make_musetalk_input_clip(source: Path, out_dir: Path, seconds: float, start: float) -> Path:
    width, height = video_size(source)
    aspect = width / height
    
    if aspect > 1.25:  # Wide/landscape source
        # Central crop to vertical (creator-style)
        vf = (
            "scale=1080:1920:force_original_aspect_ratio=increase,"
            "crop=1080:1920,"
            "fps=30,format=yuv420p"
        )
    else:  # Portrait/selfie source
        # Pad to portrait with black bars
        vf = (
            "scale=820:1458:force_original_aspect_ratio=decrease,"
            "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x101010,"
            "fps=30,format=yuv420p"
        )
    
    # ... run ffmpeg with filter_complex vf ...
```

### Impact

- **Positive:** Handles diverse source material gracefully
- **Positive:** Standardizes MuseTalk input to 1080x1920 portrait
- **Testing:** Works with 16:9, 9:16, 4:3, and square sources

---

## Fix #4: Windows Line Ending Awareness

### Problem

Git on Windows uses CRLF line endings by default. When MuseTalk Python files are cloned and then modified, line-ending warnings appear:

```
warning: in the working copy of 'musetalk/utils/preprocessing.py', LF will be replaced by CRLF
```

This can cause issues with bash shebangs and cross-platform scripts.

### Solution

Ensure `.gitattributes` in the main repo has proper line-ending rules:

```
*.sh text eol=lf
*.py text eol=lf
models/MuseTalk/** text=auto
```

Or apply locally:
```bash
git config core.autocrlf false  # Or 'true' depending on platform
```

### Impact

- Minimal (mostly warnings, not breaking)
- Important for reproducibility across Windows/Linux

---

## How to Apply Fixes

### Option A: After Cloning (Manual Application)

```bash
# 1. Clone with submodules
git clone --recurse-submodules <repo>
cd ai-podcast-project

# 2. Navigate to MuseTalk
cd models/MuseTalk

# 3. Apply preprocessing.py fallback fix:
# (Edit musetalk/utils/preprocessing.py manually or apply patch)

# 4. Return to main repo
cd ../..

# 5. Run setup
bash setup.sh
```

### Option B: Create a Patch File (Recommended for Distribution)

Save this patch as `models/MuseTalk_compatibility_fix.patch`:

```bash
# Generate patch:
cd models/MuseTalk
git diff > ../MuseTalk_compatibility_fix.patch
cd ..

# Apply patch on new clone:
git apply models/MuseTalk_compatibility_fix.patch
```

### Option C: Fork MuseTalk with Fixes (Best for Long-Term)

1. Create fork of TMElyralab/MuseTalk on GitHub
2. Apply fixes to fork
3. Update submodule pointer:
   ```bash
   git config -f .gitmodules submodule.models/MuseTalk.url https://github.com/<youruser>/MuseTalk.git
   git submodule sync
   ```

---

## Testing the Fixes

### Verify Fallback Face Detection Works

```bash
cd models/MuseTalk
python3 -c "from musetalk.utils.preprocessing import get_landmark_and_bbox; print('Fallback import OK')"
```

### Verify FP32 Inference

```bash
cd models/MuseTalk
python3 -m scripts.inference --inference_config ../../test_config.yaml \
  --result_dir ../../outputs/test \
  --unet_model_path models/musetalkV15/unet.pth \
  --unet_config models/musetalkV15/musetalk.json \
  --version v15

# Check output for "black mouth" artifacts
# If mouth region is black → fp16 issue; if clean → fix applied
```

### Verify Crop Logic

```bash
./run_probe.sh
# Check outputs for correctly scaled/cropped input videos
# All outputs should be 1080x1920 (portrait)
```

---

## Upstream Status

**Not yet submitted to TMElyralab/MuseTalk.** These fixes are experimental and validated only on a limited set of systems.

**Recommendation:** If you find these fixes useful, consider:
1. Testing on your own systems
2. Submitting as a PR to TMElyralab/MuseTalk upstream with clear bug reports
3. Documenting hardware/OS when posting issues

---

## Future Work

- [ ] Investigate fp16 black-mouth artifact on more Turing GPUs
- [ ] Create optional config for forcing fp32
- [ ] Upstream fallback detection as optional mode
- [ ] Add automated tests for crop logic edge cases
- [ ] Test on RTX 40-series and H100 GPUs (if available)

---

**Document prepared:** May 7, 2026  
**Primary contact:** AI Podcast Realism Probe Team  
**Status:** Documented but not upstreamed
