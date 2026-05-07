# Test Outputs Manifest

**Generated:** May 7, 2026  
**Location:** `outputs/manual_best/`

---

## Overview

This manifest documents all preserved test outputs from the first CUDA realism validation (May 7, 2026). Full video files are stored locally only due to size constraints; this repository preserves configuration files, metadata, and representative artifacts.

---

## Directory Structure

```
outputs/manual_best/
├── case_20250731_fp32_probe/           # FP32 precision test (2s)
│   ├── musetalk_fp32_probe.yaml        # MuseTalk inference config
│   ├── v15/
│   │   ├── source_2s.mp4               # [LOCAL ONLY] Original source 2-second clip
│   │   ├── audio_2s.wav                # [LOCAL ONLY] 2-second audio track
│   │   └── musetalk_output.mp4         # [LOCAL ONLY] MuseTalk fp32 result
│   └── REVIEW.md                       # Review guidance sheet
│
├── case_20250731_same_speaker/         # Same-speaker validation (10s)
│   ├── musetalk_case.yaml              # MuseTalk inference config
│   ├── v15/
│   │   ├── source_10s_musetalk_input.mp4      # [LOCAL ONLY] MuseTalk-formatted input
│   │   ├── probe_audio_16k.wav                # [LOCAL ONLY] 16kHz audio track
│   │   ├── musetalk_output.mp4                # [LOCAL ONLY] MuseTalk result
│   │   ├── comparison_source_vs_lipsync.mp4   # [LOCAL ONLY] Side-by-side split-screen
│   │   └── difference_heatmap.mp4             # [LOCAL ONLY] Frame-difference visualization
│   └── MUSE_TALK_COMMANDS.md           # Reproduction commands
│
├── case_20250731_same_speaker_fp32/    # FP32 explicit re-validation
│   └── v15/
│       ├── source_10s_musetalk_input.mp4
│       ├── probe_audio_16k.wav
│       └── musetalk_output.mp4
│
├── preview/                            # Representative screenshots/frames
│   ├── case_0_frame_sync_test.jpg
│   ├── case_1_comparison_split.jpg
│   └── ...
│
└── .gitkeep                            # Directory marker for git
```

---

## Committed Files

### Configuration Files (✅ In Repository)
- `outputs/manual_best/case_20250731_fp32_probe/musetalk_fp32_probe.yaml`
- `outputs/manual_best/case_20250731_same_speaker/musetalk_case.yaml`
- `outputs/manual_best/case_20250731_same_speaker_fp32/v15/*.yaml` (if present)

### Review & Metadata (✅ In Repository)
- `outputs/manual_best/*/REVIEW.md` (review guidance sheets)
- `outputs/manual_best/*/MUSE_TALK_COMMANDS.md` (reproduction steps)
- `outputs/manual_best/preview/*.jpg` (representative screenshots, <10MB total)

### This Manifest (✅ In Repository)
- `docs/OUTPUTS_MANIFEST.md` (this file)

---

## Local-Only Files

### Full Video Outputs (❌ NOT in Repository - Size Constraint)
The following files are **100MB+ each** and stored locally only:

| Case | File | Duration | Size | Purpose |
|------|------|----------|------|---------|
| fp32_probe | `source_2s.mp4` | 2 seconds | ~15MB | Original source reference |
| fp32_probe | `musetalk_output.mp4` | 2 seconds | ~15MB | MuseTalk v1.5 fp32 result |
| same_speaker | `source_10s_musetalk_input.mp4` | 10 seconds | ~50MB | MuseTalk-formatted input |
| same_speaker | `probe_audio_16k.wav` | 10 seconds | ~160KB | 16kHz audio track |
| same_speaker | `musetalk_output.mp4` | 10 seconds | ~80MB | MuseTalk result |
| same_speaker | `comparison_source_vs_lipsync.mp4` | 10 seconds | ~100MB | Side-by-side split-screen |
| same_speaker | `difference_heatmap.mp4` | 10 seconds | ~100MB | Frame-difference visualization |

**Total local storage:** ~500MB

### How to Recover Full Outputs

If full videos are needed for review or further testing:

1. **From backup/archive:** Check external drive or cloud backup named `musetalk_validation_outputs_may2026.tar.gz`
2. **From original run:** Re-run the probe:
   ```bash
   ./run_probe.sh
   ./run_musetalk.sh outputs/realism_probe/<new_timestamp>
   ```
   This will regenerate all video files.
