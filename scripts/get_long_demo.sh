#!/usr/bin/env bash

set -euo pipefail

mkdir -p samples

URL="https://github.com/Nizamohammed/Scribepad/releases/download/v0.1.0/oct_23_psychology_02.mp3"
OUT="samples/demo_long_34min.mp3"

echo "Downloding long demo audio...."
curl -L "$URL" -o "$OUT"
echo "Saved to: $OUT"

