import cv2
import numpy as np
import easyocr
import glob
import os

reader = easyocr.Reader(['pt', 'en'], gpu=False)

def get_highlighted_text(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define color ranges
    colors = {
        'Blue': ((90, 50, 50), (130, 255, 255)),
        'Yellow': ((20, 50, 50), (40, 255, 255)),
        'Green': ((40, 50, 50), (80, 255, 255))
    }
    
    for color_name, (lower, upper) in colors.items():
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
        
        # Morphological operations to merge nearby pixels into solid bands
        kernel = np.ones((5, 100), np.uint8)
        mask = cv2.dilate(mask, kernel, iterations=2)
        mask = cv2.erode(mask, kernel, iterations=1)
        
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            # Filter out small noise
            if w > 100 and h > 10:
                # Crop a slightly larger area to ensure text is captured
                crop = img[max(0, y-5):min(img.shape[0], y+h+5), max(0, x-5):min(img.shape[1], x+w+5)]
                
                # Run OCR
                result = reader.readtext(crop, detail=0)
                text = " ".join(result)
                if text.strip():
                    print(f"[{color_name} Highlight] -> {text}")

for i in range(3):
    img_path = f"../excel_stitched_{i}.png"
    if os.path.exists(img_path):
        print(f"\nProcessing {img_path}...")
        get_highlighted_text(img_path)

