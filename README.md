# Local Two-Speaker Podcast Video Pipeline (English, Offline)

This pipeline converts one NotebookLM English dialogue audio file into a 1080p podcast video with two real speakers.

## Confirmed architecture

1. Audio preprocess (`FFmpeg`)
2. Speaker diarization (`pyannote-audio`)
3. Two independent lip-sync renders (`LatentSync` primary, `VideoRetalking` fallback)
4. Two-speaker composition (`split_screen` / `cut` / `thumbnail`)
5. Speaker-labeled subtitles (`Whisper large-v3` via `faster-whisper`)
6. Final export (`FFmpeg`)

## Entry point

```bash
python /Users/pranamyajain/hindi_podcast_local/run_podcast.py \
  --audio /abs/path/notebooklm_dialogue.wav \
  --out /abs/path/out/episode_001 \
  --layout split_screen
```

## Required local assets

- `assets/speaker_a.png` or short clip still frame for speaker A
- `assets/speaker_b.png` or short clip still frame for speaker B
- `assets/background_1920x1080.png`

## Models and sources (local-only)

1. **pyannote diarization model**
   - Place local model files under: `models/pyannote/speaker-diarization-3.1`
   - Source: Hugging Face `pyannote/speaker-diarization-3.1` (download offline and copy locally)

2. **Whisper large-v3**
   - Place local model files under: `models/whisper/large-v3`
   - Source: Hugging Face `openai/whisper-large-v3` (download offline and copy locally)

3. **LatentSync weights**
   - LatentSync code checkout path: `models/LatentSync`
   - Pinned commit currently used: `a229c3948406bc2cf6eaf4873e662e70c6a04746`
   - Source: [https://github.com/bytedance/LatentSync](https://github.com/bytedance/LatentSync)
   - Download model weights from the LatentSync project release/instructions and place in its expected checkpoint path.

4. **VideoRetalking (fallback)**
   - Expected path: `models/VideoRetalking`
   - Source: install Apache-2.0 release only; keep local weights in repo-expected checkpoint paths.

## License declarations for pipeline dependencies

- `pyannote-audio`: MIT
- `faster-whisper`: MIT
- `torch`: BSD-3-Clause (permissive, allowed)
- `ffmpeg-python`: Apache-2.0
- `Pillow`: HPND-like permissive (PIL Software License)
- `numpy`: BSD-3-Clause
- `PyYAML`: MIT
- `requests`: Apache-2.0
- `LatentSync`: Apache-2.0
- `VideoRetalking` (required fallback): Apache-2.0

## Note on submodule requirement

`git submodule add` requires the project root itself to be a git repository.
Current folder `/Users/pranamyajain/hindi_podcast_local` is not a git repo, so LatentSync was cloned at a pinned commit instead.
After `git init`, convert it with:

```bash
cd /Users/pranamyajain/hindi_podcast_local
git submodule add https://github.com/bytedance/LatentSync.git models/LatentSync
cd models/LatentSync && git checkout a229c3948406bc2cf6eaf4873e662e70c6a04746
```
