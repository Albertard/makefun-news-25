# "Sum up 25 November's world news in one image" (news-image-20261125).
# The front page for Wednesday 25 November 2026 lives in this repository
# as entry.png; this program just writes those exact bytes to the output
# directory. Python 3.13, standard library only, no network, fully
# deterministic: every run produces the same file.
#
# Local check: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
import os
from pathlib import Path

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
image = Path(__file__).with_name("entry.png").read_bytes()
if len(image) == 0:
    raise SystemExit("entry.png is empty")
if len(image) > 1048576:
    raise SystemExit("entry.png exceeds 1 MiB")
# PNG magic bytes: 89 50 4E 47 0D 0A 1A 0A
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
if image[:8] != magic:
    raise SystemExit("entry.png is not a PNG file")
os.makedirs(out_dir, exist_ok=True)
out_path = Path(out_dir, "entry.png")
out_path.write_bytes(image)
# Verify the bytes on disk are exactly the source bytes before exiting.
if out_path.read_bytes() != image:
    raise SystemExit("written entry.png does not match source bytes")
