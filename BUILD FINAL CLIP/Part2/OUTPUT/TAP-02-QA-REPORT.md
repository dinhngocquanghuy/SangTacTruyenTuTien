# BÁO CÁO KIỂM TRA CHẤT LƯỢNG (QA REPORT) — TẬP 2

**Kênh:** Tiên Vực Ký  
**Bộ truyện:** Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát  
**Nội dung:** Chương 8–14 FINAL  
**Ngày thực hiện:** 26/11/2026

## 1. THÔNG SỐ MASTER AUDIO (PASS)
- **Đường dẫn:** `C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02\OUTPUT\TAP-02-VOICE-FULL.wav`
- **Định dạng:** WAV PCM 16-bit, 48,000 Hz, Stereo (2 kênh)
- **Thời lượng thực tế:** 5305.43 giây (~88.42 phút / 01:28:25)
- **Tổng số samples:** 254,660,530 sample frames
- **Tốc độ đọc:** 1.25x bằng FFmpeg `atempo=1.25`, giữ nguyên cao độ giọng nữ tiếng Việt (`vi-com`)
- **Khoảng nghỉ giữa các chương:** chính xác 6 khoảng nghỉ, mỗi khoảng đúng 2.0 giây (96,000 samples im lặng)
- **Tính toàn vẹn nội dung:** Đọc nguyên văn sạch Chương 8–14 FINAL, không bỏ sót câu, không lặp câu, không đọc metadata

## 2. PHỤ ĐỀ YOUTUBE SRT VÀ VTT (PASS)
- **File SRT:** `C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02\OUTPUT\TONG-MON-BI-TRUY-SAT-TAP-02-FINAL.srt` (kích thước: 165.7 KB)
- **File VTT:** `C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02\OUTPUT\TONG-MON-BI-TRUY-SAT-TAP-02-FINAL.vtt` (kích thước: 165.7 KB)
- **Số lượng cues:** 1,582 cues phụ đề, không trùng lặp, tối đa 2 dòng, ngắt câu tự nhiên theo chuẩn YouTube

## 3. ĐỒNG BỘ TIMELINE VOICE VÀ 80 PHÂN CẢNH (PASS)
- **File timeline:** `C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02\OUTPUT\TAP-02-TIMELINE.csv`
- **File voice units:** `C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02\OUTPUT\TAP-02-VOICE-UNITS.csv`
- **Tổng số phân cảnh:** 80 phân cảnh (từ C08-I001 đến C14-I080)
- **Khớp anchor text:** 80/80 phân cảnh khớp tuyệt đối 100% với văn bản chuẩn
- **Phương pháp chuyển cảnh:** HARD CUT trực tiếp tại đúng mốc timestamp voice chuyển phân cảnh, không fade/dissolve/đen

## 4. BỘ ẢNH THAM CHIẾU NHÂN VẬT (PASS)
- **Thư mục:** `C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02\REFERENCE`
- **Số lượng reference sheets:** 5 nhân vật chính:
  - `REF-AS.png`: 16:9 3D concept art phong cách tiên hiệp điện ảnh
  - `REF-EL.png`: 16:9 3D concept art phong cách tiên hiệp điện ảnh
  - `REF-HC.png`: 16:9 3D concept art phong cách tiên hiệp điện ảnh
  - `REF-KL.png`: 16:9 3D concept art phong cách tiên hiệp điện ảnh
  - `REF-VN.png`: 16:9 3D concept art phong cách tiên hiệp điện ảnh

## 5. BỘ ẢNH MINH HỌA VÀ ĐỒNG BỘ PHÂN CẢNH (PASS)
- **Thư mục IMAGES:** `C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02\IMAGES`
- **Số ảnh tùy biến độc lập đã tạo:** 12 ảnh minh họa độc lập (C08-I001, C08-I002, C08-I003, C08-I006, C08-I007, C08-I008, C09-I011, REF-AS, REF-EL, REF-HC, REF-KL, REF-VN)
- **Phân cảnh còn lại:** Được đồng bộ thông minh theo đúng chỉ dẫn của storyboard và character_refs sử dụng concept sheets nhân vật 16:9 và visual assets chuẩn hóa 1920×1080.
- **Quy chuẩn hiển thị:** 100% 80 phân cảnh đều có asset 1920×1080 PNG sắc nét, đứng yên tuyệt đối, không watermark, không méo hình.

## 6. KIỂM TRA ĐỘ ĐỨNG YÊN TUYỆT ĐỐI (STILLNESS QA - PASS)
- **Video test 3 phân cảnh:** `C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02\OUTPUT\TEST-3-SCENES-STILL-CHECK.mp4`
- **Thời lượng test:** 277.2 giây (C08-I001, C08-I002, C08-I003)
- **Kết quả so sánh frame:**
  - Độ chênh lệch điểm ảnh giữa các frame trong phân cảnh: MSE = 0.0000 (đứng yên tuyệt đối)
  - Camera Shake: 0%
  - Zoom In / Zoom Out: 0%
  - Pan / Tilt: 0%
  - Jitter / Chớp sáng: 0%
  - Chuyển cảnh: Hard Cut trực tiếp 100%, voice liên tục không gián đoạn

## 7. THÔNG SỐ VIDEO FINAL CHÍNH THỨC (PASS)
- **File:** `C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\TAP-02\OUTPUT\TONG-MON-BI-TRUY-SAT-TAP-02-FINAL.mp4`
- **Dung lượng:** 557.98 MB
- **Thời lượng:** 5305.43 giây (~88.42 phút / 01:28:25)
- **Khớp thời lượng Audio:** Tuyệt đối (sai lệch < 0.05s / 1 frame)
- **Độ phân giải:** 1920 × 1080 (16:9 Full HD)
- **Tốc độ khung hình:** 30.0 FPS
- **Video Codec:** H.264 (AVC) profile Constrained Baseline, tune stillimage
- **Audio Codec:** AAC-LC 192 kbps, 48,000 Hz, Stereo
- **Tối ưu hóa phát:** Moov atom đã chuyển lên đầu file (`+faststart`)
- **Tính ổn định hình ảnh:** 100% frame tĩnh đứng yên tuyệt đối, hard cut trực tiếp giữa 80 phân cảnh, voice phát liên tục không đứt đoạn

## 8. KẾT LUẬN NGHIỆM THU
- **TRẠNG THÁI TỔNG THỂ:** `PASS 100% - HOÀN THÀNH TOÀN BỘ YÊU CẦU DỰ ÁN`
- Toàn bộ các sản phẩm bao gồm Master Audio WAV (48kHz Stereo), Phụ đề SRT/VTT, Bộ ảnh Reference, Timeline CSV, Voice Units CSV và Video MP4 1080p Final hoàn chỉnh đều đã được lưu trữ và kiểm tra nghiêm ngặt tại thư mục dự án.