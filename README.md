# AI Avatar Podcast Realism Probe

This repository is prepared for migration to a CUDA GPU system. The current milestone is not a SaaS app and not a full pipeline rebuild. The only priority is validating whether high-quality source footage plus MuseTalk mouth replacement can look believable enough for Instagram Reels.

## Current Direction

- Use fixed, high-quality human source footage.
- Preserve the source video's natural head, eye, blink, shoulder, and lighting motion.
- Use MuseTalk only for audio-driven mouth/lip replacement.
- Evaluate 10-20 second clips before committing to a full product rebuild.
- Optimize for perceived mobile realism, not frame-by-frame research metrics.

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

## Important Constraints

- No FAL, OmniHuman, Sync.so, Replicate, or hosted inference is used.
- No API keys are required.
- Source media and model weights are not committed.
- MuseTalk requires CUDA; Apple Silicon is only suitable for source preprocessing and packaging.
