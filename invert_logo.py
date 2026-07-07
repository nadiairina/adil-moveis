from PIL import Image, ImageOps

try:
    # Open the logo image
    img = Image.open('images/logo.png').convert('RGBA')
    
    # Extract alpha channel
    r, g, b, a = img.split()
    
    # Merge RGB into an RGB image
    rgb_img = Image.merge('RGB', (r, g, b))
    
    # Invert the RGB image
    inverted_rgb = ImageOps.invert(rgb_img)
    
    # Split the inverted RGB back
    ir, ig, ib = inverted_rgb.split()
    
    # Merge the inverted RGB with the original Alpha channel
    inverted_img = Image.merge('RGBA', (ir, ig, ib, a))
    
    # Save the result
    inverted_img.save('images/logo_inverted.png')
    print("Successfully created images/logo_inverted.png")
except Exception as e:
    print("Error:", e)
