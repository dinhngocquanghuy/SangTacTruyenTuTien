import csv
import json
import os
import subprocess
import time
from gtts import gTTS

base_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP"
csv_path = os.path.join(base_dir, "DANH-SACH-ANH-TAP-01-AGENT.csv")
chapters_json_path = os.path.join(base_dir, "WORK", "chapters_data.json")
audio_scenes_dir = os.path.join(base_dir, "WORK", "audio", "scenes")
audio_work_dir = os.path.join(base_dir, "WORK", "audio")
output_dir = os.path.join(base_dir, "OUTPUT")

os.makedirs(audio_scenes_dir, exist_ok=True)
os.makedirs(audio_work_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

with open(csv_path, "r", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

with open(chapters_json_path, "r", encoding="utf-8") as f:
    chapters = json.load(f)

print(f"Loaded {len(rows)} scenes from CSV and {len(chapters)} chapters.")

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

# Generate 2.0s silence file
silence_wav = os.path.join(audio_work_dir, "silence_2s.wav")
subprocess.run([
    "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
    "-t", "2.0", "-c:a", "pcm_s16le", silence_wav
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Created silence_2s.wav")

all_scene_records = []
global_current_time = 0.0

for ch_num in range(1, 8):
    ch_rows = [r for r in rows if int(r["chapter"]) == ch_num]
    ch_data = chapters[ch_num - 1]
    ch_paras = ch_data["clean_paragraphs"]
    ch_title = ch_data["title"]
    
    print(f"\n==========================================")
    print(f"PROCESSING {ch_title} ({len(ch_rows)} scenes, {len(ch_paras)} paragraphs)")
    print(f"==========================================")
    
    chapter_current_time = 0.0
    ch_scene_wavs = []
    
    for s_idx, r in enumerate(ch_rows):
        start_p = int(r["source_paragraph_index"])
        end_p = int(ch_rows[s_idx + 1]["source_paragraph_index"]) if s_idx + 1 < len(ch_rows) else len(ch_paras)
        para_slice = ch_paras[start_p:end_p]
        text_content = " ".join(para_slice).strip()
        
        if s_idx == 0:
            # Prepend chapter title once at start of chapter
            text_content = f"{ch_title}. {text_content}"
        
        image_id = r["image_id"]
        mp3_path = os.path.join(audio_scenes_dir, f"{image_id}.mp3")
        wav_path = os.path.join(audio_scenes_dir, f"{image_id}.wav")
        
        # Synthesize with gTTS if not already generated
        if not (os.path.exists(wav_path) and os.path.getsize(wav_path) > 1000):
            # synthesize mp3
            success = False
            for attempt in range(5):
                try:
                    tts = gTTS(text=text_content, lang="vi", tld="com")
                    tts.save(mp3_path)
                    success = True
                    break
                except Exception as e:
                    print(f"[{image_id}] Retry {attempt+1}/5 error: {e}")
                    time.sleep(1.0 + attempt * 1.5)
            
            if not success:
                raise RuntimeError(f"Failed to generate TTS for {image_id} after 5 attempts!")
            
            # Convert to standard 48kHz stereo WAV
            cmd_convert = [
                "ffmpeg", "-y", "-i", mp3_path,
                "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
                wav_path
            ]
            subprocess.run(cmd_convert, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        duration = get_wav_duration(wav_path)
        
        ch_scene_start = chapter_current_time
        ch_scene_end = ch_scene_start + duration
        chapter_current_time = ch_scene_end
        
        glb_scene_start = global_current_time
        glb_scene_end = glb_scene_start + duration
        global_current_time = glb_scene_end
        
        ch_scene_wavs.append(wav_path)
        
        rec = dict(r)
        rec["global_start_time"] = f"{glb_scene_start:.3f}"
        rec["global_end_time"] = f"{glb_scene_end:.3f}"
        rec["duration_seconds"] = f"{duration:.3f}"
        rec["chapter_start_time"] = f"{ch_scene_start:.3f}"
        rec["chapter_end_time"] = f"{ch_scene_end:.3f}"
        rec["status"] = "SYNCED"
        rec["audio_path"] = wav_path
        all_scene_records.append(rec)
        
        if (s_idx + 1) % 5 == 0 or s_idx == len(ch_rows) - 1:
            print(f"  [{image_id}] Scene {s_idx+1}/{len(ch_rows)}: dur={duration:.2f}s, ch_time={ch_scene_end:.2f}s, glb_time={glb_scene_end/60:.2f}m")
    
    # Concatenate chapter scenes into chapter_0X.wav
    concat_txt = os.path.join(audio_work_dir, f"concat_ch_{ch_num}.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for wp in ch_scene_wavs:
            clean_wp = wp.replace("\\", "/")
            f.write(f"file '{clean_wp}'\n")
    
    ch_wav = os.path.join(audio_work_dir, f"chapter_{ch_num:02d}.wav")
    cmd_ch_concat = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_txt, "-c", "copy", ch_wav
    ]
    subprocess.run(cmd_ch_concat, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ch_dur = get_wav_duration(ch_wav)
    print(f"--> CHAPTER {ch_num} COMPLETE: Duration = {ch_dur:.2f}s ({ch_dur/60:.2f} min)")
    
    # Add chapter pause if not last chapter
    if ch_num < 7:
        global_current_time += 2.0
        print(f"  [Pause 2.0s between Chapter {ch_num} and {ch_num+1}]")

# Build full audio concatenation
full_concat_txt = os.path.join(audio_work_dir, "concat_full.txt")
with open(full_concat_txt, "w", encoding="utf-8") as f:
    for ch_num in range(1, 8):
        ch_wav = os.path.join(audio_work_dir, f"chapter_{ch_num:02d}.wav").replace("\\", "/")
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
print(f"ALL 7 CHAPTERS COMPLETE!")
print(f"Total Full Audio Duration: {full_dur:.2f} seconds ({full_dur/60:.2f} minutes / {full_dur/3600:.2f} hours)")
print(f"Output: {full_audio_wav} ({os.path.getsize(full_audio_wav) / (1024*1024):.1f} MB)")
print(f"==========================================")

# Write TAP-01-TIMELINE.csv
timeline_csv = os.path.join(output_dir, "TAP-01-TIMELINE.csv")
fieldnames = list(all_scene_records[0].keys())
with open(timeline_csv, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_scene_records)

print(f"Exported timeline to {timeline_csv} ({len(all_scene_records)} scenes)")
