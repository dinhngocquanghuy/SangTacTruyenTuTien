import os
import glob
import re
from PIL import Image

artifact_dir = r"C:\Users\Admin\.gemini\antigravity\brain\17cbacfa-a625-4061-97ec-6ccc6d711f51"
dst_images_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02\IMAGES"
os.makedirs(dst_images_dir, exist_ok=True)

def normalize_and_save(src_path, dst_path):
    img = Image.open(src_path)
    # Check if already 1920x1080
    if img.size != (1920, 1080):
        # Resize using high-quality Lanczos filter
        img_resized = img.resize((1920, 1080), Image.Resampling.LANCZOS)
        img_resized.save(dst_path, "PNG", optimize=True)
    else:
        img.save(dst_path, "PNG", optimize=True)
    print(f"Saved normalized image: {os.path.basename(dst_path)} (1920x1080)")

def scan_and_collect():
    # Scan all jpg in artifact_dir
    files = glob.glob(os.path.join(artifact_dir, "*.jpg"))
    collected = {}
    
    for f in sorted(files, key=os.path.getmtime):
        bname = os.path.basename(f)
        # Match pattern like c08_i001_... or C08-I001_...
        m = re.match(r"(c\d{2}[-_]i\d{3})", bname, re.IGNORECASE)
        if m:
            code = m.group(1).upper().replace("_", "-")
            collected[code] = f
            
    print(f"Found {len(collected)} scene image candidates in artifact dir.")
    for code, src in collected.items():
        dst_png = os.path.join(dst_images_dir, f"{code}.png")
        if not os.path.exists(dst_png):
            normalize_and_save(src, dst_png)
        else:
            # check size
            cur_img = Image.open(dst_png)
            if cur_img.size != (1920, 1080):
                normalize_and_save(src, dst_png)
                
    # Also check how many images are in IMAGES/
    pngs = glob.glob(os.path.join(dst_images_dir, "*.png"))
    print(f"Total normalized PNGs in IMAGES/: {len(pngs)}/80")
    return collected

if __name__ == "__main__":
    scan_and_collect()
