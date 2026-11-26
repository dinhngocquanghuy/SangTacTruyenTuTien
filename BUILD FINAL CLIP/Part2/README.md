# Bộ hướng dẫn agent Tập 2

1. Giải nén bộ hướng dẫn vào thư mục thuận tiện trên máy có repo SangTacTruyenTuTien.
2. Giao agent file PROMPT-GIAO-AGENT.md và HUONG-DAN-KY-THUAT.md; yêu cầu đọc cả hai. File STORYBOARD-SCHEMA.csv chỉ là một dòng mẫu cấu trúc, không phải storyboard 300 ảnh.
3. Agent thực hiện giai đoạn A ngay: voice gTTS 1.25x, script, mốc audio, phụ đề, QA. Chờ chủ dự án cung cấp storyboard + 300 ảnh rồi mới thực hiện giai đoạn B.
4. Không tạo ảnh hoặc video FINAL khi thiếu đầu vào. Không tự commit, push hay upload YouTube.

Bộ này không chứa 300 ảnh, không chứa voice hoặc MP4 và không phải script pipeline đã chạy kiểm chứng. Các đoạn code trong hướng dẫn là mẫu triển khai cho agent. Chuẩn voice/video dựa trên context v6.0 mục 43–46; dữ liệu đầu vào dựa trên ZIP 7 chương FINAL đã kiểm tra. Các quyết định kỹ thuật bổ sung (tách voice độc lập, frame rounding, cache, trạng thái và thư mục) nhằm hỗ trợ dựng sau khi ảnh được giao.
