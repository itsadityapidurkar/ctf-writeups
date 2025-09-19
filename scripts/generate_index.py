import os, json

def scan_ctfs(base_dir="."):
    ctfs = []

    for ctf_name in os.listdir(base_dir):
        ctf_path = os.path.join(base_dir, ctf_name)
        if not os.path.isdir(ctf_path) or ctf_name in ["assets", "scripts", ".git", ".github"]:
            continue

        ctf_id = ctf_name.lower().replace(" ", "-")
        ctf_data = {
            "id": ctf_id,
            "name": ctf_name,
            "status": "ended",  # default (can edit later if you want statuses)
            "banner": f"assets/{ctf_id}.png",
            "categories": {}
        }

        for category in os.listdir(ctf_path):
            cat_path = os.path.join(ctf_path, category)
            if not os.path.isdir(cat_path):
                continue

            challenges = []
            for f in os.listdir(cat_path):
                if f.endswith(".md"):
                    title = os.path.splitext(f)[0]
                    rel_path = os.path.join(ctf_name, category, f).replace("\\", "/")
                    challenges.append({"title": title, "path": rel_path})

            if challenges:
                ctf_data["categories"][category] = challenges

        ctfs.append(ctf_data)

    return ctfs


if __name__ == "__main__":
    data = scan_ctfs(".")
    with open("index.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("✅ index.json generated with", len(data), "CTFs")
