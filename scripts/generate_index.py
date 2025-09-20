#!/usr/bin/env python3
"""
Scan repository for CTF folders and .html challenge pages, output index.json
Structure:
[
  {
    "id": "picoctf",
    "name": "picoCTF",
    "status": "ended",
    "banner": "assets/picoctf.png",
    "categories": {
      "General Skills": [
         {"title": "firstfind", "path": "picoCTF/General Skills/firstfind.html"},
         ...
      ]
    }
  },
  ...
]
"""
import os
import json
import pathlib

IGNORED = {"assets", "scripts", ".github", ".git"}
ROOT_IGNORED_FILES = {"index.html", "ctf.html", "index.json", "README.md"}

def safe_id(name: str) -> str:
    return name.lower().strip().replace(" ", "-")

def scan_ctfs(base_dir="."):
    ctfs = []

    for entry in sorted(os.listdir(base_dir)):
        if entry in IGNORED or entry in ROOT_IGNORED_FILES:
            continue
        ctf_path = os.path.join(base_dir, entry)
        if not os.path.isdir(ctf_path):
            continue

        ctf_id = safe_id(entry)
        banner_path = f"assets/{ctf_id}.png"
        if not os.path.exists(banner_path):
            # fallback placeholder (you can add real images in /assets)
            banner_path = "assets/placeholder.png"

        ctf_data = {
            "id": ctf_id,
            "name": entry,
            "status": "ended",
            "banner": banner_path,
            "categories": {}
        }

        # iterate categories (subfolders)
        for cat_entry in sorted(os.listdir(ctf_path)):
            cat_path = os.path.join(ctf_path, cat_entry)
            if not os.path.isdir(cat_path):
                continue

            challenges = []
            for f in sorted(os.listdir(cat_path)):
                if f.lower().endswith(".html"):
                    title = os.path.splitext(f)[0]
                    rel_path = os.path.join(entry, cat_entry, f).replace("\\", "/")
                    challenges.append({"title": title, "path": rel_path})

            if challenges:
                ctf_data["categories"][cat_entry] = challenges

        # if CTF folder has .html files directly (no category), put them under "Uncategorized"
        direct_html = [f for f in sorted(os.listdir(ctf_path)) if f.lower().endswith(".html")]
        if direct_html:
            uncats = []
            for f in direct_html:
                title = os.path.splitext(f)[0]
                rel_path = os.path.join(entry, f).replace("\\", "/")
                uncats.append({"title": title, "path": rel_path})
            if uncats:
                ctf_data["categories"].setdefault("Uncategorized", []).extend(uncats)

        # Only include ctfs that have at least one category or direct html
        if any(ctf_data["categories"].values()):
            ctfs.append(ctf_data)
        else:
            # still include if you want empty ctfs to appear (currently includes them as empty categories)
            ctfs.append(ctf_data)

    return ctfs

def main():
    data = scan_ctfs(".")
    out_path = pathlib.Path("index.json")
    # If file exists and identical, don't rewrite timestamp
    new_json = json.dumps(data, indent=2, ensure_ascii=False)
    if out_path.exists():
        existing = out_path.read_text(encoding="utf-8")
        if existing == new_json:
            print("✅ index.json up-to-date — no changes")
            return

    out_path.write_text(new_json, encoding="utf-8")
    print(f"✅ index.json written ({len(data)} CTFs)")

if __name__ == "__main__":
    main()
