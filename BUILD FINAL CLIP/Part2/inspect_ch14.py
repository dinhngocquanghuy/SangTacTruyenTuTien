import json, os

base_dir = r"C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02"
with open(os.path.join(base_dir, "WORK", "chapters_data.json"), "r", encoding="utf-8") as f:
    chapters = json.load(f)

ch14 = chapters[6]
print("Ch 14 total paras:", len(ch14['body_paras']))
for idx, s in enumerate(ch14['scenes']):
    start_p = s['body_p_idx']
    end_p = ch14['scenes'][idx+1]['body_p_idx'] if idx + 1 < len(ch14['scenes']) else len(ch14['body_paras'])
    text = " ".join(ch14['body_paras'][start_p:end_p])
    print(f"{s['scene_id']} ({s['image_file']}): paras [{start_p}:{end_p}] -> {len(text)} chars, {len(text.split())} words, anchor: {s['anchor_text'][:30]}")
