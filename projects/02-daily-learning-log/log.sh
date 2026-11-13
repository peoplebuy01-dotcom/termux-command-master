#!/data/data/com.termux/files/usr/bin/bash
set -eu
DIR="$HOME/learning-log"
mkdir -p "$DIR"
read -r -p 'Aaj kya seekha? ' topic
if [ -z "$topic" ]; then echo 'Empty entry nahi save ki.'; exit 1; fi
printf '%s | %s\n' "$(date '+%F %T')" "$topic" >> "$DIR/log.txt"
echo "Saved at $DIR/log.txt"
