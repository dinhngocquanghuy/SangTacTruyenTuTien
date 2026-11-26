# NHIỆM VỤ: SẢN XUẤT AUDIO TRUYỆN TU TIÊN — TẬP 2

**Kênh:** Tiên Vực Ký  
**Truyện:** Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát  
**Nội dung:** Chương 8–14 FINAL, được chủ dự án chốt ngày 26/11/2026.  
**Trạng thái đầu vào hình ảnh:** Chưa có bộ 300 ảnh và storyboard hoàn chỉnh. Chủ dự án sẽ cung cấp sau. Không tự tạo ảnh thay thế.

## Mệnh lệnh thực hiện

Đọc toàn bộ `HUONG-DAN-KY-THUAT.md` trước khi chạy. Tự tìm thư mục repository `SangTacTruyenTuTien` trên máy được cấp quyền, kiểm tra đủ bảy file FINAL trong `03-MANUSCRIPTS/approved/`. Không sửa nội dung truyện, không commit/push Git, không ghi đè thành phẩm Tập 1.

**Giai đoạn A — thực hiện ngay:** kiểm tra nguồn, làm sạch văn bản, tạo giọng nữ tiếng Việt bằng Google gTTS (`lang='vi', tld='com', slow=False`), tăng tốc đúng một lần bằng FFmpeg `atempo=1.25`, giữ nguyên cao độ. Chuẩn WAV PCM 16-bit 48 kHz stereo, nghỉ đúng 2 giây giữa mỗi chương. Đọc tiêu đề chương đúng một lần, đọc đủ nguyên văn truyện, không đọc metadata. Tạo audio phân đoạn có mốc câu chính xác, master WAV, phụ đề SRT/VTT, CSV mốc lời kể và báo cáo QA. Có thể hoàn thành voice trước khi có hình. Không tạo MP4 FINAL ở giai đoạn này.

**Giai đoạn B — chỉ thực hiện khi chủ dự án giao storyboard và đủ 300 ảnh:** đối chiếu từng ảnh với câu/đoạn neo trong truyện, lập timeline ảnh theo timestamp audio đã đo, kiểm tra ảnh đúng trình tự và tình tiết. Dùng 300 ảnh tĩnh độc lập, không zoom, pan, rung, animation hay lặp cảnh. Cắt thẳng đúng thời điểm voice chuyển nội dung; không chia đều thời lượng. Giữ ảnh cuối chương trong 2 giây nghỉ nếu cần. Xuất MP4 1920×1080, 16:9, 30 fps, H.264 `-tune stillimage`, AAC 192 kbps 48 kHz stereo, toàn bộ thời lượng master audio. Không dùng thumbnail thay ảnh trong truyện, không chèn intro/outro/CTA, không ép video đúng 2 giờ.

**Điều kiện bàn giao:** đủ nội dung Chương 8–14, giọng đồng nhất Tập 1, không thiếu/lặp câu, không lệch hình/voice, không mất âm cuối, phụ đề đúng thời gian, 300 ảnh có mapping một-một, video giải mã được hết. Khi còn thiếu ảnh phải báo `VOICE_READY_WAITING_IMAGES`, không tuyên bố video hoàn thành. Khi có lỗi phải báo rõ cảnh/chương, sửa và kiểm tra lại trước khi gắn nhãn FINAL. Không tự upload YouTube.

Các quyết định về âm sắc, tốc độ, định dạng, thời gian nghỉ và hình tĩnh là bắt buộc. Các tên thư mục và phương pháp triển khai bên trong có thể thích ứng với máy nhưng phải giữ đầy đủ đầu ra và khả năng truy vết. Không yêu cầu chủ dự án nhắc lại các quy chuẩn này.
