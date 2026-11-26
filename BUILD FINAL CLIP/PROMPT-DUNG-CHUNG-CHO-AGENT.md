# PROMPT TRIỂN KHAI CHO AGENT TẠO ẢNH + DỰNG VIDEO

Nhiệm vụ: Dựng video audiobook YouTube 16:9 theo **toàn bộ Chương 1–7 FINAL** của truyện gốc "Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát". Bạn được cung cấp audio TTS và danh sách storyboard ở file `DANH-SACH-ANH-TAP-01-AGENT.csv`; đọc `STORYBOARD-ANH-TAP-01.md` để nắm quy chuẩn nhân vật.

1. Chỉ lấy sự kiện từ bản FINAL đã cung cấp. Không tự sáng tác cảnh đánh nhau, pháp lực hoặc tình tiết không nằm trong lời kể. Dùng `voice_cue` và `source_paragraph_index` làm anchor để tìm chính xác thời điểm tương ứng sau khi đã có TTS. Không tự chế timestamp.
2. Tạo các key image theo đúng `image_id`, một file PNG/WebP cho một ID, mỗi ảnh khác nội dung shot trước/sau. Lưu ảnh `visuals/C01-I001.png`... và manifest CSV có đường dẫn file.
3. Duy trì nhất quán nhân vật bằng 1 sheet nhân vật cho mỗi người và 1 sheet đạo cụ/địa hình trước khi bắt đầu. Tạ Hành Chu áo vải xanh, đao cũ một lưỡi; Vãn Ninh áo xanh với dấu đỏ cổ tay; Kỷ Thanh La áo đen, kiếm gãy, vai trúng độc; trưởng lão áo xám/hồ lô/cây chổi; A Thạch và rổ chim; Trác Cửu áo xám tro kiếm hẹp.
4. Tạo ảnh phong cách cinematic xianxia illustration, ancient Chinese-inspired mountain sect, expressive faces, subdued fantasy, varied wide / medium / close-up shots, realistic proportions. Avoid random text, logos, watermark, modern objects, nonsensical magical glows. Aspect 16:9.
5. Từ mỗi key image tạo 2–4 visual subshots khác framing/cử động; ưu tiên image-to-video motion có nguyên nhân trong cảnh: nhân vật bước, tay rung, tay áo bay, nước chảy, bếp lửa chập chờn, mưa/sương/bụi, kiếm đao va chạm trong đúng mạch. Không giữ một ảnh đứng yên hoặc chỉ lặp zoom trong thời gian dài; không tự thêm người/vũ khí/quang hiệu vào ảnh.
6. Dựng theo audio TTS liên tục không làm thay đổi câu chữ, tốc độ hay cắt tiếng. Cut theo câu/chuyển hành động; crossfade ngắn khi sang địa điểm/thời gian/hồi tưởng. Không dùng nhạc nền có bản quyền khi chưa xác minh giấy phép.
7. Chèn chữ tiêu đề/tập 1 ở mở đầu riêng; không render text truyện vào ảnh. Sử dụng thumbnail do chủ dự án duyệt ngoài video chính nếu có. Cân nhắc phụ đề nhỏ, đúng chính tả nếu có sub; không làm sub tràn viền.
8. Mỗi khi xuất bản dựng thử, tạo bảng mapping `image_id, start_time, end_time, audio_cue`, nhật ký assets/prompts, nguồn và phiên bản để làm bằng chứng workflow; QA xem kỹ chuyển cảnh giữa cuối chương và đầu chương kế tiếp, không lặp câu cuối/đầu khi ghép audio.

**Quan trọng:** Các sự kiện được duyệt ở bản FINAL là nguồn chuẩn. Danh sách hình là thiết kế sản xuất, có thể thêm bớt cảnh sau khi review, không sửa truyện. Nếu thời lượng audio khác 120 phút, ưu tiên khớp transcript chứ không kéo giãn vô lý.
