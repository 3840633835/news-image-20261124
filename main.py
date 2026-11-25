#!/usr/bin/env python3
"""news-image-20261124 entry program.

Copies the pre-drawn front page (entry.png, in this repository) to
/output/entry.png. Standard library only, no network, deterministic:
every run writes the same bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # readable by every user, as the grader collects outputs as another user
    os.chmod(dst, 0o644)
    print("wrote", dst, os.path.getsize(dst), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
