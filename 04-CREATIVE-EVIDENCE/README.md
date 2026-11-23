
# KHO LƯU TRỮ BẰNG CHỨNG SÁNG TÁC

## 1. Mục đích

Thư mục này lưu trữ các bằng chứng gốc trong quá trình phát triển bộ truyện tu tiên nguyên tác.

Mục tiêu là có thể truy xuất quá trình sáng tạo, từ ý tưởng ban đầu đến bản thảo được duyệt và sản phẩm xuất bản trên YouTube.

## 2. Những loại bằng chứng cần lưu

### A. Hội thoại ChatGPT
- Nội dung yêu cầu gốc của chủ dự án.
- Các prompt gửi đến ChatGPT.
- Phản hồi và các bản thảo do ChatGPT tạo.
- Yêu cầu sửa đổi của chủ dự án.
- Kết quả sau từng lần chỉnh sửa.
- Xác nhận FINAL của chủ dự án.

### B. Quá trình biên tập
- Các phiên bản bản thảo.
- Nhận xét và quyết định chỉnh sửa.
- Nội dung được bổ sung hoặc loại bỏ.
- Lý do thay đổi những tình tiết quan trọng.

### C. Quá trình sản xuất
- File văn bản đầu vào cho AI TTS.
- Thông tin công cụ và cấu hình giọng đọc.
- Nhật ký kiểm tra, sửa lỗi audio.
- Tài liệu dự án dựng video.
- Giấy phép sử dụng tài sản bên thứ ba.

## 3. Quy tắc đặt tên

Mỗi phiên làm việc được lưu theo cấu trúc:

YYYY-MM-DD-session-XXX/

Trong đó:
- YYYY-MM-DD: Ngày thực tế diễn ra phiên làm việc.
- XXX: Số thứ tự phiên trong ngày.

Ví dụ:

2026-11-23-session-001/

Bên trong mỗi phiên có thể chứa:

- conversation.md
- prompts.md
- review-notes.md
- evidence-metadata.md

Chỉ tạo những file phù hợp với hoạt động đã thực sự diễn ra.

## 4. Nguyên tắc bảo quản

1. Lưu nội dung gốc trung thực, không chỉnh sửa làm sai lệch lịch sử.
2. Không thay thế bằng chứng gốc bằng bản tóm tắt.
3. Các bản tóm tắt chỉ được dùng để hỗ trợ tra cứu.
4. Liên kết mỗi bằng chứng với mã EV trong EVIDENCE-LOG.md.
5. Commit và push các tài liệu văn bản lên Git.
6. Không đưa API key, mật khẩu, token hoặc thông tin nhạy cảm vào repository.
7. Không lưu file audio/video dung lượng lớn trực tiếp vào Git thông thường.
8. Sao lưu bằng chứng quan trọng ở ít nhất một nơi độc lập với repository.

## 5. Lưu ý

Bằng chứng cần phản ánh chính xác vai trò thực tế của chủ dự án và AI.

Lịch sử Git, hội thoại và tài liệu sản xuất có thể hỗ trợ giải trình nguồn gốc nội dung, nhưng không tự động chứng minh quyền tác giả hoặc bảo đảm YouTube chấp thuận kiếm tiền.
