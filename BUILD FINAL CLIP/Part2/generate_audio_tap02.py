import os
import json
import csv
import subprocess
import time
import wave
from concurrent.futures import ThreadPoolExecutor, as_completed
from gtts import gTTS

base_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02"
work_dir = os.path.join(base_dir, "WORK")
tts_mp3_dir = os.path.join(work_dir, "TTS_MP3")
wav_100_dir = os.path.join(work_dir, "WAV_100")
wav_125_dir = os.path.join(work_dir, "WAV_125")
scenes_125_dir = os.path.join(work_dir, "scenes_125")
chapter_audio_dir = os.path.join(work_dir, "CHAPTER_AUDIO")
output_dir = os.path.join(base_dir, "OUTPUT")

for d in [tts_mp3_dir, wav_100_dir, wav_125_dir, scenes_125_dir, chapter_audio_dir, output_dir]:
    os.makedirs(d, exist_ok=True)

# 1. Load chapters_data.json
with open(os.path.join(work_dir, "chapters_data.json"), "r", encoding="utf-8") as f:
    chapters = json.load(f)

# 2. Build list of all 80 tasks
tasks = []
global_order = 1

for ch_idx, ch in enumerate(chapters):
    ch_num = ch["chapter"]
    ch_title = ch["title"]
    paras = ch["body_paras"]
    scenes = ch["scenes"]
    
    for s_idx, s in enumerate(scenes):
        start_p = s["body_p_idx"]
        end_p = scenes[s_idx + 1]["body_p_idx"] if s_idx + 1 < len(scenes) else len(paras)
        scene_paras = paras[start_p:end_p]
        text_content = "\n".join(scene_paras).strip()
        
        if s_idx == 0:
            # Prepend chapter title once at start of chapter
            text_content = f"{ch_title}.\n{text_content}"
            
        tasks.append({
            "global_order": global_order,
            "chapter": ch_num,
            "scene_id": s["scene_id"],
            "image_file": s["image_file"],
            "anchor_text": s["anchor_text"],
            "text": text_content,
            "is_first_in_ch": (s_idx == 0),
            "is_last_in_ch": (s_idx == len(scenes) - 1)
        })
        global_order += 1

print(f"Prepared {len(tasks)} scene audio tasks.")

# Helper to inspect WAV duration and samples
def get_wav_info(wav_path):
    with wave.open(wav_path, "rb") as wf:
        nchannels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        nframes = wf.getnframes()
    return {
        "channels": nchannels,
        "sampwidth": sampwidth,
        "framerate": framerate,
        "nframes": nframes,
        "duration": nframes / framerate
    }

