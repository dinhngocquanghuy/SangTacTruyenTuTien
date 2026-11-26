import csv
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import cv2
import numpy as np

base_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP"
timeline_csv = os.path.join(base_dir, "OUTPUT", "TAP-01-TIMELINE.csv")
visuals_dir = os.path.join(base_dir, "WORK", "visuals_ethereal")
scenes_video_dir = os.path.join(base_dir, "WORK", "video_scenes_smooth")
work_dir = os.path.join(base_dir, "WORK")
output_dir = os.path.join(base_dir, "OUTPUT")

os.makedirs(scenes_video_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# Ethereal Xianxia Visual Assets Map
assets = {
    "celestial_path": os.path.join(visuals_dir, "C01_I001_celestial_path.jpg"),
    "mountain_path": os.path.join(visuals_dir, "C01_I001_mountain_path.jpg"),
    "ta_hanh_chu": os.path.join(visuals_dir, "C01_I002_ta_hanh_chu.jpg"),
    "sect_gate": os.path.join(visuals_dir, "C01_I008_sect_gate.jpg"),
    "tam_elder": os.path.join(visuals_dir, "C01_I010_tam_elder.jpg"),
    "van_ninh": os.path.join(visuals_dir, "C01_I016_van_ninh_xianxia.jpg"),
    "van_ninh_alt": os.path.join(visuals_dir, "C01_I016_van_ninh.jpg"),
    "a_thach": os.path.join(visuals_dir, "C01_I020_a_thach.jpg"),
    "letter_needle": os.path.join(visuals_dir, "C02_I001_letter_needle.jpg"),
    "ky_thanh_la": os.path.join(visuals_dir, "C03_I001_ky_thanh_la.jpg"),
    "trac_cuu": os.path.join(visuals_dir, "C06_I018_trac_cuu.jpg"),
    "final_token": os.path.join(visuals_dir, "C07_I038_final_token.jpg"),
    "floating_peaks": os.path.join(visuals_dir, "xianxia_floating_peaks.jpg"),
    "panorama": os.path.join(visuals_dir, "xianxia_landscape_panorama.jpg"),
    "thumbnail": os.path.join(visuals_dir, "thumbnail_part_1.png"),
}

def pick_asset(rec):
    desc = rec.get("image_direction", "").lower()
    cue = rec.get("voice_cue", "").lower()
    ch = int(rec.get("chapter", 1))
    shot = rec.get("shot_type", "").lower()
    order = int(rec.get("scene_order", 1))
    text = desc + " " + cue

    if any(k in text for k in ["kỷ thanh la", "thanh la", "sư tỷ", "kiếm gãy", "máu", "áo đen", "bị thương", "khuỵu"]):
        return assets["ky_thanh_la"]
    if any(k in text for k in ["trác cửu", "sát thủ", "giao chiến", "đao kiếm", "đánh", "chém", "tên", "cung", "trường côn", "rút đao chém"]):
        return assets["trac_cuu"]
    if any(k in text for k in ["a thạch", "chim sẻ", "đứa bé", "rổ chim", "con chim"]):
        return assets["a_thach"]
    if any(k in text for k in ["tam trưởng lão", "ông lão", "hồ lô", "rượu", "chổi"]):
        return assets["tam_elder"]
    if any(k in text for k in ["vãn ninh", "áo xanh nhạt", "vết đỏ", "nữ tử áo xanh", "kho gạo", "cháo", "bát cháo"]):
        return assets["van_ninh"]
    if any(k in text for k in ["phong thư", "lá thư", "mũi kim", "dấu son", "chữ đỏ", "chu tứ", "trói", "dây trói"]):
        return assets["letter_needle"]
    if any(k in text for k in ["thẻ đệ tử", "bình minh", "trời sáng", "đao gãy", "đóng chìm", "thẻ bài"]):
        return assets["final_token"]
    if any(k in text for k in ["sơn môn", "cổng gỗ", "thanh vân tông", "chính điện", "ngói rơi", "sân điện", "sơn môn đổ nát"]):
        return assets["sect_gate"]
    if any(k in text for k in ["tạ hành chu", "hành chu", "tán tu", "ngậm cọng cỏ", "rút đao", "luyện đao"]):
        return assets["ta_hanh_chu"]
    if any(k in text for k in ["con đường", "núi rừng", "bậc đá", "bóng lá", "hoàng hôn", "chiều muộn", "núi", "đỉnh núi"]):
        return assets["celestial_path"] if order % 2 == 1 else assets["floating_peaks"]
    
    # Fallback per chapter
    if ch == 1:
        return assets["celestial_path"] if "toàn cảnh" in shot else assets["ta_hanh_chu"]
    elif ch == 2:
        return assets["letter_needle"] if order % 2 == 0 else assets["sect_gate"]
    elif ch == 3:
        return assets["ky_thanh_la"] if order % 2 == 1 else assets["van_ninh"]
    elif ch == 4:
        return assets["floating_peaks"] if order % 2 == 1 else assets["ta_hanh_chu"]
    elif ch == 5:
        return assets["letter_needle"] if order % 2 == 1 else assets["tam_elder"]
    elif ch == 6:
        return assets["trac_cuu"] if order % 2 == 1 else assets["ta_hanh_chu"]
    elif ch == 7:
        return assets["final_token"] if order > 30 else assets["trac_cuu"]
    return assets["floating_peaks"]

target_w, target_h = 1920, 1080
fps = 30

def render_one_scene_smooth(r):
    image_id = r["image_id"]
    dur = float(r["duration_seconds"])
    ch = int(r["chapter"])
    shot = r.get("shot_type", "").lower()
    order = int(r.get("scene_order", 1))
    
    scene_mp4 = os.path.join(scenes_video_dir, f"{image_id}.mp4")
    if os.path.exists(scene_mp4) and os.path.getsize(scene_mp4) > 10000:
        return image_id, ch, scene_mp4, dur

    asset_path = pick_asset(r)
    img = cv2.imread(asset_path)
    if img is None:
        raise ValueError(f"Could not load asset: {asset_path}")
    
    h, w = img.shape[:2]
    num_frames = max(30, int(round(dur * fps)))
    base_scale = max(target_w / w, target_h / h)
    
    # Determine motion parameters (Smooth floating subpixel motion)
    mode = order % 6
    if "cận" in shot or "chi tiết" in shot:
        # Subtle slow push
        z_start, z_end = 1.05, 1.14
        cx_start, cx_end = w * 0.50, w * 0.50
        cy_start, cy_end = h * 0.48, h * 0.46
    elif "toàn cảnh" in shot:
        if mode % 2 == 0:
            # Pan right
            z_start, z_end = 1.08, 1.08
            cx_start, cx_end = w * 0.43, w * 0.57
            cy_start, cy_end = h * 0.50, h * 0.50
        else:
            # Slow pull out
            z_start, z_end = 1.14, 1.04
            cx_start, cx_end = w * 0.50, w * 0.50
            cy_start, cy_end = h * 0.48, h * 0.50
    elif mode == 0:
        # Pan right
        z_start, z_end = 1.07, 1.07
        cx_start, cx_end = w * 0.44, w * 0.56
        cy_start, cy_end = h * 0.50, h * 0.50
    elif mode == 1:
        # Slow push
        z_start, z_end = 1.04, 1.13
        cx_start, cx_end = w * 0.48, w * 0.52
        cy_start, cy_end = h * 0.50, h * 0.48
    elif mode == 2:
        # Pan left
        z_start, z_end = 1.07, 1.07
        cx_start, cx_end = w * 0.56, w * 0.44
        cy_start, cy_end = h * 0.50, h * 0.50
    elif mode == 3:
        # Tilt up
        z_start, z_end = 1.08, 1.08
        cx_start, cx_end = w * 0.50, w * 0.50
        cy_start, cy_end = h * 0.55, h * 0.45
    elif mode == 4:
        # Slow pull out
        z_start, z_end = 1.13, 1.04
        cx_start, cx_end = w * 0.50, w * 0.50
        cy_start, cy_end = h * 0.48, h * 0.50
    else:
        # Floating diagonal drift
        z_start, z_end = 1.05, 1.10
        cx_start, cx_end = w * 0.46, w * 0.54
        cy_start, cy_end = h * 0.52, h * 0.48

    # Spawn glowing spiritual motes (linh khi)
    np.random.seed(order * 1000 + 42)
    num_particles = 24
    px = np.random.uniform(0, target_w, num_particles).astype(np.float32)
    py = np.random.uniform(0, target_h, num_particles).astype(np.float32)
    ps = np.random.uniform(1.5, 3.5, num_particles).astype(np.float32)
    pv = np.random.uniform(0.3, 0.8, num_particles).astype(np.float32)
    p_phase = np.random.uniform(0, np.pi * 2, num_particles).astype(np.float32)

    # Launch FFmpeg pipe
    cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{target_w}x{target_h}",
        "-pix_fmt", "bgr24",
        "-r", str(fps),
        "-i", "-",
        "-c:v", "libx264", "-preset", "veryfast",
        "-pix_fmt", "yuv420p",
        scene_mp4
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for f in range(num_frames):
        t = f / max(1, num_frames - 1)
        # Smoothstep curve for 100% zero-jitter continuous motion
        u = t * t * (3.0 - 2.0 * t)
        
        zoom = z_start + (z_end - z_start) * u
        cx = cx_start + (cx_end - cx_start) * u
        cy = cy_start + (cy_end - cy_start) * u
        
        s = base_scale * zoom
        tx = target_w / 2.0 - cx * s
        ty = target_h / 2.0 - cy * s
        
        M = np.array([[s, 0.0, tx], [0.0, s, ty]], dtype=np.float32)
        frame = cv2.warpAffine(img, M, (target_w, target_h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
        
        # Draw subtle glowing spiritual energy motes
        for i in range(num_particles):
            px[i] = (px[i] - pv[i] * 0.7) % target_w
            py[i] = (py[i] - pv[i] * 0.3 + np.sin(p_phase[i] + t * 4.0) * 0.2) % target_h
            alpha = 0.25 + 0.15 * np.sin(p_phase[i] + t * 5.0)
            ix, iy, ir = int(px[i]), int(py[i]), max(1, int(ps[i]))
            cv2.circle(frame, (ix, iy), ir, (255, 235, 180), -1)
            cv2.circle(frame, (ix, iy), ir + 1, (220, 240, 200), 1)
        
        proc.stdin.write(frame.tobytes())

    proc.stdin.close()
    proc.wait()
    return image_id, ch, scene_mp4, dur

print("Loading TIMELINE CSV...")
with open(timeline_csv, "r", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

print(f"Loaded {len(rows)} scenes for butter-smooth rendering.")

t_start = time.time()
print("Starting butter-smooth Xianxia video rendering (4 parallel workers)...")

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(render_one_scene_smooth, r): r["image_id"] for r in rows}
    completed_count = 0
    for future in as_completed(futures):
        completed_count += 1
        s_id = futures[future]
        try:
            future.result()
        except Exception as e:
            print(f"Error rendering {s_id}: {e}")
            raise
        if completed_count % 10 == 0 or completed_count == len(rows):
            el = time.time() - t_start
            print(f"Rendered {completed_count}/{len(rows)} smooth scenes ({el:.1f}s elapsed, {el/completed_count:.2f}s/scene)")

# Step 2: Render 2.0s chapter gap video with ethereal floating peaks
silence_video = os.path.join(work_dir, "chapter_gap_smooth_2s.mp4")
gap_img = cv2.imread(assets["floating_peaks"])
gap_h, gap_w = gap_img.shape[:2]
gap_scale = max(target_w / gap_w, target_h / gap_h)

cmd_gap = [
    "ffmpeg", "-y",
    "-f", "rawvideo", "-vcodec", "rawvideo",
    "-s", f"{target_w}x{target_h}",
    "-pix_fmt", "bgr24",
    "-r", str(fps),
    "-i", "-",
    "-c:v", "libx264", "-preset", "veryfast",
    "-pix_fmt", "yuv420p",
    silence_video
]
proc_gap = subprocess.Popen(cmd_gap, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
for f in range(60):
    t = f / 59.0
    u = t * t * (3.0 - 2.0 * t)
    s = gap_scale * (1.04 + 0.02 * u)
    tx = target_w / 2.0 - (gap_w * 0.5) * s
    ty = target_h / 2.0 - (gap_h * 0.5) * s
    M = np.array([[s, 0.0, tx], [0.0, s, ty]], dtype=np.float32)
    frame = cv2.warpAffine(gap_img, M, (target_w, target_h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
    proc_gap.stdin.write(frame.tobytes())
proc_gap.stdin.close()
proc_gap.wait()
print("Created chapter_gap_smooth_2s.mp4")

# Step 3: Build full video concat file
video_concat_txt = os.path.join(work_dir, "concat_video_smooth_full.txt")
with open(video_concat_txt, "w", encoding="utf-8") as f:
    current_ch = 1
    for r in rows:
        ch = int(r["chapter"])
        image_id = r["image_id"]
        scene_mp4 = os.path.join(scenes_video_dir, f"{image_id}.mp4")
        if ch > current_ch:
            clean_gap = silence_video.replace("\\", "/")
            f.write(f"file '{clean_gap}'\n")
            current_ch = ch
        clean_path = scene_mp4.replace("\\", "/")
        f.write(f"file '{clean_path}'\n")

print(f"Wrote concat file with {len(rows)} scenes and chapter gaps.")

# Step 4: Concatenate video scenes
raw_video_mp4 = os.path.join(work_dir, "raw_video_track_smooth.mp4")
print("\nConcatenating all smooth video scenes into raw_video_track_smooth.mp4...")
subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", video_concat_txt,
    "-c", "copy",
    raw_video_mp4
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Step 5: Mux final video with audio track
final_mp4 = os.path.join(output_dir, "TONG-MON-BI-TRUY-SAT-TAP-01-FINAL.mp4")
master_audio_wav = os.path.join(output_dir, "TAP-01-VOICE-FULL.wav")

print(f"\nMuxing final video with master audio track...")
print(f"Video: {raw_video_mp4}")
print(f"Audio: {master_audio_wav}")
print(f"Output: {final_mp4}")

subprocess.run([
    "ffmpeg", "-y",
    "-i", raw_video_mp4,
    "-i", master_audio_wav,
    "-c:v", "copy",
    "-c:a", "aac",
    "-b:a", "192k",
    "-ar", "48000",
    "-shortest",
    final_mp4
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

final_size = os.path.getsize(final_mp4) / (1024 * 1024)
print(f"\n==========================================")
print(f"SMOOTH ETHEREAL XIANXIA MP4 EXPORT COMPLETE!")
print(f"File: {final_mp4}")
print(f"Size: {final_size:.2f} MB")
print(f"==========================================")
