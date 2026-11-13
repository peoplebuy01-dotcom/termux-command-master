#!/data/data/com.termux/files/usr/bin/bash
set -eu
SOURCE="${1:-$HOME/termux-learning}"
DEST="$HOME/backups"
if [ ! -d "$SOURCE" ]; then echo "Folder not found: $SOURCE" >&2; exit 1; fi
mkdir -p "$DEST"
ARCHIVE="$DEST/backup-$(date +%F-%H%M%S).tar.gz"
tar -czf "$ARCHIVE" -C "$(dirname "$SOURCE")" "$(basename "$SOURCE")"
tar -tzf "$ARCHIVE" >/dev/null
echo "Backup verified: $ARCHIVE"
