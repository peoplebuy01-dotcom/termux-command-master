from pathlib import Path
import shutil

# Safe demo: organize only a dedicated test folder.
root = Path.home() / "organizer-demo"
categories = {".jpg": "images", ".png": "images", ".pdf": "documents", ".txt": "text"}
root.mkdir(exist_ok=True)
for folder in ("images", "documents", "text", "other"):
    (root / folder).mkdir(exist_ok=True)

for item in list(root.iterdir()):
    if not item.is_file():
        continue
    destination_folder = categories.get(item.suffix.lower(), "other")
    destination = root / destination_folder / item.name
    print(f"Would move: {item.name} -> {destination_folder}/")
    # Uncomment only after reviewing the printed plan:
    # shutil.move(str(item), str(destination))
print("Dry run complete. Review the plan before enabling file moves.")
