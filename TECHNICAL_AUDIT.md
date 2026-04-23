# CTO Technical Audit Report

Generated: `2026-04-13 16:24:14` (local)
Repo root: `/Users/pranamyajain/hindi_podcast_local`

This report is generated from the current working tree and supersedes any older audit content.

### Scope and Assumptions
- Includes all files under the repo root excluding Git internals (`.git/`) and Python bytecode caches (`__pycache__/`).
- Includes `out/` artifacts and `assets/` media because they exist in this working tree and appear to be versioned here.
- For binary media (MP4/JPG) this report records `ffprobe`/`sips` metadata; it does not reverse-engineer binary contents.

## Phase 0: Complete File Inventory

- Total directories (excluding `.git/`, `__pycache__/`): `140`
- Total files (excluding `.git/`, `__pycache__/`): `606`

Top-level file distribution (files):
- `models`: `564`
- `out`: `15`
- `podcast_pipeline`: `9`
- `assets`: `5`
- `scripts`: `5`
- `.gitignore`: `1`
- `.gitmodules`: `1`
- `README.md`: `1`
- `TECHNICAL_AUDIT.md`: `1`
- `configs`: `1`
- `environment.yml`: `1`
- `requirements.txt`: `1`
- `run_podcast.py`: `1`

Recursive inventory (directories then files):
```text
.
./assets
./configs
./docs
./models
./models/LatentSync
./models/LatentSync/assets
./models/LatentSync/configs
./models/LatentSync/configs/syncnet
./models/LatentSync/configs/unet
./models/LatentSync/docs
./models/LatentSync/eval
./models/LatentSync/eval/detectors
./models/LatentSync/eval/detectors/s3fd
./models/LatentSync/eval/syncnet
./models/LatentSync/latentsync
./models/LatentSync/latentsync/data
./models/LatentSync/latentsync/models
./models/LatentSync/latentsync/pipelines
./models/LatentSync/latentsync/trepa
./models/LatentSync/latentsync/trepa/third_party
./models/LatentSync/latentsync/trepa/third_party/VideoMAEv2
./models/LatentSync/latentsync/trepa/utils
./models/LatentSync/latentsync/utils
./models/LatentSync/latentsync/whisper
./models/LatentSync/latentsync/whisper/whisper
./models/LatentSync/latentsync/whisper/whisper/assets
./models/LatentSync/latentsync/whisper/whisper/assets/gpt2
./models/LatentSync/latentsync/whisper/whisper/assets/multilingual
./models/LatentSync/latentsync/whisper/whisper/normalizers
./models/LatentSync/preprocess
./models/LatentSync/scripts
./models/LatentSync/tools
./models/SadTalker
./models/SadTalker/checkpoints
./models/SadTalker/docs
./models/SadTalker/examples
./models/SadTalker/examples/driven_audio
./models/SadTalker/examples/ref_video
./models/SadTalker/examples/source_image
./models/SadTalker/gfpgan
./models/SadTalker/gfpgan/weights
./models/SadTalker/scripts
./models/SadTalker/src
./models/SadTalker/src/audio2exp_models
./models/SadTalker/src/audio2pose_models
./models/SadTalker/src/config
./models/SadTalker/src/face3d
./models/SadTalker/src/face3d/data
./models/SadTalker/src/face3d/models
./models/SadTalker/src/face3d/models/arcface_torch
./models/SadTalker/src/face3d/models/arcface_torch/backbones
./models/SadTalker/src/face3d/models/arcface_torch/configs
./models/SadTalker/src/face3d/models/arcface_torch/docs
./models/SadTalker/src/face3d/models/arcface_torch/eval
./models/SadTalker/src/face3d/models/arcface_torch/utils
./models/SadTalker/src/face3d/options
./models/SadTalker/src/face3d/util
./models/SadTalker/src/facerender
./models/SadTalker/src/facerender/modules
./models/SadTalker/src/facerender/sync_batchnorm
./models/SadTalker/src/utils
./models/licenses
./models/video-retalking
./models/video-retalking/docs
./models/video-retalking/docs/static
./models/video-retalking/docs/static/css
./models/video-retalking/docs/static/images
./models/video-retalking/docs/static/js
./models/video-retalking/docs/static/pdfs
./models/video-retalking/docs/static/videos
./models/video-retalking/examples
./models/video-retalking/examples/audio
./models/video-retalking/examples/face
./models/video-retalking/models
./models/video-retalking/third_part
./models/video-retalking/third_part/GFPGAN
./models/video-retalking/third_part/GFPGAN/gfpgan
./models/video-retalking/third_part/GFPGAN/gfpgan/archs
./models/video-retalking/third_part/GFPGAN/gfpgan/data
./models/video-retalking/third_part/GFPGAN/gfpgan/models
./models/video-retalking/third_part/GFPGAN/gfpgan/weights
./models/video-retalking/third_part/GFPGAN/options
./models/video-retalking/third_part/GPEN
./models/video-retalking/third_part/GPEN/face_detect
./models/video-retalking/third_part/GPEN/face_detect/data
./models/video-retalking/third_part/GPEN/face_detect/data/FDDB
./models/video-retalking/third_part/GPEN/face_detect/facemodels
./models/video-retalking/third_part/GPEN/face_detect/layers
./models/video-retalking/third_part/GPEN/face_detect/layers/functions
./models/video-retalking/third_part/GPEN/face_detect/layers/modules
./models/video-retalking/third_part/GPEN/face_detect/utils
./models/video-retalking/third_part/GPEN/face_detect/utils/nms
./models/video-retalking/third_part/GPEN/face_model
./models/video-retalking/third_part/GPEN/face_model/op
./models/video-retalking/third_part/GPEN/face_morpher
./models/video-retalking/third_part/GPEN/face_morpher/facemorpher
./models/video-retalking/third_part/GPEN/face_morpher/scripts
./models/video-retalking/third_part/GPEN/face_parse
./models/video-retalking/third_part/face3d
./models/video-retalking/third_part/face3d/checkpoints
./models/video-retalking/third_part/face3d/checkpoints/model_name
./models/video-retalking/third_part/face3d/data
./models/video-retalking/third_part/face3d/models
./models/video-retalking/third_part/face3d/models/arcface_torch
./models/video-retalking/third_part/face3d/models/arcface_torch/backbones
./models/video-retalking/third_part/face3d/models/arcface_torch/configs
./models/video-retalking/third_part/face3d/models/arcface_torch/docs
./models/video-retalking/third_part/face3d/models/arcface_torch/eval
./models/video-retalking/third_part/face3d/models/arcface_torch/utils
./models/video-retalking/third_part/face3d/options
./models/video-retalking/third_part/face3d/util
./models/video-retalking/third_part/face_detection
./models/video-retalking/third_part/face_detection/detection
./models/video-retalking/third_part/face_detection/detection/sfd
./models/video-retalking/third_part/ganimation_replicate
./models/video-retalking/third_part/ganimation_replicate/checkpoints
./models/video-retalking/third_part/ganimation_replicate/ckpts
./models/video-retalking/third_part/ganimation_replicate/ckpts/ganimation
./models/video-retalking/third_part/ganimation_replicate/ckpts/ganimation/220419_183211
./models/video-retalking/third_part/ganimation_replicate/ckpts/ganimation/220419_183229
./models/video-retalking/third_part/ganimation_replicate/data
./models/video-retalking/third_part/ganimation_replicate/model
./models/video-retalking/utils
./out
./out/episode_001_preview
./out/episode_001_preview/logs
./out/episode_001_preview/stage1_audio
./out/episode_001_preview/stage2_diarize
./out/episode_001_preview/stage3_lipsync_a
./out/episode_001_preview/stage3_lipsync_b
./out/episode_001_preview/stage4_composite
./out/episode_001_preview/stage5_subtitles
./out/episode_001_preview/stage6_export
./out/episode_002_preview
./out/episode_002_preview/stage1_audio
./out/episode_002_preview/stage5_subtitles
./out/episode_002_preview/stage6_export
./podcast_pipeline
./scripts
./.gitignore
./.gitmodules
./README.md
./TECHNICAL_AUDIT.md
./assets/README.md
./assets/speaker_a.jpg
./assets/speaker_a_looped.mp4
./assets/speaker_b.jpg
./assets/speaker_b_looped.mp4
./configs/default_config.yaml
./environment.yml
./models/LatentSync/.git
./models/LatentSync/.gitignore
./models/LatentSync/LICENSE
./models/LatentSync/README.md
./models/LatentSync/assets/demo1_audio.wav
./models/LatentSync/assets/demo1_video.mp4
./models/LatentSync/assets/demo2_audio.wav
./models/LatentSync/assets/demo2_video.mp4
./models/LatentSync/assets/demo3_audio.wav
./models/LatentSync/assets/demo3_video.mp4
./models/LatentSync/cog.yaml
./models/LatentSync/configs/audio.yaml
./models/LatentSync/configs/scheduler_config.json
./models/LatentSync/configs/syncnet/syncnet_16_latent.yaml
./models/LatentSync/configs/syncnet/syncnet_16_pixel.yaml
./models/LatentSync/configs/syncnet/syncnet_16_pixel_attn.yaml
./models/LatentSync/configs/syncnet/syncnet_25_pixel.yaml
./models/LatentSync/configs/unet/stage1.yaml
./models/LatentSync/configs/unet/stage1_512.yaml
./models/LatentSync/configs/unet/stage2.yaml
./models/LatentSync/configs/unet/stage2_512.yaml
./models/LatentSync/configs/unet/stage2_efficient.yaml
./models/LatentSync/data_processing_pipeline.sh
./models/LatentSync/docs/changelog_v1.5.md
./models/LatentSync/docs/changelog_v1.6.md
./models/LatentSync/docs/framework.png
./models/LatentSync/docs/syncnet_arch.md
./models/LatentSync/eval/detectors/README.md
./models/LatentSync/eval/detectors/__init__.py
./models/LatentSync/eval/detectors/s3fd/__init__.py
./models/LatentSync/eval/detectors/s3fd/box_utils.py
./models/LatentSync/eval/detectors/s3fd/nets.py
./models/LatentSync/eval/draw_syncnet_lines.py
./models/LatentSync/eval/eval_fvd.py
./models/LatentSync/eval/eval_sync_conf.py
./models/LatentSync/eval/eval_sync_conf.sh
./models/LatentSync/eval/eval_syncnet_acc.py
./models/LatentSync/eval/eval_syncnet_acc.sh
./models/LatentSync/eval/fvd.py
./models/LatentSync/eval/hyper_iqa.py
./models/LatentSync/eval/inference_videos.py
./models/LatentSync/eval/syncnet/__init__.py
./models/LatentSync/eval/syncnet/syncnet.py
./models/LatentSync/eval/syncnet/syncnet_eval.py
./models/LatentSync/eval/syncnet_detect.py
./models/LatentSync/gradio_app.py
./models/LatentSync/inference.sh
./models/LatentSync/latentsync/data/syncnet_dataset.py
./models/LatentSync/latentsync/data/unet_dataset.py
./models/LatentSync/latentsync/models/attention.py
./models/LatentSync/latentsync/models/motion_module.py
./models/LatentSync/latentsync/models/resnet.py
./models/LatentSync/latentsync/models/stable_syncnet.py
./models/LatentSync/latentsync/models/unet.py
./models/LatentSync/latentsync/models/unet_blocks.py
./models/LatentSync/latentsync/models/utils.py
./models/LatentSync/latentsync/models/wav2lip_syncnet.py
./models/LatentSync/latentsync/pipelines/lipsync_pipeline.py
./models/LatentSync/latentsync/trepa/loss.py
./models/LatentSync/latentsync/trepa/third_party/VideoMAEv2/__init__.py
./models/LatentSync/latentsync/trepa/third_party/VideoMAEv2/utils.py
./models/LatentSync/latentsync/trepa/third_party/VideoMAEv2/videomaev2_finetune.py
./models/LatentSync/latentsync/trepa/third_party/VideoMAEv2/videomaev2_pretrain.py
./models/LatentSync/latentsync/trepa/third_party/__init__.py
./models/LatentSync/latentsync/trepa/utils/__init__.py
./models/LatentSync/latentsync/trepa/utils/data_utils.py
./models/LatentSync/latentsync/trepa/utils/metric_utils.py
./models/LatentSync/latentsync/utils/affine_transform.py
./models/LatentSync/latentsync/utils/audio.py
./models/LatentSync/latentsync/utils/av_reader.py
./models/LatentSync/latentsync/utils/face_detector.py
./models/LatentSync/latentsync/utils/image_processor.py
./models/LatentSync/latentsync/utils/mask.png
./models/LatentSync/latentsync/utils/mask2.png
./models/LatentSync/latentsync/utils/mask3.png
./models/LatentSync/latentsync/utils/mask4.png
./models/LatentSync/latentsync/utils/util.py
./models/LatentSync/latentsync/whisper/audio2feature.py
./models/LatentSync/latentsync/whisper/whisper/__init__.py
./models/LatentSync/latentsync/whisper/whisper/__main__.py
./models/LatentSync/latentsync/whisper/whisper/assets/gpt2/merges.txt
./models/LatentSync/latentsync/whisper/whisper/assets/gpt2/special_tokens_map.json
./models/LatentSync/latentsync/whisper/whisper/assets/gpt2/tokenizer_config.json
./models/LatentSync/latentsync/whisper/whisper/assets/gpt2/vocab.json
./models/LatentSync/latentsync/whisper/whisper/assets/mel_filters.npz
./models/LatentSync/latentsync/whisper/whisper/assets/multilingual/added_tokens.json
./models/LatentSync/latentsync/whisper/whisper/assets/multilingual/merges.txt
./models/LatentSync/latentsync/whisper/whisper/assets/multilingual/special_tokens_map.json
./models/LatentSync/latentsync/whisper/whisper/assets/multilingual/tokenizer_config.json
./models/LatentSync/latentsync/whisper/whisper/assets/multilingual/vocab.json
./models/LatentSync/latentsync/whisper/whisper/audio.py
./models/LatentSync/latentsync/whisper/whisper/decoding.py
./models/LatentSync/latentsync/whisper/whisper/model.py
./models/LatentSync/latentsync/whisper/whisper/normalizers/__init__.py
./models/LatentSync/latentsync/whisper/whisper/normalizers/basic.py
./models/LatentSync/latentsync/whisper/whisper/normalizers/english.json
./models/LatentSync/latentsync/whisper/whisper/normalizers/english.py
./models/LatentSync/latentsync/whisper/whisper/tokenizer.py
./models/LatentSync/latentsync/whisper/whisper/transcribe.py
./models/LatentSync/latentsync/whisper/whisper/utils.py
./models/LatentSync/predict.py
./models/LatentSync/preprocess/affine_transform.py
./models/LatentSync/preprocess/data_processing_pipeline.py
./models/LatentSync/preprocess/detect_shot.py
./models/LatentSync/preprocess/filter_high_resolution.py
./models/LatentSync/preprocess/filter_visual_quality.py
./models/LatentSync/preprocess/remove_broken_videos.py
./models/LatentSync/preprocess/remove_incorrect_affined.py
./models/LatentSync/preprocess/resample_fps_hz.py
./models/LatentSync/preprocess/segment_videos.py
./models/LatentSync/preprocess/sync_av.py
./models/LatentSync/requirements.txt
./models/LatentSync/scripts/inference.py
./models/LatentSync/scripts/train_syncnet.py
./models/LatentSync/scripts/train_unet.py
./models/LatentSync/setup_env.sh
./models/LatentSync/tools/count_total_videos_time.py
./models/LatentSync/tools/download_web_videos.py
./models/LatentSync/tools/move_files_recur.py
./models/LatentSync/tools/occupy_gpu.py
./models/LatentSync/tools/plot_videos_time_distribution.py
./models/LatentSync/tools/remove_outdated_files.py
./models/LatentSync/tools/write_fileslist.py
./models/LatentSync/train_syncnet.sh
./models/LatentSync/train_unet.sh
./models/README.md
./models/SadTalker/.gitignore
./models/SadTalker/LICENSE
./models/SadTalker/README.md
./models/SadTalker/app_sadtalker.py
./models/SadTalker/checkpoints/SadTalker_V0.0.2_256.safetensors
./models/SadTalker/checkpoints/SadTalker_V0.0.2_512.safetensors
./models/SadTalker/checkpoints/mapping_00109-model.pth.tar
./models/SadTalker/checkpoints/mapping_00229-model.pth.tar
./models/SadTalker/cog.yaml
./models/SadTalker/docs/FAQ.md
./models/SadTalker/docs/best_practice.md
./models/SadTalker/docs/changlelog.md
./models/SadTalker/docs/example_crop.gif
./models/SadTalker/docs/example_crop_still.gif
./models/SadTalker/docs/example_full.gif
./models/SadTalker/docs/example_full_crop.gif
./models/SadTalker/docs/example_full_enhanced.gif
./models/SadTalker/docs/face3d.md
./models/SadTalker/docs/free_view_result.gif
./models/SadTalker/docs/install.md
./models/SadTalker/docs/resize_good.gif
./models/SadTalker/docs/resize_no.gif
./models/SadTalker/docs/sadtalker_logo.png
./models/SadTalker/docs/using_ref_video.gif
./models/SadTalker/docs/webui_extension.md
./models/SadTalker/examples/driven_audio/RD_Radio31_000.wav
./models/SadTalker/examples/driven_audio/RD_Radio34_002.wav
./models/SadTalker/examples/driven_audio/RD_Radio36_000.wav
./models/SadTalker/examples/driven_audio/RD_Radio40_000.wav
./models/SadTalker/examples/driven_audio/bus_chinese.wav
./models/SadTalker/examples/driven_audio/chinese_news.wav
./models/SadTalker/examples/driven_audio/chinese_poem1.wav
./models/SadTalker/examples/driven_audio/chinese_poem2.wav
./models/SadTalker/examples/driven_audio/deyu.wav
./models/SadTalker/examples/driven_audio/eluosi.wav
./models/SadTalker/examples/driven_audio/fayu.wav
./models/SadTalker/examples/driven_audio/imagine.wav
./models/SadTalker/examples/driven_audio/itosinger1.wav
./models/SadTalker/examples/driven_audio/japanese.wav
./models/SadTalker/examples/ref_video/WDA_AlexandriaOcasioCortez_000.mp4
./models/SadTalker/examples/ref_video/WDA_KatieHill_000.mp4
./models/SadTalker/examples/source_image/art_0.png
./models/SadTalker/examples/source_image/art_1.png
./models/SadTalker/examples/source_image/art_10.png
./models/SadTalker/examples/source_image/art_11.png
./models/SadTalker/examples/source_image/art_12.png
./models/SadTalker/examples/source_image/art_13.png
./models/SadTalker/examples/source_image/art_14.png
./models/SadTalker/examples/source_image/art_15.png
./models/SadTalker/examples/source_image/art_16.png
./models/SadTalker/examples/source_image/art_17.png
./models/SadTalker/examples/source_image/art_18.png
./models/SadTalker/examples/source_image/art_19.png
./models/SadTalker/examples/source_image/art_2.png
./models/SadTalker/examples/source_image/art_20.png
./models/SadTalker/examples/source_image/art_3.png
./models/SadTalker/examples/source_image/art_4.png
./models/SadTalker/examples/source_image/art_5.png
./models/SadTalker/examples/source_image/art_6.png
./models/SadTalker/examples/source_image/art_7.png
./models/SadTalker/examples/source_image/art_8.png
./models/SadTalker/examples/source_image/art_9.png
./models/SadTalker/examples/source_image/full3.png
./models/SadTalker/examples/source_image/full4.jpeg
./models/SadTalker/examples/source_image/full_body_1.png
./models/SadTalker/examples/source_image/full_body_2.png
./models/SadTalker/examples/source_image/happy.png
./models/SadTalker/examples/source_image/happy1.png
./models/SadTalker/examples/source_image/people_0.png
./models/SadTalker/examples/source_image/sad.png
./models/SadTalker/examples/source_image/sad1.png
./models/SadTalker/gfpgan/weights/alignment_WFLW_4HG.pth
./models/SadTalker/gfpgan/weights/detection_Resnet50_Final.pth
./models/SadTalker/inference.py
./models/SadTalker/launcher.py
./models/SadTalker/predict.py
./models/SadTalker/quick_demo.ipynb
./models/SadTalker/req.txt
./models/SadTalker/requirements.txt
./models/SadTalker/requirements3d.txt
./models/SadTalker/scripts/download_models.sh
./models/SadTalker/scripts/extension.py
./models/SadTalker/scripts/test.sh
./models/SadTalker/src/audio2exp_models/audio2exp.py
./models/SadTalker/src/audio2exp_models/networks.py
./models/SadTalker/src/audio2pose_models/audio2pose.py
./models/SadTalker/src/audio2pose_models/audio_encoder.py
./models/SadTalker/src/audio2pose_models/cvae.py
./models/SadTalker/src/audio2pose_models/discriminator.py
./models/SadTalker/src/audio2pose_models/networks.py
./models/SadTalker/src/audio2pose_models/res_unet.py
./models/SadTalker/src/config/auido2exp.yaml
./models/SadTalker/src/config/auido2pose.yaml
./models/SadTalker/src/config/facerender.yaml
./models/SadTalker/src/config/facerender_still.yaml
./models/SadTalker/src/config/similarity_Lm3D_all.mat
./models/SadTalker/src/face3d/data/__init__.py
./models/SadTalker/src/face3d/data/base_dataset.py
./models/SadTalker/src/face3d/data/flist_dataset.py
./models/SadTalker/src/face3d/data/image_folder.py
./models/SadTalker/src/face3d/data/template_dataset.py
./models/SadTalker/src/face3d/extract_kp_videos.py
./models/SadTalker/src/face3d/extract_kp_videos_safe.py
./models/SadTalker/src/face3d/models/__init__.py
./models/SadTalker/src/face3d/models/arcface_torch/README.md
./models/SadTalker/src/face3d/models/arcface_torch/backbones/__init__.py
./models/SadTalker/src/face3d/models/arcface_torch/backbones/iresnet.py
./models/SadTalker/src/face3d/models/arcface_torch/backbones/iresnet2060.py
./models/SadTalker/src/face3d/models/arcface_torch/backbones/mobilefacenet.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/3millions.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/3millions_pfc.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/__init__.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/base.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/glint360k_mbf.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/glint360k_r100.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/glint360k_r18.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/glint360k_r34.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/glint360k_r50.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/ms1mv3_mbf.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/ms1mv3_r18.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/ms1mv3_r2060.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/ms1mv3_r34.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/ms1mv3_r50.py
./models/SadTalker/src/face3d/models/arcface_torch/configs/speed.py
./models/SadTalker/src/face3d/models/arcface_torch/dataset.py
./models/SadTalker/src/face3d/models/arcface_torch/docs/eval.md
./models/SadTalker/src/face3d/models/arcface_torch/docs/install.md
./models/SadTalker/src/face3d/models/arcface_torch/docs/modelzoo.md
./models/SadTalker/src/face3d/models/arcface_torch/docs/speed_benchmark.md
./models/SadTalker/src/face3d/models/arcface_torch/eval/__init__.py
./models/SadTalker/src/face3d/models/arcface_torch/eval/verification.py
./models/SadTalker/src/face3d/models/arcface_torch/eval_ijbc.py
./models/SadTalker/src/face3d/models/arcface_torch/inference.py
./models/SadTalker/src/face3d/models/arcface_torch/losses.py
./models/SadTalker/src/face3d/models/arcface_torch/onnx_helper.py
./models/SadTalker/src/face3d/models/arcface_torch/onnx_ijbc.py
./models/SadTalker/src/face3d/models/arcface_torch/partial_fc.py
./models/SadTalker/src/face3d/models/arcface_torch/requirement.txt
./models/SadTalker/src/face3d/models/arcface_torch/run.sh
./models/SadTalker/src/face3d/models/arcface_torch/torch2onnx.py
./models/SadTalker/src/face3d/models/arcface_torch/train.py
./models/SadTalker/src/face3d/models/arcface_torch/utils/__init__.py
./models/SadTalker/src/face3d/models/arcface_torch/utils/plot.py
./models/SadTalker/src/face3d/models/arcface_torch/utils/utils_amp.py
./models/SadTalker/src/face3d/models/arcface_torch/utils/utils_callbacks.py
./models/SadTalker/src/face3d/models/arcface_torch/utils/utils_config.py
./models/SadTalker/src/face3d/models/arcface_torch/utils/utils_logging.py
./models/SadTalker/src/face3d/models/arcface_torch/utils/utils_os.py
./models/SadTalker/src/face3d/models/base_model.py
./models/SadTalker/src/face3d/models/bfm.py
./models/SadTalker/src/face3d/models/facerecon_model.py
./models/SadTalker/src/face3d/models/losses.py
./models/SadTalker/src/face3d/models/networks.py
./models/SadTalker/src/face3d/models/template_model.py
./models/SadTalker/src/face3d/options/__init__.py
./models/SadTalker/src/face3d/options/base_options.py
./models/SadTalker/src/face3d/options/inference_options.py
./models/SadTalker/src/face3d/options/test_options.py
./models/SadTalker/src/face3d/options/train_options.py
./models/SadTalker/src/face3d/util/BBRegressorParam_r.mat
./models/SadTalker/src/face3d/util/__init__.py
./models/SadTalker/src/face3d/util/detect_lm68.py
./models/SadTalker/src/face3d/util/generate_list.py
./models/SadTalker/src/face3d/util/html.py
./models/SadTalker/src/face3d/util/load_mats.py
./models/SadTalker/src/face3d/util/my_awing_arch.py
./models/SadTalker/src/face3d/util/nvdiffrast.py
./models/SadTalker/src/face3d/util/preprocess.py
./models/SadTalker/src/face3d/util/skin_mask.py
./models/SadTalker/src/face3d/util/test_mean_face.txt
./models/SadTalker/src/face3d/util/util.py
./models/SadTalker/src/face3d/util/visualizer.py
./models/SadTalker/src/face3d/visualize.py
./models/SadTalker/src/facerender/animate.py
./models/SadTalker/src/facerender/modules/dense_motion.py
./models/SadTalker/src/facerender/modules/discriminator.py
./models/SadTalker/src/facerender/modules/generator.py
./models/SadTalker/src/facerender/modules/keypoint_detector.py
./models/SadTalker/src/facerender/modules/make_animation.py
./models/SadTalker/src/facerender/modules/mapping.py
./models/SadTalker/src/facerender/modules/util.py
./models/SadTalker/src/facerender/sync_batchnorm/__init__.py
./models/SadTalker/src/facerender/sync_batchnorm/batchnorm.py
./models/SadTalker/src/facerender/sync_batchnorm/comm.py
./models/SadTalker/src/facerender/sync_batchnorm/replicate.py
./models/SadTalker/src/facerender/sync_batchnorm/unittest.py
./models/SadTalker/src/generate_batch.py
./models/SadTalker/src/generate_facerender_batch.py
./models/SadTalker/src/gradio_demo.py
./models/SadTalker/src/test_audio2coeff.py
./models/SadTalker/src/utils/audio.py
./models/SadTalker/src/utils/croper.py
./models/SadTalker/src/utils/face_enhancer.py
./models/SadTalker/src/utils/hparams.py
./models/SadTalker/src/utils/init_path.py
./models/SadTalker/src/utils/model2safetensor.py
./models/SadTalker/src/utils/paste_pic.py
./models/SadTalker/src/utils/preprocess.py
./models/SadTalker/src/utils/safetensor_helper.py
./models/SadTalker/src/utils/text2speech.py
./models/SadTalker/src/utils/videoio.py
./models/SadTalker/webui.bat
./models/SadTalker/webui.sh
./models/licenses/README.md
./models/video-retalking/.gitignore
./models/video-retalking/CODE_OF_CONDUCT.md
./models/video-retalking/LICENSE
./models/video-retalking/README.md
./models/video-retalking/cog.yaml
./models/video-retalking/docs/index.html
./models/video-retalking/docs/static/css/bulma-carousel.min.css
./models/video-retalking/docs/static/css/bulma-slider.min.css
./models/video-retalking/docs/static/css/bulma.css.map.txt
./models/video-retalking/docs/static/css/bulma.min.css
./models/video-retalking/docs/static/css/fontawesome.all.min.css
./models/video-retalking/docs/static/css/index.css
./models/video-retalking/docs/static/images/pipeline.png
./models/video-retalking/docs/static/images/teaser.png
./models/video-retalking/docs/static/js/bulma-carousel.js
./models/video-retalking/docs/static/js/bulma-carousel.min.js
./models/video-retalking/docs/static/js/bulma-slider.js
./models/video-retalking/docs/static/js/bulma-slider.min.js
./models/video-retalking/docs/static/js/fontawesome.all.min.js
./models/video-retalking/docs/static/js/index.js
./models/video-retalking/docs/static/pdfs/sample.pdf
./models/video-retalking/docs/static/videos/Ablation.mp4
./models/video-retalking/docs/static/videos/Comparison.mp4
./models/video-retalking/docs/static/videos/Results_in_the_wild.mp4
./models/video-retalking/examples/audio/1.wav
./models/video-retalking/examples/audio/2.wav
./models/video-retalking/examples/face/1.mp4
./models/video-retalking/examples/face/2.mp4
./models/video-retalking/examples/face/3.mp4
./models/video-retalking/examples/face/4.mp4
./models/video-retalking/examples/face/5.mp4
./models/video-retalking/inference.py
./models/video-retalking/inference_videoretalking.sh
./models/video-retalking/models/DNet.py
./models/video-retalking/models/ENet.py
./models/video-retalking/models/LNet.py
./models/video-retalking/models/__init__.py
./models/video-retalking/models/base_blocks.py
./models/video-retalking/models/ffc.py
./models/video-retalking/models/transformer.py
./models/video-retalking/predict.py
./models/video-retalking/quick_demo.ipynb
./models/video-retalking/requirements.txt
./models/video-retalking/third_part/GFPGAN/LICENSE
./models/video-retalking/third_part/GFPGAN/gfpgan/__init__.py
./models/video-retalking/third_part/GFPGAN/gfpgan/archs/__init__.py
./models/video-retalking/third_part/GFPGAN/gfpgan/archs/arcface_arch.py
./models/video-retalking/third_part/GFPGAN/gfpgan/archs/gfpgan_bilinear_arch.py
./models/video-retalking/third_part/GFPGAN/gfpgan/archs/gfpganv1_arch.py
./models/video-retalking/third_part/GFPGAN/gfpgan/archs/gfpganv1_clean_arch.py
./models/video-retalking/third_part/GFPGAN/gfpgan/archs/stylegan2_bilinear_arch.py
./models/video-retalking/third_part/GFPGAN/gfpgan/archs/stylegan2_clean_arch.py
./models/video-retalking/third_part/GFPGAN/gfpgan/data/__init__.py
./models/video-retalking/third_part/GFPGAN/gfpgan/data/ffhq_degradation_dataset.py
./models/video-retalking/third_part/GFPGAN/gfpgan/models/__init__.py
./models/video-retalking/third_part/GFPGAN/gfpgan/models/gfpgan_model.py
./models/video-retalking/third_part/GFPGAN/gfpgan/train.py
./models/video-retalking/third_part/GFPGAN/gfpgan/utils.py
./models/video-retalking/third_part/GFPGAN/gfpgan/version.py
./models/video-retalking/third_part/GFPGAN/gfpgan/weights/README.md
./models/video-retalking/third_part/GFPGAN/options/train_gfpgan_v1.yml
./models/video-retalking/third_part/GFPGAN/options/train_gfpgan_v1_simple.yml
./models/video-retalking/third_part/GPEN/align_faces.py
./models/video-retalking/third_part/GPEN/face_detect/.DS_Store
./models/video-retalking/third_part/GPEN/face_detect/data/FDDB/img_list.txt
./models/video-retalking/third_part/GPEN/face_detect/data/__init__.py
./models/video-retalking/third_part/GPEN/face_detect/data/config.py
./models/video-retalking/third_part/GPEN/face_detect/data/data_augment.py
./models/video-retalking/third_part/GPEN/face_detect/data/wider_face.py
./models/video-retalking/third_part/GPEN/face_detect/facemodels/__init__.py
./models/video-retalking/third_part/GPEN/face_detect/facemodels/net.py
./models/video-retalking/third_part/GPEN/face_detect/facemodels/retinaface.py
./models/video-retalking/third_part/GPEN/face_detect/layers/__init__.py
./models/video-retalking/third_part/GPEN/face_detect/layers/functions/prior_box.py
./models/video-retalking/third_part/GPEN/face_detect/layers/modules/__init__.py
./models/video-retalking/third_part/GPEN/face_detect/layers/modules/multibox_loss.py
./models/video-retalking/third_part/GPEN/face_detect/retinaface_detection.py
./models/video-retalking/third_part/GPEN/face_detect/utils/__init__.py
./models/video-retalking/third_part/GPEN/face_detect/utils/box_utils.py
./models/video-retalking/third_part/GPEN/face_detect/utils/nms/__init__.py
./models/video-retalking/third_part/GPEN/face_detect/utils/nms/py_cpu_nms.py
./models/video-retalking/third_part/GPEN/face_detect/utils/timer.py
./models/video-retalking/third_part/GPEN/face_model/face_gan.py
./models/video-retalking/third_part/GPEN/face_model/gpen_model.py
./models/video-retalking/third_part/GPEN/face_model/op/__init__.py
./models/video-retalking/third_part/GPEN/face_model/op/fused_act.py
./models/video-retalking/third_part/GPEN/face_model/op/fused_bias_act.cpp
./models/video-retalking/third_part/GPEN/face_model/op/fused_bias_act_kernel.cu
./models/video-retalking/third_part/GPEN/face_model/op/upfirdn2d.cpp
./models/video-retalking/third_part/GPEN/face_model/op/upfirdn2d.py
./models/video-retalking/third_part/GPEN/face_model/op/upfirdn2d_kernel.cu
./models/video-retalking/third_part/GPEN/face_morpher/.gitignore
./models/video-retalking/third_part/GPEN/face_morpher/README.rst
./models/video-retalking/third_part/GPEN/face_morpher/facemorpher/__init__.py
./models/video-retalking/third_part/GPEN/face_morpher/facemorpher/aligner.py
./models/video-retalking/third_part/GPEN/face_morpher/facemorpher/averager.py
./models/video-retalking/third_part/GPEN/face_morpher/facemorpher/blender.py
./models/video-retalking/third_part/GPEN/face_morpher/facemorpher/locator.py
./models/video-retalking/third_part/GPEN/face_morpher/facemorpher/morpher.py
./models/video-retalking/third_part/GPEN/face_morpher/facemorpher/plotter.py
./models/video-retalking/third_part/GPEN/face_morpher/facemorpher/videoer.py
./models/video-retalking/third_part/GPEN/face_morpher/facemorpher/warper.py
./models/video-retalking/third_part/GPEN/face_morpher/requirements.txt
./models/video-retalking/third_part/GPEN/face_morpher/scripts/make_docs.sh
./models/video-retalking/third_part/GPEN/face_morpher/scripts/publish_ghpages.sh
./models/video-retalking/third_part/GPEN/face_morpher/setup.cfg
./models/video-retalking/third_part/GPEN/face_morpher/setup.py
./models/video-retalking/third_part/GPEN/face_parse/blocks.py
./models/video-retalking/third_part/GPEN/face_parse/face_parsing.py
./models/video-retalking/third_part/GPEN/face_parse/mask.png
./models/video-retalking/third_part/GPEN/face_parse/model.py
./models/video-retalking/third_part/GPEN/face_parse/parse_model.py
./models/video-retalking/third_part/GPEN/face_parse/resnet.py
./models/video-retalking/third_part/GPEN/face_parse/test.png
./models/video-retalking/third_part/GPEN/gpen_face_enhancer.py
./models/video-retalking/third_part/face3d/checkpoints/model_name/test_opt.txt
./models/video-retalking/third_part/face3d/coeff_detector.py
./models/video-retalking/third_part/face3d/data/__init__.py
./models/video-retalking/third_part/face3d/data/base_dataset.py
./models/video-retalking/third_part/face3d/data/flist_dataset.py
./models/video-retalking/third_part/face3d/data/image_folder.py
./models/video-retalking/third_part/face3d/data/template_dataset.py
./models/video-retalking/third_part/face3d/data_preparation.py
./models/video-retalking/third_part/face3d/extract_kp_videos.py
./models/video-retalking/third_part/face3d/face_recon_videos.py
./models/video-retalking/third_part/face3d/models/__init__.py
./models/video-retalking/third_part/face3d/models/arcface_torch/README.md
./models/video-retalking/third_part/face3d/models/arcface_torch/backbones/__init__.py
./models/video-retalking/third_part/face3d/models/arcface_torch/backbones/iresnet.py
./models/video-retalking/third_part/face3d/models/arcface_torch/backbones/iresnet2060.py
./models/video-retalking/third_part/face3d/models/arcface_torch/backbones/mobilefacenet.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/3millions.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/3millions_pfc.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/__init__.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/base.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/glint360k_mbf.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/glint360k_r100.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/glint360k_r18.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/glint360k_r34.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/glint360k_r50.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/ms1mv3_mbf.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/ms1mv3_r18.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/ms1mv3_r2060.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/ms1mv3_r34.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/ms1mv3_r50.py
./models/video-retalking/third_part/face3d/models/arcface_torch/configs/speed.py
./models/video-retalking/third_part/face3d/models/arcface_torch/dataset.py
./models/video-retalking/third_part/face3d/models/arcface_torch/docs/eval.md
./models/video-retalking/third_part/face3d/models/arcface_torch/docs/install.md
./models/video-retalking/third_part/face3d/models/arcface_torch/docs/modelzoo.md
./models/video-retalking/third_part/face3d/models/arcface_torch/docs/speed_benchmark.md
./models/video-retalking/third_part/face3d/models/arcface_torch/eval/__init__.py
./models/video-retalking/third_part/face3d/models/arcface_torch/eval/verification.py
./models/video-retalking/third_part/face3d/models/arcface_torch/eval_ijbc.py
./models/video-retalking/third_part/face3d/models/arcface_torch/inference.py
./models/video-retalking/third_part/face3d/models/arcface_torch/losses.py
./models/video-retalking/third_part/face3d/models/arcface_torch/onnx_helper.py
./models/video-retalking/third_part/face3d/models/arcface_torch/onnx_ijbc.py
./models/video-retalking/third_part/face3d/models/arcface_torch/partial_fc.py
./models/video-retalking/third_part/face3d/models/arcface_torch/requirement.txt
./models/video-retalking/third_part/face3d/models/arcface_torch/run.sh
./models/video-retalking/third_part/face3d/models/arcface_torch/torch2onnx.py
./models/video-retalking/third_part/face3d/models/arcface_torch/train.py
./models/video-retalking/third_part/face3d/models/arcface_torch/utils/__init__.py
./models/video-retalking/third_part/face3d/models/arcface_torch/utils/plot.py
./models/video-retalking/third_part/face3d/models/arcface_torch/utils/utils_amp.py
./models/video-retalking/third_part/face3d/models/arcface_torch/utils/utils_callbacks.py
./models/video-retalking/third_part/face3d/models/arcface_torch/utils/utils_config.py
./models/video-retalking/third_part/face3d/models/arcface_torch/utils/utils_logging.py
./models/video-retalking/third_part/face3d/models/arcface_torch/utils/utils_os.py
./models/video-retalking/third_part/face3d/models/base_model.py
./models/video-retalking/third_part/face3d/models/bfm.py
./models/video-retalking/third_part/face3d/models/facerecon_model.py
./models/video-retalking/third_part/face3d/models/losses.py
./models/video-retalking/third_part/face3d/models/networks.py
./models/video-retalking/third_part/face3d/models/template_model.py
./models/video-retalking/third_part/face3d/options/__init__.py
./models/video-retalking/third_part/face3d/options/base_options.py
./models/video-retalking/third_part/face3d/options/inference_options.py
./models/video-retalking/third_part/face3d/options/test_options.py
./models/video-retalking/third_part/face3d/options/train_options.py
./models/video-retalking/third_part/face3d/util/BBRegressorParam_r.mat
./models/video-retalking/third_part/face3d/util/__init__.py
./models/video-retalking/third_part/face3d/util/detect_lm68.py
./models/video-retalking/third_part/face3d/util/generate_list.py
./models/video-retalking/third_part/face3d/util/html.py
./models/video-retalking/third_part/face3d/util/load_mats.py
./models/video-retalking/third_part/face3d/util/nvdiffrast.py
./models/video-retalking/third_part/face3d/util/preprocess.py
./models/video-retalking/third_part/face3d/util/skin_mask.py
./models/video-retalking/third_part/face3d/util/test_mean_face.txt
./models/video-retalking/third_part/face3d/util/util.py
./models/video-retalking/third_part/face3d/util/visualizer.py
./models/video-retalking/third_part/face_detection/README.md
./models/video-retalking/third_part/face_detection/__init__.py
./models/video-retalking/third_part/face_detection/api.py
./models/video-retalking/third_part/face_detection/detection/__init__.py
./models/video-retalking/third_part/face_detection/detection/core.py
./models/video-retalking/third_part/face_detection/detection/sfd/__init__.py
./models/video-retalking/third_part/face_detection/detection/sfd/bbox.py
./models/video-retalking/third_part/face_detection/detection/sfd/detect.py
./models/video-retalking/third_part/face_detection/detection/sfd/net_s3fd.py
./models/video-retalking/third_part/face_detection/detection/sfd/sfd_detector.py
./models/video-retalking/third_part/face_detection/models.py
./models/video-retalking/third_part/face_detection/utils.py
./models/video-retalking/third_part/ganimation_replicate/LICENSE
./models/video-retalking/third_part/ganimation_replicate/checkpoints/opt.txt
./models/video-retalking/third_part/ganimation_replicate/checkpoints/run_script.sh
./models/video-retalking/third_part/ganimation_replicate/ckpts/ganimation/220419_183211/opt.txt
./models/video-retalking/third_part/ganimation_replicate/ckpts/ganimation/220419_183211/run_script.sh
./models/video-retalking/third_part/ganimation_replicate/ckpts/ganimation/220419_183229/opt.txt
./models/video-retalking/third_part/ganimation_replicate/ckpts/ganimation/220419_183229/run_script.sh
./models/video-retalking/third_part/ganimation_replicate/ckpts/opt.txt
./models/video-retalking/third_part/ganimation_replicate/ckpts/run_script.sh
./models/video-retalking/third_part/ganimation_replicate/data/__init__.py
./models/video-retalking/third_part/ganimation_replicate/data/base_dataset.py
./models/video-retalking/third_part/ganimation_replicate/data/celeba.py
./models/video-retalking/third_part/ganimation_replicate/data/data_loader.py
./models/video-retalking/third_part/ganimation_replicate/main.py
./models/video-retalking/third_part/ganimation_replicate/model/__init__.py
./models/video-retalking/third_part/ganimation_replicate/model/base_model.py
./models/video-retalking/third_part/ganimation_replicate/model/ganimation.py
./models/video-retalking/third_part/ganimation_replicate/model/model_utils.py
./models/video-retalking/third_part/ganimation_replicate/model/stargan.py
./models/video-retalking/third_part/ganimation_replicate/options.py
./models/video-retalking/third_part/ganimation_replicate/solvers.py
./models/video-retalking/third_part/ganimation_replicate/visualizer.py
./models/video-retalking/utils/alignment_stit.py
./models/video-retalking/utils/audio.py
./models/video-retalking/utils/ffhq_preprocess.py
./models/video-retalking/utils/flow_util.py
./models/video-retalking/utils/hparams.py
./models/video-retalking/utils/inference_utils.py
./models/video-retalking/webUI.py
./out/episode_001_preview/final_1080p.mp4
./out/episode_001_preview/final_1080p_v2.mp4
./out/episode_001_preview/logs/pipeline.log
./out/episode_001_preview/run_report.json
./out/episode_001_preview/stage1_audio/preprocessed.wav
./out/episode_001_preview/stage2_diarize/diarization.json
./out/episode_001_preview/stage2_diarize/speaker_a.wav
./out/episode_001_preview/stage2_diarize/speaker_b.wav
./out/episode_001_preview/stage4_composite/composited.mp4
./out/episode_001_preview/stage5_subtitles/transcript_en.srt
./out/episode_001_preview/stage6_export/final_1080p.mp4
./out/episode_002_preview/final_720p_preview.mp4
./out/episode_002_preview/stage1_audio/preprocessed.wav
./out/episode_002_preview/stage5_subtitles/transcript_en.srt
./out/episode_002_preview/stage6_export/composited_720p.mp4
./podcast_pipeline/__init__.py
./podcast_pipeline/audio.py
./podcast_pipeline/composite.py
./podcast_pipeline/diarize.py
./podcast_pipeline/export.py
./podcast_pipeline/lipsync.py
./podcast_pipeline/subtitles.py
./podcast_pipeline/transcribe.py
./podcast_pipeline/utils.py
./requirements.txt
./run_podcast.py
./scripts/lipsync_sync_api.py
./scripts/prep_assets.py
./scripts/self_check.log
./scripts/self_check.py
./scripts/setup_env.sh
```

