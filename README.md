# AI Avatar Podcast Realism Probe

**Status:** CUDA Realism Validation Milestone (May 7, 2026)

## ⚠️ Critical Status Update

**This is NOT a production system.** This repository documents the first successful MuseTalk v1.5 CUDA validation on fixed high-quality source footage.

### What Was Validated
- ✅ MuseTalk v1.5 runs successfully on NVIDIA GPUs (T1000 tested, fp32 mode required)
- ✅ Source footage + mouth-replacement approach produces borderline believable output on mobile
- ✅ Realism threshold reached under **highly constrained conditions**

### What This Does NOT Validate
- ❌ **NOT production-ready:** Artifacts remain visible to trained observers or on desktop inspection
- ❌ **NOT scalable:** Works only with carefully curated source material
- ❌ **NOT deployable:** No quality gating, batch processing, or ethical framework yet
- ❌ **NOT generalizable:** Extreme close-ups, outdoor lighting, multiple speakers all fail

**See [docs/FIRST_REALISM_RESULT.md](docs/FIRST_REALISM_RESULT.md) for full validation report, technical findings, and exact reproduction steps.**

## Current Direction (Experimental)

- Use fixed, high-quality human source footage (indoor, front-facing, professional lighting).
- Preserve the source video's natural head, eye, blink, shoulder, and lighting motion.
- Use MuseTalk only for audio-driven mouth/lip replacement (no full avatar generation).
- Evaluate 10-20 second clips only (longer sequences accumulate temporal drift).
- Optimize for perceived mobile realism on Instagram-size screens, NOT frame-by-frame research metrics.
- **Assume this approach may be abandoned** if scalability or ethical concerns prove insurmountable.

## Repository Structure

```text
project_root/
  app/                    # reserved; no UI in this milestone
  pipeline/               # lightweight reusable helpers
  experiments/            # realism probe generator and review workflow
  assets/                 # local-only media fixture folders
  configs/                # probe definitions and source lists
  scripts/                # setup/check/caption helper scripts
  outputs/                # generated probe outputs, gitignored
  docs/                   # migration and first-run documentation
  requirements/           # base and CUDA/MuseTalk dependency entrypoints
  models/MuseTalk/        # Git submodule, no weights committed
  setup.sh
  run_probe.sh
  run_musetalk.sh
  environment.yml
```

## Quick Start On CUDA Machine

```bash
git clone --recurse-submodules https://github.com/pranamyajainn/ai-podcast-project.git
cd ai-podcast-project
bash setup.sh
```

Place local media fixtures:

```text
assets/audio/probe_audio.mp3
assets/source_footage/ashok_vidyasagar_testimonial.mp4
assets/source_footage/direct_to_camera_indoor.mp4
assets/source_footage/podcast_reference.mp4
assets/source_footage/creator_style_vertical.mp4
```

Run source-side probe generation:

```bash
./run_probe.sh
```

Install MuseTalk CUDA dependencies and weights:

```bash
python3 -m pip install -r models/MuseTalk/requirements.txt
cd models/MuseTalk
bash download_weights.sh
cd ../..
```

Verify CUDA:

```bash
./scripts/check_cuda_env.sh
```

Run MuseTalk for every generated case and build comparisons:

```bash
./run_musetalk.sh outputs/realism_probe/<probe_id>
```

## Expected Outputs

Each probe case produces:

```text
source_15s_original_framing.mp4
source_15s_musetalk_input.mp4
source_15s_cinematic_masked.mp4
musetalk_case.yaml
musetalk_output.mp4                  # after MuseTalk run
comparison_source_vs_lipsync.mp4     # after compare pass
difference_heatmap.mp4               # after compare pass
```

The review rubric is generated as `REVIEW.md` inside each probe output directory.

## Pass/Fail Standard

Pass only if a normal Instagram viewer would not identify the clip as fake within 3-5 seconds on a phone.

Review specifically:

- teeth artifacts
- mouth edge blending
- chin and jaw motion
- blinking consistency
- head-motion preservation
- temporal stability
- compression survival

## Important Constraints & Known Limitations

- No FAL, OmniHuman, Sync.so, Replicate, or hosted inference is used.
- No API keys are required.
- Source media and model weights are not committed.
- MuseTalk requires CUDA; Apple Silicon is only suitable for source preprocessing and packaging.

### Technical Findings (May 2026)

**CRITICAL: fp16 on T1000 produces black-mouth artifacts. Always use fp32 mode.**

Other findings:
- Full DWPose/MMCV body-keypoint stack is optional; MuseTalk falls back gracefully
- Fallback face detection produces acceptable results for mouth-only replacement
- Windows CUDA setup is complex; Ubuntu 22.04 LTS recommended for validation
- Inference speed on T1000 (~10s per 10s clip in fp32) is sufficient for validation, not realtime
- Mouth sync works well, but artifacts at mouth edges remain visible to trained observers

For detailed findings, see [docs/FIRST_REALISM_RESULT.md](docs/FIRST_REALISM_RESULT.md#key-findings).
