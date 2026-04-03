1. **Phase 0: Complete File Inventory**

Assumptions:
- I audited `/Users/pranamyajain/hindi_podcast_local` as the repository root.
- I treated everything under that root as in-scope, including vendored `models/Wav2Lip/.git` metadata and generated `out/` artifacts, because you asked for every file that exists.
- For binary/media/model files, I audited metadata and stream structure with `file`, `stat`, and `ffprobe`; I did not reverse-engineer binary contents.

Counts:
- Total files: `174`
- Total directories: `82`
- Total filesystem entries under repo root: `256`

Recursive inventory:
```text
.
./.gitignore
./README.md
./assets
./assets/README.md
./configs
./configs/default_config.yaml
./docs
./docs/sample_timing_rtx3060.md
./environment.yml
./models
./models/README.md
./models/Wav2Lip
./models/Wav2Lip/.git
./models/Wav2Lip/.git/HEAD
./models/Wav2Lip/.git/config
./models/Wav2Lip/.git/description
./models/Wav2Lip/.git/hooks
./models/Wav2Lip/.git/hooks/applypatch-msg.sample
./models/Wav2Lip/.git/hooks/commit-msg.sample
./models/Wav2Lip/.git/hooks/fsmonitor-watchman.sample
./models/Wav2Lip/.git/hooks/post-update.sample
./models/Wav2Lip/.git/hooks/pre-applypatch.sample
./models/Wav2Lip/.git/hooks/pre-commit.sample
./models/Wav2Lip/.git/hooks/pre-merge-commit.sample
./models/Wav2Lip/.git/hooks/pre-push.sample
./models/Wav2Lip/.git/hooks/pre-rebase.sample
./models/Wav2Lip/.git/hooks/pre-receive.sample
./models/Wav2Lip/.git/hooks/prepare-commit-msg.sample
./models/Wav2Lip/.git/hooks/push-to-checkout.sample
./models/Wav2Lip/.git/hooks/sendemail-validate.sample
./models/Wav2Lip/.git/hooks/update.sample
./models/Wav2Lip/.git/index
./models/Wav2Lip/.git/info
./models/Wav2Lip/.git/info/exclude
./models/Wav2Lip/.git/logs
./models/Wav2Lip/.git/logs/HEAD
./models/Wav2Lip/.git/logs/refs
./models/Wav2Lip/.git/logs/refs/heads
./models/Wav2Lip/.git/logs/refs/heads/master
./models/Wav2Lip/.git/logs/refs/remotes
./models/Wav2Lip/.git/logs/refs/remotes/origin
./models/Wav2Lip/.git/logs/refs/remotes/origin/HEAD
./models/Wav2Lip/.git/objects
./models/Wav2Lip/.git/objects/info
./models/Wav2Lip/.git/objects/pack
./models/Wav2Lip/.git/objects/pack/pack-e451cea97c20da0890252c0081570b559c6f0e29.idx
./models/Wav2Lip/.git/objects/pack/pack-e451cea97c20da0890252c0081570b559c6f0e29.pack
./models/Wav2Lip/.git/objects/pack/pack-e451cea97c20da0890252c0081570b559c6f0e29.rev
./models/Wav2Lip/.git/packed-refs
./models/Wav2Lip/.git/refs
./models/Wav2Lip/.git/refs/heads
./models/Wav2Lip/.git/refs/heads/master
./models/Wav2Lip/.git/refs/remotes
./models/Wav2Lip/.git/refs/remotes/origin
./models/Wav2Lip/.git/refs/remotes/origin/HEAD
./models/Wav2Lip/.git/refs/tags
./models/Wav2Lip/.gitignore
./models/Wav2Lip/README.md
./models/Wav2Lip/__pycache__
./models/Wav2Lip/__pycache__/audio.cpython-310.pyc
./models/Wav2Lip/__pycache__/hparams.cpython-310.pyc
./models/Wav2Lip/audio.py
./models/Wav2Lip/checkpoints
./models/Wav2Lip/checkpoints/README.md
./models/Wav2Lip/checkpoints/wav2lip_gan.pth
./models/Wav2Lip/checkpoints_from_folder
./models/Wav2Lip/checkpoints_from_folder/.DS_Store
./models/Wav2Lip/checkpoints_from_folder/.ipynb_checkpoints
./models/Wav2Lip/checkpoints_from_folder/Wav2Lip-SD-GAN.pt
./models/Wav2Lip/checkpoints_from_folder/Wav2Lip-SD-NOGAN.pt
./models/Wav2Lip/checkpoints_from_folder/listing.txt
./models/Wav2Lip/color_syncnet_train.py
./models/Wav2Lip/evaluation
./models/Wav2Lip/evaluation/README.md
./models/Wav2Lip/evaluation/gen_videos_from_filelist.py
./models/Wav2Lip/evaluation/real_videos_inference.py
./models/Wav2Lip/evaluation/scores_LSE
./models/Wav2Lip/evaluation/scores_LSE/SyncNetInstance_calc_scores.py
./models/Wav2Lip/evaluation/scores_LSE/calculate_scores_LRS.py
./models/Wav2Lip/evaluation/scores_LSE/calculate_scores_real_videos.py
./models/Wav2Lip/evaluation/scores_LSE/calculate_scores_real_videos.sh
./models/Wav2Lip/evaluation/test_filelists
./models/Wav2Lip/evaluation/test_filelists/README.md
./models/Wav2Lip/evaluation/test_filelists/ReSyncED
./models/Wav2Lip/evaluation/test_filelists/ReSyncED/random_pairs.txt
./models/Wav2Lip/evaluation/test_filelists/ReSyncED/tts_pairs.txt
./models/Wav2Lip/evaluation/test_filelists/lrs2.txt
./models/Wav2Lip/evaluation/test_filelists/lrs3.txt
./models/Wav2Lip/evaluation/test_filelists/lrw.txt
./models/Wav2Lip/face_detection
./models/Wav2Lip/face_detection/README.md
./models/Wav2Lip/face_detection/__init__.py
./models/Wav2Lip/face_detection/__pycache__
./models/Wav2Lip/face_detection/__pycache__/__init__.cpython-310.pyc
./models/Wav2Lip/face_detection/__pycache__/api.cpython-310.pyc
./models/Wav2Lip/face_detection/__pycache__/models.cpython-310.pyc
./models/Wav2Lip/face_detection/__pycache__/utils.cpython-310.pyc
./models/Wav2Lip/face_detection/api.py
./models/Wav2Lip/face_detection/detection
./models/Wav2Lip/face_detection/detection/__init__.py
./models/Wav2Lip/face_detection/detection/__pycache__
./models/Wav2Lip/face_detection/detection/__pycache__/__init__.cpython-310.pyc
./models/Wav2Lip/face_detection/detection/__pycache__/core.cpython-310.pyc
./models/Wav2Lip/face_detection/detection/core.py
./models/Wav2Lip/face_detection/detection/sfd
./models/Wav2Lip/face_detection/detection/sfd/__init__.py
./models/Wav2Lip/face_detection/detection/sfd/__pycache__
./models/Wav2Lip/face_detection/detection/sfd/__pycache__/__init__.cpython-310.pyc
./models/Wav2Lip/face_detection/detection/sfd/__pycache__/bbox.cpython-310.pyc
./models/Wav2Lip/face_detection/detection/sfd/__pycache__/detect.cpython-310.pyc
./models/Wav2Lip/face_detection/detection/sfd/__pycache__/net_s3fd.cpython-310.pyc
./models/Wav2Lip/face_detection/detection/sfd/__pycache__/sfd_detector.cpython-310.pyc
./models/Wav2Lip/face_detection/detection/sfd/bbox.py
./models/Wav2Lip/face_detection/detection/sfd/detect.py
./models/Wav2Lip/face_detection/detection/sfd/net_s3fd.py
./models/Wav2Lip/face_detection/detection/sfd/s3fd.pth
./models/Wav2Lip/face_detection/detection/sfd/sfd_detector.py
./models/Wav2Lip/face_detection/models.py
./models/Wav2Lip/face_detection/utils.py
./models/Wav2Lip/filelists
./models/Wav2Lip/filelists/README.md
./models/Wav2Lip/hparams.py
./models/Wav2Lip/hq_wav2lip_train.py
./models/Wav2Lip/inference.py
./models/Wav2Lip/models
./models/Wav2Lip/models/__init__.py
./models/Wav2Lip/models/__pycache__
./models/Wav2Lip/models/__pycache__/__init__.cpython-310.pyc
./models/Wav2Lip/models/__pycache__/conv.cpython-310.pyc
./models/Wav2Lip/models/__pycache__/syncnet.cpython-310.pyc
./models/Wav2Lip/models/__pycache__/wav2lip.cpython-310.pyc
./models/Wav2Lip/models/conv.py
./models/Wav2Lip/models/syncnet.py
./models/Wav2Lip/models/wav2lip.py
./models/Wav2Lip/preprocess.py
./models/Wav2Lip/requirements.txt
./models/Wav2Lip/results
./models/Wav2Lip/results/README.md
./models/Wav2Lip/temp
./models/Wav2Lip/temp/README.md
./models/Wav2Lip/temp/result.avi
./models/Wav2Lip/wav2lip_train.py
./models/licenses
./models/licenses/README.md
./out
./out/.DS_Store
./out/episode_old_rj_1_fallback
./out/episode_old_rj_1_fallback/.DS_Store
./out/episode_old_rj_1_fallback/assets
./out/episode_old_rj_1_fallback/assets/avatar_rgba.png
./out/episode_old_rj_1_fallback/assets/background_1920x1080.png
./out/episode_old_rj_1_fallback/index.html
./out/episode_old_rj_1_fallback/logs
./out/episode_old_rj_1_fallback/logs/http_server.log
./out/episode_old_rj_1_fallback/logs/http_server.pid
./out/episode_old_rj_1_fallback/stage1_audio
./out/episode_old_rj_1_fallback/stage1_audio/preprocessed.wav
./out/episode_old_rj_1_fallback/stage5_subtitles
./out/episode_old_rj_1_fallback/stage5_subtitles/transcript_hi.srt
./out/episode_old_rj_1_fallback/stage5_subtitles/transcript_hi_medium.srt
./out/episode_old_rj_1_fallback/stage6_export
./out/episode_old_rj_1_fallback/stage6_export/final_1080p.mp4
./out/episode_old_rj_1_realhost_web
./out/episode_old_rj_1_realhost_web/final_1080p.mp4
./out/episode_old_rj_1_realhost_web/http_server.log
./out/episode_old_rj_1_realhost_web/http_server.pid
./out/episode_old_rj_1_realhost_web/index.html
./out/episode_old_rj_1_realhost_web/preview_frame.png
./out/episode_old_rj_1_realhost_web/preview_syncfix_final.png
./out/episode_old_rj_1_realhost_web/preview_userface.png
./out/episode_old_rj_1_reallipsync
./out/episode_old_rj_1_reallipsync/assets
./out/episode_old_rj_1_reallipsync/assets/background_real_1920x1080.png
./out/episode_old_rj_1_reallipsync/assets/source_face.jpg
./out/episode_old_rj_1_reallipsync/logs
./out/episode_old_rj_1_reallipsync/logs/wav2lip_infer.log
./out/episode_old_rj_1_reallipsync/stage1_audio
./out/episode_old_rj_1_reallipsync/stage1_audio/preprocessed.wav
./out/episode_old_rj_1_reallipsync/stage3_lipsync
./out/episode_old_rj_1_reallipsync/stage3_lipsync/frame_100.png
./out/episode_old_rj_1_reallipsync/stage3_lipsync/wav2lip_raw.mp4
./out/episode_old_rj_1_reallipsync/stage4_composite
./out/episode_old_rj_1_reallipsync/stage6_export
./out/episode_old_rj_1_reallipsync/stage6_export/final_realhost_1080p.mp4
./out/episode_old_rj_1_refstyle_v3
./out/episode_old_rj_1_refstyle_v3/assets
./out/episode_old_rj_1_refstyle_v3/assets/reference_motion.mp4
./out/episode_old_rj_1_refstyle_v3/calib
./out/episode_old_rj_1_refstyle_v3/calib/audio_12s.wav
./out/episode_old_rj_1_refstyle_v3/calib/calib_auto.log
./out/episode_old_rj_1_refstyle_v3/calib/driver_12s.mp4
./out/episode_old_rj_1_refstyle_v3/calib/out_auto.mp4
./out/episode_old_rj_1_refstyle_v3/logs
./out/episode_old_rj_1_refstyle_v3/logs/wav2lip_infer.log
./out/episode_old_rj_1_refstyle_v3/stage1_audio
./out/episode_old_rj_1_refstyle_v3/stage1_audio/preprocessed.wav
./out/episode_old_rj_1_refstyle_v3/stage2_driver
./out/episode_old_rj_1_refstyle_v3/stage2_driver/ref_driver_92s.mp4
./out/episode_old_rj_1_refstyle_v3/stage2_driver/ref_fwd.mp4
./out/episode_old_rj_1_refstyle_v3/stage2_driver/ref_pingpong.mp4
./out/episode_old_rj_1_refstyle_v3/stage2_driver/ref_rev.mp4
./out/episode_old_rj_1_refstyle_v3/stage3_lipsync
./out/episode_old_rj_1_refstyle_v3/stage3_lipsync/contact_refstyle.png
./out/episode_old_rj_1_refstyle_v3/stage3_lipsync/frame360.png
./out/episode_old_rj_1_refstyle_v3/stage3_lipsync/wav2lip_refstyle.mp4
./out/episode_old_rj_1_refstyle_v3/stage6_export
./out/episode_old_rj_1_syncfix_v2
./out/episode_old_rj_1_syncfix_v2/assets
./out/episode_old_rj_1_syncfix_v2/assets/source_face.png
./out/episode_old_rj_1_syncfix_v2/assets/source_face_1280x720.png
./out/episode_old_rj_1_syncfix_v2/logs
./out/episode_old_rj_1_syncfix_v2/logs/wav2lip_infer.log
./out/episode_old_rj_1_syncfix_v2/stage1_audio
./out/episode_old_rj_1_syncfix_v2/stage1_audio/preprocessed.wav
./out/episode_old_rj_1_syncfix_v2/stage3_lipsync
./out/episode_old_rj_1_syncfix_v2/stage3_lipsync/preview_syncfix.png
./out/episode_old_rj_1_syncfix_v2/stage3_lipsync/wav2lip_syncfix.mp4
./out/episode_old_rj_1_syncfix_v2/stage6_export
./out/episode_old_rj_1_syncfix_v2/stage6_export/final_1080p_syncfix.mp4
./out/episode_old_rj_1_userface_multiframe
./out/episode_old_rj_1_userface_multiframe/.DS_Store
./out/episode_old_rj_1_userface_multiframe/assets
./out/episode_old_rj_1_userface_multiframe/assets/host_image.png
./out/episode_old_rj_1_userface_multiframe/logs
./out/episode_old_rj_1_userface_multiframe/logs/wav2lip_infer.log
./out/episode_old_rj_1_userface_multiframe/stage1_audio
./out/episode_old_rj_1_userface_multiframe/stage1_audio/preprocessed.wav
./out/episode_old_rj_1_userface_multiframe/stage2_driver
./out/episode_old_rj_1_userface_multiframe/stage2_driver/driver_face_92s.mp4
./out/episode_old_rj_1_userface_multiframe/stage2_driver/driver_forward.mp4
./out/episode_old_rj_1_userface_multiframe/stage2_driver/driver_pingpong.mp4
./out/episode_old_rj_1_userface_multiframe/stage2_driver/driver_reverse.mp4
./out/episode_old_rj_1_userface_multiframe/stage3_lipsync
./out/episode_old_rj_1_userface_multiframe/stage3_lipsync/wav2lip_userface.mp4
./out/episode_old_rj_1_userface_multiframe/stage6_export
./out/episode_old_rj_1_userface_multiframe/stage6_export/final_1080p_userface.mp4
./out/reference_inspect
./out/reference_inspect/reference_contact.png
./podcast_pipeline
./podcast_pipeline/__init__.py
./podcast_pipeline/__pycache__
./podcast_pipeline/__pycache__/__init__.cpython-313.pyc
./podcast_pipeline/__pycache__/utils.cpython-313.pyc
./podcast_pipeline/audio.py
./podcast_pipeline/avatar.py
./podcast_pipeline/composite.py
./podcast_pipeline/export.py
./podcast_pipeline/lipsync.py
./podcast_pipeline/subtitles.py
./podcast_pipeline/utils.py
./requirements.txt
./run_podcast.py
./scripts
./scripts/self_check.py
./scripts/setup_env.sh
```