## Phase 1: Architecture Reconstruction

### Entrypoints
- `run_podcast.py`: orchestrates stages, writes `run_report.json`, and produces `final_720p.mp4` inside `--out`.
- `scripts/prep_assets.py`: extracts `assets/speaker_{a,b}.jpg` and loops Veo videos to `assets/speaker_{a,b}_looped.mp4`.
- `scripts/self_check.py`: sanity checks for assets and imports.

### Implemented stage graph
```text
run_podcast.py
  1) podcast_pipeline/audio.py:preprocess_audio
  2) podcast_pipeline/transcribe.py:transcribe_audio
  3) podcast_pipeline/diarize.py:diarize_audio
  4a) podcast_pipeline/lipsync.py:render_speaker_full_video (HOST_A)
  4b) podcast_pipeline/lipsync.py:render_speaker_full_video (HOST_B)
  5) podcast_pipeline/composite.py:composite_video
  6) podcast_pipeline/subtitles.py:generate_srt
  7) podcast_pipeline/export.py:burn_subtitles_and_export

External executables: ffmpeg, ffprobe
Python deps: faster-whisper (transcribe), PyYAML (config)
Third-party model repos invoked by subprocess: models/SadTalker (speech segments)
```

## Phase 2: File-by-File Deep Analysis

