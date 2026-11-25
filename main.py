#!/usr/bin/env python3
"""Entry program for make.fun bounty "Sum up 25 November's world news in one image".

Writes one image to /output/entry.png by copying the front page bundled
in this repository (news.png). Deterministic: no network, no randomness,
no clock reads -- two runs write identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "news.png")
DST = "/output/entry.png"


def main() -> int:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote " + DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