2. **Phase 1: Architecture Reconstruction**

What this system is supposed to be:
- A single-entry local pipeline driven by [`run_podcast.py`](/Users/pranamyajain/hindi_podcast_local/run_podcast.py) that turns one Hindi audio file into a 1080p podcast video.
- Pipeline stages live in `podcast_pipeline/`.
- External local dependencies are FFmpeg, Faster-Whisper model files, a local AUTOMATIC1111 server, and intended local `SadTalker`/`MuseTalk` repos.

What this system actually is:
- The orchestrated product code is the `podcast_pipeline` package plus `run_podcast.py`.
- That orchestrated code is incomplete because the required `models/SadTalker` and `models/MuseTalk` repos do not exist.
- A separate vendored third-party repo, [`models/Wav2Lip`](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip), plus manual output folders under `out/`, records the real experiments that produced the files the user saw.
- The codebase therefore has two architectures:
  1. Intended architecture: `run_podcast.py` -> modular pipeline.
  2. Actual executed architecture during experimentation: ad-hoc FFmpeg + Wav2Lip scripts + hand-built preview HTML.

Module responsibilities:

- [`run_podcast.py`](/Users/pranamyajain/hindi_podcast_local/run_podcast.py)
  - Responsibility: CLI entrypoint and stage orchestration.
  - Input: CLI args, YAML config, input MP3/WAV.
  - Output: stage directories, final MP4, SRT, `run_report.json`.
  - Pattern: orchestrator.

- [`podcast_pipeline/utils.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/utils.py)
  - Responsibility: default config, logging, subprocess execution, GPU detection, JSON output, misc helpers.
  - Input: config path, command args, media path.
  - Output: merged config, logger, subprocess results, ffprobe JSON, VRAM size.
  - Pattern: shared utility layer.

- [`podcast_pipeline/audio.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/audio.py)
  - Responsibility: normalize/convert input audio to 16 kHz mono WAV.
  - Input: source audio path, stage dir, config.
  - Output: `preprocessed.wav` or denoised variant.
  - Pattern: pipeline stage.

- [`podcast_pipeline/avatar.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/avatar.py)
  - Responsibility: generate or reuse avatar/background images.
  - Input: assets dir, config, regen flags.
  - Output: `assets/avatar.png`, `assets/background_1920x1080.png`.
  - Pattern: asset generator/cache.
  - Connection: local HTTP calls to AUTOMATIC1111.

- [`podcast_pipeline/lipsync.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/lipsync.py)
  - Responsibility: call external lipsync backend.
  - Input: WAV, avatar, config, chosen backend, fps.
  - Output: standardized talking-head MP4.
  - Pattern: subprocess adapter.
  - Connection: subprocess into missing `SadTalker` or `MuseTalk`.

- [`podcast_pipeline/composite.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/composite.py)
  - Responsibility: overlay talking-head video on background.
  - Input: background image, talking-head video, audio WAV, config.
  - Output: composited MP4.
  - Pattern: FFmpeg compositor stage.

- [`podcast_pipeline/subtitles.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/subtitles.py)
  - Responsibility: local ASR and SRT creation.
  - Input: WAV, local Faster-Whisper model dir, language.
  - Output: `transcript_hi.srt`.
  - Pattern: ASR stage.

