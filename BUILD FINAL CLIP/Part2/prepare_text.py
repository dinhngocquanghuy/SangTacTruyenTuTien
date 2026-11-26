import os
import re
import json
import csv

base_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02"
repo_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien"
approved_dir = os.path.join(repo_dir, "03-MANUSCRIPTS", "approved")
csv_path = os.path.join(base_dir, "INPUT", "STORYBOARD-TAP-02.csv")

with open(csv_path, "r", encoding="utf-8-sig") as f:
    scenes = list(csv.DictReader(f))

by_ch = {}
for s in scenes:
    by_ch.setdefault(int(s["chapter"]), []).append(s)

all_tts_script_lines = []
chapters_data = []

for ch_num in range(8, 15):
    fpath = os.path.join(approved_dir, f"CHUONG-{ch_num:04d}-FINAL.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        
    raw_paras = [p.strip() for p in re.split(r"\n\s*\n", content) if p.strip()]
    
    # Title extraction
    title_match = re.search(r"\*\*Chương\s+(\d+):\s*([^\*]+)\*\*", content)
    title_text = f"Chương {ch_num}: {title_match.group(2).strip()}"
    
    # Body extraction and mapping
    start_body = False
    raw_to_body = {}
    body_paras = []
    
    for idx, p in enumerate(raw_paras):
        if p.startswith("---") or p == "---":
            start_body = True
            continue
        if not start_body:
            continue
        if "Hết chương" in p and "FINAL" in p:
            break
        # Skip isolated scene dividers
        if p.strip() in ("***", "---", "* * *"):
            continue
        # Clean markdown symbols but keep text and dialogue
        cleaned = re.sub(r"\*\*(.+?)\*\*", r"\1", p)
        cleaned = re.sub(r"\*(.+?)\*", r"\1", cleaned)
        cleaned = re.sub(r"_(.+?)_", r"\1", cleaned).strip()
        if cleaned:
            raw_to_body[idx] = len(body_paras)
            body_paras.append(cleaned)
            
    ch_text_content = title_text + "\n\n" + "\n\n".join(body_paras)
    
    # Save Cxx.txt
    ch_txt_path = os.path.join(base_dir, "WORK", "TEXT", f"C{ch_num:02d}.txt")
    with open(ch_txt_path, "w", encoding="utf-8") as f:
        f.write(ch_text_content)
        
    all_tts_script_lines.append(ch_text_content)
    
    # Map scenes to paragraphs
    ch_scenes = by_ch[ch_num]
    scene_mappings = []
    
    for s_idx, s in enumerate(ch_scenes):
        raw_idx = int(s["source_paragraph_index"])
        anchor = s["anchor_text"].strip()
        
        # Use raw_to_body first
        b_idx = raw_to_body.get(raw_idx)
        if b_idx is None or (anchor not in body_paras[b_idx]):
            # search with delta near raw_idx
            found = False
            for delta in range(-5, 6):
                cand = raw_to_body.get(raw_idx + delta)
                if cand is not None and anchor in body_paras[cand]:
                    b_idx = cand
                    found = True
                    break
            if not found:
                raise ValueError(f"Anchor not found for {s['scene_id']} around raw {raw_idx}: {anchor}")
                
        scene_mappings.append({
            "scene_id": s["scene_id"],
            "image_file": s["image_file"],
            "anchor_text": anchor,
            "body_p_idx": b_idx
        })
        
    # Verify strict monotonicity
    b_indices = [sm["body_p_idx"] for sm in scene_mappings]
    assert all(b_indices[i] < b_indices[i+1] for i in range(len(b_indices)-1)), f"Not monotonic in Ch {ch_num}: {b_indices}"
    assert b_indices[0] == 0, f"Ch {ch_num} doesn't start at 0: {b_indices[0]}"
    
    chapters_data.append({
        "chapter": ch_num,
        "title": title_text,
        "body_paras": body_paras,
        "scenes": scene_mappings
    })
    print(f"Chương {ch_num}: {len(body_paras)} clean paragraphs, {len(scene_mappings)} scenes mapped. Slices: {b_indices}")

# Save combined TTS script
tts_script_path = os.path.join(base_dir, "OUTPUT", "TAP-02-TTS-SCRIPT.txt")
with open(tts_script_path, "w", encoding="utf-8") as f:
    f.write("\n\n\n========================================\n\n\n".join(all_tts_script_lines))

# Save chapters_data.json
with open(os.path.join(base_dir, "WORK", "chapters_data.json"), "w", encoding="utf-8") as f:
    json.dump(chapters_data, f, ensure_ascii=False, indent=2)

print("Successfully verified and created all text files and chapters_data.json!")