### `run_podcast.py`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/run_podcast.py`
- Size: `7427` bytes
- Role: entrypoint/orchestrator
- SHA-256 (first 2MB): `980aa1c1c49f3cf94415f10563003678f9d3bfa7c1eff0b7eb77db34a9b7b472`

**Code analysis**
- Top-level functions: `4`
  - `parse_args()` (line 33)
  - `resolve_path(base, value)` (line 45)
  - `cleanup(paths)` (line 50)
  - `main()` (line 56)
- Top-level classes: `0`
- Imports (unique): `25`
  - `__future__.annotations`, `argparse`, `dataclasses.asdict`, `pathlib.Path`, `podcast_pipeline.audio.preprocess_audio`, `podcast_pipeline.composite.composite_video`, `podcast_pipeline.diarize.diarize_audio`, `podcast_pipeline.export.burn_subtitles_and_export`, `podcast_pipeline.lipsync.render_speaker_full_video`, `podcast_pipeline.subtitles.generate_srt`, `podcast_pipeline.transcribe.transcribe_audio`, `podcast_pipeline.utils.PipelineError`, `podcast_pipeline.utils.StageStat`, `podcast_pipeline.utils.StageTimer`, `podcast_pipeline.utils.bool_from_optional_flag`, `podcast_pipeline.utils.ensure_dir`, `podcast_pipeline.utils.load_config`, `podcast_pipeline.utils.probe_audio_duration`, `podcast_pipeline.utils.setup_logger`, `podcast_pipeline.utils.stage_error_boundary`, `podcast_pipeline.utils.write_json`, `shutil`, `sys`, `time`, `typing.List`
