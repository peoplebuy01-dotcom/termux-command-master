#!/data/data/com.termux/files/usr/bin/bash
set -eu
echo '=== Filesystem space ==='
df -h
echo
echo '=== Termux home size ==='
du -sh "$HOME"
echo
echo '=== Largest immediate folders (if supported) ==='
du -h -d 1 "$HOME" 2>/dev/null | sort -h | tail -n 10 || true
