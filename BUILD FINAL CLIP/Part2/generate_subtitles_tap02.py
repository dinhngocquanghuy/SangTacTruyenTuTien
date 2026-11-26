import os
import csv
import json
import re

base_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02"
work_dir = os.path.join(base_dir, "WORK")
output_dir = os.path.join(base_dir, "OUTPUT")
timeline_csv = os.path.join(output_dir, "TAP-02-TIMELINE.csv")
chapters_json_path = os.path.join(work_dir, "chapters_data.json")

def format_srt_time(secs):
    hrs = int(secs // 3600)
    mins = int((secs % 3600) // 60)
    s = int(secs % 60)
    ms = int(round((secs - int(secs)) * 1000))
    if ms >= 1000:
        ms = 999
    return f"{hrs:02d}:{mins:02d}:{s:02d},{ms:03d}"

def format_vtt_time(secs):
    hrs = int(secs // 3600)
    mins = int((secs % 3600) // 60)
    s = int(secs % 60)
    ms = int(round((secs - int(secs)) * 1000))
    if ms >= 1000:
        ms = 999
    return f"{hrs:02d}:{mins:02d}:{s:02d}.{ms:03d}"

def split_into_subtitle_chunks(text, max_words=16):
    raw_sentences = re.split(r'(?<=[.?!…])\s+(?=[A-ZÀ-Ỹ“"0-9])', text)
    chunks = []
    for s in raw_sentences:
        s = s.strip()
        if not s:
            continue
        words = s.split()
        if len(words) <= max_words:
            chunks.append(s)
        else:
            sub_parts = re.split(r'(?<=[,;:\-–—])\s+', s)
            current_chunk = []
            for part in sub_parts:
                part = part.strip()
                if not part:
                    continue
                part_words = part.split()
                if len(current_chunk) + len(part_words) <= max_words:
                    current_chunk.extend(part_words)
                else:
                    if current_chunk:
                        chunks.append(" ".join(current_chunk))
                    current_chunk = list(part_words)
            if current_chunk:
                chunks.append(" ".join(current_chunk))
    chunks = [c.strip() for c in chunks if c.strip()]
    return chunks if chunks else [text.strip()]

def wrap_subtitle_lines(text, max_line_len=42):
    words = text.split()
    if len(text) <= max_line_len or len(words) <= 7:
        return text
    mid = len(words) // 2
    best_split = mid
    best_diff = 999
    for i in range(max(1, mid - 2), min(len(words), mid + 3)):
        l1 = " ".join(words[:i])
        l2 = " ".join(words[i:])
        diff = abs(len(l1) - len(l2))
        if diff < best_diff and len(l1) <= max_line_len + 10 and len(l2) <= max_line_len + 10:
            best_diff = diff
            best_split = i
    line1 = " ".join(words[:best_split])
    line2 = " ".join(words[best_split:])
    return f"{line1}\n{line2}"

def generate_subtitles():
    with open(timeline_csv, "r", encoding="utf-8-sig") as f:
        scenes = list(csv.DictReader(f))
    with open(chapters_json_path, "r", encoding="utf-8") as f:
        chapters = json.load(f)

    # Build scene text map
    scene_texts = {}
    for ch in chapters:
        ch_num = ch["chapter"]
        ch_title = ch["title"]
        paras = ch["body_paras"]
        ch_scenes = ch["scenes"]
        for s_idx, s in enumerate(ch_scenes):
            start_p = s["body_p_idx"]
            end_p = ch_scenes[s_idx + 1]["body_p_idx"] if s_idx + 1 < len(ch_scenes) else len(paras)
            txt = "\n".join(paras[start_p:end_p]).strip()
            if s_idx == 0:
                txt = f"{ch_title}.\n{txt}"
            scene_texts[s["scene_id"]] = txt

    cues = []
    cue_idx = 1

    for row in scenes:
        sid = row["scene_id"]
        sc_start = float(row["start_sec"])
        sc_end = float(row["end_sec"])
        # If this is the last scene of a chapter with pause, keep cue within speech duration
        sc_dur = float(row["duration_sec"])
        # Check if pause was included in duration
        # In TIMELINE.csv, the speech part is sc_start to sc_start + original_duration
        full_text = scene_texts.get(sid, "")
        chunks = split_into_subtitle_chunks(full_text)
        
        # Word counts
        total_words = sum(len(c.split()) for c in chunks)
        if total_words == 0:
            continue
            
        # Distribute time proportionally across chunks
        cur_time = sc_start
        for c in chunks:
            c_words = len(c.split())
            c_dur = (c_words / total_words) * (sc_dur - 0.2 if sc_dur > 1.0 else sc_dur)
            c_start = cur_time
            c_end = c_start + c_dur
            
            wrapped_text = wrap_subtitle_lines(c)
            cues.append({
                "index": cue_idx,
                "start": c_start,
                "end": c_end,
                "text": wrapped_text
            })
            cue_idx += 1
            cur_time = c_end

    print(f"Generated {len(cues)} subtitle cues.")

    # Write SRT
    srt_path = os.path.join(output_dir, "TONG-MON-BI-TRUY-SAT-TAP-02-FINAL.srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        for c in cues:
            f.write(f"{c['index']}\n")
            f.write(f"{format_srt_time(c['start'])} --> {format_srt_time(c['end'])}\n")
            f.write(f"{c['text']}\n\n")

    # Write VTT
    vtt_path = os.path.join(output_dir, "TONG-MON-BI-TRUY-SAT-TAP-02-FINAL.vtt")
    with open(vtt_path, "w", encoding="utf-8") as f:
        f.write("WEBVTT\n\n")
        for c in cues:
            f.write(f"{c['index']}\n")
            f.write(f"{format_vtt_time(c['start'])} --> {format_vtt_time(c['end'])}\n")
            f.write(f"{c['text']}\n\n")

    print(f"Saved SRT: {srt_path}")
    print(f"Saved VTT: {vtt_path}")

if __name__ == "__main__":
    generate_subtitles()