- subprocess usage refs: `0`
- ffmpeg string refs: `0`

**Content head (first 40 lines)**
```text
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
import time
from dataclasses import asdict
from pathlib import Path
from typing import List

from podcast_pipeline.audio import preprocess_audio
from podcast_pipeline.composite import composite_video
from podcast_pipeline.diarize import diarize_audio
from podcast_pipeline.export import burn_subtitles_and_export
from podcast_pipeline.lipsync import render_speaker_full_video
from podcast_pipeline.subtitles import generate_srt
from podcast_pipeline.transcribe import transcribe_audio
from podcast_pipeline.utils import (
    PipelineError,
    StageStat,
    StageTimer,
    bool_from_optional_flag,
    ensure_dir,
    load_config,
    probe_audio_duration,
    setup_logger,
    stage_error_boundary,
    write_json,
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Two-host local podcast video generator")
    p.add_argument("--audio", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--config", default="configs/default_config.yaml")
    p.add_argument("--speaker-a-image", default="")
    p.add_argument("--speaker-b-image", default="")
    p.add_argument("--keep-intermediates", nargs="?", const="true", default=None)
```

### `README.md`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/README.md`
- Size: `2764` bytes
- Role: first-party
- SHA-256 (first 2MB): `3f7089ae6299d9a1360bc25b2573a62c0290d096d84d75efe014c5e0707cef6b`

**Content head (first 80 lines)**
```text
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
```

### `requirements.txt`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/requirements.txt`
- Size: `132` bytes
- Role: python dependency manifest
- SHA-256 (first 2MB): `9bd7ff12d7a84967ed2e8ca02acec6f18d2df18f7f229b5b794fa9401bd53e74`

**Content head (first 80 lines)**
```text
faster-whisper==1.0.3
torch>=2.1.0
torchaudio>=2.1.0
numpy>=1.26.0
PyYAML>=6.0
requests>=2.31.0
Pillow>=10.0.0
ffmpeg-python>=0.2.0
```

### `environment.yml`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/environment.yml`
- Size: `205` bytes
- Role: configuration
- SHA-256 (first 2MB): `88d17c161aa092962b9d4a1aa200c6bb151739ec98effab6289d45764c61aaad`

**Content head (first 80 lines)**
```text
name: hindi-podcast-local
channels:
  - pytorch
  - nvidia
  - conda-forge
dependencies:
  - python=3.10
  - ffmpeg=6.1
  - pytorch=2.4.*
  - pytorch-cuda=12.1
  - pip
  - pip:
      - -r requirements.txt
```

### `configs/default_config.yaml`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/configs/default_config.yaml`
- Size: `1139` bytes
- Role: configuration
- SHA-256 (first 2MB): `93fefef8b06e0d2bd059a6bc623206266316d7b7ca70fe6fa5dc1c1ef5294fe8`

**Content head (first 80 lines)**
```text
project:
  name: english-two-speaker-podcast
  seed: 124578

paths:
  assets_dir: assets
  models_dir: models
  work_dir: out

audio:
  target_sample_rate: 16000
  target_channels: 1
  loudnorm: "I=-16:TP=-1.5:LRA=11"
  denoise: false
  denoise_nf: -25
  min_duration_sec: 60
  max_duration_sec: 300

speakers:
  a:
    source_image: "assets/speaker_a.jpg"
    idle_video: "assets/speaker_a_looped.mp4"
    input_video: "/Users/pranamyajain/Downloads/male podcast studio.mp4"
  b:
    source_image: "assets/speaker_b.jpg"
    idle_video: "assets/speaker_b_looped.mp4"
    input_video: "/Users/pranamyajain/Downloads/female podcast studio.mp4"

transcription:
  model_name: "large-v3"
  language: "en"
  word_timestamps: true

diarize:
  speaker_change_gap_sec: 0.8

lipsync:
  backend: "sadtalker"
  repo_path: "models/SadTalker"

subtitles:
  model_name: "large-v3"
  device: "cpu"
  compute_type: "int8"
  language: "en"
  beam_size: 5
  vad_filter: true
  output_srt: "transcript_en.srt"

export:
  width: 1280
  height: 720
  fps: 25
  crf: 18
  audio_bitrate: "192k"
  audio_sample_rate: 48000
  preset: "medium"
  pix_fmt: "yuv420p"
```

