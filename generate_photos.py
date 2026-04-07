# import os, json

# photos = sorted([
#     f"photos/{f}" for f in os.listdir("photos")
#     if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))
# ])

# with open("photos.json", "w") as out:
#     json.dump(photos, out)

import os, json
from PIL import Image

os.makedirs("photos/thumbs", exist_ok=True)

photos = []
for f in sorted(os.listdir("photos")):
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')) and not f.startswith('.'):
        src = f"photos/{f}"
        thumb = f"photos/thumbs/{f}"
        
        # Create thumbnail if it doesn't exist
        if not os.path.exists(thumb):
            img = Image.open(src)
            img.thumbnail((600, 600))  # max 600px wide/tall
            img.save(thumb, quality=70, optimize=True)
        
        photos.append({"src": src, "thumb": thumb})

with open("photos.json", "w") as out:
    json.dump(photos, out)