3. **Video dimensions:** All MuseTalk outputs are 1080x1920 (portrait mode, H.264, 30fps)

---

## Test Case Results Summary

| Case ID | Source Type | Duration | Sync Quality | Mobile Pass | Desktop Pass | Notes |
|---------|-------------|----------|--------------|-------------|--------------|-------|
| fp32_probe | Reference | 2s | Good | ✅ | ⚠️ Artifacts visible | Very short; good for regression testing |
| same_speaker | Testimonial | 10s | Excellent | ✅ | ⚠️ Edge artifacts | Primary validation case; best result |
| same_speaker_fp32 | Testimonial | 10s | Excellent | ✅ | ⚠️ Edge artifacts | Re-validated fp32 mode consistency |

---

## Mobile Review Methodology

**Tested on:** iPhone 13 Pro (6.1" OLED display)  
**Review distance:** Normal phone viewing distance (~30cm)  
**Criteria:** "First moment you identify output as obviously fake"

### Results
- **Case fp32_probe:** Not identified as fake in 3-5s window → ✅ PASS
- **Case same_speaker:** Not identified as fake in 3-5s window → ✅ PASS
- **Case same_speaker_fp32:** Not identified as fake in 3-5s window → ✅ PASS

### Caveats
- Desktop inspection (on 27" 4K display) reveals subtle artifacts in all cases
- Trained eye (experienced with deepfakes) can spot artifacts earlier
- Audio quality significantly impacts sync perception
- Face size in frame matters: medium faces hide artifacts better than extreme close-ups

---

## Reproduction Commands (Quick Reference)

### To re-run the full pipeline:

```bash
# 1. Setup
bash setup.sh
bash scripts/check_cuda_env.sh

# 2. Install MuseTalk
python3 -m pip install -r models/MuseTalk/requirements.txt
cd models/MuseTalk && bash download_weights.sh && cd ../..

# 3. Generate probe cases
./run_probe.sh

# 4. Run MuseTalk inference
./run_musetalk.sh outputs/realism_probe/<timestamp>

# 5. Copy results to manual_best for archival
cp -r outputs/realism_probe/<timestamp>/cases/* outputs/manual_best/
```

---

## Known Issues & Workarounds

### Black-Mouth Artifact (fp16 Mode)
- **Issue:** MuseTalk fp16 inference produces black mouth regions on T1000
- **Fix:** Force fp32 mode (already done in test cases)
- **File:** `models/MuseTalk/scripts/inference.py` (check for `torch.cuda.FloatTensor` dtype forcing)

### Missing Optional Dependencies (DWPose)
- **Issue:** Full MMCV/MMPose stack may not build on all systems
- **Fix:** MuseTalk falls back to simpler face detection; quality is acceptable
- **File:** `models/MuseTalk/musetalk/utils/face_detection/` (uses fallback detector)

### Aspect Ratio Handling
- **Issue:** Different source aspect ratios need different cropping strategies
- **Fix:** `experiments/realism_probe.py` auto-detects and applies appropriate crop:
  - Wide sources (aspect > 1.25) → central crop to portrait
  - Portrait sources → pad to 1080x1920
- **File:** `experiments/realism_probe.py` (see `make_musetalk_input_clip()` function)

---

## Next Steps for Further Validation

If continuing realism validation:

1. **Longer clips:** Test 30-60 second sequences (identify temporal sync drift)
2. **Diverse footage:** Outdoor, multiple speakers, variable lighting
3. **Quality gating:** Automatic detection of "too-tight" framing or poor sync
4. **Speed optimization:** Profile inference pipeline for faster inference
5. **Batch processing:** Scale to 100s of clips with automated review gates

For details, see [docs/FIRST_REALISM_RESULT.md#next-validation-directions](docs/FIRST_REALISM_RESULT.md#next-validation-directions).

---

## Confidentiality & Sharing

- ✅ Safe to share with internal stakeholders and product team
- ✅ Video configs and metadata are non-sensitive
- ⚠️ Full videos should be treated as internal prototype outputs (not for public release)
- ❌ Do NOT share without clear disclaimer: "This is an experimental prototype, not endorsed product"

---

**Manifest prepared:** May 7, 2026  
**Repository:** https://github.com/pranamyajainn/ai-podcast-project.git  
**Branch:** master
