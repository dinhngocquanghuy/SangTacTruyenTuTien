import json
import os
import subprocess

video_path = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\OUTPUT\TONG-MON-BI-TRUY-SAT-TAP-01-FINAL.mp4"
audio_path = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\OUTPUT\TAP-01-VOICE-FULL.wav"
timeline_path = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\OUTPUT\TAP-01-TIMELINE.csv"
script_path = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\OUTPUT\TAP-01-TTS-SCRIPT.txt"

cmd = [
    "ffprobe", "-v", "error",
    "-show_entries", "format=duration,size,bit_rate:stream=index,codec_name,codec_type,width,height,r_frame_rate,sample_rate,channels",
    "-of", "json",
    video_path
]

res = subprocess.check_output(cmd).decode()
data = json.loads(res)
print("=== VIDEO FILE PROBE ===")
for k, v in data.get("format", {}).items():
    print(f"  {k}: {v}")

print("\n=== STREAMS PROBE ===")
for s in data.get("streams", []):
    idx = s.get("index")
    ctype = s.get("codec_type")
    cname = s.get("codec_name")
    w = s.get("width")
    h = s.get("height")
    fps = s.get("r_frame_rate")
    sr = s.get("sample_rate")
    ch = s.get("channels")
    print(f"  Stream {idx}: {ctype} | {cname} | res={w}x{h} | fps={fps} | sr={sr} | channels={ch}")

# Check audio file
cmd_a = [
    "ffprobe", "-v", "error",
    "-show_entries", "format=duration,size:stream=codec_name,sample_rate,channels",
    "-of", "json",
    audio_path
]
res_a = subprocess.check_output(cmd_a).decode()
data_a = json.loads(res_a)
print("\n=== AUDIO MASTER PROBE ===")
print("  Duration:", data_a.get("format", {}).get("duration"))
print("  Size:", data_a.get("format", {}).get("size"))

# Check file sizes
print("\n=== DELIVERABLES EXISTENCE & SIZE ===")
for p in [video_path, audio_path, timeline_path, script_path]:
    exists = os.path.exists(p)
    sz = os.path.getsize(p) if exists else 0
    print(f"  {os.path.basename(p)}: exists={exists}, size={sz:,} bytes ({sz/(1024*1024):.2f} MB)")
