import csv
import os
import subprocess
import time

base_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP"
timeline_csv = os.path.join(base_dir, "OUTPUT", "TAP-01-TIMELINE.csv")
visuals_dir = os.path.join(base_dir, "WORK", "visuals_ethereal")
work_dir = os.path.join(base_dir, "WORK")
output_dir = os.path.join(base_dir, "OUTPUT")

# Ethereal Xianxia Visual Assets Map (Still Images)
assets = {
    "celestial_path": os.path.join(visuals_dir, "C01_I001_celestial_path.jpg"),
    "mountain_path": os.path.join(visuals_dir, "C01_I001_mountain_path.jpg"),
    "ta_hanh_chu": os.path.join(visuals_dir, "C01_I002_ta_hanh_chu.jpg"),
    "sect_gate": os.path.join(visuals_dir, "C01_I008_sect_gate.jpg"),
    "tam_elder": os.path.join(visuals_dir, "C01_I010_tam_elder.jpg"),
    "van_ninh": os.path.join(visuals_dir, "C01_I016_van_ninh_xianxia.jpg"),
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

with open(timeline_csv, "r", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

print(f"Loaded {len(rows)} scenes for still-image video rendering.")

# Build ffconcat file
concat_txt = os.path.join(work_dir, "still_scenes_concat.txt")
with open(concat_txt, "w", encoding="utf-8") as f:
    f.write("ffconcat version 1.0\n")
    current_ch = 1
    for r in rows:
        ch = int(r["chapter"])
        dur = float(r["duration_seconds"])
        asset_path = pick_asset(r).replace("\\", "/")
        
        if ch > current_ch:
            gap_asset = assets["floating_peaks"].replace("\\", "/")
            f.write(f"file '{gap_asset}'\n")
            f.write(f"duration 2.0\n")
            current_ch = ch
        
        f.write(f"file '{asset_path}'\n")
        f.write(f"duration {dur:.3f}\n")
    
    # Last image line to cap the last duration
    last_asset = pick_asset(rows[-1]).replace("\\", "/")
    f.write(f"file '{last_asset}'\n")

print(f"Generated {concat_txt} for all 217 scenes with 100% still images.")

# Fast Single-Pass Rendering with FFmpeg
final_mp4 = os.path.join(output_dir, "TONG-MON-BI-TRUY-SAT-TAP-01-FINAL.mp4")
master_audio_wav = os.path.join(output_dir, "TAP-01-VOICE-FULL.wav")

cmd = [
    "ffmpeg", "-y",
    "-f", "concat", "-safe", "0",
    "-i", concat_txt,
    "-i", master_audio_wav,
    "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080",
    "-r", "30",
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-tune", "stillimage",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    "-ar", "48000",
    "-shortest",
    final_mp4
]

print(f"\nStarting FAST single-pass still-image video rendering...")
print(f"Command: {' '.join(cmd)}")

t0 = time.time()
subprocess.run(cmd, check=True)
el = time.time() - t0

final_size = os.path.getsize(final_mp4) / (1024 * 1024)
print(f"\n==========================================")
print(f"STILL-IMAGE FINAL MP4 EXPORT COMPLETE IN {el:.1f}s!")
print(f"File: {final_mp4}")
print(f"Size: {final_size:.2f} MB")
print(f"==========================================")
