import os
from PIL import Image

def analyze_image(path):
    if not os.path.exists(path):
        print(f"{path} does not exist!")
        return
    img = Image.open(path)
    print(f"Image {path}: format={img.format}, size={img.size}, mode={img.mode}")
    # Let's find bounding box of non-transparent pixels if it has an alpha channel
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        bbox = img.getbbox()
        if bbox:
            print(f"  Non-transparent bounding box: {bbox}")
            # If the bounding box is much smaller than the image size, it has white/transparent margins
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            print(f"  Content size: {width}x{height} (vs image size {img.size})")
        else:
            print("  Image is fully transparent!")
    else:
        print("  No transparency channel.")

analyze_image("images/new-gioestofos.png")
analyze_image("images/catalog-gioestofos.jpg")
