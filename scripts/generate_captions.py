#!/usr/bin/env python3
"""Generate a simple SRT file from audio using faster-whisper.

This is included for migration completeness. Captions are not part of the
current MuseTalk realism threshold test unless explicitly enabled later.
"""
from __future__ import annotations

import argparse
from pathlib import Path


def ts(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, rem = divmod(ms, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--audio', required=True)
    parser.add_argument('--out', required=True)
    parser.add_argument('--model', default='base')
    args = parser.parse_args()

    from faster_whisper import WhisperModel

    model = WhisperModel(args.model, device='auto', compute_type='auto')
    segments, _ = model.transcribe(args.audio, language='en', vad_filter=True)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', encoding='utf-8') as handle:
        for idx, seg in enumerate(segments, start=1):
            handle.write(f"{idx}\n{ts(seg.start)} --> {ts(seg.end)}\n{seg.text.strip()}\n\n")
    print(out)


if __name__ == '__main__':
    main()