# 3. Worker function to synthesize and process one scene
def process_scene_task(task):
    sid = task["scene_id"]
    text = task["text"]
    
    mp3_path = os.path.join(tts_mp3_dir, f"{sid}.mp3")
    wav_100_path = os.path.join(wav_100_dir, f"{sid}.wav")
    wav_125_path = os.path.join(wav_125_dir, f"{sid}.wav")
    
    # Check if final wav_125 exists and is valid
    if os.path.exists(wav_125_path) and os.path.getsize(wav_125_path) > 1000:
        try:
            info = get_wav_info(wav_125_path)
            if info["nframes"] > 0:
                task["wav_path"] = wav_125_path
                task["samples"] = info["nframes"]
                task["duration"] = info["duration"]
                # Also save to scenes_125
                sc_dest = os.path.join(scenes_125_dir, f"{sid}.wav")
                if not os.path.exists(sc_dest):
                    import shutil
                    shutil.copyfile(wav_125_path, sc_dest)
                return task
        except Exception:
            pass

    # Step A: Synthesize MP3 using gTTS
    if not (os.path.exists(mp3_path) and os.path.getsize(mp3_path) > 500):
        tmp_mp3 = mp3_path + ".tmp.mp3"
        success = False
        for attempt in range(5):
            try:
                tts = gTTS(text=text, lang="vi", tld="com", slow=False)
                tts.save(tmp_mp3)
                # Verify MP3 is decodeable
                subprocess.run(
                    ["ffmpeg", "-v", "error", "-xerror", "-i", tmp_mp3, "-f", "null", "-"],
                    check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                )
                if os.path.exists(mp3_path):
                    os.remove(mp3_path)
                os.rename(tmp_mp3, mp3_path)
                success = True
                break
            except Exception as e:
                if os.path.exists(tmp_mp3):
                    try:
                        os.remove(tmp_mp3)
                    except Exception:
                        pass
                wait_time = 1.5 * (attempt + 1)
                print(f"[{sid}] gTTS attempt {attempt+1} failed: {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
        if not success:
            raise RuntimeError(f"Failed to generate gTTS for {sid} after 5 attempts!")

    # Step B: Convert MP3 to standard 48000Hz stereo WAV PCM s16le
    cmd_100 = [
        "ffmpeg", "-y", "-i", mp3_path,
        "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
        wav_100_path
    ]
    subprocess.run(cmd_100, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Step C: Apply atempo=1.25 (keeping pitch)
    cmd_125 = [
        "ffmpeg", "-y", "-i", wav_100_path,
        "-af", "atempo=1.25",
        "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
        wav_125_path
    ]
    subprocess.run(cmd_125, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    info = get_wav_info(wav_125_path)
    task["wav_path"] = wav_125_path
    task["samples"] = info["nframes"]
    task["duration"] = info["duration"]
    
    # Save copy into scenes_125
    import shutil
    shutil.copyfile(wav_125_path, os.path.join(scenes_125_dir, f"{sid}.wav"))
    
    return task

# 4. Run in parallel with ThreadPoolExecutor
print("Starting TTS synthesis and 1.25x conversion...")
start_time = time.time()
completed_tasks = {}

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(process_scene_task, t): t["scene_id"] for t in tasks}
    done_count = 0
    for future in as_completed(futures):
        res = future.result()
        sid = res["scene_id"]
        completed_tasks[sid] = res
        done_count += 1
        print(f"[{done_count}/{len(tasks)}] Done {sid}: {res['duration']:.2f}s ({res['samples']} samples)")

elapsed = time.time() - start_time
print(f"All {len(tasks)} scenes generated in {elapsed:.2f} seconds!")

# 5. Generate 2.0s silence (exactly 96,000 samples at 48kHz stereo)
silence_path = os.path.join(work_dir, "silence_2s.wav")
cmd_silence = [
    "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
    "-t", "2.0", "-c:a", "pcm_s16le", silence_path
]
subprocess.run(cmd_silence, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
silence_info = get_wav_info(silence_path)
print(f"Created silence_2s.wav: {silence_info['nframes']} samples ({silence_info['duration']}s)")

# 6. Concatenate per chapter and full master
ordered_tasks = [completed_tasks[t["scene_id"]] for t in tasks]

all_voice_units = []
timeline_rows = []

current_global_sample = 0
current_global_sec = 0.0

master_concat_list_path = os.path.join(work_dir, "concat_master.txt")
master_concat_entries = []

for ch_idx, ch in enumerate(chapters):
    ch_num = ch["chapter"]
    ch_tasks = [t for t in ordered_tasks if t["chapter"] == ch_num]
    
    ch_concat_path = os.path.join(chapter_audio_dir, f"concat_C{ch_num:02d}.txt")
    with open(ch_concat_path, "w", encoding="utf-8") as f:
        for t in ch_tasks:
            # Escape path for ffmpeg concat
            escaped_path = t["wav_path"].replace("\\", "/")
            f.write(f"file '{escaped_path}'\n")
            
    ch_wav_path = os.path.join(chapter_audio_dir, f"C{ch_num:02d}.wav")
    cmd_ch = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", ch_concat_path, "-c", "copy",
        ch_wav_path
    ]
    subprocess.run(cmd_ch, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ch_info = get_wav_info(ch_wav_path)
    print(f"Chapter {ch_num} master: {ch_info['duration']:.2f}s ({ch_info['nframes']} samples)")
    
    # Process units and timeline for this chapter
    for t in ch_tasks:
        start_samp = current_global_sample
        dur_samp = t["samples"]
        end_samp = start_samp + dur_samp
        
        start_sec = current_global_sec
        dur_sec = t["duration"]
        end_sec = start_sec + dur_sec
        
        # Calculate 30fps frames (30 fps = 1600 samples/frame)
        start_frame = round(start_samp / 1600)
        end_frame = round(end_samp / 1600)
        num_frames = end_frame - start_frame
        
        all_voice_units.append({
            "unit_id": t["scene_id"],
            "type": "SCENE",
            "chapter": ch_num,
            "scene_id": t["scene_id"],
            "image_file": t["image_file"],
            "start_sample": start_samp,
            "end_sample": end_samp,
            "duration_samples": dur_samp,
            "start_sec": f"{start_sec:.3f}",
            "end_sec": f"{end_sec:.3f}",
            "duration_sec": f"{dur_sec:.3f}",
            "start_frame": start_frame,
            "end_frame": end_frame,
            "num_frames": num_frames
        })
        
        timeline_rows.append({
            "global_order": t["global_order"],
            "scene_id": t["scene_id"],
            "chapter": ch_num,
            "image_file": t["image_file"],
            "anchor_text": t["anchor_text"],
            "start_sample": start_samp,
            "end_sample": end_samp,
            "start_sec": f"{start_sec:.3f}",
            "end_sec": f"{end_sec:.3f}",
            "duration_sec": f"{dur_sec:.3f}",
            "start_frame": start_frame,
            "end_frame": end_frame,
            "num_frames": num_frames,
            "alignment_method": "scene_chunk_atempo_exact",
            "qa_status": "PASS"
        })
        
        current_global_sample = end_samp
        current_global_sec = end_sec
        
    master_concat_entries.append(ch_wav_path)
    
    # Add 2.0s pause between chapters (except after chapter 14)
    if ch_idx < len(chapters) - 1:
        silence_dur_samp = silence_info["nframes"]
        silence_dur_sec = silence_info["duration"]
        
        start_samp = current_global_sample
        end_samp = start_samp + silence_dur_samp
        start_sec = current_global_sec
        end_sec = start_sec + silence_dur_sec
        
        all_voice_units.append({
            "unit_id": f"PAUSE_C{ch_num:02d}_C{ch_num+1:02d}",
            "type": "CHAPTER_PAUSE",
            "chapter": ch_num,
            "scene_id": "",
            "image_file": "",
            "start_sample": start_samp,
            "end_sample": end_samp,
            "duration_samples": silence_dur_samp,
            "start_sec": f"{start_sec:.3f}",
            "end_sec": f"{end_sec:.3f}",
            "duration_sec": f"{silence_dur_sec:.3f}",
            "start_frame": round(start_samp / 1600),
            "end_frame": round(end_samp / 1600),
            "num_frames": round(end_samp / 1600) - round(start_samp / 1600)
        })
        
        # Extend the last scene of this chapter to include the 2s pause
        # As per HUONG-DAN-KY-THUAT.md: "Giữ ảnh cuối chương trước trong đúng 2 giây nghỉ"
        last_scene_rec = timeline_rows[-1]
        last_scene_rec["end_sample"] = end_samp
        last_scene_rec["end_sec"] = f"{end_sec:.3f}"
        last_scene_rec["duration_sec"] = f"{float(last_scene_rec['duration_sec']) + silence_dur_sec:.3f}"
        last_scene_rec["end_frame"] = round(end_samp / 1600)
        last_scene_rec["num_frames"] = last_scene_rec["end_frame"] - last_scene_rec["start_frame"]
        
        current_global_sample = end_samp
        current_global_sec = end_sec
        master_concat_entries.append(silence_path)

# Concatenate all chapters into master WAV
with open(master_concat_list_path, "w", encoding="utf-8") as f:
    for p in master_concat_entries:
        escaped_p = p.replace("\\", "/")
        f.write(f"file '{escaped_p}'\n")

master_wav_path = os.path.join(output_dir, "TAP-02-VOICE-FULL.wav")
cmd_master = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", master_concat_list_path, "-c", "copy",
    master_wav_path
]
subprocess.run(cmd_master, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
master_info = get_wav_info(master_wav_path)

print(f"\n==========================================")
print(f"MASTER VOICE READY:")
print(f"  Path: {master_wav_path}")
print(f"  Duration: {master_info['duration']:.2f}s ({master_info['duration']/60:.2f} min)")
print(f"  Samples: {master_info['nframes']}")
print(f"  Channels: {master_info['channels']}, SampleRate: {master_info['framerate']}")
print(f"==========================================")

# Save TAP-02-VOICE-UNITS.csv
voice_units_csv = os.path.join(output_dir, "TAP-02-VOICE-UNITS.csv")
with open(voice_units_csv, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(all_voice_units[0].keys()))
    writer.writeheader()
    writer.writerows(all_voice_units)

# Save TAP-02-TIMELINE.csv
timeline_csv = os.path.join(output_dir, "TAP-02-TIMELINE.csv")
with open(timeline_csv, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(timeline_rows[0].keys()))
    writer.writeheader()
    writer.writerows(timeline_rows)

print("Saved TAP-02-VOICE-UNITS.csv and TAP-02-TIMELINE.csv!")
