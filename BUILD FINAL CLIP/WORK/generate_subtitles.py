import csv
import json
import os
import re

base_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP"
work_dir = os.path.join(base_dir, "WORK")
output_dir = os.path.join(base_dir, "OUTPUT")
timeline_csv = os.path.join(output_dir, "TAP-01-TIMELINE.csv")
chapters_json_path = os.path.join(work_dir, "chapters_data.json")

with open(timeline_csv, "r", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

with open(chapters_json_path, "r", encoding="utf-8") as f:
    chapters = json.load(f)

# Helper to format seconds to SRT timestamp (HH:MM:SS,mmm)
def format_srt_time(secs):
    hrs = int(secs // 3600)
    mins = int((secs % 3600) // 60)
    s = int(secs % 60)
    ms = int(round((secs - int(secs)) * 1000))
    if ms >= 1000:
        ms = 999
    return f"{hrs:02d}:{mins:02d}:{s:02d},{ms:03d}"

# Helper to format seconds to VTT timestamp (HH:MM:SS.mmm)
def format_vtt_time(secs):
    hrs = int(secs // 3600)
    mins = int((secs % 3600) // 60)
    s = int(secs % 60)
    ms = int(round((secs - int(secs)) * 1000))
    if ms >= 1000:
        ms = 999
    return f"{hrs:02d}:{mins:02d}:{s:02d}.{ms:03d}"

# Clean text from markdown formatting
def clean_sub_text(text):
    text = re.sub(r"\*+([^\*]+)\*+", r"\1", text) # Remove bold/italics
    text = re.sub(r"_+([^_]+)_+", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Split a block of text into natural subtitle sentences / short chunks
def split_into_subtitle_chunks(text, max_words=18):
    # First split by sentence endings
    # Regex preserves punctuation and quotes
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
            # Further split long sentences by comma, semicolon, dash, or dialog
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
    
    # If any chunk is empty, remove
    chunks = [c.strip() for c in chunks if c.strip()]
    if not chunks:
        chunks = [text.strip()]
    return chunks

# Wrap text into 1 or 2 lines for YouTube display (max ~42 chars per line)
def wrap_subtitle_lines(text, max_line_len=45):
    words = text.split()
    if len(text) <= max_line_len or len(words) <= 7:
        return text
    # Try to find a balanced split point near the middle
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

subtitle_entries = []
entry_idx = 1

for ch_num in range(1, 8):
    ch_rows = [r for r in rows if int(r["chapter"]) == ch_num]
    ch_data = chapters[ch_num - 1]
    ch_paras = ch_data["clean_paragraphs"]
    ch_title = ch_data["title"]
    
    for s_idx, r in enumerate(ch_rows):
        start_p = int(r["source_paragraph_index"])
        end_p = int(ch_rows[s_idx + 1]["source_paragraph_index"]) if s_idx + 1 < len(ch_rows) else len(ch_paras)
        para_slice = ch_paras[start_p:end_p]
        text_content = " ".join(para_slice).strip()
        
        if s_idx == 0:
            text_content = f"{ch_title}. {text_content}"
            
        text_content = clean_sub_text(text_content)
        
        glb_start = float(r["global_start_time"])
        glb_end = float(r["global_end_time"])
        dur = glb_end - glb_start
        
        chunks = split_into_subtitle_chunks(text_content)
        
        # Calculate weights based on word count (minimum 1 word weight)
        weights = [max(len(c.split()), 1) for c in chunks]
        total_weight = sum(weights)
        
        curr_t = glb_start
        for i, (chunk, w) in enumerate(zip(chunks, weights)):
            chunk_dur = dur * (w / total_weight)
            c_start = curr_t
            c_end = c_start + chunk_dur
            if i == len(chunks) - 1:
                c_end = glb_end # prevent float drift
            
            wrapped_text = wrap_subtitle_lines(chunk)
            subtitle_entries.append({
                "index": entry_idx,
                "start": c_start,
                "end": c_end,
                "text": wrapped_text,
                "image_id": r["image_id"],
                "chapter": ch_num
            })
            entry_idx += 1
            curr_t = c_end

print(f"Generated {len(subtitle_entries)} subtitle entries across {len(rows)} scenes!")

# Write SRT file
srt_file = os.path.join(output_dir, "TONG-MON-BI-TRUY-SAT-TAP-01-FINAL.srt")
with open(srt_file, "w", encoding="utf-8-sig") as f:
    for sub in subtitle_entries:
        f.write(f"{sub['index']}\n")
        f.write(f"{format_srt_time(sub['start'])} --> {format_srt_time(sub['end'])}\n")
        f.write(f"{sub['text']}\n\n")

print(f"Wrote SRT file: {srt_file} ({os.path.getsize(srt_file)/1024:.1f} KB)")

# Write VTT file
vtt_file = os.path.join(output_dir, "TONG-MON-BI-TRUY-SAT-TAP-01-FINAL.vtt")
with open(vtt_file, "w", encoding="utf-8") as f:
    f.write("WEBVTT\n\n")
    for sub in subtitle_entries:
        f.write(f"{sub['index']}\n")
        f.write(f"{format_vtt_time(sub['start'])} --> {format_vtt_time(sub['end'])}\n")
        f.write(f"{sub['text']}\n\n")

print(f"Wrote VTT file: {vtt_file} ({os.path.getsize(vtt_file)/1024:.1f} KB)")
