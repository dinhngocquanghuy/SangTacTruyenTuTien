# CHƯƠNG 2 — NHẬT KÝ REVIEW VÀ PHÊ DUYỆT

- Ngày ghi nhận: 25/11/2026
- Chương: 2 — Người Trong Phong Thư
- Trạng thái: FINAL sau khi người dùng phê duyệt V2
- Nguồn liên tục: `03-MANUSCRIPTS/approved/CHUONG-0001-FINAL.md`

## V1 — Vấn đề người dùng phát hiện

Phản hồi nguyên văn của người dùng:

> chương 2 tôi thấy câu đầu hình như trùng với câu cuối của chương 1 thì phải, làm như vậy thì khi tạo voice sẽ gây ra lặp câu, bạn kiểm tra lại đúng như tôi nói không, nếu đúng thì chỉnh lại, với lại hạn chế commit nhiều lần, chốt 1 chương rồi commit luôn cứ commit theo từng hành động vậy không hợp lý

Kiểm tra thực tế: Câu cuối nội dung truyện Chương 1 và câu đầu V1 Chương 2 đều là:

> Trước khi trời sáng, giao người ra. Nếu không, cả núi cùng chôn.

Đầu Chương 2 V1 còn nhắc lại một phần lời đe dọa trong lời thoại của Tạ Hành Chu.

## V2 — Chỉnh sửa nối chương

- Loại bỏ câu trùng ở đầu Chương 2; bỏ phần lời thoại nhắc lại cụm từ đe dọa.
- Mở đầu V2 bằng cảnh gió đêm, mũi kim trên cột gỗ và phản ứng của những người chứng kiến; giữ sự nối tiếp của cùng cảnh.
- Các phần diễn biến tiếp sau đoạn mở đầu được giữ nguyên từ V1.
- Kiểm tra lại ranh giới Chương 1 FINAL → Chương 2 V2: không còn lặp nguyên văn câu đe dọa.

## Xác nhận phê duyệt

Người dùng xác nhận nguyên văn ngày 25/11/2026:

> chốt chương 2

- **Bản chuẩn:** `03-MANUSCRIPTS/approved/CHUONG-0002-FINAL.md`
- **Bản nguồn đã duyệt:** `03-MANUSCRIPTS/drafts/CHUONG-0002-v2-DRAFT.md`
- Khi tạo FINAL, chỉ cập nhật metadata và dòng nhãn kết chương từ `DRAFT V1` (nhãn bị sót trong file V2) sang `FINAL`. Không thay đổi phần truyện.

## Quy tắc Git áp dụng từ đây

- Tạo và review các bản DRAFT mà không commit riêng từng thao tác.
- Sau khi người dùng chốt FINAL một chương, gộp bản thảo, bản FINAL và bằng chứng review vào **một lần commit/push cho chương đó**.
- Trước khi chốt chương tiếp theo, soát đoạn cuối chương trước với đoạn đầu chương sau để tránh lặp khi ghép audiobook.
