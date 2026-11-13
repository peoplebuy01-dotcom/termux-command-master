"""SHA-256 file integrity manifests. Source files are never modified."""
import hashlib
import json
from pathlib import Path


def _digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _files(root):
    root = root.resolve()
    for path in sorted(root.rglob("*")):
        if path.is_file() and not path.is_symlink():
            yield path


def create_manifest(directory, output):
    root = Path(directory).expanduser().resolve()
    if not root.is_dir():
        raise ValueError("Directory does not exist.")
    output_path = Path(output).expanduser().resolve()
    entries = {}
    for path in _files(root):
        if path.resolve() == output_path:
            continue
        entries[str(path.relative_to(root))] = _digest(path)
    payload = {"algorithm": "sha256", "root_name": root.name, "files": entries}
    output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return {"status": "created", "manifest": str(output_path), "file_count": len(entries), "algorithm": "sha256"}


def verify_manifest(directory, manifest):
    root = Path(directory).expanduser().resolve()
    manifest_path = Path(manifest).expanduser().resolve()
    if not root.is_dir() or not manifest_path.is_file():
        raise ValueError("Directory or manifest file does not exist.")
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    if data.get("algorithm") != "sha256" or not isinstance(data.get("files"), dict):
        raise ValueError("Unsupported or invalid manifest.")
    changed, missing, unchanged = [], [], []
    for relative, expected in data["files"].items():
        candidate = (root / relative).resolve()
        if root not in candidate.parents and candidate != root:
            raise ValueError("Manifest contains an unsafe path.")
        if not candidate.is_file():
            missing.append(relative)
        elif _digest(candidate) == expected:
            unchanged.append(relative)
        else:
            changed.append(relative)
    known = set(data["files"])
    extra = [str(p.relative_to(root)) for p in _files(root)
             if str(p.relative_to(root)) not in known and p.resolve() != manifest_path]
    return {"status": "OK" if not (changed or missing or extra) else "REVIEW",
            "unchanged": unchanged, "changed": changed, "missing": missing, "new_files": extra}
