#!/usr/bin/env python3
"""news-image-20261126 — the world's news of Thursday 26 November 2026
on a single broadsheet front page (1024x1024).

Stdlib only. No rendering happens here: the finished front page is
stored in the repository as entry.png (rendered once, byte-identical
every run) and this program simply copies it to the output location,
then validates the result with pure-stdlib checks. This is the pattern
the bounty itself blesses: "the simplest program copies an image the
repository holds".

Usage:  python3 main.py   ->  /output/entry.png (or ./entry.png)
"""
import os
import shutil
import struct
import sys

EXPECTED_W, EXPECTED_H = 1024, 1024
MAX_BYTES = 1 * 1024 * 1024  # 1 MiB
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1

    # Prefer /output when present; create it if we can, else fall back
    # to the current directory (grader containers normally mount /output).
    out_dir = "."
    if os.path.isdir("/output"):
        out_dir = "/output"
    else:
        try:
            os.makedirs("/output", exist_ok=True)
            out_dir = "/output"
        except OSError:
            out_dir = "."
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)

    # --- pure-stdlib validation of the copied file -------------------
    with open(dst, "rb") as f:
        data = f.read()

    if data[:8] != PNG_MAGIC:
        print("error: output is not a PNG (bad magic bytes)", file=sys.stderr)
        return 1
    if len(data) < 33 or data[12:16] != b"IHDR":
        print("error: output has no IHDR chunk", file=sys.stderr)
        return 1
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_W, EXPECTED_H):
        print(
            "error: expected %dx%d, got %dx%d" % (EXPECTED_W, EXPECTED_H, width, height),
            file=sys.stderr,
        )
        return 1
    if len(data) > MAX_BYTES:
        print("error: output %d bytes exceeds 1 MiB" % len(data), file=sys.stderr)
        return 1

    print(
        "wrote %s (%d, %d) %d bytes from entry.png — VALID" % (dst, width, height, len(data))
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
