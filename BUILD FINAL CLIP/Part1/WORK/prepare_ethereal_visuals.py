import os
import cv2
import numpy as np

src_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\WORK\visuals"
dst_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\WORK\visuals_ethereal"
os.makedirs(dst_dir, exist_ok=True)

def apply_ethereal_xianxia_grade(img):
    # 1. Soft ethereal luminous bloom (Tien quang thanh le)
    blur = cv2.GaussianBlur(img, (0, 0), sigmaX=12, sigmaY=12)
    bloom = cv2.addWeighted(img, 0.72, blur, 0.38, 0)
    
    # 2. Celestial color grading: boost vibrance, cyan/jade tones, soft golden highlights
    hsv = cv2.cvtColor(bloom, cv2.COLOR_BGR2HSV).astype(np.float32)
    # Enhance vibrance of celestial colors
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 1.15, 0, 255)
    # Slightly increase brightness of midtones
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] * 1.05 + 5.0, 0, 255)
    bloom_graded = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR).astype(np.float32)
    
    # 3. Lift dark murky shadows into ethereal mist (Cyan/Azure undertone)
    luminance = cv2.cvtColor(bloom_graded.astype(np.uint8), cv2.COLOR_BGR2GRAY) / 255.0
    shadow_mask = np.clip(1.0 - luminance * 1.3, 0.0, 1.0)[:, :, None]
    
    # Celestial mist tint (Blue/Cyan/Jade)
    celestial_tint = np.zeros_like(bloom_graded)
    celestial_tint[:, :, 0] = 22.0  # Blue
    celestial_tint[:, :, 1] = 16.0  # Green
    celestial_tint[:, :, 2] = 4.0   # Red
    
    # Soft golden highlights in bright areas
    highlight_mask = np.clip((luminance - 0.6) * 2.5, 0.0, 1.0)[:, :, None]
    golden_tint = np.zeros_like(bloom_graded)
    golden_tint[:, :, 0] = 2.0   # Blue
    golden_tint[:, :, 1] = 10.0  # Green
    golden_tint[:, :, 2] = 18.0  # Red
    
    result = bloom_graded + (celestial_tint * shadow_mask) + (golden_tint * highlight_mask)
    return np.clip(result, 0, 255).astype(np.uint8)

for fname in os.listdir(src_dir):
    if fname.lower().endswith(('.jpg', '.png')):
        src_path = os.path.join(src_dir, fname)
        img = cv2.imread(src_path)
        if img is not None:
            ethereal = apply_ethereal_xianxia_grade(img)
            dst_path = os.path.join(dst_dir, fname)
            cv2.imwrite(dst_path, ethereal)
            print(f"Processed ethereal Xianxia: {fname}")

print(f"\nAll visuals upgraded to Ethereal Xianxia style in {dst_dir}!")
