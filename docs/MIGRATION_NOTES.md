# Migration Notes

## What Was Removed

Removed from the active repo scope:

- FAL/OmniHuman POC code
- FAL-backed UI and templates
- Replicate/SadTalker V1 app code
- old two-speaker Hindi pipeline modules
- Sync.so API experiment code
- generated outputs and temporary renders
- local model weights and large private media
- obsolete configs tied to old architectures

## Why FAL Was Abandoned

FAL/OmniHuman was dropped because the paid run produced unacceptable visual quality and wasted the available test budget. The current client requirement is zero paid API cost and fully open-source/local inference.

## Why MuseTalk Is Current Direction

MuseTalk matches the current product hypothesis better than full avatar generation:

- it modifies a real source video instead of generating the entire human
- it preserves source lighting, head movement, blinking, body motion, and camera texture
- it focuses compute on the mouth region where synchronization matters
- it is open source and suitable for CUDA validation

The hypothesis is that strong source footage plus constrained mouth replacement can cross the Instagram perceived-realism threshold faster than generalized avatar generation.

## Current Architectural Assumptions

- V1 uses fixed curated source footage, not arbitrary avatars.
- Source video quality is the dominant variable.
- Face should stay medium-sized in frame to hide artifacts.
- Cinematic masking is part of the product strategy, not a cosmetic afterthought.
- The realism milestone is a 10-20 second validation clip, not a 3-minute production render.

## Known Limitations

- MuseTalk is not validated yet in this repo because the current machine has no CUDA.
- Source media is not committed because it is large/private and should not be pushed without rights review or Git LFS.
- The current probe uses local fixture filenames; the CUDA machine must place equivalent files under `assets/`.
- The generated MuseTalk output filename may vary by upstream version; `run_musetalk.sh` copies the newest result into `musetalk_output.mp4`.

## Next Validation Goals

1. Run `run_probe.sh` on the CUDA machine.
2. Run MuseTalk v1.5 for all cases.
3. Generate side-by-side and difference videos.
4. Review on a real phone, not desktop only.
5. Decide whether MuseTalk plus source-footage illusion passes the 3-5 second Instagram believability threshold.
