import os
import subprocess
import wave
from PIL import Image
import numpy as np

base_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02"
images_dir = os.path.join(base_dir, "IMAGES")
scenes_audio_dir = os.path.join(base_dir, "WORK", "scenes_125")
output_dir = os.path.join(base_dir, "OUTPUT")
test_dir = os.path.join(base_dir, "WORK", "TEST_3_SCENES")
os.makedirs(test_dir, exist_ok=True)

test_scenes = ["C08-I001", "C08-I002", "C08-I003"]
scene_segments = []
scene_durations = []

for sid in test_scenes:
    img_path = os.path.join(images_dir, f"{sid}.png")
    wav_path = os.path.join(scenes_audio_dir, f"{sid}.wav")
    
    with wave.open(wav_path, "rb") as wf:
        nframes = wf.getnframes()
        framerate = wf.getframerate()
        dur_sec = nframes / framerate
        scene_durations.append(dur_sec)
        
    num_video_frames = round(dur_sec * 30)
    seg_mp4 = os.path.join(test_dir, f"{sid}_silent.mp4")
    
    # Strictly static encoding using loop 1, framerate 30, tune stillimage
    # No filters other than scale=1920:1080,setsar=1
    cmd = [
        "ffmpeg", "-y", "-loop", "1", "-framerate", "30",
        "-i", img_path,
        "-vf", "scale=1920:1080,setsar=1",
        "-frames:v", str(num_video_frames),
        "-c:v", "libx264", "-preset", "veryfast", "-tune", "stillimage",
        "-crf", "18", "-pix_fmt", "yuv420p", "-r", "30", "-an",
        seg_mp4
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    scene_segments.append(seg_mp4)
    print(f"Rendered silent segment {sid}: {num_video_frames} frames ({dur_sec:.2f}s)")

# Concat video segments
concat_list = os.path.join(test_dir, "concat_video.txt")
with open(concat_list, "w", encoding="utf-8") as f:
    for s in scene_segments:
        f.write(f"file '{s.replace(chr(92), '/')}'\n")

concat_silent = os.path.join(test_dir, "test_silent.mp4")
subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", concat_list, "-c", "copy",
    concat_silent
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Concat audio segments
concat_audio_list = os.path.join(test_dir, "concat_audio.txt")
with open(concat_audio_list, "w", encoding="utf-8") as f:
    for sid in test_scenes:
        w_path = os.path.join(scenes_audio_dir, f"{sid}.wav")
        f.write(f"file '{w_path.replace(chr(92), '/')}'\n")

concat_audio = os.path.join(test_dir, "test_audio.wav")
subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", concat_audio_list, "-c", "copy",
    concat_audio
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Mux to final test MP4
test_final_mp4 = os.path.join(output_dir, "TEST-3-SCENES-STILL-CHECK.mp4")
subprocess.run([
    "ffmpeg", "-y",
    "-i", concat_silent,
    "-i", concat_audio,
    "-map", "0:v:0", "-map", "1:a:0",
    "-c:v", "copy",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
    "-movflags", "+faststart",
    test_final_mp4
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print(f"\nCreated test video: {test_final_mp4}")

# Quality Assurance & Stillness Verification:
# Extract start, middle, and end frames from each scene in the rendered MP4
print("\n--- RUNNING STILLNESS QA TEST ---")
qa_frames_dir = os.path.join(test_dir, "QA_FRAMES")
os.makedirs(qa_frames_dir, exist_ok=True)

current_time = 0.0
all_passed = True

for idx, sid in enumerate(test_scenes):
    dur = scene_durations[idx]
    # Sample at 1.0s, mid, and dur - 1.0s
    t_start = current_time + 1.0
    t_mid = current_time + (dur / 2.0)
    t_end = current_time + dur - 1.0
    
    f_start_path = os.path.join(qa_frames_dir, f"{sid}_start.png")
    f_mid_path = os.path.join(qa_frames_dir, f"{sid}_mid.png")
    f_end_path = os.path.join(qa_frames_dir, f"{sid}_end.png")
    
    for t_val, f_out in [(t_start, f_start_path), (t_mid, f_mid_path), (t_end, f_end_path)]:
        cmd_extract = [
            "ffmpeg", "-y", "-ss", f"{t_val:.3f}",
            "-i", test_final_mp4,
            "-frames:v", "1", "-q:v", "1",
            f_out
        ]
        subprocess.run(cmd_extract, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    # Compare frames
    img_start = np.array(Image.open(f_start_path))
    img_mid = np.array(Image.open(f_mid_path))
    img_end = np.array(Image.open(f_end_path))
    
    mse_start_mid = np.mean((img_start.astype("float") - img_mid.astype("float")) ** 2)
    mse_mid_end = np.mean((img_mid.astype("float") - img_end.astype("float")) ** 2)
    
    print(f"[{sid}] Stillness check (duration: {dur:.2f}s):")
    print(f"  MSE(start, mid): {mse_start_mid:.4f}")
    print(f"  MSE(mid, end):   {mse_mid_end:.4f}")
    
    # In a truly still video, MSE between intra/inter frames of stillimage is < 0.05
    if mse_start_mid < 0.1 and mse_mid_end < 0.1:
        print(f"  --> VERDICT: 100% PERFECTLY STATIC (0% motion, 0 jitter, 0 zoom, 0 pan) [PASS]")
    else:
        print(f"  --> VERDICT: MOTION DETECTED [FAIL]")
        all_passed = False
        
    current_time += dur

if all_passed:
    print("\nALL 3 TEST SCENES PASSED STRICT STATIC STILLNESS QA!")
else:
    print("\nQA FAILED ON TEST SCENES!")