### `podcast_pipeline/__init__.py`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/__init__.py`
- Size: `201` bytes
- Role: pipeline module
- SHA-256 (first 2MB): `7a67062e869f50100daaf7fba1d56c67becfe3c17d8d95ac7f66e55e84b7eb78`

**Code analysis**
- Top-level functions: `0`
- Top-level classes: `0`
- Imports (unique): `0`
- subprocess usage refs: `0`
- ffmpeg string refs: `0`

**Content head (first 40 lines)**
```text
"""Local two-speaker English podcast video pipeline package."""

__all__ = [
    "audio",
    "transcribe",
    "diarize",
    "lipsync",
    "composite",
    "subtitles",
    "export",
    "utils",
]
```

### `podcast_pipeline/audio.py`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/audio.py`
- Size: `1683` bytes
- Role: pipeline module
- SHA-256 (first 2MB): `0c2b7c0b4987b4cbed2551071137407aea534171f0e3fd3c0b672cf483ea63a3`

**Code analysis**
- Top-level functions: `1`
  - `preprocess_audio(input_audio, stage_dir, config, logger)` (line 10)
- Top-level classes: `0`
- Imports (unique): `9`
  - `__future__.annotations`, `logging`, `pathlib.Path`, `typing.Any`, `typing.Dict`, `utils.PipelineError`, `utils.ensure_binary`, `utils.ensure_dir`, `utils.run_command`
- subprocess usage refs: `0`
- ffmpeg string refs: `3`

**Content head (first 40 lines)**
```text
from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict

from .utils import PipelineError, ensure_binary, ensure_dir, run_command


def preprocess_audio(
    input_audio: Path,
    stage_dir: Path,
    config: Dict[str, Any],
    logger: logging.Logger,
) -> Path:
    ensure_binary("ffmpeg")
    ensure_dir(stage_dir)

    audio_cfg = config["audio"]
    target_sr = int(audio_cfg["target_sample_rate"])
    target_ch = int(audio_cfg["target_channels"])
    loudnorm = str(audio_cfg["loudnorm"])

    normalized_wav = stage_dir / "preprocessed.wav"
    denoised_wav = stage_dir / "preprocessed_denoised.wav"

    # highpass at 20Hz removes most DC components in practice.
    audio_filter = f"highpass=f=20,loudnorm={loudnorm}"
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(input_audio),
        "-af",
        audio_filter,
        "-ar",
        str(target_sr),
        "-ac",
        str(target_ch),
        str(normalized_wav),
```

### `podcast_pipeline/transcribe.py`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/transcribe.py`
- Size: `2920` bytes
- Role: pipeline module
- SHA-256 (first 2MB): `a51849a3f0003975a469fd30a8aa39f41799ead5c69c949a914e9e2f05174c75`

**Code analysis**
- Top-level functions: `1`
  - `transcribe_audio(audio_wav, stage_dir, config, logger)` (line 11)
- Top-level classes: `0`
- Imports (unique): `12`
  - `__future__.annotations`, `faster_whisper.WhisperModel`, `json`, `logging`, `pathlib.Path`, `typing.Any`, `typing.Dict`, `typing.Iterable`, `typing.List`, `typing.Tuple`, `utils.PipelineError`, `utils.ensure_dir`
- subprocess usage refs: `0`
- ffmpeg string refs: `0`

**Content head (first 40 lines)**
```text
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

from .utils import PipelineError, ensure_dir


def transcribe_audio(
    audio_wav: Path,
    stage_dir: Path,
    config: Dict[str, Any],
    logger: logging.Logger,
) -> Tuple[Path, Path]:
    ensure_dir(stage_dir)
    try:
        from faster_whisper import WhisperModel  # MIT
    except Exception as exc:
        raise PipelineError("faster-whisper is not installed") from exc

    sub_cfg = config.get("subtitles", {})
    model_name = str(sub_cfg.get("model_name", "large-v3"))
    device = str(sub_cfg.get("device", "cpu"))
    compute_type = str(sub_cfg.get("compute_type", "int8"))
    beam_size = int(sub_cfg.get("beam_size", 5))
    vad_filter = bool(sub_cfg.get("vad_filter", True))

    logger.info(
        "Transcribing with faster-whisper model=%s device=%s compute_type=%s",
        model_name,
        device,
        compute_type,
    )
    model = WhisperModel(model_name, device=device, compute_type=compute_type)
    segments, info = model.transcribe(
        str(audio_wav),
        language="en",
        task="transcribe",
```

### `podcast_pipeline/diarize.py`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/diarize.py`
- Size: `4158` bytes
- Role: pipeline module
- SHA-256 (first 2MB): `0ff1fc048474db5daef72fd15a3346a1b12c61bac4337428cf267b394984cf8a`

**Code analysis**
- Top-level functions: `5`
  - `diarize_audio(transcript_words_json, audio_wav, stage_dir, config, logger)` (line 11)
  - `_build_turn_segments(words, max_gap)` (line 53)
  - `_segments_for(segments, speaker)` (line 82)
  - `_volume_expr(segments)` (line 94)
  - `_render_speaker_masked_wav(input_wav, output_wav, active_segments, logger)` (line 100)
- Top-level classes: `0`
- Imports (unique): `14`
  - `__future__.annotations`, `json`, `logging`, `pathlib.Path`, `typing.Any`, `typing.Dict`, `typing.List`, `typing.Sequence`, `typing.Tuple`, `utils.PipelineError`, `utils.ensure_binary`, `utils.ensure_dir`, `utils.probe_audio_duration`, `utils.run_command`
- subprocess usage refs: `0`
- ffmpeg string refs: `2`

**Content head (first 40 lines)**
```text
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

from .utils import PipelineError, ensure_binary, ensure_dir, probe_audio_duration, run_command


def diarize_audio(
    transcript_words_json: Path,
    audio_wav: Path,
    stage_dir: Path,
    config: Dict[str, Any],
    logger: logging.Logger,
) -> Tuple[Path, Path, Path]:
    ensure_binary("ffmpeg")
    ensure_dir(stage_dir)

    if not transcript_words_json.exists():
        raise PipelineError(f"Transcript words JSON missing: {transcript_words_json}")
    words = json.loads(transcript_words_json.read_text(encoding="utf-8"))
    if not isinstance(words, list) or not words:
        raise PipelineError("Transcript words JSON is empty/invalid")

    gap = float(config.get("diarize", {}).get("speaker_change_gap_sec", 0.8))
    segments = _build_turn_segments(words, max_gap=gap)

    diarization_json = stage_dir / "diarization.json"
    diarization_json.write_text(json.dumps(segments, indent=2), encoding="utf-8")

    speaker_a_wav = stage_dir / "speaker_a.wav"
    speaker_b_wav = stage_dir / "speaker_b.wav"
    _render_speaker_masked_wav(audio_wav, speaker_a_wav, _segments_for(segments, "HOST_A"), logger)
    _render_speaker_masked_wav(audio_wav, speaker_b_wav, _segments_for(segments, "HOST_B"), logger)

    for p in (diarization_json, speaker_a_wav, speaker_b_wav):
        if not p.exists() or p.stat().st_size <= 0:
            raise PipelineError(f"Diarization stage output missing/empty: {p}")
```

### `podcast_pipeline/lipsync.py`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/lipsync.py`
- Size: `7477` bytes
- Role: pipeline module
- SHA-256 (first 2MB): `866480449d9810019359ecc6d3b8915ccf9be623f2079e419e9daa3eaaa84084`

**Code analysis**
- Top-level functions: `6`
  - `render_speaker_full_video(speaker_label, source_image, speaker_padded_wav, original_full_wav, diarization_json, idle_clip_mp4, output_dir, config, fps, logger)` (line 11)
  - `_render_speech_segment_sadtalker(source_image, speaker_padded_wav, start, duration, out_path, tmp_dir, config, fps, logger)` (line 106)
  - `_render_idle_segment(idle_clip, duration, fps, out_path, logger)` (line 190)
  - `_build_timeline(segments, speaker_label, full_duration)` (line 214)
  - `_find_latest_mp4(path)` (line 237)
  - `_validate_duration(video_path, reference_audio)` (line 244)
- Top-level classes: `0`
- Imports (unique): `13`
  - `__future__.annotations`, `json`, `logging`, `pathlib.Path`, `typing.Any`, `typing.Dict`, `typing.List`, `typing.Tuple`, `utils.PipelineError`, `utils.ensure_binary`, `utils.ensure_dir`, `utils.probe_audio_duration`, `utils.run_command`
- subprocess usage refs: `0`
- ffmpeg string refs: `5`

**Content head (first 40 lines)**
```text
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Tuple

from .utils import PipelineError, ensure_binary, ensure_dir, probe_audio_duration, run_command


def render_speaker_full_video(
    speaker_label: str,
    source_image: Path,
    speaker_padded_wav: Path,
    original_full_wav: Path,
    diarization_json: Path,
    idle_clip_mp4: Path,
    output_dir: Path,
    config: Dict[str, Any],
    fps: int,
    logger: logging.Logger,
) -> Path:
    ensure_binary("ffmpeg")
    ensure_dir(output_dir)

    if speaker_label not in {"HOST_A", "HOST_B"}:
        raise PipelineError(f"Invalid speaker label: {speaker_label}")
    for p in (source_image, speaker_padded_wav, original_full_wav, diarization_json, idle_clip_mp4):
        if not p.exists():
            raise PipelineError(f"Lipsync input missing: {p}")

    timeline = _build_timeline(
        segments=json.loads(diarization_json.read_text(encoding="utf-8")),
        speaker_label=speaker_label,
        full_duration=probe_audio_duration(original_full_wav),
    )
    if not timeline:
        raise PipelineError(f"No timeline segments built for {speaker_label}")

    tmp_dir = ensure_dir(output_dir / f"tmp_{speaker_label.lower()}")
```

### `podcast_pipeline/composite.py`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/composite.py`
- Size: `1857` bytes
- Role: pipeline module
- SHA-256 (first 2MB): `1ca863d47aad1f21b271bae186f748884d11296a8b2b3f65c27416cd2e899d9b`

**Code analysis**
- Top-level functions: `1`
  - `composite_video(host_a_video, host_b_video, full_audio_wav, stage_dir, logger)` (line 9)
- Top-level classes: `0`
- Imports (unique): `8`
  - `__future__.annotations`, `logging`, `pathlib.Path`, `utils.PipelineError`, `utils.ensure_binary`, `utils.ensure_dir`, `utils.probe_audio_duration`, `utils.run_command`
- subprocess usage refs: `0`
- ffmpeg string refs: `2`

**Content head (first 40 lines)**
```text
from __future__ import annotations

import logging
from pathlib import Path

from .utils import PipelineError, ensure_binary, ensure_dir, probe_audio_duration, run_command


def composite_video(
    host_a_video: Path,
    host_b_video: Path,
    full_audio_wav: Path,
    stage_dir: Path,
    logger: logging.Logger,
) -> Path:
    ensure_binary("ffmpeg")
    ensure_dir(stage_dir)

    for p in (host_a_video, host_b_video, full_audio_wav):
        if not p.exists():
            raise PipelineError(f"Composite input missing: {p}")

    out_path = stage_dir / "composited.mp4"
    target_duration = probe_audio_duration(full_audio_wav)
    filter_complex = (
        "[0:v]scale=640:720:force_original_aspect_ratio=decrease,"
        "pad=640:720:(ow-iw)/2:(oh-ih)/2,setsar=1[left];"
        "[1:v]scale=640:720:force_original_aspect_ratio=decrease,"
        "pad=640:720:(ow-iw)/2:(oh-ih)/2,setsar=1[right];"
        "[left][right]hstack=inputs=2[v]"
    )

    # HOST_B on left, HOST_A on right
    run_command(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(host_b_video),
            "-i",
```

### `podcast_pipeline/subtitles.py`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/subtitles.py`
- Size: `2533` bytes
- Role: pipeline module
- SHA-256 (first 2MB): `dbcb9eb301d53fbe9e821cd357b3c1d6f96fd08817f5749857953d65724baaf3`

**Code analysis**
- Top-level functions: `3`
  - `generate_srt(transcript_segments_json, diarization_json, stage_dir, logger)` (line 11)
  - `_speaker_for_segment(start, end, diar, tolerance)` (line 54)
  - `_fmt(seconds)` (line 71)
