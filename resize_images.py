import os
from PIL import Image

# Directory where your images are stored
ROOT_DIR = "images"
# Output folder for resized versions (optional)
OUTPUT_DIR = "images/resized"

# Max width/height (adjust as needed)
MAX_WIDTH = 800
MAX_HEIGHT = 600

def resize_image(path, output_path):
    with Image.open(path) as img:
        width, height = img.size
        if width > MAX_WIDTH or height > MAX_HEIGHT:
            print(f"Resizing: {path} ({width}x{height})")
            img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.LANCZOS)

            # Convert if image has alpha channel
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            img.save(output_path, optimize=True)
        else:
            print(f"Skipping (already small): {path}")


def process_images():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, ROOT_DIR)
                output_path = os.path.join(OUTPUT_DIR, rel_path)

                # Make sure subdirectories exist in output
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                resize_image(full_path, output_path)

if __name__ == "__main__":
    process_images()
