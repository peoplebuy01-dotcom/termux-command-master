#!/data/data/com.termux/files/usr/bin/bash
# Simple notes manager. Stores notes only in ~/termux-notes.
set -eu
DIR="$HOME/termux-notes"
mkdir -p "$DIR"
FILE="$DIR/notes.txt"
printf '1) Add note\n2) View notes\n3) Search notes\n4) Exit\n'
read -r -p 'Choose: ' choice
case "$choice" in
  1) read -r -p 'Note: ' note; printf '%s | %s\n' "$(date '+%F %T')" "$note" >> "$FILE"; echo 'Saved.' ;;
  2) if [ -f "$FILE" ]; then cat "$FILE"; else echo 'No notes yet.'; fi ;;
  3) read -r -p 'Search word: ' word; if [ -f "$FILE" ]; then grep -in -- "$word" "$FILE" || true; else echo 'No notes yet.'; fi ;;
  4) exit 0 ;;
  *) echo 'Invalid choice'; exit 1 ;;
esac
