#!/bin/sh
# Check that two runs of main.py write byte-identical output.
set -e
cd "$(dirname "$0")"
rm -rf /tmp/ni24_a /tmp/ni24_b
mkdir -p /tmp/ni24_a /tmp/ni24_b
MAKEFUN_OUTPUT_DIR=/tmp/ni24_a python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/ni24_b python3 main.py
cmp /tmp/ni24_a/entry.png /tmp/ni24_b/entry.png && echo "deterministic: identical bytes"
cmp /tmp/ni24_a/entry.png entry.png && echo "matches entry.png in repo"
python3 -c "
from PIL import Image
im = Image.open('/tmp/ni24_a/entry.png')
assert im.size == (1024, 1024), im.size
assert im.mode == 'RGB', im.mode
import os
assert os.path.getsize('/tmp/ni24_a/entry.png') <= 1048576
print('size ok:', im.size, im.mode)
"
