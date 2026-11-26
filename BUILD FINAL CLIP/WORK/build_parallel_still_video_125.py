import csv
import json
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

base_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP"
timeline_csv = os.path.join(base_dir, "OUTPUT", "TAP-01-TIMELINE.csv")
visuals_dir = os.path.join(base_dir, "WORK", "visuals_ethereal")
work_dir = os.path.join(base_dir, "WORK")
audio_125_dir = os.path.join(work_dir, "audio_125")
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

def get_wav_dur(p):
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", p]
    return float(subprocess.check_output(cmd).decode().strip())

# 2.0s chapter gap video (100% still)
silence_video = os.path.join(work_dir, "chapter_gap_still_2s.mp4")
if not os.path.exists(silence_video):
    gap_asset = assets["floating_peaks"]
    cmd_gap = [
        "ffmpeg", "-y", "-loop", "1", "-i", gap_asset,
        "-t", "2.0", "-r", "30",
        "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080",
        "-c:v", "libx264", "-preset", "ultrafast", "-tune", "stillimage", "-pix_fmt", "yuv420p",
        silence_video
    ]
    subprocess.run(cmd_gap, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Created chapter_gap_still_2s.mp4")

def render_chapter_video(ch_num):
    ch_rows = [r for r in rows if int(r["chapter"]) == ch_num]
    ch_wav = os.path.join(audio_125_dir, f"chapter_{ch_num:02d}.wav")
    ch_dur = get_wav_dur(ch_wav)
    
    concat_txt = os.path.join(work_dir, f"still_concat_ch_{ch_num}_125.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        f.write("ffconcat version 1.0\n")
        for r in ch_rows:
            dur = float(r["duration_seconds"])
            asset_path = pick_asset(r).replace("\\", "/")
            f.write(f"file '{asset_path}'\n")
            f.write(f"duration {dur:.3f}\n")
        last_asset = pick_asset(ch_rows[-1]).replace("\\", "/")
        f.write(f"file '{last_asset}'\n")
    
    ch_mp4 = os.path.join(work_dir, f"still_video_ch_{ch_num}_125.mp4")
    cmd_ch = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_txt,
        "-t", f"{ch_dur:.3f}",
        "-r", "30",
        "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080",
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-tune", "stillimage",
        "-pix_fmt", "yuv420p",
        ch_mp4
    ]
    t0 = time.time()
    subprocess.run(cmd_ch, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    el = time.time() - t0
    print(f"--> Chapter {ch_num} rendered: {ch_dur:.1f}s video in {el:.1f}s ({ch_dur/el:.1f}x speed)")
    return ch_num, ch_mp4, ch_dur

print("Starting PARALLEL STILL-IMAGE VIDEO RENDERING (1.25x Speed, 7 chapters concurrently)...")
t_all = time.time()
chapter_videos = {}

with ThreadPoolExecutor(max_workers=7) as executor:
    futures = {executor.submit(render_chapter_video, ch): ch for ch in range(1, 8)}
    for future in as_completed(futures):
        ch_num = futures[future]
        c_num, c_mp4, c_dur = future.result()
        chapter_videos[c_num] = c_mp4

el_all = time.time() - t_all
print(f"\nAll 7 chapters rendered in {el_all:.1f} seconds (~{el_all/60:.2f} minutes)!")

# Concat all chapters + 2s gaps
concat_full_txt = os.path.join(work_dir, "still_concat_all_chapters_125.txt")
with open(concat_full_txt, "w", encoding="utf-8") as f:
    for ch_num in range(1, 8):
        clean_mp4 = chapter_videos[ch_num].replace("\\", "/")
        f.write(f"file '{clean_mp4}'\n")
        if ch_num < 7:
            clean_gap = silence_video.replace("\\", "/")
            f.write(f"file '{clean_gap}'\n")

raw_still_video = os.path.join(work_dir, "raw_still_video_track_125.mp4")
print("\nConcatenating chapter videos into raw_still_video_track_125.mp4...")
subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", concat_full_txt,
    "-c", "copy",
    raw_still_video
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Mux with master audio
final_mp4 = os.path.join(output_dir, "TONG-MON-BI-TRUY-SAT-TAP-01-FINAL.mp4")
master_audio_wav = os.path.join(output_dir, "TAP-01-VOICE-FULL.wav")

print(f"\nMuxing final video with master audio 1.25x...")
print(f"Video: {raw_still_video}")
print(f"Audio: {master_audio_wav}")
print(f"Output: {final_mp4}")

subprocess.run([
    "ffmpeg", "-y",
    "-i", raw_still_video,
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
print(f"100% STILL-IMAGE FINAL MP4 (1.25X) COMPLETE IN {time.time()-t_all:.1f}s!")
print(f"File: {final_mp4}")
print(f"Size: {final_size:.2f} MB")
print(f"==========================================")