- Top-level classes: `0`
- Imports (unique): `10`
  - `__future__.annotations`, `json`, `logging`, `pathlib.Path`, `typing.Any`, `typing.Dict`, `typing.List`, `typing.Sequence`, `utils.PipelineError`, `utils.ensure_dir`
- subprocess usage refs: `0`
- ffmpeg string refs: `0`

**Content head (first 40 lines)**
```text
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Sequence

from .utils import PipelineError, ensure_dir


def generate_srt(
    transcript_segments_json: Path,
    diarization_json: Path,
    stage_dir: Path,
    logger: logging.Logger,
) -> Path:
    ensure_dir(stage_dir)
    if not transcript_segments_json.exists():
        raise PipelineError(f"Transcript segments JSON missing: {transcript_segments_json}")
    if not diarization_json.exists():
        raise PipelineError(f"Diarization JSON missing: {diarization_json}")

    segments = json.loads(transcript_segments_json.read_text(encoding="utf-8"))
    diar = json.loads(diarization_json.read_text(encoding="utf-8"))
    if not isinstance(segments, list) or not segments:
        raise PipelineError("Transcript segments are empty")

    tolerance = 0.2
    lines: List[str] = []
    idx = 1
    for seg in segments:
        s = float(seg.get("start", 0.0))
        e = float(seg.get("end", 0.0))
        txt = str(seg.get("text", "")).strip()
        if not txt or e <= s:
            continue
        speaker = _speaker_for_segment(s, e, diar, tolerance)
        label = "[HOST A]" if speaker == "HOST_A" else "[HOST B]"
        lines.append(str(idx))
        lines.append(f"{_fmt(s)} --> {_fmt(e)}")
```

### `podcast_pipeline/export.py`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/export.py`
- Size: `2481` bytes
- Role: pipeline module
- SHA-256 (first 2MB): `57717c6a2a45e49fb7e8991ead75cc0f7ebeb0144d02fd5c8816f25cc1bbbe5d`

**Code analysis**
- Top-level functions: `3`
  - `burn_subtitles_and_export(composited_video, subtitles_srt, output_path, logger)` (line 9)
  - `validate_final_video(video_path)` (line 52)
  - `_escape_filter_path(path)` (line 67)
- Top-level classes: `0`
- Imports (unique): `7`
  - `__future__.annotations`, `logging`, `pathlib.Path`, `utils.PipelineError`, `utils.ensure_binary`, `utils.ffprobe_streams`, `utils.run_command`
- subprocess usage refs: `0`
- ffmpeg string refs: `2`

**Content head (first 40 lines)**
```text
from __future__ import annotations

import logging
from pathlib import Path

from .utils import PipelineError, ensure_binary, ffprobe_streams, run_command


def burn_subtitles_and_export(
    composited_video: Path,
    subtitles_srt: Path,
    output_path: Path,
    logger: logging.Logger,
) -> Path:
    ensure_binary("ffmpeg")
    if not composited_video.exists():
        raise PipelineError(f"Composited video missing: {composited_video}")
    if not subtitles_srt.exists():
        raise PipelineError(f"SRT file missing: {subtitles_srt}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    subtitle_filter = (
        f"subtitles={_escape_filter_path(subtitles_srt)}:"
        "force_style='FontSize=18,PrimaryColour=&Hffffff,OutlineColour=&H000000,Outline=1,Alignment=2'"
    )
    run_command(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(composited_video),
            "-vf",
            subtitle_filter,
            "-c:v",
            "libx264",
            "-c:a",
            "copy",
            "-movflags",
            "+faststart",
            str(output_path),
```

### `podcast_pipeline/utils.py`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/podcast_pipeline/utils.py`
- Size: `8852` bytes
- Role: pipeline module
- SHA-256 (first 2MB): `453653a75d133618ee9bb8ab23f646ec9c7149cd58d1ff3b87eb83fdf5adecca`

**Code analysis**
- Top-level functions: `12`
  - `deep_merge(base, update)` (line 131)
  - `load_config(config_path)` (line 141)
  - `setup_logger(log_path, verbose)` (line 149)
  - `ensure_dir(path)` (line 170)
  - `ensure_binary(binary_name)` (line 175)
  - `run_command(command, logger, cwd, env, timeout_sec)` (line 180)
  - `ffprobe_streams(path)` (line 212)
  - `probe_audio_duration(path)` (line 235)
  - `detect_gpu_vram_gb(logger)` (line 244)
  - `bool_from_optional_flag(value, default)` (line 280)
  - `write_json(path, payload)` (line 291)
  - `stage_error_boundary(stage_name, logger)` (line 297)
- Top-level classes: `3`
  - `StageStat` (line 92)
  - `PipelineError` (line 100)
  - `StageTimer` (line 104)
- Imports (unique): `17`
  - `__future__.annotations`, `contextlib.contextmanager`, `copy`, `dataclasses.dataclass`, `json`, `logging`, `pathlib.Path`, `shutil`, `subprocess`, `time`, `torch`, `typing.Any`, `typing.Dict`, `typing.Iterable`, `typing.List`, `typing.Optional`, `yaml`
- subprocess usage refs: `3`
- ffmpeg string refs: `0`

**Content head (first 40 lines)**
```text
from __future__ import annotations

import copy
import json
import logging
import shutil
import subprocess
import time
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import yaml


DEFAULT_CONFIG: Dict[str, Any] = {
    "project": {
        "name": "english-two-speaker-podcast",
        "seed": 124578,
    },
    "paths": {
        "assets_dir": "assets",
        "models_dir": "models",
        "work_dir": "out",
    },
    "audio": {
        "target_sample_rate": 16000,
        "target_channels": 1,
        "loudnorm": "I=-16:TP=-1.5:LRA=11",
        "denoise": False,
        "denoise_nf": -25,
        "max_duration_sec": 1800,
    },
    "diarize": {
        "model": "base",
        "min_segment_duration": 0.5,
        "speaker_change_gap_sec": 0.8,
    },
    "speakers": {
```

### `scripts/prep_assets.py`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/scripts/prep_assets.py`
- Size: `5478` bytes
- Role: utility script
- SHA-256 (first 2MB): `92a069663856a3bb18f7efa2c25eb0601498b1044f53521cd72803b3775aebca`

**Code analysis**
- Top-level functions: `8`
  - `parse_args()` (line 17)
  - `run_cmd(cmd, timeout_sec)` (line 25)
  - `ffprobe_info(path)` (line 39)
  - `probe_resolution_duration(path)` (line 59)
  - `ensure_nonzero(path)` (line 79)
  - `process_speaker(input_video, still_out, looped_out, duration)` (line 86)
  - `format_size(path)` (line 142)
  - `main()` (line 146)
- Top-level classes: `0`
- Imports (unique): `9`
  - `__future__.annotations`, `argparse`, `json`, `pathlib.Path`, `podcast_pipeline.utils.PipelineError`, `subprocess`, `sys`, `typing.Dict`, `typing.Tuple`
- subprocess usage refs: `1`
- ffmpeg string refs: `2`

**Content head (first 40 lines)**
```text
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, Tuple

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from podcast_pipeline.utils import PipelineError  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare speaker assets from Veo videos")
    parser.add_argument("--speaker-a", required=True, help="Path to speaker A video")
    parser.add_argument("--speaker-b", required=True, help="Path to speaker B video")
    parser.add_argument("--duration", required=True, type=int, help="Looped duration in seconds")
    return parser.parse_args()


def run_cmd(cmd: list[str], timeout_sec: int) -> str:
    proc = subprocess.run(
        cmd,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=timeout_sec,
    )
    if proc.returncode != 0:
        raise PipelineError(f"Command failed ({proc.returncode}): {' '.join(cmd)}\n{proc.stdout}")
    return proc.stdout


def ffprobe_info(path: Path) -> Dict[str, object]:
    out = run_cmd(
```

### `scripts/self_check.py`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/scripts/self_check.py`
- Size: `3420` bytes
- Role: utility script
- SHA-256 (first 2MB): `64c56dc729f869aaaa43d47921b8bb3c0cd5da97bdfc18daaf48ddd0b76cc286`

**Code analysis**
- Top-level functions: `4`
  - `_ffprobe_readable(path)` (line 11)
  - `_exists_nonzero(path)` (line 38)
  - `_print_check(name, ok, reason)` (line 47)
  - `main()` (line 52)
- Top-level classes: `0`
- Imports (unique): `5`
  - `__future__.annotations`, `faster_whisper`, `pathlib.Path`, `subprocess`, `sys`
- subprocess usage refs: `1`
- ffmpeg string refs: `0`

**Content head (first 40 lines)**
```text
#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _ffprobe_readable(path: Path) -> tuple[bool, str]:
    try:
        proc = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                str(path),
            ],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=30,
        )
    except Exception as exc:
        return False, f"ffprobe exception: {exc}"
    if proc.returncode != 0:
        return False, f"ffprobe failed: {proc.stdout.strip()}"
    out = proc.stdout.strip()
    return True, f"readable (duration={out}s)"


def _exists_nonzero(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, "missing"
```

### `scripts/lipsync_sync_api.py`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/scripts/lipsync_sync_api.py`
- Size: `940` bytes
- Role: utility script
- SHA-256 (first 2MB): `2bd501c9291b3ff1af9899472d68b69a1a88d669e40f7864cc109fe481e0d9ce`

**Code analysis**
- Top-level functions: `1`
  - `upload(path)` (line 15)
- Top-level classes: `0`
- Imports (unique): `4`
  - `os`, `requests`, `sys`, `time`
- subprocess usage refs: `0`
- ffmpeg string refs: `0`

**Content head (first 40 lines)**
```text
#!/usr/bin/env python3
import os, sys, time, requests

API_KEY = os.environ["SYNC_API_KEY"]
AUDIO = sys.argv[1]
VIDEO = sys.argv[2]
OUTPUT = sys.argv[3]

BASE = "https://api.sync.so/v1"
headers = {"x-api-key": API_KEY, "Content-Type": "application/json"}

# Step A: Submit generation job using public URLs
# Since we have local files we must upload them first
# Use the correct upload endpoint
def upload(path):
    with open(path, "rb") as f:
        r = requests.post(
            f"{BASE}/assets",
            headers={"x-api-key": API_KEY},
            files={"file": (os.path.basename(path), f)}
        )
    print(f"Upload {path}: {r.status_code} {r.text[:200]}")
    r.raise_for_status()
    return r.json()


audio_asset = upload(AUDIO)
video_asset = upload(VIDEO)

print("Audio asset:", audio_asset)
print("Video asset:", video_asset)

# Stop here and paste output so we can see
# the actual asset URL structure before proceeding
```

### `scripts/setup_env.sh`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/scripts/setup_env.sh`
- Size: `632` bytes
- Role: utility script
- SHA-256 (first 2MB): `616560a929850c7bb524b18fbc7172f39ff797abed83f70db015955fc98bb587`

**Content head (first 80 lines)**
```text
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install --upgrade pip wheel setuptools
python3 -m pip install -r requirements.txt

echo
echo "Environment installed."
echo "Next steps:"
echo "1) Ensure ffmpeg/ffprobe are installed and in PATH."
echo "2) Ensure faster-whisper model cache is available locally."
echo "3) Ensure local backend repos:"
echo "   - models/LatentSync (pinned commit)"
echo "   - models/VideoRetalking (Apache-2.0 build)"
echo "4) Place speaker/background assets in assets/."
```

### `assets/README.md`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/assets/README.md`
- Size: `149` bytes
- Role: asset/media
- SHA-256 (first 2MB): `5f5d6a194e4777134fe2359230bd15f5f3ed78c18f2e2acaa0d800a754336af0`

**Content head (first 80 lines)**
```text
Generated/cached assets:
- avatar.png (>=512x512)
- background_1920x1080.png

These are reused across episodes unless regeneration flags are passed.
```

### `assets/speaker_a.jpg`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/assets/speaker_a.jpg`
- Size: `126094` bytes
- Role: asset/media
- SHA-256 (first 2MB): `53b9943c014187ad8e8e579851d77cf26fb74fa155073a37e952ab08caade54f`

**Image metadata (`sips`)**
- Dimensions: `1280x720`

### `assets/speaker_b.jpg`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/assets/speaker_b.jpg`
- Size: `136284` bytes
- Role: asset/media
- SHA-256 (first 2MB): `478d4032cf570dca8d6e2282e4147fd11417ba6278d51d2b9531a0730876db8a`

**Image metadata (`sips`)**
- Dimensions: `1280x720`

### `assets/speaker_a_looped.mp4`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/assets/speaker_a_looped.mp4`
- Size: `21080762` bytes
- Role: asset/media
- SHA-256 (first 2MB): `34801e2c8a03a7e7f65f9bcdf33605f2ab02d2d8911bd7ef64e44fa61569b8a8`

