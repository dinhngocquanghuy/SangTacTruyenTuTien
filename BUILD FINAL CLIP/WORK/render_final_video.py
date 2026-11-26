import csv
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

base_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP"
timeline_csv = os.path.join(base_dir, "OUTPUT", "TAP-01-TIMELINE.csv")
visuals_dir = os.path.join(base_dir, "WORK", "visuals")
scenes_video_dir = os.path.join(base_dir, "WORK", "video_scenes")
work_dir = os.path.join(base_dir, "WORK")
output_dir = os.path.join(base_dir, "OUTPUT")

os.makedirs(scenes_video_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# Visual assets map
assets = {
    "mountain_path": os.path.join(visuals_dir, "C01_I001_mountain_path.jpg"),
    "ta_hanh_chu": os.path.join(visuals_dir, "C01_I002_ta_hanh_chu.jpg"),
    "sect_gate": os.path.join(visuals_dir, "C01_I008_sect_gate.jpg"),
    "tam_elder": os.path.join(visuals_dir, "C01_I010_tam_elder.jpg"),
    "van_ninh": os.path.join(visuals_dir, "C01_I016_van_ninh.jpg"),
    "a_thach": os.path.join(visuals_dir, "C01_I020_a_thach.jpg"),
    "letter_needle": os.path.join(visuals_dir, "C02_I001_letter_needle.jpg"),
    "ky_thanh_la": os.path.join(visuals_dir, "C03_I001_ky_thanh_la.jpg"),
    "trac_cuu": os.path.join(visuals_dir, "C06_I018_trac_cuu.jpg"),
    "final_token": os.path.join(visuals_dir, "C07_I038_final_token.jpg"),
    "panorama": os.path.join(visuals_dir, "xianxia_landscape_panorama.jpg"),
    "thumbnail": os.path.join(visuals_dir, "thumbnail_part_1.png"),
}

def pick_asset(rec):
    desc = rec.get("image_direction", "").lower()
    cue = rec.get("voice_cue", "").lower()
    ch = int(rec.get("chapter", 1))
    shot = rec.get("shot_type", "").lower()
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
    if any(k in text for k in ["con đường", "núi rừng", "bậc đá", "bóng lá", "hoàng hôn", "chiều muộn", "núi"]):
        return assets["mountain_path"]
    
    # Fallback per chapter
    if ch == 1:
        return assets["mountain_path"] if "toàn cảnh" in shot else assets["ta_hanh_chu"]
    elif ch == 2:
        return assets["letter_needle"]
    elif ch == 3:
        return assets["ky_thanh_la"]
    elif ch == 4:
        return assets["mountain_path"]
    elif ch == 5:
        return assets["letter_needle"]
    elif ch == 6:
        return assets["trac_cuu"]
    elif ch == 7:
        return assets["final_token"] if int(rec.get("scene_order", 0)) > 30 else assets["trac_cuu"]
    return assets["panorama"]

def get_motion_filter(rec, duration_sec):
    num_frames = max(30, int(round(duration_sec * 30)))
    shot = rec.get("shot_type", "").lower()
    order = int(rec.get("scene_order", 1))

    mode = order % 5
    if "cận" in shot or "chi tiết" in shot:
        return f"scale=2560:1440,zoompan=z='min(zoom+0.0004,1.15)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={num_frames}:s=1920x1080:fps=30"
    elif "toàn cảnh" in shot:
        if mode % 2 == 0:
            return f"scale=2560:1440,zoompan=z=1.12:x='if(lte(on,1),(iw-iw/zoom)*0.2,min((iw-iw/zoom)*0.8,x+0.4))':y='ih/2-(ih/zoom/2)':d={num_frames}:s=1920x1080:fps=30"
        else:
            return f"scale=2560:1440,zoompan=z='if(lte(on,1),1.14,max(1.0,zoom-0.0004))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={num_frames}:s=1920x1080:fps=30"
    elif mode == 0:
        return f"scale=2560:1440,zoompan=z='min(zoom+0.0004,1.14)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={num_frames}:s=1920x1080:fps=30"
    elif mode == 1:
        return f"scale=2560:1440,zoompan=z=1.12:x='if(lte(on,1),(iw-iw/zoom)*0.8,max((iw-iw/zoom)*0.2,x-0.4))':y='ih/2-(ih/zoom/2)':d={num_frames}:s=1920x1080:fps=30"
    elif mode == 2:
        return f"scale=2560:1440,zoompan=z='if(lte(on,1),1.14,max(1.0,zoom-0.0004))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={num_frames}:s=1920x1080:fps=30"
    elif mode == 3:
        return f"scale=2560:1440,zoompan=z=1.10:x='iw/2-(iw/zoom/2)':y='if(lte(on,1),(ih-ih/zoom)*0.1,min((ih-ih/zoom)*0.85,y+0.3))':d={num_frames}:s=1920x1080:fps=30"
    else:
        return f"scale=2560:1440,zoompan=z='min(zoom+0.0003,1.10)':x='if(lte(on,1),(iw-iw/zoom)*0.3,x+0.2)':y='if(lte(on,1),(ih-ih/zoom)*0.3,y+0.15)':d={num_frames}:s=1920x1080:fps=30"

def render_one_scene(r):
    image_id = r["image_id"]
    dur = float(r["duration_seconds"])
    ch = int(r["chapter"])
    asset_path = pick_asset(r)
    motion_filter = get_motion_filter(r, dur)
    scene_mp4 = os.path.join(scenes_video_dir, f"{image_id}.mp4")
    
    if os.path.exists(scene_mp4) and os.path.getsize(scene_mp4) > 10000:
        return image_id, ch, scene_mp4, dur
    
    cmd = [
        "ffmpeg", "-y", "-loop", "1",
        "-i", asset_path,
        "-vf", motion_filter,
        "-t", f"{dur:.3f}",
        "-r", "30",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-pix_fmt", "yuv420p",
        scene_mp4
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return image_id, ch, scene_mp4, dur

print("Loading TIMELINE CSV...")
with open(timeline_csv, "r", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

print(f"Loaded {len(rows)} scenes.")

# Step 1: Render each scene video clip in parallel using 4 worker threads
t_start = time.time()
print("Starting parallel video rendering (4 workers)...")

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(render_one_scene, r): r["image_id"] for r in rows}
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
            print(f"Rendered {completed_count}/{len(rows)} scenes ({el:.1f}s elapsed, {el/completed_count:.2f}s/scene)")

# Step 2: Render 2.0s chapter gap video
silence_video = os.path.join(work_dir, "chapter_gap_2s.mp4")
if not os.path.exists(silence_video) or os.path.getsize(silence_video) < 5000:
    cmd_gap = [
        "ffmpeg", "-y", "-loop", "1",
        "-i", assets["panorama"],
        "-vf", "scale=2560:1440,zoompan=z='min(zoom+0.0003,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=60:s=1920x1080:fps=30",
        "-t", "2.0", "-r", "30",
        "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p",
        silence_video
    ]
    subprocess.run(cmd_gap, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Created chapter_gap_2s.mp4")

# Step 3: Build full video concat file in EXACT order from rows
video_concat_txt = os.path.join(work_dir, "concat_video_full.txt")
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
raw_video_mp4 = os.path.join(work_dir, "raw_video_track.mp4")
print("\nConcatenating all video scenes into raw_video_track.mp4...")
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
print(f"FINAL MP4 EXPORT COMPLETE!")
print(f"File: {final_mp4}")
print(f"Size: {final_size:.2f} MB")
print(f"==========================================")
