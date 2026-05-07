# Realism Probe

This is a narrow perception test, not a product pipeline.

Goal: determine whether high-quality source footage plus MuseTalk mouth replacement can look believable enough for Instagram Reels before rebuilding the full app.

## Build Source-Side Test Pack

```bash
python3 experiments/realism_probe.py \
  --seconds 15 \
  --sources \
  "/Users/pranamyajain/Downloads/Ashok Vidyasagar Testimonial.mp4" \
  "/Users/pranamyajain/Downloads/VID_20260331_191341000.mp4" \
  "/Users/pranamyajain/Downloads/Podcast_Video_Generation_With_Lip_Sync.mp4" \
  "/Users/pranamyajain/Downloads/WhatsApp Video 2026-05-06 at 16.57.37.mp4"
```

The script writes:

- `source_15s_original_framing.mp4`: raw source framing reference
- `source_15s_musetalk_input.mp4`: vertical MuseTalk-ready input
- `source_15s_cinematic_masked.mp4`: artifact-hiding social-media treatment
- `musetalk_case.yaml`: per-case MuseTalk config
- `MUSE_TALK_COMMANDS.md`: commands to run on a CUDA machine
- `REVIEW.md`: pass/fail rubric

## Run MuseTalk

MuseTalk is not installed in this repo and this Apple Silicon machine has no CUDA. Run the commands from the generated `MUSE_TALK_COMMANDS.md` on a CUDA machine with MuseTalk 1.5 installed.

Expected output per case:

```text
musetalk_output.mp4
```

## Build Comparisons

After copying `musetalk_output.mp4` into each case directory:

```bash
python3 experiments/realism_probe.py \
  --compare-only \
  --out out/realism_probe/<probe_id>
```

This generates:

- `comparison_source_vs_lipsync.mp4`
- `difference_heatmap.mp4`

## Pass/Fail Standard

Pass only if a normal Instagram viewer would not identify the clip as fake within 3-5 seconds on a phone.

Score these failure modes:

- teeth artifacts
- mouth edge blending
- chin and jaw motion
- blinking consistency
- head-motion preservation
- temporal stability
- compression survival

