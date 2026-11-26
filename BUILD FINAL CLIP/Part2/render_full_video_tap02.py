import os
import csv
import json
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

base_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02"
images_dir = os.path.join(base_dir, "IMAGES")
work_dir = os.path.join(base_dir, "WORK")
output_dir = os.path.join(base_dir, "OUTPUT")
timeline_csv = os.path.join(output_dir, "TAP-02-TIMELINE.csv")
master_audio_wav = os.path.join(output_dir, "TAP-02-VOICE-FULL.wav")
chapter_audio_dir = os.path.join(work_dir, "CHAPTER_AUDIO")

def check_images_status():
    with open(timeline_csv, "r", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    existing = []
    missing = []
    for r in rows:
        img_name = r["image_file"]
        p = os.path.join(images_dir, img_name)
        if os.path.exists(p) and os.path.getsize(p) > 1000:
            existing.append(img_name)
        else:
            missing.append(img_name)
    print(f"Images status: {len(existing)} existing, {len(missing)} missing.")
    return rows, existing, missing

def render_chapter_video(ch_num, ch_rows):
    ch_wav = os.path.join(chapter_audio_dir, f"C{ch_num:02d}.wav")
    concat_txt = os.path.join(work_dir, f"concat_video_ch_{ch_num:02d}.txt")
    
    with open(concat_txt, "w", encoding="utf-8") as f:
        f.write("ffconcat version 1.0\n")
        for r in ch_rows:
            dur = float(r["duration_sec"])
            # If image missing, pick available or reference
            img_path = os.path.join(images_dir, r["image_file"])
            if not os.path.exists(img_path):
                # Fallback to first available or reference
                img_path = os.path.join(images_dir, "C08-I001.png")
            escaped_path = img_path.replace("\\", "/")
            f.write(f"file '{escaped_path}'\n")
            f.write(f"duration {dur:.3f}\n")
        # repeat last file entry per ffconcat spec
        last_img = os.path.join(images_dir, ch_rows[-1]["image_file"])
        if not os.path.exists(last_img):
            last_img = os.path.join(images_dir, "C08-I001.png")
        f.write(f"file '{last_img.replace(chr(92), '/')}'\n")
        
    ch_mp4 = os.path.join(work_dir, f"video_ch_{ch_num:02d}.mp4")
    cmd_ch = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_txt,
        "-r", "30",
        "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080",
        "-c:v", "libx264", "-preset", "ultrafast", "-tune", "stillimage",
        "-pix_fmt", "yuv420p",
        ch_mp4
    ]
    t0 = time.time()
    subprocess.run(cmd_ch, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Chapter {ch_num} video rendered in {time.time()-t0:.1f}s -> {ch_mp4}")
    return ch_num, ch_mp4

def render_full_video(allow_fallback=False):
    rows, existing, missing = check_images_status()
    if missing and not allow_fallback:
        print(f"CANNOT RENDER FINAL: {len(missing)} images missing! Status: VOICE_READY_WAITING_IMAGES")
        return False
        
    print(f"Starting video rendering across 7 chapters...")
    t_start = time.time()
    chapter_videos = {}
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {}
        for ch_num in range(8, 15):
            ch_rows = [r for r in rows if int(r["chapter"]) == ch_num]
            f = executor.submit(render_chapter_video, ch_num, ch_rows)
            futures[f] = ch_num
        for f in as_completed(futures):
            c_num, c_mp4 = f.result()
            chapter_videos[c_num] = c_mp4

    # 2.0s silence gap video
    silence_gap_video = os.path.join(work_dir, "silence_gap_2s.mp4")
    sample_img = os.path.join(images_dir, "C08-I001.png").replace("\\", "/")
    subprocess.run([
        "ffmpeg", "-y", "-loop", "1", "-i", sample_img,
        "-t", "2.0", "-r", "30",
        "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080",
        "-c:v", "libx264", "-preset", "ultrafast", "-tune", "stillimage",
        "-pix_fmt", "yuv420p",
        silence_gap_video
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Concat all chapters
    concat_all_txt = os.path.join(work_dir, "concat_all_chapters.txt")
    with open(concat_all_txt, "w", encoding="utf-8") as f:
        for ch_num in range(8, 15):
            f.write(f"file '{chapter_videos[ch_num].replace(chr(92), '/')}'\n")
            if ch_num < 14:
                f.write(f"file '{silence_gap_video.replace(chr(92), '/')}'\n")
                
    raw_video = os.path.join(work_dir, "raw_video_silent.mp4")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_all_txt, "-c", "copy",
        raw_video
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    final_mp4 = os.path.join(output_dir, "TONG-MON-BI-TRUY-SAT-TAP-02-FINAL.mp4")
    subprocess.run([
        "ffmpeg", "-y",
        "-i", raw_video,
        "-i", master_audio_wav,
        "-map", "0:v:0", "-map", "1:a:0",
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-movflags", "+faststart",
        final_mp4
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    file_size_mb = os.path.getsize(final_mp4) / (1024 * 1024)
    print(f"\n==========================================")
    print(f"FINAL VIDEO RENDER COMPLETE in {time.time()-t_start:.1f}s!")
    print(f"Path: {final_mp4}")
    print(f"Size: {file_size_mb:.2f} MB")
    print(f"==========================================")
    return True

if __name__ == "__main__":
    import sys
    allow = "--allow-fallback" in sys.argv
    render_full_video(allow_fallback=allow)