**Media metadata (`ffprobe`)**
```json
{
  "streams": [
    {
      "index": 0,
      "codec_name": "h264",
      "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
      "profile": "High",
      "codec_type": "video",
      "codec_tag_string": "avc1",
      "codec_tag": "0x31637661",
      "width": 1280,
      "height": 720,
      "coded_width": 1280,
      "coded_height": 720,
      "has_b_frames": 2,
      "pix_fmt": "yuv420p",
      "level": 31,
      "chroma_location": "left",
      "field_order": "progressive",
      "refs": 1,
      "is_avc": "true",
      "nal_length_size": "4",
      "id": "0x1",
      "r_frame_rate": "25/1",
      "avg_frame_rate": "25/1",
      "time_base": "1/12800",
      "start_pts": 0,
      "start_time": "0.000000",
      "duration_ts": 1920000,
      "duration": "150.000000",
      "bit_rate": "1115900",
      "bits_per_raw_sample": "8",
      "nb_frames": "3750",
      "extradata_size": 46,
      "disposition": {
        "default": 1,
        "dub": 0,
        "original": 0,
        "comment": 0,
        "lyrics": 0,
        "karaoke": 0,
        "forced": 0,
        "hearing_impaired": 0,
        "visual_impaired": 0,
        "clean_effects": 0,
        "attached_pic": 0,
        "timed_thumbnails": 0,
        "non_diegetic": 0,
        "captions": 0,
        "descriptions": 0,
        "metadata": 0,
        "dependent": 0,
        "still_image": 0,
        "multilayer": 0
      },
      "tags": {
        "language": "und",
        "handler_name": "VideoHandler",
        "vendor_id": "[0][0][0][0]",
        "encoder": "Lavc62.11.100 libx264"
      }
    },
    {
      "index": 1,
      "codec_name": "aac",
      "codec_long_name": "AAC (Advanced Audio Coding)",
      "profile": "LC",
      "codec_type": "audio",
      "codec_tag_string": "mp4a",
      "codec_tag": "0x6134706d",
      "sample_fmt": "fltp",
      "sample_rate": "48000",
      "channels": 2,
      "channel_layout": "stereo",
      "bits_per_sample": 0,
      "initial_padding": 0,
      "id": "0x2",
      "r_frame_rate": "0/0",
      "avg_frame_rate": "0/0",
      "time_base": "1/48000",
      "start_pts": 0,
      "start_time": "0.000000",
      "duration_ts": 7200000,
      "duration": "150.000000",
      "bit_rate": "2275",
      "nb_frames": "7033",
      "extradata_size": 5,
      "disposition": {
        "default": 1,
        "dub": 0,
        "original": 0,
        "comment": 0,
        "lyrics": 0,
        "karaoke": 0,
        "forced": 0,
        "hearing_impaired": 0,
        "visual_impaired": 0,
        "clean_effects": 0,
        "attached_pic": 0,
        "timed_thumbnails": 0,
        "non_diegetic": 0,
        "captions": 0,
        "descriptions": 0,
        "metadata": 0,
        "dependent": 0,
        "still_image": 0,
        "multilayer": 0
      },
      "tags": {
        "language": "und",
        "handler_name": "SoundHandler",
        "vendor_id": "[0][0][0][0]"
      }
    }
  ],
  "format": {
    "filename": "/Users/pranamyajain/hindi_podcast_local/assets/speaker_a_looped.mp4",
    "nb_streams": 2,
    "nb_programs": 0,
    "nb_stream_groups": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "150.000000",
    "size": "21080762",
    "bit_rate": "1124307",
    "probe_score": 100,
    "tags": {
      "major_brand": "isom",
      "minor_version": "512",
      "compatible_brands": "isomiso2avc1mp41",
      "encoder": "Lavf62.3.100"
    }
  }
}
```

### `assets/speaker_b_looped.mp4`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/assets/speaker_b_looped.mp4`
- Size: `30693547` bytes
- Role: asset/media
- SHA-256 (first 2MB): `5d6af83617d8dc087b89eff5a2d527bbbd73e97d69536549b7d509a68ed8ee5f`

**Media metadata (`ffprobe`)**
```json
{
  "streams": [
    {
      "index": 0,
      "codec_name": "h264",
      "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
      "profile": "High",
      "codec_type": "video",
      "codec_tag_string": "avc1",
      "codec_tag": "0x31637661",
      "width": 1280,
      "height": 720,
      "coded_width": 1280,
      "coded_height": 720,
      "has_b_frames": 2,
      "pix_fmt": "yuv420p",
      "level": 31,
      "chroma_location": "left",
      "field_order": "progressive",
      "refs": 1,
      "is_avc": "true",
      "nal_length_size": "4",
      "id": "0x1",
      "r_frame_rate": "25/1",
      "avg_frame_rate": "25/1",
      "time_base": "1/12800",
      "start_pts": 0,
      "start_time": "0.000000",
      "duration_ts": 1920000,
      "duration": "150.000000",
      "bit_rate": "1628564",
      "bits_per_raw_sample": "8",
      "nb_frames": "3750",
      "extradata_size": 46,
      "disposition": {
        "default": 1,
        "dub": 0,
        "original": 0,
        "comment": 0,
        "lyrics": 0,
        "karaoke": 0,
        "forced": 0,
        "hearing_impaired": 0,
        "visual_impaired": 0,
        "clean_effects": 0,
        "attached_pic": 0,
        "timed_thumbnails": 0,
        "non_diegetic": 0,
        "captions": 0,
        "descriptions": 0,
        "metadata": 0,
        "dependent": 0,
        "still_image": 0,
        "multilayer": 0
      },
      "tags": {
        "language": "und",
        "handler_name": "VideoHandler",
        "vendor_id": "[0][0][0][0]",
        "encoder": "Lavc62.11.100 libx264"
      }
    },
    {
      "index": 1,
      "codec_name": "aac",
      "codec_long_name": "AAC (Advanced Audio Coding)",
      "profile": "LC",
      "codec_type": "audio",
      "codec_tag_string": "mp4a",
      "codec_tag": "0x6134706d",
      "sample_fmt": "fltp",
      "sample_rate": "48000",
      "channels": 2,
      "channel_layout": "stereo",
      "bits_per_sample": 0,
      "initial_padding": 0,
      "id": "0x2",
      "r_frame_rate": "0/0",
      "avg_frame_rate": "0/0",
      "time_base": "1/48000",
      "start_pts": 0,
      "start_time": "0.000000",
      "duration_ts": 7200000,
      "duration": "150.000000",
      "bit_rate": "2275",
      "nb_frames": "7033",
      "extradata_size": 5,
      "disposition": {
        "default": 1,
        "dub": 0,
        "original": 0,
        "comment": 0,
        "lyrics": 0,
        "karaoke": 0,
        "forced": 0,
        "hearing_impaired": 0,
        "visual_impaired": 0,
        "clean_effects": 0,
        "attached_pic": 0,
        "timed_thumbnails": 0,
        "non_diegetic": 0,
        "captions": 0,
        "descriptions": 0,
        "metadata": 0,
        "dependent": 0,
        "still_image": 0,
        "multilayer": 0
      },
      "tags": {
        "language": "und",
        "handler_name": "SoundHandler",
        "vendor_id": "[0][0][0][0]"
      }
    }
  ],
  "format": {
    "filename": "/Users/pranamyajain/hindi_podcast_local/assets/speaker_b_looped.mp4",
    "nb_streams": 2,
    "nb_programs": 0,
    "nb_stream_groups": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "150.000000",
    "size": "30693547",
    "bit_rate": "1636989",
    "probe_score": 100,
    "tags": {
      "major_brand": "isom",
      "minor_version": "512",
      "compatible_brands": "isomiso2avc1mp41",
      "encoder": "Lavf62.3.100"
    }
  }
}
```

### `out/episode_002_preview/final_720p_preview.mp4`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/out/episode_002_preview/final_720p_preview.mp4`
- Size: `13686097` bytes
- Role: generated artifact
- SHA-256 (first 2MB): `afcbe0b490eead1c4ccff9f61ae29cabbf267e96999088dbde55460798756f52`

**Media metadata (`ffprobe`)**
```json
{
  "streams": [
    {
      "index": 0,
      "codec_name": "h264",
      "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
      "profile": "High",
      "codec_type": "video",
      "codec_tag_string": "avc1",
      "codec_tag": "0x31637661",
      "width": 1280,
      "height": 720,
      "coded_width": 1280,
      "coded_height": 720,
      "has_b_frames": 2,
      "sample_aspect_ratio": "1:1",
      "display_aspect_ratio": "16:9",
      "pix_fmt": "yuv420p",
      "level": 31,
      "chroma_location": "left",
      "field_order": "progressive",
      "refs": 1,
      "is_avc": "true",
      "nal_length_size": "4",
      "id": "0x1",
      "r_frame_rate": "25/1",
      "avg_frame_rate": "25/1",
      "time_base": "1/12800",
      "start_pts": 0,
      "start_time": "0.000000",
      "duration_ts": 1739264,
      "duration": "135.880000",
      "bit_rate": "724736",
      "bits_per_raw_sample": "8",
      "nb_frames": "3397",
      "extradata_size": 47,
      "disposition": {
        "default": 1,
        "dub": 0,
        "original": 0,
        "comment": 0,
        "lyrics": 0,
        "karaoke": 0,
        "forced": 0,
        "hearing_impaired": 0,
        "visual_impaired": 0,
        "clean_effects": 0,
        "attached_pic": 0,
        "timed_thumbnails": 0,
        "non_diegetic": 0,
        "captions": 0,
        "descriptions": 0,
        "metadata": 0,
        "dependent": 0,
        "still_image": 0,
        "multilayer": 0
      },
      "tags": {
        "language": "und",
        "handler_name": "VideoHandler",
        "vendor_id": "[0][0][0][0]",
        "encoder": "Lavc62.11.100 libx264"
      }
    },
    {
      "index": 1,
      "codec_name": "aac",
      "codec_long_name": "AAC (Advanced Audio Coding)",
      "profile": "LC",
      "codec_type": "audio",
      "codec_tag_string": "mp4a",
      "codec_tag": "0x6134706d",
      "sample_fmt": "fltp",
      "sample_rate": "16000",
      "channels": 1,
      "channel_layout": "mono",
      "bits_per_sample": 0,
      "initial_padding": 0,
      "id": "0x2",
      "r_frame_rate": "0/0",
      "avg_frame_rate": "0/0",
      "time_base": "1/16000",
      "start_pts": 0,
      "start_time": "0.000000",
      "duration_ts": 2146224,
      "duration": "134.139000",
      "bit_rate": "76846",
      "nb_frames": "2097",
      "extradata_size": 5,
      "disposition": {
        "default": 1,
        "dub": 0,
        "original": 0,
        "comment": 0,
        "lyrics": 0,
        "karaoke": 0,
        "forced": 0,
        "hearing_impaired": 0,
        "visual_impaired": 0,
        "clean_effects": 0,
        "attached_pic": 0,
        "timed_thumbnails": 0,
        "non_diegetic": 0,
        "captions": 0,
        "descriptions": 0,
        "metadata": 0,
        "dependent": 0,
        "still_image": 0,
        "multilayer": 0
      },
      "tags": {
        "language": "und",
        "handler_name": "SoundHandler",
        "vendor_id": "[0][0][0][0]"
      }
    }
  ],
  "format": {
    "filename": "/Users/pranamyajain/hindi_podcast_local/out/episode_002_preview/final_720p_preview.mp4",
    "nb_streams": 2,
    "nb_programs": 0,
    "nb_stream_groups": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "135.880000",
    "size": "13686097",
    "bit_rate": "805775",
    "probe_score": 100,
    "tags": {
      "major_brand": "isom",
      "minor_version": "512",
      "compatible_brands": "isomiso2avc1mp41",
      "encoder": "Lavf62.3.100"
    }
  }
}
```

### `out/episode_001_preview/final_1080p.mp4`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/out/episode_001_preview/final_1080p.mp4`
- Size: `27890408` bytes
- Role: generated artifact
- SHA-256 (first 2MB): `dd8f257a3f5111cde2d21368512f493f5848c4dafe1b0403ad0dcc76cad72dc0`

