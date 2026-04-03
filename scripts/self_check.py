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
    size = path.stat().st_size
    if size <= 0:
        return False, "zero bytes"
    return True, f"size={size}B"


def _print_check(name: str, ok: bool, reason: str) -> None:
    status = "PASS" if ok else "FAIL"
    print(f"{status} | {name} | {reason}")


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    speaker_a_jpg = ROOT / "assets" / "speaker_a.jpg"
    speaker_b_jpg = ROOT / "assets" / "speaker_b.jpg"
    speaker_a_loop = ROOT / "assets" / "speaker_a_looped.mp4"
    speaker_b_loop = ROOT / "assets" / "speaker_b_looped.mp4"
    male_src = Path("/Users/pranamyajain/Downloads/male podcast studio.mp4")
    female_src = Path("/Users/pranamyajain/Downloads/female podcast studio.mp4")
    latentsync_repo = ROOT / "models" / "LatentSync"
    latentsync_infer = latentsync_repo / "inference.py"

    for name, path in [
        ("assets/speaker_a.jpg exists and non-zero", speaker_a_jpg),
        ("assets/speaker_b.jpg exists and non-zero", speaker_b_jpg),
        ("assets/speaker_a_looped.mp4 exists and non-zero", speaker_a_loop),
        ("assets/speaker_b_looped.mp4 exists and non-zero", speaker_b_loop),
    ]:
        ok, reason = _exists_nonzero(path)
        checks.append((name, ok, reason))

    for name, path in [
        ("/Users/pranamyajain/Downloads/male podcast studio.mp4 readable", male_src),
        ("/Users/pranamyajain/Downloads/female podcast studio.mp4 readable", female_src),
    ]:
        if not path.exists():
            checks.append((name, False, "missing"))
        else:
            ok, reason = _ffprobe_readable(path)
            checks.append((name, ok, reason))

    ok_repo = latentsync_repo.exists()
    checks.append(("models/LatentSync exists", ok_repo, "present" if ok_repo else "missing"))
    ok_inf = latentsync_infer.exists()
    checks.append(("models/LatentSync/inference.py exists", ok_inf, "present" if ok_inf else "missing"))

    try:
        import faster_whisper  # MIT  # noqa: F401

        checks.append(("faster-whisper importable", True, "import ok"))
    except Exception as exc:
        checks.append(("faster-whisper importable", False, f"import failed: {exc}"))

    all_ok = True
    for name, ok, reason in checks:
        _print_check(name, ok, reason)
        all_ok = all_ok and ok

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
