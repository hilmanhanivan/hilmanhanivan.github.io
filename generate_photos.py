import os, json

photos = sorted([
    f"photos/{f}" for f in os.listdir("photos")
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))
])

with open("photos.json", "w") as out:
    json.dump(photos, out)