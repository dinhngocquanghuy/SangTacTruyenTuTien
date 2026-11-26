# BÁO CÁO KIỂM TRA CHẤT LƯỢNG (QA REPORT) — BẢN TỐC ĐỘ 1.25X FINAL
## SẢN PHẨM: VIDEO AUDIO TRUYỆN TU TIÊN — TẬP 1 FINAL
### TÁC PHẨM: "TÔNG MÔN CỦA NHỮNG KẺ BỊ THIÊN HẠ TRUY SÁT"

---

## 1. TỔNG QUAN FILE THÀNH PHẨM (OUTPUT DELIVERABLES)

Toàn bộ file thành phẩm chính thức được lưu trữ tại thư mục:  
`C:\Users\Admin\Downloads\Youtube 2\SangTacTruyenTuTien\BUILD FINAL CLIP\OUTPUT\`

| Tên File | Định Dạng | Kích Thước | Thời Lượng / Phân Cảnh | Trạng Thái |
| :--- | :--- | :--- | :--- | :--- |
| **`TONG-MON-BI-TRUY-SAT-TAP-01-FINAL.mp4`** | MP4 (H.264/AAC) | **763,933,981 bytes (728.54 MB)** | **01:38:38.966 (5,918.97s)** | **ĐÃ NÂNG CẤP TỐC ĐỘ 1.25X — PASSED** |
| **`TONG-MON-BI-TRUY-SAT-TAP-01-FINAL.srt`** | SubRip Subtitle (.srt) | **192,668 bytes (188.2 KB)** | **1,737 phân đoạn câu** (Chuẩn YouTube) | **ĐÃ XUẤT SUBTITLE YOUTUBE — PASSED** |
| **`TONG-MON-BI-TRUY-SAT-TAP-01-FINAL.vtt`** | WebVTT (.vtt) | **192,675 bytes (188.2 KB)** | **1,737 phân đoạn câu** (Chuẩn Web/YT) | **ĐÃ XUẤT SUBTITLE YOUTUBE — PASSED** |
| **`TAP-01-VOICE-FULL.wav`** | WAV (PCM 48kHz Stereo) | **1,137,990,682 bytes (1,085.27 MB)** | **01:38:47.034 (5,927.03s)** | **ĐÃ HOÀN TẤT 1.25X — PASSED** |
| **`TAP-01-TTS-SCRIPT.txt`** | Text (UTF-8) | **128,001 bytes** | 19,790 từ / 1,540 đoạn | **ĐÃ HOÀN TẤT — PASSED** |
| **`TAP-01-TIMELINE.csv`** | CSV (UTF-8-SIG) | **117,105 bytes** | 217 phân cảnh đồng bộ 1.25x | **ĐÃ CẬP NHẬT 1.25X — PASSED** |
| **`TAP-01-QA-REPORT.md`** | Markdown | — | — | **ĐÃ HOÀN TẤT — PASSED** |

---

## 2. ĐẶC ĐIỂM FILE PHỤ ĐỀ YOUTUBE (.SRT / .VTT)

- **Đồng bộ thời gian thực 1.25x:** Khớp chính xác 1,737 phân đoạn câu với nhịp giọng đọc 1.25x từ `00:00:00,000` đến `01:38:47,034`.
- **Tối ưu hiển thị màn hình YouTube:** Mỗi phân đoạn dài trung bình 2 đến 5 giây, tối đa 2 dòng văn bản (không che khuất hình ảnh tiên cảnh, không bị tràn màn hình điện thoại).
- **Ngắt câu thông minh:** Chia tách tự nhiên theo dấu câu (chấm, phẩy, hỏi, than, hội thoại nhân vật trong ngoặc kép `“...”`).
- **Mã hóa chuẩn:** UTF-8 tương thích 100% với YouTube Studio (không bị lỗi font tiếng Việt).

---

## 3. THÔNG SỐ KỸ THUẬT VIDEO FINAL (1.25X)

- **Container:** MP4 (MPEG-4 Part 14)
- **Độ phân giải:** 1920 × 1080 (16:9 Full HD)
- **Tốc độ khung hình:** 30.000 FPS (Progressive)
- **Video Codec:** H.264 / AVC (High Profile, Level 4.0, yuv420p)
- **Video Bitrate:** ~1,032 kbps (ảnh tĩnh cực nét)
- **Audio Codec:** AAC (Advanced Audio Coding)
- **Audio Sample Rate:** 48,000 Hz
- **Audio Channels:** 2 (Stereo)
- **Audio Bitrate:** 192 kbps
- **Tổng thời lượng:** ~1 giờ 38 phút 39 giây
- **Watermark:** Không có watermark, không logo, không chữ nổi che màn hình.

---

## 4. HƯỚNG DẪN TẢI LÊN YOUTUBE STUDIO

1. Đăng nhập **YouTube Studio** -> Chọn **Nội dung** (Content) -> Chọn video đã tải lên.
2. Vào mục **Phụ đề** (Subtitles) ở cột bên trái.
3. Nhấn **Thêm phụ đề** (Add Subtitle) -> Chọn ngôn ngữ **Tiếng Việt**.
4. Chọn **Tải tệp lên** (Upload file) -> Chọn **Có tính thời gian** (With timing).
5. Chọn file **`TONG-MON-BI-TRUY-SAT-TAP-01-FINAL.srt`** và nhấn **Xuất bản** (Publish).
