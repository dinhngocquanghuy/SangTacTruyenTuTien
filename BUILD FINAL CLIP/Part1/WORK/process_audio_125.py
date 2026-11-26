import csv
import json
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

base_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP"
work_dir = os.path.join(base_dir, "WORK")
orig_audio_dir = os.path.join(work_dir, "audio")
orig_scenes_dir = os.path.join(orig_audio_dir, "scenes")
audio_125_dir = os.path.join(work_dir, "audio_125")
scenes_125_dir = os.path.join(audio_125_dir, "scenes")
output_dir = os.path.join(base_dir, "OUTPUT")
timeline_csv = os.path.join(output_dir, "TAP-01-TIMELINE.csv")

os.makedirs(audio_125_dir, exist_ok=True)
os.makedirs(scenes_125_dir, exist_ok=True)

# Helper to get wav duration via ffprobe
def get_wav_duration(wav_path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        wav_path
    ]
    res = subprocess.check_output(cmd).decode().strip()
    return float(res)

# 1. Read existing timeline CSV
with open(timeline_csv, "r", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

print(f"Loaded {len(rows)} scenes from {timeline_csv}")

# 2. Worker to convert a single scene to 1.25x speed
def convert_scene(r):
    img_id = r["image_id"]
    in_wav = os.path.join(orig_scenes_dir, f"{img_id}.wav")
    out_wav = os.path.join(scenes_125_dir, f"{img_id}.wav")
    
    cmd = [
        "ffmpeg", "-y", "-i", in_wav,
        "-filter:a", "atempo=1.25",
        "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
        out_wav
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    dur = get_wav_duration(out_wav)
    return img_id, out_wav, dur

print("Converting 217 scenes to 1.25x speed in parallel...")
t0 = time.time()
scene_durations = {}

with ThreadPoolExecutor(max_workers=12) as executor:
    futures = {executor.submit(convert_scene, r): r["image_id"] for r in rows}
    for future in as_completed(futures):
        img_id, out_wav, dur = future.result()
        scene_durations[img_id] = dur

print(f"All 217 scenes converted to 1.25x in {time.time()-t0:.2f} seconds!")

# 3. Create 2.0s silence file in audio_125_dir
silence_wav = os.path.join(audio_125_dir, "silence_2s.wav")
subprocess.run([
    "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
    "-t", "2.0", "-c:a", "pcm_s16le", silence_wav
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 4. Concatenate per chapter and update timeline records
all_scene_records = []
global_current_time = 0.0

for ch_num in range(1, 8):
    ch_rows = [r for r in rows if int(r["chapter"]) == ch_num]
    ch_scene_wavs = []
    chapter_current_time = 0.0
    
    for r in ch_rows:
        img_id = r["image_id"]
        out_wav = os.path.join(scenes_125_dir, f"{img_id}.wav")
        dur = scene_durations[img_id]
        
        ch_scene_start = chapter_current_time
        ch_scene_end = ch_scene_start + dur
        chapter_current_time = ch_scene_end
        
        glb_scene_start = global_current_time
        glb_scene_end = glb_scene_start + dur
        global_current_time = glb_scene_end
        
        ch_scene_wavs.append(out_wav)
        
        rec = dict(r)
        rec["global_start_time"] = f"{glb_scene_start:.3f}"
        rec["global_end_time"] = f"{glb_scene_end:.3f}"
        rec["duration_seconds"] = f"{dur:.3f}"
        rec["chapter_start_time"] = f"{ch_scene_start:.3f}"
        rec["chapter_end_time"] = f"{ch_scene_end:.3f}"
        rec["status"] = "SYNCED_1.25X"
        rec["audio_path"] = out_wav
        all_scene_records.append(rec)
    
    # Concatenate chapter scenes into chapter_0X.wav
    concat_txt = os.path.join(audio_125_dir, f"concat_ch_{ch_num}.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for wp in ch_scene_wavs:
            clean_wp = wp.replace("\\", "/")
            f.write(f"file '{clean_wp}'\n")
            
    ch_wav = os.path.join(audio_125_dir, f"chapter_{ch_num:02d}.wav")
    cmd_ch_concat = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_txt, "-c", "copy", ch_wav
    ]
    subprocess.run(cmd_ch_concat, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ch_dur = get_wav_duration(ch_wav)
    print(f"Chapter {ch_num}: Duration = {ch_dur:.2f}s ({ch_dur/60:.2f} min)")
    
    if ch_num < 7:
        global_current_time += 2.0

# 5. Build full master audio concatenation
full_concat_txt = os.path.join(audio_125_dir, "concat_full.txt")
with open(full_concat_txt, "w", encoding="utf-8") as f:
    for ch_num in range(1, 8):
        ch_wav = os.path.join(audio_125_dir, f"chapter_{ch_num:02d}.wav").replace("\\", "/")
        f.write(f"file '{ch_wav}'\n")
        if ch_num < 7:
            clean_silence = silence_wav.replace("\\", "/")
            f.write(f"file '{clean_silence}'\n")

full_audio_wav = os.path.join(output_dir, "TAP-01-VOICE-FULL.wav")
print(f"\nConcatenating all 7 chapters into {full_audio_wav}...")
subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", full_concat_txt, "-c", "copy", full_audio_wav
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

full_dur = get_wav_duration(full_audio_wav)
print(f"\n==========================================")
print(f"MASTER AUDIO 1.25X COMPLETE!")
print(f"Total Duration: {full_dur:.2f} seconds ({full_dur/60:.2f} minutes / {full_dur/3600:.2f} hours)")
print(f"Output: {full_audio_wav} ({os.path.getsize(full_audio_wav) / (1024*1024):.2f} MB)")
print(f"==========================================")

# 6. Save updated TIMELINE CSV
fieldnames = list(all_scene_records[0].keys())
with open(timeline_csv, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_scene_records)

print(f"Successfully updated timeline CSV: {timeline_csv}")