- [`podcast_pipeline/export.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/export.py)
  - Responsibility: burn subtitles and validate final MP4.
  - Input: composited video, audio WAV, SRT, export settings.
  - Output: final `final_1080p.mp4`.
  - Pattern: finalizer/validator.

- [`scripts/self_check.py`](/Users/pranamyajain/hindi_podcast_local/scripts/self_check.py)
  - Responsibility: environment validation.
  - Input: config path, strict flag.
  - Output: exit code and printed checks.
  - Pattern: diagnostic tool.

- [`models/Wav2Lip/inference.py`](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/inference.py)
  - Responsibility: third-party lip-sync inference.
  - Input: face image/video, audio, checkpoint, padding/crop/box controls.
  - Output: lip-synced MP4.
  - Pattern: vendored inference tool.
  - Connection: used in actual experiments, not wired into `run_podcast.py`.

Text dependency graph:

```text
run_podcast.py
  -> podcast_pipeline.utils.load_config
  -> podcast_pipeline.utils.setup_logger
  -> podcast_pipeline.utils.probe_audio_duration
  -> podcast_pipeline.utils.detect_gpu_vram_gb
  -> podcast_pipeline.utils.choose_lipsync_backend
  -> podcast_pipeline.audio.preprocess_audio
      -> ffmpeg
  -> podcast_pipeline.avatar.ensure_avatar
      -> podcast_pipeline.avatar._generate_via_sd_api
          -> requests -> local AUTOMATIC1111 HTTP API
  -> podcast_pipeline.avatar.ensure_background
      -> podcast_pipeline.avatar._generate_via_sd_api
          -> requests -> local AUTOMATIC1111 HTTP API
  -> podcast_pipeline.lipsync.generate_talking_head
      -> podcast_pipeline.lipsync._run_backend
          -> subprocess -> models/SadTalker/inference.py OR models/MuseTalk/inference.py
      -> ffmpeg standardization
  -> podcast_pipeline.composite.composite_video
      -> ffmpeg overlay
  -> podcast_pipeline.subtitles.generate_hindi_srt
      -> faster_whisper.WhisperModel(local_files_only=True)
  -> podcast_pipeline.export.burn_subtitles_and_export
      -> ffmpeg subtitle burn-in
      -> podcast_pipeline.export.validate_youtube_specs
          -> podcast_pipeline.utils.ffprobe_streams
              -> ffprobe
  -> podcast_pipeline.utils.write_json

scripts/self_check.py
  -> torch import
  -> faster_whisper import
  -> path existence checks for whisper model / SD checkpoint / SadTalker / MuseTalk

Actual experiment path under out/
  -> manual preprocessing WAVs
  -> vendored models/Wav2Lip/inference.py
      -> models/Wav2Lip/audio.py
      -> models/Wav2Lip/models/*
      -> models/Wav2Lip/face_detection/*
      -> ffmpeg muxing
  -> manual preview HTML + python HTTP server logs/pid files
```

Intended data flow:
`audio input` -> `preprocessed.wav` -> `avatar/background` -> `talkinghead.mp4` -> `composited.mp4` -> `transcript_hi.srt` -> `final_1080p.mp4`

Actual observed data flow in generated artifacts:
`audio input` -> `preprocessed.wav` -> `manual source image / manual driver video` -> `models/Wav2Lip/inference.py` -> `wav2lip_*.mp4` -> optional upscale/composite -> preview HTML served locally

3. **Phase 2: File-by-File Deep Analysis**

I split this into source/config/docs, vendored third-party code, vendored metadata/binaries, and generated artifacts. Every file is covered.

### Core source and config

### [/.gitignore](/Users/pranamyajain/hindi_podcast_local/.gitignore)
- Metadata: root git ignore file; excludes virtualenv, caches, `out/`, `models/`, logs, generated assets.
- Code: none.
- Quality: project state contradicts it; `models/` and `out/` are present anyway. This is evidence of tracked/generated drift.
- Evolution: file says repo intended to stay clean; current tree does not.

### [/README.md](/Users/pranamyajain/hindi_podcast_local/README.md)
- Metadata: primary project documentation.
- Code analysis: documents setup, offline model placement, expected pipeline, CLI usage.
- Quality:
  - Claims end-to-end local pipeline, but required `SadTalker` and `MuseTalk` repos are absent.
  - Claims AUTOMATIC1111 or ComfyUI support; code implements only AUTOMATIC1111.
  - Claims license records under `models/licenses`; only a placeholder README exists.
- Evolution: reflects intended product, not current executable reality.

### [/assets/README.md](/Users/pranamyajain/hindi_podcast_local/assets/README.md)
- Metadata: asset placement note.
- Code: none.
- Quality: accurate but minimal; does not mention that avatar/background are generated through local HTTP API.
- Evolution: starter-template doc.

### [/configs/default_config.yaml](/Users/pranamyajain/hindi_podcast_local/configs/default_config.yaml)
- Metadata: YAML config mirror of defaults.
- Code analysis: sets seed, audio, avatar/background prompts, A1111 endpoint, lipsync backend paths, subtitle styling, export parameters.
- Hardcoded assumptions: `http://127.0.0.1:7860`, RealisticVision checkpoint name, missing repo paths `models/SadTalker` and `models/MuseTalk`.
- Quality:
  - Duplicates defaults already hardcoded in [`podcast_pipeline/utils.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/utils.py), so config is split across code and YAML.
  - Includes unsupported branches: config implies both backends are usable; repo contents contradict this.
- Evolution: starter config never reconciled with actual manual Wav2Lip path.

### [/docs/sample_timing_rtx3060.md](/Users/pranamyajain/hindi_podcast_local/docs/sample_timing_rtx3060.md)
- Metadata: performance note.
- Code: none.
- Quality: aspirational only; there is no automated benchmark harness and current clean repo cannot run stage 3.
- Evolution: documentation-first artifact.

### [/environment.yml](/Users/pranamyajain/hindi_podcast_local/environment.yml)
- Metadata: Conda environment spec.
- Code analysis: pins Python 3.10, FFmpeg 6.1, PyTorch 2.4.*, CUDA 12.1, then pip-installs root requirements.
- Quality:
  - Conflicts with root `requirements.txt` pin of `torch==2.4.1`.
  - Does not include Wav2Lip’s older dependency stack.
- Evolution: written for orchestrator, not vendored Wav2Lip.

### [/models/README.md](/Users/pranamyajain/hindi_podcast_local/models/README.md)
- Metadata: model placement instructions.
- Quality: incomplete; repo does not include the documented model tree for whisper, SadTalker, MuseTalk, or SD checkpoints.
- Evolution: placeholder.

### [/models/licenses/README.md](/Users/pranamyajain/hindi_podcast_local/models/licenses/README.md)
- Metadata: placeholder for license records.
- Quality: empty of actual license evidence. This means license compliance is not documented in-repo.
- Evolution: intent existed; execution did not.

### [/environment requirements.txt](/Users/pranamyajain/hindi_podcast_local/requirements.txt)
- Metadata: root pip requirements.
- Code analysis: `PyYAML`, `requests`, `Pillow`, `numpy`, `faster-whisper`, `torch`.
- Quality:
  - Missing deps for vendored Wav2Lip path: `librosa`, `scipy`, `opencv-python`, `tqdm`, `numba`, `python_speech_features`, possibly `dlib`.
  - Root and vendored dependency stacks are incompatible.
- Evolution: supports orchestrator only.

### [/run_podcast.py](/Users/pranamyajain/hindi_podcast_local/run_podcast.py)
- Metadata: main entrypoint.
- Code analysis:
  - `parse_args()`: CLI parsing.
  - `resolve_path()`: absolute/relative resolution.
  - `validate_input_audio()`: existence, extension, duration check.
  - `run_self_check()`: binary/model/repo presence checks.
  - `cleanup_intermediate_dirs()`: deletes stage dirs.
  - `main()`: end-to-end orchestration.
  - `_resolve_backend_paths()`: rewrites backend repo dirs absolute.
  - `_resolve_whisper_path()`: rewrites whisper model path absolute.
- Inputs/outputs: consumes CLI/config/audio, emits stage files and report JSON.
- External dependencies: imports every pipeline module and utility helper.
- Hardcoded assumptions:
  - Only `.mp3` and `.wav` accepted.
  - Hard max audio length 180s.
  - Stage names and output file names fixed.
- Quality:
  - Hard dependency on CUDA via [`utils.detect_gpu_vram_gb()`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/utils.py#L248).
  - Self-check does not validate AUTOMATIC1111 reachability.
  - MuseTalk fallback to SadTalker only helps if SadTalker repo exists; it does not.
- Evolution: architecture is modular and deliberate; actual repo contents never caught up.

### [/podcast_pipeline/__init__.py](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/__init__.py)
- Metadata: package export list.
- Code: exports module names only.
- Quality: fine.
- Evolution: minimal package scaffolding.

### [/podcast_pipeline/audio.py](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/audio.py)
- Metadata: audio preprocessing stage.
- Code analysis:
  - `preprocess_audio()`: runs FFmpeg loudnorm/high-pass and optional `afftdn`.
- Inputs/outputs: input audio -> `preprocessed.wav` or denoised version.
- Dependencies: FFmpeg via `run_command`.
- Hardcoded assumptions: high-pass at 20 Hz, 16 kHz mono, loudnorm target `I=-16:TP=-1.5:LRA=11`.
- Quality:
  - No cache reuse; always rewrites.
  - No audio quality validation after preprocessing.
- Evolution: simple and functional.

### [/podcast_pipeline/avatar.py](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/avatar.py)
- Metadata: avatar/background generator.
- Code analysis:
  - `ensure_avatar()`: cache or generate avatar.
  - `ensure_background()`: cache or generate background.
  - `_generate_via_sd_api()`: local A1111 txt2img.
  - `_set_checkpoint()`: mutate A1111 model checkpoint.
  - `_validate_image()`: min size check.
- Dependencies: `requests`, `PIL.Image`.
- Hardcoded assumptions:
  - Only `runner=automatic1111` is implemented at [`avatar.py` lines 95-101](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/avatar.py#L95).
  - Local HTTP endpoint must exist.
  - Changes global A1111 checkpoint state.
- Quality:
  - No retry/backoff on HTTP calls.
  - No isolation across concurrent runs.
  - Documentation implies ComfyUI option; code does not support it.
- Evolution: built as a “starter pipeline” and stopped there.

### [/podcast_pipeline/composite.py](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/composite.py)
- Metadata: FFmpeg compositor.
- Code analysis:
  - `composite_video()`: scales talking-head video and overlays onto static background.
- Inputs/outputs: background PNG + talking-head MP4 + WAV -> composited MP4.
- Dependencies: FFmpeg.
- Hardcoded assumptions: fixed overlay width/x/y from config; no keying or segmentation.
- Quality:
  - Assumes static PiP composition is acceptable.
  - No check for talking-head aspect mismatch beyond FFmpeg scaling.
- Evolution: robust but basic.

### [/podcast_pipeline/export.py](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/export.py)
- Metadata: subtitle burn-in and final validation.
- Code analysis:
  - `burn_subtitles_and_export()`
  - `validate_youtube_specs()`
  - `_parse_fps()`
  - `_escape_filter_path()`
- Dependencies: FFmpeg, ffprobe.
- Hardcoded assumptions: H.264, AAC, `yuv420p`, `+faststart`, subtitle style fields.
- Quality:
  - Validation checks resolution/codecs/fps only; it does not verify `faststart` despite exporting with it. See [`export.py` lines 94-124](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/export.py#L94).
  - No validation that subtitles were actually rendered.
- Evolution: functional but incomplete validator.

### [/podcast_pipeline/lipsync.py](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/lipsync.py)
- Metadata: backend adapter.
- Code analysis:
  - `generate_talking_head()`: call backend then standardize with FFmpeg.
  - `_run_backend()`: constructs SadTalker or MuseTalk CLI calls.
  - `_find_latest_video()`: find newest media file in output dir.
- Dependencies: FFmpeg, external repos.
- Hardcoded assumptions:
  - Backend names limited to `sadtalker` / `musetalk`.
  - Entry point named `inference.py`.
  - Raw backend output can be detected by suffix scan.
- Quality:
  - Fatal on clean repo because required repos are absent at [`lipsync.py` lines 74-86](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/lipsync.py#L74).
  - No schema/contract validation of backend outputs.
- Evolution: intended abstraction layer not matched by repo contents.

### [/podcast_pipeline/subtitles.py](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/subtitles.py)
- Metadata: Hindi subtitle stage.
- Code analysis:
  - `generate_hindi_srt()`: load local faster-whisper model and transcribe.
  - `_write_srt()`: serialize segments.
  - `_format_srt_time()`
  - `_cuda_available()`
- Dependencies: `faster_whisper`, `torch` optionally.
- Hardcoded assumptions:
  - Output file name is always `transcript_hi.srt` at [`subtitles.py` line 48](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/subtitles.py#L48), even if `language != hi`.
- Quality:
  - SRT numbering bug: blank segments consume indexes because `enumerate()` happens before empty-text skip at [`subtitles.py` lines 58-64](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/subtitles.py#L58).
  - Uses CPU fallback even though product constraint says GPU required.
- Evolution: implementation exists, polish missing.

### [/podcast_pipeline/utils.py](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/utils.py)
- Metadata: shared utility module.
- Code analysis:
  - `DEFAULT_CONFIG`, `StageStat`, `PipelineError`, `StageTimer`
  - config merge/load, logging, dir/binary checks
  - `run_command()`, `ffprobe_streams()`, `probe_audio_duration()`
  - GPU detection via torch then `nvidia-smi`
  - backend chooser, JSON writer, misc helpers
- Dependencies: `json`, `logging`, `subprocess`, `yaml`, `torch` optional.
- Hardcoded assumptions:
  - `backend_auto_threshold_gb=12`
  - `RealisticVisionV60B1_v51HyperVAE.safetensors`
  - strict CUDA requirement at [`utils.py` lines 248-257](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/utils.py#L248).
- Quality:
  - `load_config()` silently returns defaults if config file missing.
  - `run_command()` has no timeout.
  - `ffprobe_streams()` raises raw `CalledProcessError`, not wrapped `PipelineError`.
  - `copy_if_needed()`, `as_posix()`, `list_relative_paths()` are currently unused.
- Evolution: generic starter utils with some unused carry-over.

### [/scripts/self_check.py](/Users/pranamyajain/hindi_podcast_local/scripts/self_check.py)
- Metadata: environment check script.
- Code analysis:
  - `parse_args()`, `resolve_path()`, `main()`
  - checks binaries, imports, model/repo paths.
- Dependencies: `torch`, `faster_whisper`, `shutil`, `Path`.
- Quality:
  - Does not verify local A1111 server availability.
  - Only checks repo/entrypoint existence, not backend weights/model internals.
- Evolution: useful but incomplete health check.

### [/scripts/setup_env.sh](/Users/pranamyajain/hindi_podcast_local/scripts/setup_env.sh)
- Metadata: bootstrap shell script.
- Code: creates `.venv`, upgrades pip, installs root requirements.
- Quality:
  - Does not install FFmpeg, CUDA stack, Faster-Whisper models, A1111, SadTalker, MuseTalk, or Wav2Lip deps.
- Evolution: minimal bootstrap, not a reproducible environment builder.

### Vendored Wav2Lip source

### [/models/Wav2Lip/.gitignore](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.gitignore)
- Metadata: vendored project ignore rules.
- Quality: standard ignore file; not used by root repo behavior.
- Evolution: upstream carry-over.

### [/models/Wav2Lip/README.md](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/README.md)
- Metadata: vendored upstream README.
- Quality:
  - Contains commercial Sync API instructions requiring an API key at lines 3-90.
  - Open-source section explicitly states non-commercial restriction at lines 228-230 and 308-310.
  - This alone violates the user’s required permissive-license constraint.
- Evolution: upstream README with newer commercial overlay plus old OSS docs.

### [/models/Wav2Lip/audio.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/audio.py)
- Metadata: vendored audio feature extraction.
- Code analysis: waveform load/save, preemphasis, STFT, spectrograms, mel basis creation, normalization.
- Dependencies: `librosa`, `scipy`, `numpy`, vendored `hparams`.
- Quality:
  - `save_wavenet_wav()` uses deprecated `librosa.output.write_wav`.
  - `_stft()` calls `_lws_processor(hp)` even though `_lws_processor()` takes no args at [`audio.py` lines 53-60](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/audio.py#L53).
  - Mixed indentation around `_build_mel_basis()`.
- Evolution: locally modified to use keyword args in `librosa.filters.mel`.

### [/models/Wav2Lip/hparams.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/hparams.py)
- Metadata: vendored hyperparameters.
- Code analysis: `get_image_list`, `HParams`, global `hparams`, `hparams_debug_string`.
- Hardcoded assumptions:
  - `img_size=96`, `fps=25`, `batch_size=16`, `num_workers=16`
  - absurd `nepochs=200000000000000000`
- Quality:
  - `hparams_debug_string()` calls `hparams.values()`, which does not exist on `HParams`, so it is broken at [`hparams.py` lines 98-100](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/hparams.py#L98).
  - Indentation is inconsistent around lines 85-87.
- Evolution: upstream training config, not adapted to current environment.

### [/models/Wav2Lip/color_syncnet_train.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/color_syncnet_train.py)
- Metadata: SyncNet discriminator training script.
- Code analysis: dataset loading, cosine loss, train/eval loops, checkpointing, checkpoint load.
- Dependencies: torch, numpy, cv2, audio/hparams/models.
- Quality:
  - Training-only; unused by product.
  - Assumes dataset/filelists exist.
- Evolution: pure upstream training path.

### [/models/Wav2Lip/hq_wav2lip_train.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/hq_wav2lip_train.py)
- Metadata: Wav2Lip+GAN training script.
- Code analysis: GAN discriminator loss path, training loop, checkpointing.
- Quality: training-only, environment mismatch with root.
- Evolution: upstream.

### [/models/Wav2Lip/preprocess.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/preprocess.py)
- Metadata: dataset preprocessor.
- Code analysis: frame extraction/audio extraction for LRS2-style training data.
- Quality: unused by product; assumes dataset layout.
- Evolution: upstream training support.

### [/models/Wav2Lip/wav2lip_train.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/wav2lip_train.py)
- Metadata: non-GAN Wav2Lip training script.
- Code analysis: dataset, train/eval, SyncNet loss integration, checkpoints.
- Quality: training-only; not compatible with root environment without extra deps.
- Evolution: upstream.

### [/models/Wav2Lip/inference.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/inference.py)
- Metadata: core vendored inference script.
- Code analysis:
  - arg parsing
  - smoothing boxes
  - batched face detect or fixed box
  - mel chunking
  - model loading
  - AVI writer and ffmpeg mux
- Quality:
  - Uses shell-string FFmpeg commands.
  - Writes fixed `temp/result.avi`.
  - Visible seam artifacts are expected when using fixed `--box`.
  - Filename parsing uses `split('.')[1]`, unsafe for multiple dots.
  - Local modifications load TorchScript archives and force `weights_only=False`; not documented.
- Evolution: this is the actual path used in experiments.

### [/models/Wav2Lip/models/__init__.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/models/__init__.py)
- Metadata: model export file.
- Code: exports `Wav2Lip`, `Wav2Lip_disc_qual`, `SyncNet_color`.
- Quality: fine.

### [/models/Wav2Lip/models/conv.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/models/conv.py)
- Metadata: small conv block library.
- Code analysis: `Conv2d`, `nonorm_Conv2d`, `Conv2dTranspose`.
- Quality: standard upstream helper.

### [/models/Wav2Lip/models/syncnet.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/models/syncnet.py)
- Metadata: SyncNet audio/face encoder.
- Code analysis: `SyncNet_color`.
- Quality: training/inference component; not directly wrong.

### [/models/Wav2Lip/models/wav2lip.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/models/wav2lip.py)
- Metadata: model architecture definitions.
- Code analysis: `Wav2Lip`, `Wav2Lip_disc_qual`.
- Quality:
  - `Wav2Lip_disc_qual.perceptual_forward()` hardcodes `.cuda()` at line 172 equivalent, breaking CPU-only discriminator use.
  - Architecture itself is upstream.
- Evolution: upstream.

### [/models/Wav2Lip/face_detection/README.md](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/README.md)
- Metadata: provenance note for face detection code.
- Quality: accurate.

### [/models/Wav2Lip/face_detection/__init__.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/__init__.py)
- Metadata: package init.
- Code: exports `FaceAlignment`, enums.
- Quality: fine.

### [/models/Wav2Lip/face_detection/api.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/api.py)
- Metadata: face detection API wrapper.
- Code analysis: enums and `FaceAlignment.get_detections_for_batch`.
- Quality:
  - Only detection path is used; landmark enums are vestigial here.
  - Uses dynamic import string `face_detection.detection.<detector>`.
- Evolution: adapted from `face_alignment`.

### [/models/Wav2Lip/face_detection/detection/__init__.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/__init__.py)
- Metadata: subpackage init.
- Code: exports `FaceDetector`.
- Quality: fine.

### [/models/Wav2Lip/face_detection/detection/core.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/core.py)
- Metadata: abstract face detector base.
- Code analysis: constructor, `detect_from_directory`, tensor/path conversion.
- Quality:
  - Uses undefined `logger` in one branch if invalid device and not verbose.
  - Abstract base only; product uses subclass.
- Evolution: borrowed upstream.

### [/models/Wav2Lip/face_detection/detection/sfd/__init__.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/sfd/__init__.py)
- Metadata: exports SFD detector class alias.
- Quality: fine.

### [/models/Wav2Lip/face_detection/detection/sfd/bbox.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/sfd/bbox.py)
- Metadata: bbox math helpers.
- Code analysis: IOU fallback, encode/decode, NMS.
- Quality: utility code; no product-specific issues.

### [/models/Wav2Lip/face_detection/detection/sfd/detect.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/sfd/detect.py)
- Metadata: SFD inference helpers.
- Code analysis: `detect`, `batch_detect`, `flip_detect`, `pts_to_bb`.
- Quality:
  - Threshold `> 0.05` is hardcoded.
  - Returns zero arrays instead of explicit “no detections”, so callers must interpret carefully.
- Evolution: upstream.

### [/models/Wav2Lip/face_detection/detection/sfd/net_s3fd.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/sfd/net_s3fd.py)
- Metadata: S3FD network definition.
- Code analysis: `L2Norm`, `s3fd`.
- Quality: vendored model architecture.

### [/models/Wav2Lip/face_detection/detection/sfd/sfd_detector.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/sfd/sfd_detector.py)
- Metadata: SFD detector implementation.
- Code analysis: model load and batch detection wrapper.
- Quality: depends on `s3fd.pth` presence; no graceful recovery if absent.

### [/models/Wav2Lip/face_detection/models.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/models.py)
- Metadata: FAN/ResNet landmark model defs.
- Code analysis: `conv3x3`, `ConvBlock`, `Bottleneck`, `HourGlass`, `FAN`, `ResNetDepth`.
- Quality: not used in current Wav2Lip inference path; vendored.

### [/models/Wav2Lip/face_detection/utils.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/utils.py)
- Metadata: heatmap/crop utility funcs.
- Code analysis: gaussian drawing, transforms, crop, get_preds, flip, appdata path.
- Quality:
  - Uses deprecated `np.int`.
  - Large upstream helper set; much of it is unused by current inference.
- Evolution: borrowed upstream.

### [/models/Wav2Lip/evaluation/README.md](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/README.md)
- Metadata: evaluation instructions.
- Quality:
  - Requires separate external `syncnet_python` repo and extra env.
  - Not usable from this repo alone.
- Evolution: upstream evaluation docs.

### [/models/Wav2Lip/evaluation/gen_videos_from_filelist.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/gen_videos_from_filelist.py)
- Metadata: evaluation video generation script.
- Code analysis: loads filelist, extracts temp audio, runs face detect, datagen, Wav2Lip inference, muxes output.
- Quality:
  - Uses shell FFmpeg commands.
  - Hardcodes temp paths `../temp/temp.wav` and `../temp/result.avi`.
  - Skips NaN mel clips silently.
- Evolution: evaluation helper, not product code.

### [/models/Wav2Lip/evaluation/real_videos_inference.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/real_videos_inference.py)
- Metadata: real-video evaluation generator.
- Code analysis: rescaling heuristic, face detect, frame duplication, Wav2Lip inference.
- Quality:
  - Multiple hardcoded thresholds.
  - Uses shell FFmpeg and temp files.
  - Evaluation-only.
- Evolution: upstream.

### [/models/Wav2Lip/evaluation/scores_LSE/SyncNetInstance_calc_scores.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/scores_LSE/SyncNetInstance_calc_scores.py)
- Metadata: LSE-D/LSE-C score calculator.
- Code analysis: `calc_pdist`, `SyncNetInstance`.
- Quality:
  - Hardcodes `.cuda()` in constructor and feature paths.
  - Hardcodes 224x224 resize with comment “CHANGE BEFORE RELEASE”.
  - Uses external `SyncNetModel` not present in this repo.
- Evolution: upstream evaluation utility.

### [/models/Wav2Lip/evaluation/scores_LSE/calculate_scores_LRS.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/scores_LSE/calculate_scores_LRS.py)
- Metadata: batch scoring wrapper.
- Code analysis: loads `SyncNetInstance`, globs MP4s, averages scores.
- Quality: requires external `syncnet_v2.model`; not reproducible from this repo.

### [/models/Wav2Lip/evaluation/scores_LSE/calculate_scores_real_videos.py](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/scores_LSE/calculate_scores_real_videos.py)
- Metadata: score wrapper for real-videos pipeline.
- Code analysis: resolves temp dirs, globs crop AVIs, prints scores.
- Quality: depends on external preprocessing pipeline not included here.

### [/models/Wav2Lip/evaluation/scores_LSE/calculate_scores_real_videos.sh](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/scores_LSE/calculate_scores_real_videos.sh)
- Metadata: shell wrapper.
- Quality:
  - Calls `run_pipeline.py`, which is not present in this repo.
  - Hard fail if used.
- Evolution: broken upstream helper in current vendored snapshot.

### [/models/Wav2Lip/evaluation/test_filelists/README.md](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/test_filelists/README.md)
- Metadata: filelist doc.
- Quality: documentation only.

### [/models/Wav2Lip/evaluation/test_filelists/ReSyncED/random_pairs.txt](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/test_filelists/ReSyncED/random_pairs.txt)
- Metadata: evaluation pair list.
- Code: none.
- Quality: data file only.

### [/models/Wav2Lip/evaluation/test_filelists/ReSyncED/tts_pairs.txt](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/test_filelists/ReSyncED/tts_pairs.txt)
- Metadata: evaluation pair list.
- Quality: data only.

### [/models/Wav2Lip/evaluation/test_filelists/lrs2.txt](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/test_filelists/lrs2.txt)
- Metadata: large upstream evaluation file list.
- Quality: data only.

### [/models/Wav2Lip/evaluation/test_filelists/lrs3.txt](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/test_filelists/lrs3.txt)
- Metadata: large upstream evaluation file list.
- Quality: data only.

### [/models/Wav2Lip/evaluation/test_filelists/lrw.txt](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/test_filelists/lrw.txt)
- Metadata: large upstream evaluation file list.
- Quality: data only.

### [/models/Wav2Lip/filelists/README.md](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/filelists/README.md)
- Metadata: training filelist placeholder note.
- Quality: documentation only.

### [/models/Wav2Lip/checkpoints/README.md](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/checkpoints/README.md)
- Metadata: checkpoint placeholder note.
- Quality: documentation only.

### [/models/Wav2Lip/checkpoints_from_folder/listing.txt](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/checkpoints_from_folder/listing.txt)
- Metadata: failed `gdown` command output.
- Quality: evidence of incomplete model-download workflow; not a valid manifest.
- Evolution: setup attempt failed and was committed.

### [/models/Wav2Lip/results/README.md](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/results/README.md)
- Metadata: placeholder note for results folder.
- Quality: documentation only.

### [/models/Wav2Lip/temp/README.md](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/temp/README.md)
- Metadata: placeholder note for temp folder.
- Quality: accurate.

### [/models/Wav2Lip/requirements.txt](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/requirements.txt)
- Metadata: vendored dependency pins.
- Quality:
  - Pins `torch==1.1.0`, `librosa==0.7.0`, old OpenCV.
  - Incompatible with root environment.
- Evolution: upstream old stack.

### Vendored Wav2Lip metadata, git internals, models, and caches

### [/models/Wav2Lip/.git/HEAD](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/HEAD)
- Metadata: nested git HEAD.
- Quality: proves vendored repo was cloned, not flattened.

### [/models/Wav2Lip/.git/config](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/config)
- Metadata: nested git config.
- Quality: points to upstream origin `https://github.com/Rudrabha/Wav2Lip.git`; nested git inside parent repo is a maintenance risk.

### [/models/Wav2Lip/.git/description](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/description)
- Metadata: default git description.
- Quality: irrelevant runtime-wise.

### [/models/Wav2Lip/.git/info/exclude](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/info/exclude)
- Metadata: default git exclude.
- Quality: irrelevant runtime-wise.

### [/models/Wav2Lip/.git/logs/HEAD](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/logs/HEAD)
- Metadata: clone log.
- Quality: leaks personal username/email in repository content.

### [/models/Wav2Lip/.git/logs/refs/heads/master](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/logs/refs/heads/master)
- Metadata: clone log.
- Quality: same privacy leak.

### [/models/Wav2Lip/.git/logs/refs/remotes/origin/HEAD](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/logs/refs/remotes/origin/HEAD)
- Metadata: clone log.
- Quality: same privacy leak.

### [/models/Wav2Lip/.git/packed-refs](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/packed-refs)
- Metadata: git refs metadata.
- Quality: irrelevant runtime-wise.

### [/models/Wav2Lip/.git/refs/heads/master](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/refs/heads/master)
- Metadata: commit pointer.
- Quality: vendored git state.

### [/models/Wav2Lip/.git/refs/remotes/origin/HEAD](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/refs/remotes/origin/HEAD)
- Metadata: remote HEAD pointer.
- Quality: vendored git state.

### [/models/Wav2Lip/.git/hooks/applypatch-msg.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/applypatch-msg.sample)
- Metadata: stock git sample hook.
- Code: no product role.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/hooks/commit-msg.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/commit-msg.sample)
- Metadata: stock sample hook.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/hooks/fsmonitor-watchman.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/fsmonitor-watchman.sample)
- Metadata: stock sample hook.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/hooks/post-update.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/post-update.sample)
- Metadata: stock sample hook.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/hooks/pre-applypatch.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/pre-applypatch.sample)
- Metadata: stock sample hook.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/hooks/pre-commit.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/pre-commit.sample)
- Metadata: stock sample hook.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/hooks/pre-merge-commit.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/pre-merge-commit.sample)
- Metadata: stock sample hook.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/hooks/pre-push.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/pre-push.sample)
- Metadata: stock sample hook.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/hooks/pre-rebase.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/pre-rebase.sample)
- Metadata: stock sample hook.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/hooks/pre-receive.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/pre-receive.sample)
- Metadata: stock sample hook.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/hooks/prepare-commit-msg.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/prepare-commit-msg.sample)
- Metadata: stock sample hook.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/hooks/push-to-checkout.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/push-to-checkout.sample)
- Metadata: stock sample hook.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/hooks/sendemail-validate.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/sendemail-validate.sample)
- Metadata: stock sample hook.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/hooks/update.sample](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/hooks/update.sample)
- Metadata: stock sample hook.
- Quality: irrelevant noise.

### [/models/Wav2Lip/.git/index](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/index)
- Metadata: binary git index.
- Quality: nested VCS payload; not source.

### [/models/Wav2Lip/.git/objects/pack/pack-e451cea97c20da0890252c0081570b559c6f0e29.idx](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/objects/pack/pack-e451cea97c20da0890252c0081570b559c6f0e29.idx)
- Metadata: git pack index.
- Quality: nested VCS payload.

### [/models/Wav2Lip/.git/objects/pack/pack-e451cea97c20da0890252c0081570b559c6f0e29.pack](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/objects/pack/pack-e451cea97c20da0890252c0081570b559c6f0e29.pack)
- Metadata: git object pack.
- Quality: nested VCS payload.

### [/models/Wav2Lip/.git/objects/pack/pack-e451cea97c20da0890252c0081570b559c6f0e29.rev](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/.git/objects/pack/pack-e451cea97c20da0890252c0081570b559c6f0e29.rev)
- Metadata: git reverse index.
- Quality: nested VCS payload.

### [/models/Wav2Lip/__pycache__/audio.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/__pycache__/audio.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated, stale-prone, should not be source of truth.

### [/models/Wav2Lip/__pycache__/hparams.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/__pycache__/hparams.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/checkpoints/wav2lip_gan.pth](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/checkpoints/wav2lip_gan.pth)
- Metadata: 145.8 MB model checkpoint.
- Role: vendored GAN checkpoint.
- Quality: model blob only; license in upstream README is non-commercial.

### [/models/Wav2Lip/checkpoints_from_folder/.DS_Store](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/checkpoints_from_folder/.DS_Store)
- Metadata: macOS Finder metadata.
- Quality: noise.

### [/models/Wav2Lip/checkpoints_from_folder/Wav2Lip-SD-GAN.pt](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/checkpoints_from_folder/Wav2Lip-SD-GAN.pt)
- Metadata: 145.8 MB checkpoint.
- Role: actual checkpoint used in `userface_multiframe` logs.
- Quality: local blob; undocumented provenance in repo.

### [/models/Wav2Lip/checkpoints_from_folder/Wav2Lip-SD-NOGAN.pt](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/checkpoints_from_folder/Wav2Lip-SD-NOGAN.pt)
- Metadata: 145.8 MB checkpoint.
- Role: actual checkpoint used in `syncfix` and `refstyle` logs.
- Quality: local blob; undocumented provenance in repo.

### [/models/Wav2Lip/face_detection/__pycache__/__init__.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/__pycache__/__init__.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/face_detection/__pycache__/api.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/__pycache__/api.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/face_detection/__pycache__/models.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/__pycache__/models.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/face_detection/__pycache__/utils.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/__pycache__/utils.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/face_detection/detection/__pycache__/__init__.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/__pycache__/__init__.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/face_detection/detection/__pycache__/core.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/__pycache__/core.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/face_detection/detection/sfd/__pycache__/__init__.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/sfd/__pycache__/__init__.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/face_detection/detection/sfd/__pycache__/bbox.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/sfd/__pycache__/bbox.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/face_detection/detection/sfd/__pycache__/detect.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/sfd/__pycache__/detect.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/face_detection/detection/sfd/__pycache__/net_s3fd.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/sfd/__pycache__/net_s3fd.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/face_detection/detection/sfd/__pycache__/sfd_detector.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/sfd/__pycache__/sfd_detector.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/face_detection/detection/sfd/s3fd.pth](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/face_detection/detection/sfd/s3fd.pth)
- Metadata: 89.8 MB detector weights.
- Role: required by vendored Wav2Lip face detector.
- Quality: binary blob; no in-repo license record.

### [/models/Wav2Lip/models/__pycache__/__init__.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/models/__pycache__/__init__.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/models/__pycache__/conv.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/models/__pycache__/conv.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/models/__pycache__/syncnet.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/models/__pycache__/syncnet.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/models/__pycache__/wav2lip.cpython-310.pyc](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/models/__pycache__/wav2lip.cpython-310.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/models/Wav2Lip/temp/result.avi](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/temp/result.avi)
- Metadata: temporary AVI, 1280x720, MPEG-4, 24 fps, 11.875s.
- Role: temp output from latest Wav2Lip run.
- Quality: non-final temp artifact; stale and overwritten by subsequent runs.
- Evolution: confirms ad-hoc recent manual usage.

### Generated outputs and local-host artifacts

### [/out/.DS_Store](/Users/pranamyajain/hindi_podcast_local/out/.DS_Store)
- Metadata: Finder metadata.
- Quality: noise.

### [/out/episode_old_rj_1_fallback/.DS_Store](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_fallback/.DS_Store)
- Metadata: Finder metadata.
- Quality: noise.

### [/out/episode_old_rj_1_fallback/assets/avatar_rgba.png](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_fallback/assets/avatar_rgba.png)
- Metadata: generated 1024x1024 PNG.
- Role: fallback avatar asset.
- Quality: output artifact only.

### [/out/episode_old_rj_1_fallback/assets/background_1920x1080.png](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_fallback/assets/background_1920x1080.png)
- Metadata: generated 1920x1080 background PNG.
- Role: fallback background.
- Quality: output artifact only.

### [/out/episode_old_rj_1_fallback/index.html](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_fallback/index.html)
- Metadata: preview page.
- Role: local playback wrapper for fallback render.
- Quality: hand-authored static HTML; not generated by pipeline code in repo.
- Evolution: confirms manual local-host step.

### [/out/episode_old_rj_1_fallback/logs/http_server.log](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_fallback/logs/http_server.log)
- Metadata: empty log.
- Role: placeholder from local HTTP server.
- Quality: no forensic value beyond showing hosting step existed.

### [/out/episode_old_rj_1_fallback/logs/http_server.pid](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_fallback/logs/http_server.pid)
- Metadata: process ID file.
- Role: local server bookkeeping.
- Quality: stale after process exits.

### [/out/episode_old_rj_1_fallback/stage1_audio/preprocessed.wav](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_fallback/stage1_audio/preprocessed.wav)
- Metadata: 92.357s PCM 16 kHz mono WAV.
- Role: preprocessed audio.
- Quality: stage artifact.

### [/out/episode_old_rj_1_fallback/stage5_subtitles/transcript_hi.srt](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_fallback/stage5_subtitles/transcript_hi.srt)
- Metadata: generated Hindi SRT.
- Role: subtitle output from one ASR pass.
- Quality: transcript contains obvious Hindi word errors; this is evidence that default subtitle quality is not production-grade.

### [/out/episode_old_rj_1_fallback/stage5_subtitles/transcript_hi_medium.srt](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_fallback/stage5_subtitles/transcript_hi_medium.srt)
- Metadata: second SRT variant.
- Role: likely rerun with medium model or manual overwrite.
- Quality: better segmentation than the first file, still error-prone.
- Evolution: evidence of iteration.

### [/out/episode_old_rj_1_fallback/stage6_export/final_1080p.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_fallback/stage6_export/final_1080p.mp4)
- Metadata: H.264 1920x1080 25 fps MP4, 94.36s.
- Role: fallback final video.
- Quality: output duration does not exactly match preprocessed WAV; potential timing drift.

### [/out/episode_old_rj_1_realhost_web/final_1080p.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_realhost_web/final_1080p.mp4)
- Metadata: H.264 1920x1080 24 fps MP4, 92.416s.
- Role: served final video for “sync-fix”.
- Quality: artifact only.

### [/out/episode_old_rj_1_realhost_web/http_server.log](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_realhost_web/http_server.log)
- Metadata: HTTP HEAD requests from localhost.
- Role: confirms local hosting worked.
- Quality: artifact only.

### [/out/episode_old_rj_1_realhost_web/http_server.pid](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_realhost_web/http_server.pid)
- Metadata: PID file.
- Quality: stale.

### [/out/episode_old_rj_1_realhost_web/index.html](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_realhost_web/index.html)
- Metadata: preview page for “sync-fix”.
- Quality: hand-authored static page; not represented in source pipeline.

### [/out/episode_old_rj_1_realhost_web/preview_frame.png](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_realhost_web/preview_frame.png)
- Metadata: preview PNG.
- Role: visual snapshot of one render.
- Quality: artifact.

### [/out/episode_old_rj_1_realhost_web/preview_syncfix_final.png](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_realhost_web/preview_syncfix_final.png)
- Metadata: preview PNG.
- Role: snapshot of sync-fix render.
- Quality: artifact.

### [/out/episode_old_rj_1_realhost_web/preview_userface.png](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_realhost_web/preview_userface.png)
- Metadata: preview PNG.
- Role: snapshot of userface render.
- Quality: artifact.

### [/out/episode_old_rj_1_reallipsync/assets/background_real_1920x1080.png](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_reallipsync/assets/background_real_1920x1080.png)
- Metadata: 1920x1080 PNG.
- Role: background asset for “reallipsync” iteration.
- Quality: artifact.

### [/out/episode_old_rj_1_reallipsync/assets/source_face.jpg](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_reallipsync/assets/source_face.jpg)
- Metadata: 720x720 JPEG.
- Role: source face for Wav2Lip run.
- Quality: artifact.

### [/out/episode_old_rj_1_reallipsync/logs/wav2lip_infer.log](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_reallipsync/logs/wav2lip_infer.log)
- Metadata: inference log.
- Role: forensic record of Wav2Lip run.
- Quality:
  - Confirms CPU inference.
  - Confirms TorchScript archive warning.
  - Confirms mux path into `wav2lip_raw.mp4`.
- Evolution: first real-face experiment.

### [/out/episode_old_rj_1_reallipsync/stage1_audio/preprocessed.wav](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_reallipsync/stage1_audio/preprocessed.wav)
- Metadata: 92.357s PCM WAV.
- Role: stage artifact.

### [/out/episode_old_rj_1_reallipsync/stage3_lipsync/frame_100.png](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_reallipsync/stage3_lipsync/frame_100.png)
- Metadata: frame capture.
- Role: debug snapshot.
- Quality: artifact.

### [/out/episode_old_rj_1_reallipsync/stage3_lipsync/wav2lip_raw.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_reallipsync/stage3_lipsync/wav2lip_raw.mp4)
- Metadata: H.264 720x720 25 fps MP4, 92.358s.
- Role: direct Wav2Lip output.
- Quality: artifact; not final format.

### [/out/episode_old_rj_1_reallipsync/stage6_export/final_realhost_1080p.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_reallipsync/stage6_export/final_realhost_1080p.mp4)
- Metadata: H.264 1920x1080 25 fps MP4, 92.416s.
- Role: composited/exported version.
- Quality: artifact.

### [/out/episode_old_rj_1_refstyle_v3/assets/reference_motion.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/assets/reference_motion.mp4)
- Metadata: H.264 1280x720 24 fps, 8s.
- Role: reference motion clip.
- Quality: artifact proving reference-style approach was manual.

### [/out/episode_old_rj_1_refstyle_v3/calib/audio_12s.wav](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/calib/audio_12s.wav)
- Metadata: 12s PCM WAV.
- Role: calibration excerpt.
- Quality: artifact.

### [/out/episode_old_rj_1_refstyle_v3/calib/calib_auto.log](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/calib/calib_auto.log)
- Metadata: calibration log.
- Role: forensic evidence of automated calibration attempt.
- Quality: artifact only.

### [/out/episode_old_rj_1_refstyle_v3/calib/driver_12s.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/calib/driver_12s.mp4)
- Metadata: H.264 1280x720 24 fps, 12s.
- Role: calibration driver video.
- Quality: artifact.

### [/out/episode_old_rj_1_refstyle_v3/calib/out_auto.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/calib/out_auto.mp4)
- Metadata: H.264 1280x720 24 fps, 12s.
- Role: calibration output.
- Quality: artifact.

### [/out/episode_old_rj_1_refstyle_v3/logs/wav2lip_infer.log](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/logs/wav2lip_infer.log)
- Metadata: inference log.
- Role: confirms 24 fps reference-style Wav2Lip run with fixed box.
- Quality: artifact.

### [/out/episode_old_rj_1_refstyle_v3/stage1_audio/preprocessed.wav](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/stage1_audio/preprocessed.wav)
- Metadata: 92.357s PCM WAV.
- Role: artifact.

### [/out/episode_old_rj_1_refstyle_v3/stage2_driver/ref_driver_92s.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/stage2_driver/ref_driver_92s.mp4)
- Metadata: H.264 1280x720 24 fps, 92.375s.
- Role: looped reference motion driver.
- Quality: artifact.

### [/out/episode_old_rj_1_refstyle_v3/stage2_driver/ref_fwd.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/stage2_driver/ref_fwd.mp4)
- Metadata: H.264 1280x720 24 fps, 8s.
- Role: forward driver segment.
- Quality: artifact.

### [/out/episode_old_rj_1_refstyle_v3/stage2_driver/ref_pingpong.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/stage2_driver/ref_pingpong.mp4)
- Metadata: H.264 1280x720 24 fps, 16s.
- Role: ping-pong loop driver.
- Quality: artifact.

### [/out/episode_old_rj_1_refstyle_v3/stage2_driver/ref_rev.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/stage2_driver/ref_rev.mp4)
- Metadata: H.264 1280x720 24 fps, 8s.
- Role: reversed driver segment.
- Quality: artifact.

### [/out/episode_old_rj_1_refstyle_v3/stage3_lipsync/contact_refstyle.png](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/stage3_lipsync/contact_refstyle.png)
- Metadata: contact-sheet PNG.
- Role: debug visual.
- Quality: artifact.

### [/out/episode_old_rj_1_refstyle_v3/stage3_lipsync/frame360.png](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/stage3_lipsync/frame360.png)
- Metadata: debug frame PNG.
- Quality: artifact.

### [/out/episode_old_rj_1_refstyle_v3/stage3_lipsync/wav2lip_refstyle.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_refstyle_v3/stage3_lipsync/wav2lip_refstyle.mp4)
- Metadata: H.264 1280x720 24 fps, 92.358s.
- Role: reference-style Wav2Lip output.
- Quality: artifact.

### [/out/episode_old_rj_1_syncfix_v2/assets/source_face.png](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_syncfix_v2/assets/source_face.png)
- Metadata: 2528x1686 RGBA source image.
- Role: sync-fix input face.
- Quality: artifact.

### [/out/episode_old_rj_1_syncfix_v2/assets/source_face_1280x720.png](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_syncfix_v2/assets/source_face_1280x720.png)
- Metadata: normalized source image.
- Role: sync-fix resized source.
- Quality: artifact.

### [/out/episode_old_rj_1_syncfix_v2/logs/wav2lip_infer.log](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_syncfix_v2/logs/wav2lip_infer.log)
- Metadata: empty log.
- Quality: failed or redirected run left no log body.

### [/out/episode_old_rj_1_syncfix_v2/stage1_audio/preprocessed.wav](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_syncfix_v2/stage1_audio/preprocessed.wav)
- Metadata: 92.357s PCM WAV.
- Role: artifact.

### [/out/episode_old_rj_1_syncfix_v2/stage3_lipsync/preview_syncfix.png](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_syncfix_v2/stage3_lipsync/preview_syncfix.png)
- Metadata: preview PNG.
- Role: debug snapshot.
- Quality: artifact.

### [/out/episode_old_rj_1_syncfix_v2/stage3_lipsync/wav2lip_syncfix.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_syncfix_v2/stage3_lipsync/wav2lip_syncfix.mp4)
- Metadata: H.264 1280x720 24 fps, 92.358s.
- Role: sync-fix Wav2Lip output.
- Quality: artifact.

### [/out/episode_old_rj_1_syncfix_v2/stage6_export/final_1080p_syncfix.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_syncfix_v2/stage6_export/final_1080p_syncfix.mp4)
- Metadata: H.264 1920x1080 24 fps, 92.416s.
- Role: exported sync-fix final.
- Quality: artifact.

### [/out/episode_old_rj_1_userface_multiframe/.DS_Store](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_userface_multiframe/.DS_Store)
- Metadata: Finder metadata.
- Quality: noise.

### [/out/episode_old_rj_1_userface_multiframe/assets/host_image.png](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_userface_multiframe/assets/host_image.png)
- Metadata: 2528x1686 source host image.
- Role: user-supplied face.
- Quality: artifact.

### [/out/episode_old_rj_1_userface_multiframe/logs/wav2lip_infer.log](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_userface_multiframe/logs/wav2lip_infer.log)
- Metadata: detailed inference log.
- Role: confirms CPU inference with GAN checkpoint and fixed bounding box.
- Quality: artifact; explains why output blurred and over-articulated.

### [/out/episode_old_rj_1_userface_multiframe/stage1_audio/preprocessed.wav](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_userface_multiframe/stage1_audio/preprocessed.wav)
- Metadata: 92.357s PCM WAV.
- Role: artifact.

### [/out/episode_old_rj_1_userface_multiframe/stage2_driver/driver_face_92s.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_userface_multiframe/stage2_driver/driver_face_92s.mp4)
- Metadata: H.264 1280x720 25 fps, 92.36s, `yuvj420p`.
- Role: assembled looping multi-frame driver video.
- Quality: artifact; driver approach causes mouth-speed drift because loop timing is decoupled from phonemes.

### [/out/episode_old_rj_1_userface_multiframe/stage2_driver/driver_forward.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_userface_multiframe/stage2_driver/driver_forward.mp4)
- Metadata: 1.6s forward lip cycle.
- Role: artifact.

### [/out/episode_old_rj_1_userface_multiframe/stage2_driver/driver_pingpong.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_userface_multiframe/stage2_driver/driver_pingpong.mp4)
- Metadata: 3.2s ping-pong cycle.
- Role: artifact.

### [/out/episode_old_rj_1_userface_multiframe/stage2_driver/driver_reverse.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_userface_multiframe/stage2_driver/driver_reverse.mp4)
- Metadata: 1.6s reverse cycle.
- Role: artifact.

### [/out/episode_old_rj_1_userface_multiframe/stage3_lipsync/wav2lip_userface.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_userface_multiframe/stage3_lipsync/wav2lip_userface.mp4)
- Metadata: H.264 1280x720 25 fps, 92.358s.
- Role: multi-image driver Wav2Lip output.
- Quality: artifact.

### [/out/episode_old_rj_1_userface_multiframe/stage6_export/final_1080p_userface.mp4](/Users/pranamyajain/hindi_podcast_local/out/episode_old_rj_1_userface_multiframe/stage6_export/final_1080p_userface.mp4)
- Metadata: H.264 1920x1080 25 fps, 92.416s, high bitrate.
- Role: exported userface render.
- Quality: artifact.

### [/out/reference_inspect/reference_contact.png](/Users/pranamyajain/hindi_podcast_local/out/reference_inspect/reference_contact.png)
- Metadata: debug contact-sheet PNG.
- Role: inspection artifact.
- Quality: artifact.

### Root package caches

### [/podcast_pipeline/__pycache__/__init__.cpython-313.pyc](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/__pycache__/__init__.cpython-313.pyc)
- Metadata: compiled cache.
- Quality: generated only.

### [/podcast_pipeline/__pycache__/utils.cpython-313.pyc](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/__pycache__/utils.cpython-313.pyc)
- Metadata: compiled cache.
- Quality: generated only.

4. **Phase 3: Pipeline Integrity Audit**

What triggers the pipeline:
- Intended trigger: `python run_podcast.py --audio ... --out ...`
- Actual observed trigger for successful real-person outputs: manual Wav2Lip invocation plus manual FFmpeg and preview-page construction.

Exact intended sequence:
1. Parse CLI.
2. Load YAML config with code defaults merged in.
3. Validate input path/extension/duration.
4. Detect CUDA VRAM.
5. Auto-select backend: `musetalk` if VRAM >= threshold, else `sadtalker`.
6. Stage 1: preprocess audio to 16 kHz mono WAV.
7. Stage 2: generate/reuse avatar and background via local A1111 API.
8. Stage 3: run lipsync backend subprocess.
9. Stage 4: composite foreground video over background.
10. Stage 5: generate SRT from local Faster-Whisper.
11. Stage 6: burn subtitles and export final MP4.
12. Write `run_report.json`.
13. Optionally delete intermediate dirs.

Exact actual failure point on clean repo:
- Stage 3. [`podcast_pipeline/lipsync.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/lipsync.py#L80) raises if `models/SadTalker` or `models/MuseTalk` does not exist. They do not exist in this repo.

Actual manual execution path evidenced by artifacts:
1. Input audio normalized to `preprocessed.wav`.
2. User/host source image chosen.
3. Either:
   - static image -> Wav2Lip directly, or
   - looping reference/driver video built first.
4. [`models/Wav2Lip/inference.py`](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/inference.py) generates `temp/result.avi`.
5. FFmpeg muxes `temp/result.avi` + `preprocessed.wav` -> `wav2lip_*.mp4`.
6. Optional upscale/composite/export to 1080p.
7. Manual HTML page created under `out/*/index.html`.
8. Local HTTP server serves the result.

Where data transforms:
- Input compressed audio -> PCM WAV in stage 1.
- Text prompt -> avatar/background PNG in stage 2.
- Avatar PNG + WAV -> talking-head MP4 in stage 3.
- Talking-head MP4 + background PNG -> composited MP4 in stage 4.
- WAV -> SRT in stage 5.
- Composited MP4 + WAV + SRT -> final MP4 in stage 6.

Silent-failure points:
- [`subtitles.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/subtitles.py#L58): blank segments silently skip numbering.
- [`export.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/export.py#L94): validator does not check `faststart`; file can violate documented promise without being flagged.
- [`avatar.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/avatar.py#L144): checkpoint mutation can change future outputs globally without local record.
- [`models/Wav2Lip/evaluation/gen_videos_from_filelist.py`](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/gen_videos_from_filelist.py): clips with NaN mel are skipped silently.

Hard-failure points:
- No CUDA GPU -> [`utils.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/utils.py#L257) throws.
- Missing Faster-Whisper model dir -> [`subtitles.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/subtitles.py#L26) throws.
- Missing A1111 server -> [`avatar.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/avatar.py#L125) throws.
- Missing SadTalker/MuseTalk repos -> [`lipsync.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/lipsync.py#L80) throws.
- Missing video output from backend -> [`lipsync.py`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/lipsync.py#L115) throws.
- Missing subtitles -> export stage fails.
- Vendored Wav2Lip eval scripts -> fail due missing external repos/models/scripts.

Determinism:
- Intended avatar/background generation is deterministic if seed and checkpoint stay fixed.
- Actual system is not fully deterministic because:
  - A1111 server global checkpoint state is mutable.
  - backend repos are external and not pinned in-repo.
  - Wav2Lip face detection uses runtime batching and can vary by environment.
  - manual experiment path is not codified, so operator choices dominate.

5. **Phase 4: Dependency and Environment Audit**

External binaries:
- `ffmpeg`: required, checked by self-check.
- `ffprobe`: required, checked by self-check.
- `nvidia-smi`: optional for VRAM fallback.
- `python`: used to invoke backends.
- Additional binary use in vendored Wav2Lip path: FFmpeg again.

Python libraries used by root pipeline:
- `PyYAML`
- `requests`
- `Pillow`
- `numpy`
- `faster-whisper`
- `torch`

Python libraries used by vendored Wav2Lip code but missing from root requirements:
- `librosa`
- `scipy`
- `opencv-python`
- `opencv-contrib-python`
- `tqdm`
- `numba`
- `python_speech_features`
- `dlib` in eval helpers

Model/repo dependencies expected by root pipeline:
- Faster-Whisper model dir at `models/faster-whisper-medium` or configured path: missing from repo.
- AUTOMATIC1111 local server with SD checkpoint `RealisticVisionV60B1_v51HyperVAE.safetensors`: not shipped.
- `models/SadTalker`: missing.
- `models/MuseTalk`: missing.

Model/repo dependencies actually present:
- Vendored `models/Wav2Lip` repo.
- `models/Wav2Lip/checkpoints/wav2lip_gan.pth`
- `models/Wav2Lip/checkpoints_from_folder/Wav2Lip-SD-GAN.pt`
- `models/Wav2Lip/checkpoints_from_folder/Wav2Lip-SD-NOGAN.pt`
- `models/Wav2Lip/face_detection/detection/sfd/s3fd.pth`

Versioning state:
- Root env partially pinned.
- Vendored Wav2Lip deps pinned to obsolete versions that conflict with root.
- SadTalker/MuseTalk versions cannot be audited because repos are absent.
- A1111 version cannot be audited because it is external to repo.

Reproducibility from scratch using only this repo:
- No.
- Missing:
  - Faster-Whisper model files
  - SD checkpoint and server setup
  - SadTalker repo
  - MuseTalk repo
  - license records
  - Wav2Lip-compatible environment pinning in root env
- Therefore repo is not self-contained.

Open-source/free-only and license compliance:
- Hard failure on permissive-license constraint:
  - Vendored Wav2Lip README explicitly restricts OSS version to personal/research/non-commercial use. That is not MIT/Apache/LGPL-equivalent.
- Potential additional license gap:
  - RealisticVision V6 checkpoint license is not documented in-repo.
- Documentation-only proprietary dependency:
  - Vendored Wav2Lip README contains Sync.so API-key-based commercial instructions. Those are not executed by this project, but they are in the codebase.

6. **Phase 5: Gap Analysis Between Intent and Implementation**

Clearly intended but not implemented:
- ComfyUI support.
- End-to-end usable SadTalker/MuseTalk path inside repo.
- Automated local hosting of final result.
- Model license registry under `models/licenses`.
- Reproducible full environment bootstrap.

Partially implemented:
- Avatar/background generation: works only via local A1111; no alternative runner.
- Subtitle generation: works if model exists; quality and serialization issues remain.
- Export validation: checks basic codecs/resolution/fps, not full YouTube compliance.
- Self-check: checks some files, not actual service readiness.

Implemented but wrong:
- `subtitles.py` always writes `transcript_hi.srt` even for non-Hindi language argument.
- `subtitles.py` SRT numbering can skip indexes.
- `run_podcast.py` claims backend auto-selection, but both backend repos are absent.
- Root repo claims no cloud/API behavior; code uses local HTTP API. That is local-only, but still an API call boundary.

In docs/config but unsupported in code:
- ComfyUI.
- Fully working MuseTalk path.
- Fully working SadTalker path.
- Complete license documentation.
- Performance claims for RTX 3060 as a verified system property.

Supported in code but undocumented:
- MuseTalk -> SadTalker fallback logic.
- CPU fallback inside subtitle stage.
- Manual Wav2Lip path present in vendored repo and actual artifacts, despite not being part of documented orchestrator.

7. **Phase 6: Current State Verdict**

1. What is actually working
- CLI parsing and config loading in [`run_podcast.py`](/Users/pranamyajain/hindi_podcast_local/run_podcast.py).
- Input audio validation by extension and duration.
- Logging, stage timing, and JSON report writing.
- Audio preprocessing to 16 kHz mono WAV.
- Avatar/background reuse and A1111-based generation if local server exists.
- Subtitle generation with Faster-Whisper if model files exist.
- FFmpeg compositing.
- FFmpeg subtitle burn-in and final MP4 export.
- Vendored Wav2Lip manual inference path, evidenced by successful outputs in `out/`.

2. What is broken
- Core lipsync stage on clean repo: missing backend repos at [`podcast_pipeline/lipsync.py#L74-L86`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/lipsync.py#L74).
- Claimed ComfyUI option: not implemented at [`podcast_pipeline/avatar.py#L95-L101`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/avatar.py#L95).
- Subtitle file naming ignores selected language at [`podcast_pipeline/subtitles.py#L48`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/subtitles.py#L48).
- SRT numbering bug at [`podcast_pipeline/subtitles.py#L58-L64`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/subtitles.py#L58).
- YouTube validation incomplete at [`podcast_pipeline/export.py#L94-L124`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/export.py#L94).
- Root environment does not satisfy vendored Wav2Lip dependency needs.
- Wav2Lip audio helper bug at [`models/Wav2Lip/audio.py#L53-L60`](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/audio.py#L53).
- `hparams_debug_string` broken at [`models/Wav2Lip/hparams.py#L98-L100`](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/hparams.py#L98).
- Eval shell wrapper references missing `run_pipeline.py` at [`models/Wav2Lip/evaluation/scores_LSE/calculate_scores_real_videos.sh#L6-L7`](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/evaluation/scores_LSE/calculate_scores_real_videos.sh#L6).

3. What is missing entirely
- `models/SadTalker`
- `models/MuseTalk`
- local Faster-Whisper model dir
- local SD checkpoint in repo
- license manifests for shipped models
- tests
- automated benchmark harness
- integrated Wav2Lip backend inside `run_podcast.py`

4. System readiness score
- Stage 1 audio preprocess: `2/3`
- Stage 2 avatar/background: `2/3`
- Stage 3 lipsync: `1/3`
- Stage 4 composite: `2/3`
- Stage 5 subtitles: `2/3`
- Stage 6 export: `2/3`
- Overall system score: `1.8/3`

Reason for overall score:
- Several stages work in isolation.
- The documented end-to-end path does not run from a clean checkout because the central lipsync dependency is missing.

5. Top 5 critical issues
1. Missing production lipsync backends
- Where: [`podcast_pipeline/lipsync.py#L74-L86`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/lipsync.py#L74)
- Why it matters: the documented pipeline cannot complete.
- Minimum fix: vendor or submodule-pin `SadTalker` and/or `MuseTalk`, add weight checks, add deterministic integration tests.

2. License non-compliance with stated constraints
- Where: [`models/Wav2Lip/README.md#L228`](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/README.md#L228), [`models/Wav2Lip/README.md#L308`](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/README.md#L308)
- Why it matters: current dependency set does not satisfy permissive open-source-only requirement.
- Minimum fix: replace Wav2Lip or document and obtain compliant alternative; add explicit model license registry.

3. Environment is not reproducible
- Where: root [`requirements.txt`](/Users/pranamyajain/hindi_podcast_local/requirements.txt), [`environment.yml`](/Users/pranamyajain/hindi_podcast_local/environment.yml), vendored [`models/Wav2Lip/requirements.txt`](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/requirements.txt)
- Why it matters: fresh setup cannot reach the current working manual path.
- Minimum fix: choose one supported inference stack, freeze one environment, remove conflicting stacks.

4. Documentation and implementation diverge materially
- Where: [`README.md`](/Users/pranamyajain/hindi_podcast_local/README.md), [`podcast_pipeline/avatar.py#L95-L101`](/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/avatar.py#L95)
- Why it matters: users will follow unsupported setup instructions and fail.
- Minimum fix: rewrite README to match actual executable system.

5. Working path is manual and unintegrated
- Where: `out/*` artifacts plus vendored [`models/Wav2Lip/inference.py`](/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip/inference.py)
- Why it matters: the only evidenced successful renders are not reproducible through the official entrypoint.
- Minimum fix: either integrate Wav2Lip as a supported backend or delete experimental path from product claims.

8. **Phase 7: Technical Debt Register**

Hardcoded paths and machine-specific assumptions:
- A1111 at `http://127.0.0.1:7860`
- backend repos under `models/SadTalker` and `models/MuseTalk`
- whisper model under `models/faster-whisper-medium`
- fixed output names like `final_1080p.mp4`, `transcript_hi.srt`
- nested Wav2Lip temp path `temp/result.avi`
- local-user email inside vendored git logs

Untested code paths:
- MuseTalk fallback path in clean repo.
- non-Hindi subtitle file naming path.
- ComfyUI path is dead because not implemented.
- evaluation scripts requiring external SyncNet repo.
- cleanup path with `--keep-intermediates false`.

Synchronous operations that should be async or at least time-bounded:
- all HTTP calls to A1111
- all subprocess calls via `run_command`
- all FFmpeg runs
- all large model loads

Missing input validation at boundaries:
- no validation that A1111 is actually serving expected model
- no validation that backend repos have correct weights
- no validation that generated avatar resembles requested framing
- no validation that subtitles match audio language beyond forcing `language=hi`

Missing output validation before downstream handoff:
- no validation that talking-head output is lip-synced
- no validation that composited video duration matches audio exactly
- no validation that subtitle burn-in visually succeeded
- no validation that final file has `faststart`

Configuration scattered instead of centralized:
- defaults duplicated in code and YAML
- manual experiment parameters live only in output logs and ad-hoc files
- vendored Wav2Lip has its own completely separate config stack
- model locations partly in docs, partly in code, partly external to repo

**Executive Summary**

This repository is two systems at once.

The first is the intended product: a modular local podcast pipeline in `/Users/pranamyajain/hindi_podcast_local/run_podcast.py` and `/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/`. That system is architecturally coherent. Audio preprocessing, subtitle generation, compositing, export, logging, and reporting are implemented. The problem is that the central lipsync stage depends on `SadTalker` and `MuseTalk`, and neither repo exists in this codebase. From a clean checkout, the documented end-to-end pipeline does not run.

The second is the system that actually produced the outputs you were testing: a vendored `Wav2Lip` repo under `/Users/pranamyajain/hindi_podcast_local/models/Wav2Lip`, plus manual experiment folders under `/Users/pranamyajain/hindi_podcast_local/out`. That manual path clearly ran. The logs show CPU Wav2Lip inference, fixed bounding boxes, looped driver videos, FFmpeg muxing, and hand-authored localhost preview pages. That is the real operational history of the project. It is not integrated into the official entrypoint, not documented as the primary path, and not compatible with the repository’s stated license constraints.

The current state is not production-ready. The repo contains useful building blocks, but it is not a reproducible, policy-compliant, single-command system. The largest gaps are not cosmetic. They are structural:
1. the orchestrated lipsync backend is missing,
2. the environment is split across incompatible stacks,
3. the only evidenced working path relies on a non-permissive vendored dependency and manual orchestration.

The three highest-leverage actions to take next are:
1. Pick one lipsync path and commit to it. Either integrate Wav2Lip as an official backend with a real adapter, or remove it and vendor/pin SadTalker or MuseTalk properly. Do not keep two half-systems.
2. Rebuild the environment and licensing story from zero. Produce one lockable environment, one model manifest, and one license registry that actually matches the shipped files.
3. Rewrite the README to describe only what the repo can do from a clean checkout, then add one integration test that proves `run_podcast.py` reaches a final MP4 on a prepared local machine. Without that, every future change will drift the system further from reality.
