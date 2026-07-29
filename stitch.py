import glob
from PIL import Image

images = sorted(glob.glob('../excel/*.png'))
if not images:
    print("No images found.")
    exit()

def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

chunks = list(chunk_list(images, 8)) # Up to 8 images per chunk

for i, chunk in enumerate(chunks):
    imgs = [Image.open(p) for p in chunk]
    widths, heights = zip(*(i.size for i in imgs))
    
    max_width = max(widths)
    total_height = sum(heights)
    
    new_im = Image.new('RGB', (max_width, total_height))
    
    y_offset = 0
    for im in imgs:
        new_im.paste(im, (0, y_offset))
        y_offset += im.size[1]
        
    new_im.save(f'../excel_stitched_{i}.png')
    print(f"Saved ../excel_stitched_{i}.png")