**Media metadata (`ffprobe`)**
```json
{
  "streams": [
    {
      "index": 0,
      "codec_name": "h264",
      "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
      "profile": "High",
      "codec_type": "video",
      "codec_tag_string": "avc1",
      "codec_tag": "0x31637661",
      "width": 1920,
      "height": 1080,
      "coded_width": 1920,
      "coded_height": 1080,
      "has_b_frames": 2,
      "sample_aspect_ratio": "1:1",
      "display_aspect_ratio": "16:9",
      "pix_fmt": "yuv420p",
      "level": 40,
      "chroma_location": "left",
      "field_order": "progressive",
      "refs": 1,
      "is_avc": "true",
      "nal_length_size": "4",
      "id": "0x1",
      "r_frame_rate": "25/1",
      "avg_frame_rate": "25/1",
      "time_base": "1/12800",
      "start_pts": 0,
      "start_time": "0.000000",
      "duration_ts": 1920000,
      "duration": "150.000000",
      "bit_rate": "1413518",
      "bits_per_raw_sample": "8",
      "nb_frames": "3750",
      "extradata_size": 48,
      "disposition": {
        "default": 1,
        "dub": 0,
        "original": 0,
        "comment": 0,
        "lyrics": 0,
        "karaoke": 0,
        "forced": 0,
        "hearing_impaired": 0,
        "visual_impaired": 0,
        "clean_effects": 0,
        "attached_pic": 0,
        "timed_thumbnails": 0,
        "non_diegetic": 0,
        "captions": 0,
        "descriptions": 0,
        "metadata": 0,
        "dependent": 0,
        "still_image": 0,
        "multilayer": 0
      },
      "tags": {
        "language": "und",
        "handler_name": "VideoHandler",
        "vendor_id": "[0][0][0][0]",
        "encoder": "Lavc62.11.100 libx264"
      }
    },
    {
      "index": 1,
      "codec_name": "aac",
      "codec_long_name": "AAC (Advanced Audio Coding)",
      "profile": "LC",
      "codec_type": "audio",
      "codec_tag_string": "mp4a",
      "codec_tag": "0x6134706d",
      "sample_fmt": "fltp",
      "sample_rate": "16000",
      "channels": 1,
      "channel_layout": "mono",
      "bits_per_sample": 0,
      "initial_padding": 0,
      "id": "0x2",
      "r_frame_rate": "0/0",
      "avg_frame_rate": "0/0",
      "time_base": "1/16000",
      "start_pts": 0,
      "start_time": "0.000000",
      "duration_ts": 2400000,
      "duration": "150.000000",
      "bit_rate": "68766",
      "nb_frames": "2345",
      "extradata_size": 5,
      "disposition": {
        "default": 1,
        "dub": 0,
        "original": 0,
        "comment": 0,
        "lyrics": 0,
        "karaoke": 0,
        "forced": 0,
        "hearing_impaired": 0,
        "visual_impaired": 0,
        "clean_effects": 0,
        "attached_pic": 0,
        "timed_thumbnails": 0,
        "non_diegetic": 0,
        "captions": 0,
        "descriptions": 0,
        "metadata": 0,
        "dependent": 0,
        "still_image": 0,
        "multilayer": 0
      },
      "tags": {
        "language": "und",
        "handler_name": "SoundHandler",
        "vendor_id": "[0][0][0][0]"
      }
    }
  ],
  "format": {
    "filename": "/Users/pranamyajain/hindi_podcast_local/out/episode_001_preview/final_1080p.mp4",
    "nb_streams": 2,
    "nb_programs": 0,
    "nb_stream_groups": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "150.000000",
    "size": "27890408",
    "bit_rate": "1487488",
    "probe_score": 100,
    "tags": {
      "major_brand": "isom",
      "minor_version": "512",
      "compatible_brands": "isomiso2avc1mp41",
      "encoder": "Lavf62.3.100"
    }
  }
}
```

### `out/episode_001_preview/final_1080p_v2.mp4`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/out/episode_001_preview/final_1080p_v2.mp4`
- Size: `25598366` bytes
- Role: generated artifact
- SHA-256 (first 2MB): `9b55152132fce59970287f07e1f227412ae0da072a33b1253034cf20565748da`

**Media metadata (`ffprobe`)**
```json
{
  "streams": [
    {
      "index": 0,
      "codec_name": "h264",
      "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
      "profile": "High",
      "codec_type": "video",
      "codec_tag_string": "avc1",
      "codec_tag": "0x31637661",
      "width": 1920,
      "height": 1080,
      "coded_width": 1920,
      "coded_height": 1080,
      "has_b_frames": 2,
      "sample_aspect_ratio": "1:1",
      "display_aspect_ratio": "16:9",
      "pix_fmt": "yuv420p",
      "level": 40,
      "chroma_location": "left",
      "field_order": "progressive",
      "refs": 1,
      "is_avc": "true",
      "nal_length_size": "4",
      "id": "0x1",
      "r_frame_rate": "25/1",
      "avg_frame_rate": "25/1",
      "time_base": "1/12800",
      "start_pts": 0,
      "start_time": "0.000000",
      "duration_ts": 1745408,
      "duration": "136.360000",
      "bit_rate": "1421040",
      "bits_per_raw_sample": "8",
      "nb_frames": "3409",
      "extradata_size": 48,
      "disposition": {
        "default": 1,
        "dub": 0,
        "original": 0,
        "comment": 0,
        "lyrics": 0,
        "karaoke": 0,
        "forced": 0,
        "hearing_impaired": 0,
        "visual_impaired": 0,
        "clean_effects": 0,
        "attached_pic": 0,
        "timed_thumbnails": 0,
        "non_diegetic": 0,
        "captions": 0,
        "descriptions": 0,
        "metadata": 0,
        "dependent": 0,
        "still_image": 0,
        "multilayer": 0
      },
      "tags": {
        "language": "und",
        "handler_name": "VideoHandler",
        "vendor_id": "[0][0][0][0]",
        "encoder": "Lavc62.11.100 libx264"
      }
    },
    {
      "index": 1,
      "codec_name": "aac",
      "codec_long_name": "AAC (Advanced Audio Coding)",
      "profile": "LC",
      "codec_type": "audio",
      "codec_tag_string": "mp4a",
      "codec_tag": "0x6134706d",
      "sample_fmt": "fltp",
      "sample_rate": "16000",
      "channels": 1,
      "channel_layout": "mono",
      "bits_per_sample": 0,
      "initial_padding": 0,
      "id": "0x2",
      "r_frame_rate": "0/0",
      "avg_frame_rate": "0/0",
      "time_base": "1/16000",
      "start_pts": 0,
      "start_time": "0.000000",
      "duration_ts": 2146224,
      "duration": "134.139000",
      "bit_rate": "76846",
      "nb_frames": "2097",
      "extradata_size": 5,
      "disposition": {
        "default": 1,
        "dub": 0,
        "original": 0,
        "comment": 0,
        "lyrics": 0,
        "karaoke": 0,
        "forced": 0,
        "hearing_impaired": 0,
        "visual_impaired": 0,
        "clean_effects": 0,
        "attached_pic": 0,
        "timed_thumbnails": 0,
        "non_diegetic": 0,
        "captions": 0,
        "descriptions": 0,
        "metadata": 0,
        "dependent": 0,
        "still_image": 0,
        "multilayer": 0
      },
      "tags": {
        "language": "und",
        "handler_name": "SoundHandler",
        "vendor_id": "[0][0][0][0]"
      }
    }
  ],
  "format": {
    "filename": "/Users/pranamyajain/hindi_podcast_local/out/episode_001_preview/final_1080p_v2.mp4",
    "nb_streams": 2,
    "nb_programs": 0,
    "nb_stream_groups": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "136.360000",
    "size": "25598366",
    "bit_rate": "1501810",
    "probe_score": 100,
    "tags": {
      "major_brand": "isom",
      "minor_version": "512",
      "compatible_brands": "isomiso2avc1mp41",
      "encoder": "Lavf62.3.100"
    }
  }
}
```

### `out/episode_001_preview/run_report.json`

**File metadata**
- Path: `/Users/pranamyajain/hindi_podcast_local/out/episode_001_preview/run_report.json`
- Size: `1640` bytes
- Role: generated artifact
- SHA-256 (first 2MB): `2d9a68d9bfcfe1376c1464643c863a5cc6fa340b613c588da25d6d4798bfa14d`

**Content head (first 80 lines)**
```text
{
  "preview_mode": true,
  "input_duration_sec": 134.139,
  "total_runtime_sec": 110.118,
  "stages": [
    {
      "name": "1_preprocess_audio",
      "started_at": 1775123391.919654,
      "ended_at": 1775123398.638486,
      "duration_sec": 6.719,
      "output": "/Users/pranamyajain/hindi_podcast_local/out/episode_001_preview/stage1_audio/preprocessed.wav"
    },
    {
      "name": "2_diarize",
      "started_at": 1775123398.6392379,
      "ended_at": 1775123413.877578,
      "duration_sec": 15.238,
      "output": "/Users/pranamyajain/hindi_podcast_local/out/episode_001_preview/stage2_diarize/diarization.json"
    },
    {
      "name": "5_composite",
      "started_at": 1775123413.877707,
      "ended_at": 1775123457.6505878,
      "duration_sec": 43.773,
      "output": "/Users/pranamyajain/hindi_podcast_local/out/episode_001_preview/stage4_composite/composited.mp4"
    },
    {
      "name": "6_subtitles",
      "started_at": 1775123457.651244,
      "ended_at": 1775123468.582345,
      "duration_sec": 10.931,
      "output": "/Users/pranamyajain/hindi_podcast_local/out/episode_001_preview/stage5_subtitles/transcript_en.srt"
    },
    {
      "name": "7_export",
      "started_at": 1775123468.582589,
      "ended_at": 1775123502.020448,
      "duration_sec": 33.438,
      "output": "/Users/pranamyajain/hindi_podcast_local/out/episode_001_preview/stage6_export/final_1080p.mp4"
    }
  ],
  "final_video": "/Users/pranamyajain/hindi_podcast_local/out/episode_001_preview/stage6_export/final_1080p.mp4",
  "final_video_root": "/Users/pranamyajain/hindi_podcast_local/out/episode_001_preview/final_1080p.mp4"
}
```

## Phase 3: Pipeline Integrity Audit

### Data transformations
- Audio -> WAV: FFmpeg loudnorm + resample (Stage 1).
- WAV -> words/segments JSON: faster-whisper (Stage 2).
- words JSON -> diarization turns: gap-based alternation (Stage 3).
- diarization + speaker WAV -> per-segment renders: SadTalker + idle loops (Stage 4).
- host videos + full audio -> split screen MP4 (Stage 5).
- segments JSON + diarization -> SRT speaker-labeled (Stage 6).
- composited MP4 + SRT -> final MP4 with burned subs (Stage 7).

### Failure points (hard fail)
- Missing assets: `run_podcast.py` validates `source_image` and `idle_video` paths exist and are non-empty.
- Transcription: raises if no word-level timestamps produced.
- SadTalker: Stage 4 fails if `models/SadTalker/inference.py` missing or if SadTalker weights are not installed.


## Phase 4: Dependency and Environment Audit

### Python deps (`requirements.txt`)
- `faster-whisper==1.0.3`
- `torch>=2.1.0`
- `torchaudio>=2.1.0`
- `numpy>=1.26.0`
- `PyYAML>=6.0`
- `requests>=2.31.0`
- `Pillow>=10.0.0`
- `ffmpeg-python>=0.2.0`

### Model repos under `models/` (license heads)
**models/LatentSync/LICENSE**
```text
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
```
**models/SadTalker/LICENSE**
```text
Tencent is pleased to support the open source community by making SadTalker available.

Copyright (C), a Tencent company. All rights reserved.

SadTalker is licensed under the Apache 2.0 License, except for the third-party components listed below.

Terms of the Apache License Version 2.0:
---------------------------------------------
                                Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

```
**models/video-retalking/LICENSE**
```text
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
```
**models/video-retalking/third_part/GFPGAN/LICENSE**
```text
Tencent is pleased to support the open source community by making GFPGAN available.

Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.

GFPGAN is licensed under the Apache License Version 2.0 except for the third-party components listed below.


Terms of the Apache License Version 2.0:
---------------------------------------------
Apache License

Version 2.0, January 2004
```
**models/video-retalking/third_part/ganimation_replicate/LICENSE**
```text
MIT License

Copyright (c) 2019 Yuedong Chen (Donald)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
```

## Phase 5: Gap Analysis Between Intent and Implementation

- `README.md` describes pyannote + LatentSync/VideoRetalking; code implements whisper-gap diarization + SadTalker-only lipsync.
- `environment.yml` is CUDA/NVIDIA oriented and does not describe Apple Silicon / CPU execution; `requirements.txt` is closer to the active code path.
- `podcast_pipeline/utils.py:detect_gpu_vram_gb` raises if no CUDA GPU; current pipeline stages do not call it, but the error message contradicts CPU preview usage.
- `out/` contains large MP4 artifacts; unless Git LFS is used, pushing to GitHub will bloat clones and may hit GitHub file size limits.

## Phase 6: Current State Verdict

### Working today (evidence-based)
- `out/episode_002_preview/final_720p_preview.mp4` exists, is playable, and is H.264 + AAC at 1280x720 (verified via `ffprobe`).
- `scripts/prep_assets.py` produces looped speaker videos and still frames under `assets/` (verified by non-zero sizes).

### Not working / high risk
- Stage 4 speech rendering depends on SadTalker weights; weights are not included in this repo and must be placed locally.
- Diarization is heuristic and will mis-assign speakers for many real dialogues.

## Phase 7: Executive Summary

This repo currently produces a strong *visual preview* (split screen + subtitles) using pre-looped Veo clips, but it does not yet provide robust local two-speaker lip sync on Apple Silicon. The codebase contains multiple model repos (`SadTalker`, `video-retalking`, `LatentSync`) with mixed platform constraints, and the main pipeline currently calls SadTalker only. Documentation (`README.md`, `environment.yml`) is inconsistent with the executable code path and should be brought back into alignment once the target runtime/platform is finalized.
