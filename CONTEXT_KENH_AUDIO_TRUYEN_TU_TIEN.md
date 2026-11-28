# CONTEXT CHUYỂN SESSION — DỰ ÁN KÊNH YOUTUBE AUDIO TRUYỆN TU TIÊN NGUYÊN TÁC

**Phiên bản:** 8.0 (bảo lưu toàn bộ lịch sử v1–v7)  
**Ngày cập nhật:** 29/11/2026, giờ Việt Nam.  
**Tên kênh:** Tiên Vực Ký. **Truyện:** Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát.

**TRẠNG THÁI MỚI NHẤT:** Chương 1–21 đã chốt FINAL. Tập 3 (Ch15–21) đã bàn giao ZIP, người dùng đã giải nén 7 file FINAL vào approved (ảnh Explorer xác nhận), đã tạo 10 ảnh độc lập, người dùng đổi tên 1.png–10.png và đặt tại BUILD FINAL CLIP/Part3; đã giao prompt dựng video sửa đúng yêu cầu mỗi ảnh xuất hiện duy nhất một lần và thumbnail Tập 3. Chưa xác nhận push Ch15–21, render MP4/WAV, QA thực tế, SEO hoặc đăng Tập 3. **Tập 4 dự kiến Chương 22–28, chưa sáng tác.**

**ĐỌC TRƯỚC:** Mục 57–65 (v8.0) ghi tiến độ và quy chuẩn mới nhất; mục 47–56 là lịch sử Tập 2, mục 43–46 voice, mục 36–42 continuity. Quy tắc 10 ảnh mỗi ảnh một lần của Tập 3 ghi đè quy tắc 80/217/300 ảnh khi sản xuất Tập 3; không tự mặc định số ảnh Tập 4 nếu chưa giao.

**HANDOFF:** Kiểm tra repo `dinhngocquanghuy/SangTacTruyenTuTien`, branch `main`; đọc nguyên văn Ch21 FINAL và các chương liên quan Ch15–20, tra Ch1–14 theo phục bút. Nếu thiếu trên GitHub, dùng ZIP FINAL hoặc bản nguyên văn dự phòng tại mục 65. Khi user giao viết Tập 4, viết Ch22–28 DRAFT liền mạch, không ngoặc kép, không lặp câu nối chương, chỉ xuất FINAL khi được duyệt. Nếu chỉ đọc context thì báo kết quả và chờ yêu cầu. Không tự commit/push/upload. Không suy diễn trạng thái sản xuất.

---

## 1. MỤC TIÊU CHÍNH

Người dùng muốn xây dựng **một kênh YouTube mới** chuyên phát hành **truyện tu tiên/tiên hiệp dài kỳ bằng tiếng Việt dưới dạng audiobook** (giọng đọc AI), hướng đến:

1. Thu hút người nghe và phát triển lượt xem, giờ xem, người đăng ký dài hạn.
2. Đăng audio dài khoảng **1–3 giờ/video**, có thể chia thành nhiều tập liên tục và playlist.
3. **Đủ điều kiện tham gia YouTube Partner Program (YPP) và thu doanh thu quảng cáo** theo cách bền vững.
4. Sở hữu/phát triển một **bộ truyện tu tiên nguyên tác hoàn toàn mới**, thay vì lấy truyện Trung Quốc có sẵn rồi dịch lại, để giảm rủi ro quyền tác giả và xây dựng tài sản nội dung riêng.
5. Có hồ sơ đáng tin cậy giải thích quá trình sáng tạo và sản xuất khi YouTube kiểm duyệt hoặc khi cần kháng nghị YPP.

**Ưu tiên:** Nội dung hấp dẫn, có khả năng giữ chân người nghe, logic xuyên suốt hàng nghìn chương; quy trình đủ khả thi để sản xuất định kỳ; không chỉ chạy theo số lượng tập.

## 2. BỐI CẢNH RA QUYẾT ĐỊNH

- Ban đầu người dùng tìm hiểu việc lấy trailer phim Marvel/DC ghép lại để đăng lên kênh riêng và kiếm tiền. Ví dụ cụ thể người dùng đưa là video YouTube: https://youtu.be/7bU4ojt7WGU .
- Người dùng quan tâm mô hình kênh khác có nhiều lượt xem dù dùng nội dung có bản quyền, và yêu cầu **phân tích khách quan**, không phóng đại rủi ro hay dùng cảnh báo để ngăn việc thử nghiệm.
- Người dùng tiếp tục quan tâm các kênh dịch truyện Trung Quốc sang tiếng Việt rồi dùng AI đọc dài 1–3 giờ/tập.
- Sau khi trao đổi về quyền chuyển ngữ truyện có sẵn và rủi ro YPP đối với nội dung đọc lại, người dùng hỏi khả năng **nhờ ChatGPT hỗ trợ viết một bộ truyện tu tiên hoàn toàn mới, dài kỳ**.
- Assistant xác nhận có thể hỗ trợ xây dựng thế giới, nhân vật, cốt truyện, sáng tác chương, kiểm tra tính nhất quán, hỗ trợ audio, đồng thời giải thích giới hạn của việc ghi nhớ nội dung cực dài.
- Người dùng tiếp tục hỏi **làm sao chứng minh với nhân viên YouTube rằng đây là nội dung tự tạo**. Đã thảo luận về lịch sử ý tưởng, bản thảo, chỉnh sửa, project TTS/video và video kháng nghị YPP.
- **Tiến độ sau khi lập file v1.0:** Đã thiết lập repo Git và kho evidence; đã thử và loại các tiền đề không hấp dẫn; đã chọn một hướng truyện để phát triển; đã thống nhất mẫu thử văn phong kể truyện thực sự tương đối ổn. Chi tiết chính xác tại mục 12–17.

**Không được nhầm:** Phương án truyện dịch là ý tưởng đã khảo sát, **không phải phương án hiện tại đã chọn**. Phương án làm việc hiện tại là **truyện tu tiên nguyên tác mới với AI hỗ trợ sáng tác, giọng đọc AI**.

## 3. NHỮNG GÌ ĐÃ CHỐT VÀ CHƯA CHỐT

### Đã xác định
- Nền tảng phân phối chính: **YouTube**.
- Định dạng chính: **Audio truyện tiên hiệp/tu tiên tiếng Việt dài kỳ**.
- Nội dung dự kiến: **Truyện nguyên tác mới**, ChatGPT hỗ trợ toàn bộ chuỗi từ ý tưởng đến bản thảo/chỉnh sửa.
- Công nghệ đọc: **AI text-to-speech (TTS)**, cần giọng rõ, tự nhiên, nhất quán qua nhiều tập.
- Video mục tiêu: **1–3 giờ/video** (không bắt buộc mỗi video tương ứng đúng một số chương cố định).
- Mục tiêu kinh doanh: **Phát triển kênh và kiếm tiền quảng cáo từ YPP**.
- Cần lưu bằng chứng quá trình tạo nội dung **từ đầu**, không đợi khi gặp vấn đề YPP.
- Đã bắt đầu **định hướng sáng tác** và thử văn phong minh họa; chưa có chương chính thức. Session sau nên tiếp tục **phát triển premise, nhân vật và Story Bible**, từng bước một, theo mục 16.

### Chưa được chốt — không tự giả định là quyết định của người dùng
- Tên kênh, thương hiệu, nhận diện hình ảnh, **tên bộ truyện chính thức** (đã có tên làm việc *Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát*, chưa FINAL).
- Tiểu thể loại chi tiết: phàm nhân lưu, hệ thống, trọng sinh, v.v. (đã có yêu cầu về hài hước, tu luyện, chiến đấu, kỳ ngộ, phiêu lưu, tình cảm đa đạo lữ, nhưng chưa chốt cơ chế cụ thể).
- Tệp khán giả, tuổi, phong cách ngôn ngữ, mức độ bạo lực/tình cảm.
- Bối cảnh, tuyến nhân vật, nam/nữ chính, mức độ độc đáo và nhịp truyện.
- Số chương cuối cùng, độ dài từng chương, số phần và lịch phát hành.
- Giọng đọc AI, nền tảng TTS, công cụ dựng, cách dùng nhạc/hình.
- Ngân sách, lịch sản xuất, có làm trên Windows/Linux hay cloud không.
- Ngày mở kênh, cách đặt lịch upload, kế hoạch marketing cụ thể.
- Bất cứ tuyên bố nào rằng YouTube đã duyệt kiếm tiền, hay tác phẩm đã được đăng ký bản quyền.

### Quy mô tham khảo, KHÔNG PHẢI cam kết
- Có thể thiết kế bộ truyện hướng tới khoảng **2.000 chương** hoặc nhiều hơn.
- Ví dụ **2.500 từ/chương** dẫn đến khoảng **5 triệu từ** nếu có 2.000 chương; cần thống nhất cách đếm từ/chữ tiếng Việt trước khi ước lượng audio.
- Chất lượng và tính nhất quán ưu tiên hơn số chương lớn ngay lập tức.

## 4. CÁCH LÀM VIỆC VỚI NGƯỜI DÙNG

1. Trả lời **khách quan, dựa trên bằng chứng**; phân biệt điều khoản chính thức, rủi ro có khả năng, và suy đoán. Không mặc định kênh của người khác đang vi phạm chỉ vì họ dùng AI hay đăng trailer.
2. Đưa ra quyết định và phương án triển khai **cụ thể, có thể thực hiện**, tránh chỉ khuyên chung chung.
3. **Không bắt đầu viết truyện hoặc tạo ảnh/audio khi người dùng chưa yêu cầu.** Trong các lượt trước, người dùng mới hỏi tính khả thi và cách chứng minh; hiện chỉ yêu cầu file context.
4. Khi được giao việc sáng tác, cần viết truyện mạch lạc, hấp dẫn, phát triển nhân vật và phục bút; tránh câu rời rạc, lặp công thức, kéo dài vô nghĩa.
5. Nếu đã có bản truyện hoặc kế hoạch được người dùng đánh dấu FINAL/CHỐT, coi đó là **nguồn chuẩn**, không tự sửa nội dung không được yêu cầu.
6. Theo dõi phiên bản và checklist để session mới không mất tiến độ. Không tuyên bố có thể nhớ chính xác hàng triệu từ nếu không có tệp lưu trữ và tái nạp.
7. Nội dung thương mại và bản quyền: không đảm bảo tuyệt đối tính độc nhất hay việc YPP phê duyệt; kiểm tra quyền sử dụng nhạc, ảnh, âm thanh/TTS và các tài sản bên thứ ba.

## 5. KIẾN TRÚC DỰ ÁN ĐỀ XUẤT

```text
TU-TIEN-ORIGINAL/
├── 00-project-context/
│   ├── CONTEXT_KENH_AUDIO_TRUYEN_TU_TIEN.md
│   ├── decisions-log.md
│   ├── roadmap.md
│   └── next-session-handoff.md
├── 01-story-bible/
│   ├── premise-and-themes.md
│   ├── worldbuilding.md
│   ├── cultivation-system.md
│   ├── sects-and-factions.md
│   └── glossary-and-naming-rules.md
├── 02-characters/
│   ├── character-index.md
│   └── character-arcs.md
├── 03-outlines/
│   ├── master-outline.md
│   ├── volume-outline.md
│   └── arc-outline.md
├── 04-manuscripts/
│   ├── drafts/
│   └── approved/
├── 05-continuity/
│   ├── timeline.md
│   ├── power-and-items-ledger.md
│   ├── foreshadowing-ledger.md
│   └── chapter-summaries.md
├── 06-audio/
│   ├── tts-input/
│   ├── voice-settings/
│   ├── rendered-audio/
│   └── pronunciation-and-qa.md
├── 07-video/
│   ├── project-files/
│   ├── assets/
│   ├── thumbnails/
│   └── exports/
├── 08-publishing/
│   ├── titles-descriptions-tags.md
│   ├── playlists-and-schedule.md
│   └── analytics.md
└── 09-rights-and-ypp-evidence/
    ├── asset-licenses/
    ├── ai-and-editing-process/
    ├── version-history/
    └── ypp-appeal-materials/
```

Đây là **cấu trúc gợi ý**, chưa khẳng định các file/thư mục đã tồn tại. Có thể áp dụng Git để lưu lịch sử bản thảo và ngày cập nhật; nếu dùng Google Docs/Drive thì giữ lịch sử phiên bản gốc.

## 6. QUY TRÌNH SÁNG TÁC VÀ SẢN XUẤT DỰ KIẾN

### Giai đoạn A — Lên nền tảng sáng tạo
1. Định nghĩa người nghe mục tiêu, điểm khác biệt, chất truyện, nhịp kể.
2. Đề xuất vài premise mới để người dùng chọn (khi được yêu cầu).
3. Chốt tên tạm, logline, xung đột trung tâm, bí mật dài hạn và kết thúc lớn.
4. Soạn Story Bible: quy tắc thế giới, hệ thống cảnh giới, công pháp, tài nguyên, giới hạn sức mạnh, tính hợp lý.
5. Xây dựng nhân vật chính/phụ/phản diện, động lực và phát triển tâm lý.
6. Lập khung đa quyển và outline nhóm chương đầu trước khi viết chi tiết.

### Giai đoạn B — Viết thử và kiểm định
1. Viết **pilot** (ví dụ 3–5 chương, số lượng do người dùng quyết định).
2. Kiểm tra tính hấp dẫn của mở truyện, tính tự nhiên của thoại, logic hành động, hạn chế sáo mòn/giống quá mức các truyện nổi tiếng.
3. Đọc thử bằng TTS để kiểm tra âm đọc tên riêng, câu quá dài, nhịp kể.
4. Nhận chỉnh sửa và **chốt mẫu văn phong** trước khi viết hàng chục chương.
5. Mỗi chương đều cập nhật nhân vật, cảnh giới, sự kiện, vật phẩm, bí mật và recap phục vụ session sau.

### Giai đoạn C — Sản xuất audio/video
1. Chọn công cụ TTS được phép sử dụng thương mại; ghi lại điều khoản gói dịch vụ tại thời điểm dùng.
2. Thiết lập một giọng kể ổn định; từ điển phát âm tên nhân vật, địa danh, cảnh giới.
3. Chia truyện thành các tập dài 1–3 giờ theo nhịp câu chuyện, không cắt ngang thiếu hợp lý.
4. Dùng hình/nhạc có quyền sử dụng phù hợp, hoặc sản xuất nội dung hình riêng.
5. Kiểm tra QA: phát âm, câu thiếu/lặp, lệch nội dung, âm lượng, thời lượng, lỗi hình/sub.
6. Lưu bản thảo đầu vào, phiên bản audio, project dựng và file xuất.

### Giai đoạn D — Xuất bản và tăng trưởng
1. Thiết lập branding kênh, ảnh đại diện/cover, playlist, giới thiệu minh bạch về truyện nguyên tác được AI hỗ trợ sản xuất.
2. Xuất bản đều đặn theo năng lực thực tế; dùng title/thumbnail rõ tình tiết, tránh gây hiểu nhầm.
3. Theo dõi CTR, retention, thời gian nghe trung bình, giờ xem, nguồn traffic, returning viewers, đăng ký/tập.
4. Cải thiện dựa trên số liệu, nhưng giữ thống nhất mạch truyện.
5. Đánh giá YPP trước và sau khi đạt ngưỡng theo chính sách mới nhất tại thời điểm nộp.

## 7. BỘ BẰNG CHỨNG TÍNH NGUYÊN BẢN CHO YOUTUBE

**Chú ý quan trọng:** Đây là hồ sơ thực hành được đề xuất để giải trình nguồn gốc và đóng góp sáng tạo, **không phải danh sách tài liệu YouTube bắt buộc nộp trong đơn YPP thông thường**.

Mỗi tập/chương nên giữ:
- Đề bài/ý tưởng và quyết định sáng tạo của người dùng.
- Prompt và lịch sử trao đổi với ChatGPT có liên quan; ghi rõ AI hỗ trợ phần nào.
- Bản nháp, phản hồi sửa, bản được duyệt, lịch sử phiên bản và ngày giờ thực tế.
- Outline và các ghi chú logic nhất quán giữa các chương.
- Bản text dùng cho TTS, log chỉnh phát âm/nhịp đọc, file audio nguồn.
- Project video có timeline biên tập, hình, âm thanh, phụ đề và ảnh bìa.
- Giấy phép tài nguyên bên ngoài (nhạc, ảnh, voice/TTS theo điều khoản thương mại).
- Bản xuất cuối cùng và URL video tương ứng sau khi đăng.

**YPP:** YouTube xem xét chất lượng/tính nguyên bản của **toàn kênh**, không chỉ việc truyện do ai sở hữu. Nội dung đọc lại hàng loạt theo mẫu lặp lại có thể bị xem là nội dung không đủ tính xác thực/giá trị, ngay cả khi bản thảo có nguồn gốc riêng. Quy trình phải cho thấy chủ kênh có định hướng sáng tạo, duyệt và biên tập thực chất, đồng thời chất lượng sản phẩm thể hiện điều đó.

**Nếu phải kháng nghị bằng video:** Kiểm tra hướng dẫn chính thức tại thời điểm kháng nghị. Quy trình đã thảo luận là quay màn hình (không cần lộ thông tin nhạy cảm) minh họa từ story bible → draft → sửa → TTS → project dựng → các tập đã xuất bản. Những điều kiện như độ dài, trạng thái hiển thị, hạn nộp có thể thay đổi; không coi tài liệu này là thay thế chính sách YouTube mới nhất.

Nguồn chính thức tham khảo, cần kiểm tra lại khi hành động:
- YouTube Channel Monetization Policies: https://support.google.com/youtube/answer/1311392
- YPP overview / eligibility: https://support.google.com/youtube/answer/72851
- YouTube copyright: https://support.google.com/youtube/answer/2797466
- Copyright strikes: https://support.google.com/youtube/answer/2814000
- YouTube appeal by video: https://support.google.com/youtube/answer/9564590

## 8. CÁC RỦI RO CẦN THEO DÕI (KHÔNG ĐỒNG NGHĨA DỰ ÁN KHÔNG KHẢ THI)

1. **Tính sáng tạo:** AI có thể tạo motif quen thuộc, văn phong lặp hoặc tình tiết tương đồng; cần biên tập, kiểm tra và phát triển khác biệt.
2. **Tính nhất quán:** Truyện nhiều chương dễ quên quy tắc, cảnh giới và chi tiết; phải cập nhật tài liệu chuẩn sau mỗi nhóm chương.
3. **Kiếm tiền:** Truyện nguyên tác/AI đọc không tự động đảm bảo được YPP phê duyệt; YouTube xem xét toàn bộ giá trị nội dung và sự lặp lại.
4. **Quyền sử dụng tài nguyên:** Quyền tác phẩm truyện và giấy phép nhạc/hình/TTS là các vấn đề riêng biệt.
5. **Bằng chứng:** Lịch sử chat hay timestamp file chỉ giúp chứng minh quy trình; không phải chứng nhận độc quyền bản quyền hoặc giấy đảm bảo bật kiếm tiền.
6. **Vận hành:** Không nên cam kết đăng hàng ngày hoặc sản xuất hàng nghìn chương trước khi kiểm chứng chất lượng pilot và chi phí.

## 9. LỘ TRÌNH HÀNH ĐỘNG GỢI Ý CHO SESSION KẾ TIẾP

**Lưu ý lịch sử:** Các checkbox dưới đây là kế hoạch sơ bộ từ v1.0 ngày 22/11/2026; một số bước đã được thực hiện sau đó. **Để tiếp tục từ trạng thái mới nhất, xem mục 16.**

Ưu tiên tuần tự:

- [ ] Đề xuất và lựa chọn định vị kênh; đối tượng nghe, phong cách và điểm khác biệt.
- [ ] Đưa ra 3–5 ý tưởng truyện nguyên tác có hook mạnh, tiềm năng dài kỳ; so sánh có lý do.
- [ ] Chọn một premise, phác thảo xung đột lớn và hướng kết thúc.
- [ ] Chốt các luật hệ thống tu luyện và nhân vật chính để tạo Story Bible v1.
- [ ] Lập outline quyển 1 / 30–50 chương đầu ở mức tổng quan.
- [ ] Viết thử vài chương khi người dùng đồng ý; chỉnh đến khi chốt phong cách.
- [ ] Chạy thử TTS và đo thời lượng/ngân sách/tốc độ sản xuất.
- [ ] Chuẩn hóa hệ thống lưu file, revision, nhật ký bằng chứng YPP.
- [ ] Xây bộ nhận diện, template audiobook và lịch ra mắt sau khi có pilot đạt chất lượng.

**Không bắt đầu tự động bất kỳ bước sáng tác nào chỉ vì đã đọc file này.** Khi người dùng yêu cầu thực hiện một bước, triển khai ngay trong phạm vi được giao, không hỏi lại những điều đã có ở file.

## 10. PROMPT ĐỂ DÁN VÀO SESSION CHATGPT MỚI

> Hãy đọc **toàn bộ file context**, đặc biệt mục 12–17 cập nhật ngày 23/11/2026 (ưu tiên thông tin mới hơn thay cho tình trạng cũ trong mục 1–11). Tôi đã push xong bước 7 vào repo Git `SangTacTruyenTuTien`. Hướng truyện đang phát triển là **Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát** (chưa FINAL). Nam chính hài hước, nhân hậu, thông minh sắc bén nhưng giả cà lơ phất phơ; truyện cần tu luyện, chiến đấu, kỳ ngộ, phiêu lưu và nhiều đạo lữ có xây dựng tình cảm. Tôi đã nhận xét một đoạn mẫu **văn xuôi có cảnh và đối thoại** là "ổn"; tránh dùng văn phong synopsis/tóm tắt bìa sách để viết chương. Hãy chỉ dẫn **mỗi lần một bước**, giúp tôi lưu Git/evidence, và **không tự chốt FINAL, không viết chương chính thức, không tạo audio/ảnh/video khi tôi chưa giao**.

## 11. MẪU HANDOFF SAU MỖI SESSION

Cuối mỗi buổi làm việc có tiến độ, cập nhật một tệp `next-session-handoff.md` với:

```markdown
# HANDOFF — YYYY-MM-DD
## Quyết định đã chốt (nguồn chuẩn / phiên bản)
## File được tạo hoặc cập nhật
## Tình trạng chương/arc đã hoàn thành
## Nhân vật, cảnh giới, vật phẩm và phục bút mới
## Những điều chưa giải quyết / cần kiểm chứng
## Bước hành động tiếp theo được người dùng yêu cầu
## Những điều tuyệt đối không tự thay đổi
```

Nếu một phần của file context này mâu thuẫn với **quyết định mới hơn do người dùng xác nhận**, ưu tiên quyết định mới nhất, cập nhật decisions-log và context.

---

**Tóm tắt một câu để bắt đầu mọi session (cập nhật 23/11/2026):** Xây kênh YouTube audio truyện tu tiên nguyên tác; repo `SangTacTruyenTuTien` đã push bước 1–7; đã chọn hướng truyện *Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát* để phát triển (chưa FINAL), đã thử đoạn mở đầu có đối thoại/hành động và người dùng nói "ổn"; cần tiếp tục phát triển premise, nhân vật, văn phong, Story Bible, đồng thời lưu bằng chứng Git — **chưa có chương FINAL/audio/video**.


---

## 12. CẬP NHẬT QUAN TRỌNG NGÀY 23/11/2026 — ƯU TIÊN KHI MỞ SESSION MỚI

Đây là **trạng thái mới nhất**, thay thế các khẳng định lỗi thời ở mục 1–11 nếu có mâu thuẫn.

### 12.1. Nền tảng lưu trữ đã thiết lập

- Người dùng **tự tạo Git repository `SangTacTruyenTuTien` và clone về thư mục cùng tên trên máy**.
- Người dùng đã xác nhận **đã commit và push thành công từng bước 1 đến bước 7**. Trợ lý không trực tiếp kiểm tra Git remote; đây là thông tin do người dùng xác nhận.
- Repository nên là **private**; không được suy diễn rằng private đã được kiểm tra.
- Lưu lịch sử trung thực: ý tưởng, prompt, bản nháp, phản hồi review, phiên bản sửa, FINAL do người dùng duyệt, tài liệu TTS, dữ liệu dựng, giấy phép tài nguyên và URL xuất bản. Nhật ký và Git **không** bảo đảm tự động có quyền tác giả hoặc được YouTube YPP duyệt.

### 12.2. Các bước đã hoàn thành và đường dẫn file trong repo

| Bước | File/path trong `SangTacTruyenTuTien/` | Trạng thái |
|---|---|---|
| 1 | `README.md` | Đã push — giới thiệu mục tiêu, nguyên tắc dự án |
| 2 | `DECISIONS.md` | Đã push — nhật ký quyết định; `DEC-0001` khởi tạo dự án |
| 3 | `EVIDENCE-LOG.md` | Đã push — nhật ký bằng chứng, mẫu mã `EV-XXXX` |
| 4 | `04-CREATIVE-EVIDENCE/README.md` | Đã push — quy ước kho lưu prompt, chat, review, nguồn sản xuất |
| 5 | `01-STORY-BIBLE/CREATIVE-BRIEF.md` | Đã push — định hướng cơ sở, nhiều mục CHƯA CHỐT |
| 6 | `01-STORY-BIBLE/PREMISE-CANDIDATES-v1.md` | Đã push — 4 ý tưởng đầu tiên; không có ý tưởng nào được FINAL |
| 7 | `01-STORY-BIBLE/CHARACTER-DIRECTION-v1.md` | Đã push — nguyên văn định hướng nam chính, các phương án A/B/C trước đó (DRAFT) |

**Quan trọng:** Không tạo lại các file trên như thể chúng chưa tồn tại. Có thể yêu cầu người dùng cung cấp phiên bản repo mới nhất khi cần chỉnh nội dung chính xác. Bất kỳ thay đổi trong phiên này cần hướng dẫn người dùng lưu file/commit/push **từng bước một**, không dồn nhiều bước trong một lần.

### 12.3. Tiến độ evidence còn thiếu

- Mặc dù đã có `EVIDENCE-LOG.md` và `04-CREATIVE-EVIDENCE/README.md`, **chưa có xác nhận rằng hội thoại ChatGPT gốc, các review hoặc phiên bản đề xuất đã được xuất và lưu đầy đủ vào kho bằng chứng**.
- Lần tới nên ghi nhận thật rằng các nhóm đề xuất trước đã bị từ chối, hướng truyện mới được chọn để *phát triển* và đoạn thử văn phong được đánh giá ổn; **không tự tạo ngày commit hay mã EV đã tồn tại nếu chưa kiểm tra**.
- Cần bảo tồn nguyên văn yêu cầu người dùng và nhận xét người dùng, không chỉ lời tóm tắt của trợ lý.

## 13. HƯỚNG TRUYỆN HIỆN TẠI — ĐÃ ĐƯỢC NGƯỜI DÙNG CHỌN ĐỂ PHÁT TRIỂN, CHƯA FINAL

### 13.1. Đề xuất cũ bị từ chối

Người dùng đánh giá các ý tưởng đầu tiên (người gác mộ thiên đạo, phàm nhân giữ sổ nợ, linh điền trên lưng cự thú, kẻ bị tông môn xóa tên), cũng như ba phương án kết hợp A/B/C tiếp theo là **không hấp dẫn / nghe chán**. Không tự đưa lại những ý tưởng này làm lựa chọn chính.

### 13.2. Tên làm việc và premise được người dùng chủ động chọn

**Tên làm việc (chưa chốt tên chính thức):** `Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát`.

**Tiền đề được người dùng trích lại và chọn để phát triển:**

> Một thiếu niên vô công rồi nghề vô tình gia nhập một tông môn sắp giải tán. Hắn tưởng mình tìm được chỗ ăn không ngồi rồi, nhưng nhanh chóng phát hiện các thành viên đều che giấu thân phận kinh thiên động địa.
>
> Đại sư tỷ là ma nữ bị chính đạo săn đuổi. Nhị sư tỷ từng là thiên tài luyện đan bị vu oan. Một vị trưởng lão là cường giả mất hết tu vi. Còn tông chủ đang giữ bí mật có thể khiến nhiều tiên môn liên thủ tiêu diệt họ.
>
> Trong khi mọi người xem hắn là tên đệ tử ham ăn lười làm, hắn âm thầm giải quyết những âm mưu hướng về tông môn.
>
> Sức hút: Một tập thể nhân vật đáng nhớ, tình huynh đệ, những mỹ nhân mạnh mẽ, hài hước đời thường xen lẫn các trận chiến sinh tử.

**Không được nhầm:** Người dùng *chọn hướng này để tiếp tục phát triển*, nhưng đã nói rõ **"chưa chốt FINAL"**. Chi tiết tên riêng, bí mật tông môn, nhân vật, cảnh giới, hệ thống công pháp, tuyến tình cảm vẫn là DRAFT/chưa quyết định. Không mặc định các đề xuất phụ của trợ lý đã được phê duyệt.

### 13.3. Hình tượng nam chính do người dùng yêu cầu

Nguyên văn nhận xét của người dùng trước đó:

> Tôi muốn làm một nhân vật chính hài hước, nhưng có tấm lòng nhân hậu, che giấu sự sắc bén và thông minh của mình dưới lớp một tên cà lơ phất phơ, trong hành trình tu tiên ngoài việc đề thăng cảnh giới còn tiếp xúc và kết làm đạo lữ với nhiều mỹ nữ xinh đẹp

Nhận xét bổ sung tiếp theo của người dùng:

> Tu luyện, chiến đấu, kỳ ngộ, trở thành cường giả
> Phiêu lưu, mỹ nữ, tình cảm, nhiều đạo lữ

Các yếu tố **phải giữ làm định hướng**: hài hước và phóng khoáng; lòng nhân hậu, trọng tình; thông minh/sắc bén nhưng che giấu dưới vẻ cà lơ phất phơ; tu luyện và đột phá cảnh giới thật; chiến đấu, kỳ ngộ, bí cảnh/phiêu lưu; nhiều nữ nhân vật đẹp và nhiều đạo lữ có tiến triển tình cảm. Tránh nhân vật chính chỉ luôn giả vờ vô dụng mà không có hành động hay tu luyện thực tế. Các nữ nhân vật nên có ý chí, động cơ và tuyến phát triển riêng (đây là **đề xuất biên tập** được nêu trong trao đổi, chưa được chốt riêng).

### 13.4. Các đề xuất của trợ lý đã nêu, vẫn CHƯA PHÊ DUYỆT

- Mở đầu chàng trai vào tông môn đổ nát vì bảng tuyển đệ tử "không thu phí, bao ăn, bao ở".
- Có đại sư tỷ bị truy sát, nhị sư tỷ luyện đan bị oan, trưởng lão mất tu vi và tông chủ giữ bí mật — **khung này thuộc tiền đề người dùng đã chọn**; nhưng nhân thân, động cơ, quan hệ, tên gọi và diễn biến vẫn chưa chốt.
- Các phương án bí mật tông môn A (bị oan khuất), B (người thật sự có quá khứ nguy hiểm), C (tông chủ có kế hoạch lớn) và gợi ý kết hợp B+C chỉ là **đề xuất trợ lý**, chưa được người dùng lựa chọn.
- Các đề xuất về giai đoạn mở rộng thế giới, tuyến đạo lữ, thứ tự tuyến tu luyện và nhân vật khác vẫn DRAFT.

## 14. BÀI HỌC QUAN TRỌNG VỀ VĂN PHONG — NGƯỜI DÙNG ĐÃ PHẢN HỒI

### 14.1. Điều người dùng KHÔNG thích

Sau khi trợ lý viết phần "mở đầu" thực chất là một đoạn giới thiệu/tóm tắt, người dùng nhận xét nguyên văn:

> bạn mở đầu như thể giới thiệu truyện mà không phải đang sáng tác truyện thật sự vậy, cái văn phóng đó của bạn thường chỉ dùng để tóm tắt bối cảnh truyện in ở bìa sách thôi

**Yêu cầu bắt buộc khi bắt đầu viết chương:** Không dùng văn phong synopsis, lời quảng cáo bìa sau hay tóm tắt toàn bộ bối cảnh thay cho một chương truyện. Không giới thiệu ngay tất cả thân phận, bí mật, quan hệ của nhân vật như người thuyết minh đang kể trước nội dung; cần để độc giả tự chứng kiến qua cảnh, hành động, lời thoại, nội tâm và từng tình tiết cụ thể.

### 14.2. Điều người dùng đánh giá là ổn

Trợ lý viết lại **một cảnh thử văn phong** (văn xuôi tiểu thuyết thật, có không gian, chuyển động, đối thoại tự nhiên và hài hước tình huống). Người dùng nói:

> ok bạn cái đoạn mẫu bạn viết ổn đấy

Điều này nghĩa là **hướng văn phong ở đoạn thử được người dùng đánh giá tích cực**. Nó **KHÔNG** có nghĩa đoạn đó đã được duyệt làm **chương 1 FINAL**, không có nghĩa tất cả câu chữ/tên gọi trong đó đã chốt vĩnh viễn. Dùng nó làm *mẫu tham chiếu giọng kể* cho các thử nghiệm tiếp theo; văn phong có thể tiếp tục chỉnh nếu người dùng góp ý.

### 14.3. Nguyên tắc viết chương rút ra từ phản hồi

- Viết **một cảnh đang diễn ra**: hoàn cảnh cụ thể, những gì nhân vật nhìn/nghe/làm, đối thoại, phản ứng, hậu quả; không chỉ kể rằng "hắn gia nhập tông môn rồi phát hiện ...".
- Hài hước qua **chi tiết và tương tác nhân vật**, không phải lời giới thiệu của người kể rằng hắn "vốn rất hài hước".
- Hé lộ dần bí mật về đại sư tỷ, nhị sư tỷ, trưởng lão, tông chủ và các thế lực. Không tiết lộ toàn bộ ngay đầu truyện.
- Sự thông minh của nam chính phải **được chứng minh bằng các quyết định cụ thể**, không chỉ được gán nhãn "sắc bén".
- Khi có trận chiến: diễn biến chiêu thức/chiến thuật, sức mạnh và hậu quả phải có logic, không tóm tắt lướt qua.
- Hình thức audiobook yêu cầu đoạn văn dễ theo dõi bằng tai, nhịp cảnh rõ, lời thoại phân biệt được nhân vật, không quá nhiều danh từ/cảnh giới xuất hiện dồn dập.
- Viết dài kỳ tránh lặp mô típ bị coi thường → lật kèo hoặc kỳ ngộ vô hạn thiếu trả giá.

## 15. NGUYÊN VĂN ĐOẠN THỬ VĂN PHONG ĐÃ ĐƯỢC NHẬN XÉT "ỔN" (KHÔNG PHẢI CHƯƠNG 1 FINAL)

**Nguồn:** Trợ lý tạo trong hội thoại ngày 23/11/2026 để minh họa khác biệt giữa synopsis và văn xuôi tiểu thuyết. **Trạng thái:** Ví dụ tham chiếu DRAFT. **Chưa có tên nhân vật chính được chốt, “Thanh Vân Tông” chỉ xuất hiện trong đoạn thử.**

> Mặt trời đã ngả về phía tây.
>
> Trên con đường núi quanh co, một thiếu niên mặc áo vải xanh đang chậm rãi bước đi. Trên vai hắn vắt một tay nải cũ, trong miệng ngậm một cọng cỏ, dáng vẻ ung dung như thể đang đi dạo chứ không phải leo hơn ba trăm bậc thềm đá.
>
> Đi được một đoạn, hắn dừng lại, ngẩng đầu nhìn tấm bia đá bên đường.
>
> Trên đó khắc ba chữ lớn đã bị rêu xanh phủ kín.
>
> *Thanh Vân Tông.*
>
> Bên dưới còn có một tấm bảng gỗ, nét mực tuy đã phai nhưng vẫn miễn cưỡng đọc được.
>
> *Bổn môn tuyển nhận đệ tử. Không thu phí nhập môn. Bao ăn, bao ở. Không bắt buộc xuống núi lịch luyện.*
>
> Hai mắt thiếu niên lập tức sáng lên.
>
> "Hay!"
>
> Hắn vỗ đùi đánh đét.
>
> "Ta đã đi qua mười bảy tông môn, cuối cùng cũng tìm được một nơi có chút lương tâm!"
>
> Hắn đọc lại tấm bảng thêm một lần, đặc biệt dừng mắt ở hai chữ *bao ăn*, rồi hài lòng gật đầu.
>
> Chỉ riêng điều này đã đáng để hắn trèo thêm mấy trăm bậc thềm.
>
> Nửa canh giờ sau, thiếu niên cuối cùng cũng đến trước sơn môn.
>
> Nụ cười trên mặt hắn dần cứng lại.
>
> Hai cánh cổng gỗ đã mục mất một bên. Tường viện đổ nát, cỏ dại mọc cao quá đầu gối. Trên mái chính điện, mấy con quạ đang tranh nhau một thứ gì đó không rõ hình dạng.
>
> Một cơn gió thổi qua.
>
> Tấm biển Thanh Vân Tông treo nghiêng trên cổng khẽ đung đưa, phát ra tiếng kẽo kẹt.
>
> Thiếu niên im lặng hồi lâu.
>
> Sau đó hắn cúi đầu nhìn lại tấm bảng tuyển đệ tử mình đã mang theo.
>
> "Không thu phí nhập môn..."
>
> Hắn ngẩng đầu nhìn cánh cổng mục nát.
>
> "Xem ra đúng là không có gì đáng để thu."
>
> Đang lúc hắn cân nhắc có nên quay đầu hay không, một giọng nói già nua bỗng vang lên sau lưng.
>
> "Tiểu tử, ngươi đến bái sư?"
>
> Thiếu niên giật mình quay lại.
>
> Chẳng biết từ lúc nào, bên cạnh gốc tùng già đã xuất hiện một lão nhân tóc bạc. Lão mặc đạo bào màu xám, tay cầm hồ lô rượu, hai mắt lim dim như vừa tỉnh ngủ.
>
> Thiếu niên lập tức chắp tay.
>
> "Vãn bối nghe danh quý tông đã lâu, hôm nay đặc biệt đến xin bái nhập môn hạ."
>
> Lão nhân nhìn hắn, rồi nhìn con đường núi phía sau.
>
> "Nghe danh đã lâu?"
>
> "Đúng vậy."
>
> "Nghe được những gì?"
>
> Thiếu niên không đổi sắc mặt.
>
> "Nghe nói quý tông thanh tịnh thoát tục, không màng danh lợi, đệ tử một lòng hướng đạo, không bị thế tục quấy nhiễu."
>
> Lão nhân trầm mặc.
>
> Thiếu niên cũng trầm mặc.
>
> Một viên ngói trên nóc chính điện bất ngờ rơi xuống.
>
> *Choang!*
>
> Hai người đồng thời quay đầu.
>
> Một lát sau, lão nhân chậm rãi hỏi:
>
> "Ngươi nói thật?"
>
> Thiếu niên nghiêm mặt.
>
> "Từng chữ đều xuất phát từ tận đáy lòng."
>
> Lão nhân nhìn hắn thêm một lúc, cuối cùng bật cười.
>
> "Được! Được lắm! Bổn môn đã lâu không có người trẻ tuổi có nhãn lực như ngươi!"
>
> Thiếu niên cũng cười theo.
>
> Một già một trẻ nhìn nhau, trong lòng đều cảm thấy đối phương là một nhân tài hiếm có.
>
> "Đi thôi, lão phu dẫn ngươi vào gặp tông chủ."
>
> "Khoan đã, tiền bối."
>
> "Chuyện gì?"
>
> Thiếu niên hơi ngượng ngùng, đưa tay xoa bụng.
>
> "Vãn bối đi đường xa, quả thực có chút đói bụng. Không biết trong tông có thể dùng cơm trước hay không?"
>
> Lão nhân sững người.
>
> "Cơm?"
>
> "Đúng vậy. Trên bảng tuyển đệ tử có ghi bao ăn bao ở."
>
> Khóe miệng lão nhân giật nhẹ.
>
> Đúng lúc ấy, trong chính điện bỗng truyền ra một tiếng quát của nữ tử.
>
> "Tam trưởng lão! Người lại đem gạo trong kho đi đổi rượu phải không?"
>
> Thiếu niên chậm rãi quay đầu nhìn lão nhân.
>
> Lão nhân chậm rãi quay đầu nhìn thiếu niên.
>
> Gió núi thổi qua.
>
> Hồ lô rượu trong tay lão nhân khẽ va vào thắt lưng.
>
> Một lúc lâu sau, thiếu niên mới nhẹ giọng hỏi:
>
> "Tiền bối..."
>
> "Hử?"
>
> "Bây giờ rút lại lời xin nhập môn, có còn kịp không?"

## 16. NEXT SESSION — HƯỚNG DẪN LỊCH SỬ 23/11 (THAM KHẢO; XEM MỤC 24 CHO BƯỚC HIỆN TẠI)

**Ngay khi mở session mới:** Người dùng sẽ cung cấp file context này. Trợ lý đọc trước, **xác nhận nắm được tiến độ** và chờ yêu cầu tiếp theo, không tự viết tiếp đoạn truyện.

**Bước phù hợp tiếp theo (bước 8 tiếp diễn, CHƯA FINAL):**

1. Tiếp tục thảo luận/chỉnh sửa tiền đề *Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát* và chuẩn văn phong kể chuyện dựa trên mẫu đã được đánh giá "ổn"; không lặp lại toàn bộ những ý tưởng đã bị bác bỏ.
2. Xác định xung đột chính, lý do tông môn thu nhận những kẻ bị truy sát, cấu trúc tu luyện, nam chính bắt đầu ở đâu, và vai trò các sư tỷ/đạo lữ; chỉ phê duyệt từng nội dung khi người dùng thực sự nói chốt.
3. Khi người dùng phê duyệt ý tưởng hoặc phần cụ thể, đề xuất **đúng một thao tác Git mỗi lượt**: thêm/sửa file DRAFT hoặc FINAL tương ứng, cập nhật `DECISIONS.md` và `EVIDENCE-LOG.md` theo lịch sử thực tế. Không khẳng định đã push nếu người dùng chưa nói.
4. Chỉ bắt đầu viết **chương 1 chính thức** khi người dùng yêu cầu; lúc đó phải viết văn xuôi tiểu thuyết hoàn chỉnh, không phải lời giới thiệu in bìa sách. Trước khi làm audio/video, cần có bản FINAL do người dùng review chốt.

**Các quyết định vẫn còn mở:** tên chính thức; tên/tuổi nam chính; tên tông môn ("Thanh Vân Tông" trong mẫu chưa chốt); hệ thống tu luyện và tài nguyên; bí mật tông chủ; tính cách/số lượng/cung bậc tình cảm của đạo lữ; kẻ địch; các đại arc; khối lượng chương; nền tảng TTS; kế hoạch phát hành.

**Tuyệt đối không tự suy diễn** rằng người dùng đã xác nhận bí mật tông môn thuộc A, B hoặc C, hoặc đã chọn phối hợp B+C; người dùng chỉ phản hồi **"đoạn mẫu ... ổn"** về chất lượng văn phong minh họa.

## 17. MẪU LỜI NHẮN LỊCH SỬ CHO SESSION TIẾP THEO (V2.0, ĐÃ ĐƯỢC THAY BẰNG MỤC 25)

> Tôi gửi file `CONTEXT_KENH_AUDIO_TRUYEN_TU_TIEN(2).md` bản cập nhật v2.0 ngày 23/11/2026. Hãy đọc toàn bộ, đặc biệt mục 12–17. Repo `SangTacTruyenTuTien` đã được tôi commit/push đến bước 7. Tôi đã chọn hướng *Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát* để phát triển, **chưa chốt FINAL**. Nam chính cần hài hước, nhân hậu, sắc bén nhưng giấu dưới vẻ cà lơ phất phơ; truyện có tu luyện, chiến đấu, kỳ ngộ, phiêu lưu, nhiều mỹ nữ và đạo lữ. Tôi đã nói đoạn thử văn xuôi trong mục 15 là "ổn", nhưng đó chưa phải chương 1. Hãy làm việc **từng bước một**, quản lý bằng chứng Git trung thực, và **không tự bắt đầu viết tiếp hay tự chốt gì** nếu tôi chưa yêu cầu.


---

# CẬP NHẬT V3.0 — TIẾN ĐỘ SAU BƯỚC 8.14, NGÀY 25/11/2026

> **Đọc mục 18–25 trước tiên khi chuyển session.** Các câu như "chưa quyết định cách tu luyện", "bước tiếp theo là bước 8" trong phần cũ phản ánh thời điểm 23/11, không phải tiến độ mới nhất. Đặc biệt, **đã lựa chọn hướng thiết kế** KHÁC với việc **chốt FINAL**: tất cả hệ thống nhân vật, thể chất, kỹ năng, cốt truyện cụ thể vẫn DRAFT cho đến khi người dùng phê duyệt bản tổng hợp.

## 18. TÓM TẮT TRẠNG THÁI MỚI NHẤT — ĐỌC TRONG 1 PHÚT

- **Dự án:** Sáng tác truyện tu tiên nguyên tác tiếng Việt, review/chốt từng bản rồi mới chuyển thành audiobook AI 1–3 giờ/video cho YouTube; giữ bằng chứng sáng tạo và sản xuất cho mục tiêu YPP (không bảo đảm phê duyệt).
- **Git:** Repo `SangTacTruyenTuTien`; chủ dự án đã xác nhận commit/push bước 1–7 và đã commit/push **một file context mới** sau đó. Không có quyền truy cập trực tiếp repo trong session này, vì vậy không suy diễn chính xác tên/path file context đã lưu trong repo, không tuyên bố đã push tài liệu phát triển bước 8.
- **Hướng truyện đang theo:** *Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát* — tên làm việc, chưa phải tên chính thức. Một tán tu trẻ có vẻ ham chơi, lười phiền phức vô tình gia nhập tông môn sắp tan rã; các thành viên mang quá khứ bị truy sát. Chất truyện: hài, tu luyện, chiến đấu, kỳ ngộ, phiêu lưu, tình nghĩa, nhiều mỹ nữ và nhiều đạo lữ có quá trình xây dựng tình cảm.
- **Nam chính:** Tán tu lang bạt, đã tu luyện nhưng ở cấp thấp; thông minh, sắc bén nhưng bên ngoài cà lơ phất phơ, hài hước; nhân hậu, trọng tình nghĩa; thích tiêu dao nhưng muốn đủ mạnh để bảo vệ người quan trọng. **Đao Tu + Thể Tu**.
- **Thể chất:** Chọn hướng nguyên tác mới; thiết kế hiện mang tên *Vạn Chiến Tàng Phong Thể* (tên DRAFT), càng chiến đấu/vận đao có chất lượng càng mạnh, vừa tăng chiến lực ngay trong trận vừa trưởng thành lâu dài. Có cơ chế dự thảo *Chiến Thế – Tàng Phong – Ngưng Phong*. Cái giá chủ yếu là **tiêu hao khí huyết lớn**, không chọn Đao Ngân tích tụ gây phản phệ.
- **Điều khiển/thức tỉnh:** Thức tỉnh dần do luyện đao và thực chiến; Chiến Thế ban đầu tự động, về sau nam chính **tự nghiên cứu** để điều khiển, không có cao nhân trực tiếp giải thích cơ chế; không cố giấu biểu hiện càng đánh càng mạnh nhưng giữ kín điều kiện, nhược điểm và giới hạn.
- **Bước 8.14 vừa chọn:** **C — Ban đầu Đao Tu và Thể Tu song hành độc lập, sau đó cộng hưởng và từng bước Đao Thể Hợp Nhất**. Đao Thể Hợp Nhất là con đường vận dụng sức mạnh, không tự động thành cảnh giới vô địch.
- **Văn phong:** Người dùng không thích kiểu synopsis tóm tắt như giới thiệu bìa sách; đã nhận xét đoạn thử **văn xuôi có cảnh, hành động, đối thoại và hài tình huống** ở mục 15 là "ổn". Đoạn thử **không phải chương 1 FINAL** và "Thanh Vân Tông" là tên minh họa, chưa chốt.
- **Việc tiếp theo hợp lý:** **Bước 8.15: tổng hợp toàn bộ hồ sơ nam chính + Vạn Chiến Tàng Phong Thể V1 DRAFT** để người dùng review, kiểm tra logic/cân bằng, rồi **hướng dẫn Git từng thao tác một**. Không tự bắt đầu viết chương 1, không chốt FINAL.

## 19. LỊCH SỬ LỰA CHỌN CHI TIẾT CỦA NGƯỜI DÙNG (BƯỚC 8 → 8.14)

**Quy tắc diễn giải:** Trong bảng, "ĐÃ CHỌN" chỉ có nghĩa người dùng đã quyết định **hướng thiết kế để tiếp tục phát triển**. Không tương đương một văn bản hoàn chỉnh đã được duyệt FINAL. Phần nào chỉ do trợ lý đề xuất phải ghi DRAFT, không gán nhầm cho người dùng.

| Mốc | Lựa chọn/định hướng người dùng thực sự đưa ra | Tình trạng |
|---|---|---|
| Bước 7 | Chọn để phát triển tiền đề **Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát**, không chọn 3 phương án kết hợp cũ; muốn tu luyện, chiến đấu, kỳ ngộ, cường giả, phiêu lưu, mỹ nữ, tình cảm và nhiều đạo lữ | Chọn hướng; chưa FINAL |
| Bước 8 | **B:** Nam chính đã là tu sĩ cấp thấp, có kinh nghiệm nhưng không phải cao thủ giấu tu vi | Đã chọn hướng |
| 8.1 | **A:** Xuất thân tán tu lang bạt, không có gia tộc/tông môn chống lưng; **chi tiết mồ côi chưa được chốt** | Đã chọn hướng |
| 8.2 | **A kết hợp B:** Tu tiên để tiêu dao tự do **và** đủ sức bảo vệ những người yêu thương | Đã chọn hướng |
| 8.3 | Không chọn kiếm tu/toàn năng/thể pháp; **người dùng tự nêu "Tôi muốn nhân vật là đao tu đi song song với thể tu"** | Đã chọn hướng |
| 8.4 | **B:** Nam chính có **thể chất đặc biệt chưa thức tỉnh**, ban đầu không biết bản chất | Đã chọn hướng |
| 8.5 | **D:** Không dùng sẵn Hoang Cổ Chiến Thể/Hỗn Nguyên Đạo Thể/Bất Diệt Bá Thể; **sáng tạo một thể chất nguyên tác mới** | Đã chọn hướng |
| 8.6 | Người dùng nêu yêu cầu: **"có thể sáng tạo ra thể chất chiến đấu càng nhiều, chém càng nhiều đao thể chất càng khủng bố không"**. Trợ lý đề xuất tên **Vạn Chiến Tàng Phong Thể**, hai trục chiến đấu/vận đao và ba cơ chế dưới đây | Hướng do người dùng đưa ra; tên và tên cơ chế DRAFT |
| 8.7 | **C:** Vừa mạnh lên ngay trong trận, vừa giữ lại một phần tiến bộ vĩnh viễn sau trận | Đã chọn hướng |
| 8.8 | Trợ lý khai triển ba cơ chế **Chiến Thế – Tàng Phong – Ngưng Phong**, các giới hạn và ví dụ; người dùng tiếp tục phát triển dựa trên đó nhưng chưa duyệt từng chi tiết là FINAL | Đề xuất DRAFT |
| 8.9 | **B:** Thức tỉnh **dần qua nhiều lần vung đao, luyện tập, giao chiến và tích lũy**, không phải nhờ một lần sinh tử ngẫu nhiên hoặc nhặt bảo vật mở khóa tức thì | Đã chọn hướng |
| 8.10 | **A:** Cái giá chính là **tiêu hao khí huyết cực lớn** khi dùng Chiến Thế; **không chọn** phản phệ vì Đao Ngân quá tải, cũng không chọn ghép A+B | Đã chọn hướng |
| 8.11 | **C:** Ban đầu Chiến Thế **tự kích hoạt**, về sau học cách điều khiển, điều tiết và thu hồi | Đã chọn hướng |
| 8.12 | **A:** Nam chính **tự nghiên cứu/lĩnh ngộ** phương pháp kiểm soát Chiến Thế; **không chọn** trưởng lão trực tiếp chỉ điểm bí mật thể chất, cũng không chọn kết hợp | Đã chọn hướng |
| 8.13 | **C:** **Không cố giấu dấu hiệu năng lực** càng đánh càng mạnh, chỉ che giấu cơ chế, cách vận hành, cái giá và ngưỡng giới hạn; không chọn giấu kín tuyệt đối hoặc chọn người để kể hết bí mật | Đã chọn hướng |
| 8.14 | **C:** Đao Tu và Thể Tu **ban đầu độc lập, sau này cộng hưởng, cuối cùng có khả năng Đao Thể Hợp Nhất** | Đã chọn hướng, vừa hoàn tất |
| 8.15 | Trợ lý **đề xuất** tạm ngừng mở rộng năng lực, tổng hợp hồ sơ thiết kế V1, review rồi mới lập file Git | Chưa triển khai, chưa được người dùng xác nhận FINAL |

### 19.1. Tính cách/động cơ cần giữ

- Ban đầu **tu sĩ thấp cấp** nhưng sắc bén, thực chiến/quan sát tốt, không phải lão quái vật hoặc cường giả vô địch giả dạng; tránh "thông minh" chỉ có trong lời giới thiệu.
- **Xuất thân tán tu**, từng mưu sinh/lăn lộn; tuổi, họ tên, gia cảnh cụ thể, quá khứ đau thương, nghề đã làm, mức tu vi chính xác **chưa chốt**.
- **Bề ngoài:** phóng khoáng, hài hước, đôi lúc thích rượu/ăn ngon/ngắm mỹ nhân, muốn tránh chuyện phiền phức, ngôn ngữ tự nhiên.
- **Bản chất:** nhân hậu, trọng tình nghĩa, nhìn thấu việc người khác bỏ sót, dùng trí khôn chuẩn bị trước; khi người quan trọng bị hại sẽ quyết đoán.
- **Động cơ kép A+B:** muốn sống tiêu dao theo ý mình **và** trở thành cường giả để bảo vệ bằng hữu, người thân, đạo lữ. **Chưa chốt** bất kỳ biến cố nào kiểu không cứu được người thân trong quá khứ; đó mới là gợi ý của trợ lý.
- **Không quên romance:** Nhiều mỹ nữ/đạo lữ là mong muốn thực của người dùng, phải được phát triển qua tương tác, cảm xúc và các arc, không chỉ dùng như trang trí. Số lượng, danh tính, mối quan hệ với đại/nhị sư tỷ vẫn CHƯA CHỐT.

## 20. HỒ SƠ CƠ CHẾ DỰ THẢO: VẠN CHIẾN TÀNG PHONG THỂ

**Tình trạng toàn bộ mục 20: DRAFT — CHƯA FINAL.** Tên *Vạn Chiến Tàng Phong Thể* do trợ lý đề xuất, được sử dụng liên tục trong câu lựa chọn của người dùng nhưng **chưa có lời xác nhận chốt tên chính thức**. Có thể đổi tên sau. Nguồn của năng lực, ai khác từng có thể chất này, nguyên lý chính xác và các chỉ số định lượng chưa quyết định.

### 20.1. Trục sức mạnh đã chọn

- **Chiến đấu càng nhiều → chiến lực trong trận có thể tăng:** đòi hỏi vận đao/giao chiến thực chất, sự thích nghi và tiến bộ, không phải chỉ bị đánh là mạnh hơn.
- **Chém đao càng nhiều, có chất lượng → thể chất và đao thuật tiến bộ:** các nhát chém tập luyện có ích, nhưng một động tác máy móc lặp mãi không tạo tăng trưởng vô hạn; áp lực chiến đấu, cách phát lực, lĩnh ngộ và đối thủ mới cũng có giá trị.
- **Sau trận → một phần thành quả trở thành sức mạnh lâu dài**, thông qua hồi phục, tu luyện và điều kiện thể phách/cảnh giới. Chiến lực tạm thời không được giữ nguyên 100%.
- **Đao là binh khí/chủ công**, **thể là nền tảng** cung cấp khí huyết, sức bền, lực bộc phát và khả năng chịu đựng; nam chính không phải tu sĩ toàn năng biết mọi pháp thuật.

### 20.2. Ba năng lực do trợ lý đề xuất và được sử dụng làm khung thảo luận

**Chiến Thế — tăng trưởng trong trận:**
- Khi nam chính thực sự vận đao/giao chiến, trạng thái chiến đấu đặc biệt dần hình thành: cải thiện lực bộc phát, phản ứng, vận đao, phối hợp thân thể và đao pháp. Sau một số hiệp, hắn có thể mạnh hơn lúc mới vào trận.
- **Không đảm bảo thắng:** đối thủ quá mạnh có thể kết liễu sớm; đối thủ thông minh biết tách giao chiến, kéo giãn khoảng cách, áp chế/khống chế hoặc dụ hắn tiêu hao khí huyết.
- Mức tăng có thể giảm khi thử thách/động tác đã quá quen; không nhảy vọt vô hạn hay tự phá cảnh giới linh lực giữa trận.

**Tàng Phong — lưu dấu trải nghiệm vận đao:**
- Các lần vận đao, luyện tập, thích nghi và lĩnh ngộ để lại dấu tích kinh nghiệm và khả năng phát triển (trong thảo luận gọi **Đao Ngân**, chỉ là thuật ngữ DRAFT).
- Khả năng tích lũy khác nhau tùy chất lượng nhát đao/thử thách. Không tự cấp cho hắn một bộ công pháp, tri thức hoặc kỹ thuật chưa học.
- **Không** có cơ chế mặc định Đao Ngân quá tải gây phản phệ — người dùng đã loại phương án ấy ở 8.10.

**Ngưng Phong — chuyển hóa sau trận:**
- Sau khi hồi phục, củng cố và tiếp tục tu luyện, một phần thành quả Chiến Thế/Tàng Phong thành tiến bộ vĩnh viễn: thể phách, hiệu quả vận đao, thích nghi/khả năng dùng đao.
- Chuyển hóa **phụ thuộc nền tảng và tài nguyên**, không tự tăng tất cả cảnh giới tu luyện. Nếu đang thương nặng, có thể bị trì hoãn; không tạo thêm hình phạt "phản phệ Đao Ngân".

**Chu trình DRAFT:** Luyện đao + thực chiến → Chiến Thế tăng chiến lực tạm thời, Tàng Phong ghi nhận thành quả → nghỉ ngơi/tu luyện → Ngưng Phong củng cố tiến bộ dài hạn → tiếp tục gặp thử thách mới.

### 20.3. Cái giá duy nhất được chọn là khí huyết (8.10 A)

- Khi **Chiến Thế càng mạnh/duy trì càng lâu**, khí huyết càng hao tổn. Giới hạn hiện tại tùy thể phách và mức tu luyện.
- Nếu cố duy trì đến cạn khí huyết: suy kiệt, đau đớn, có thể tổn thương thể phách/căn cơ hoặc nguy hiểm tính mạng. Đây là hậu quả của suy kiệt, **không phải** hình phạt bí ẩn do Đao Ngân tích tụ.
- Trợ lý từng đề xuất 3 mức vận dụng: **Chiến Huyết Khởi Động → Chiến Thế Sôi Trào → Cực Hạn Chiến Thế**. Những tên mức độ này chỉ là DRAFT và **không phải ba cảnh giới chính thức**.
- Khí huyết mạnh dần theo thể tu, cho phép thời gian/mức duy trì Chiến Thế tăng nhưng không loại bỏ nhu cầu nghỉ ngơi và tiếp tế tài nguyên.

### 20.4. Thức tỉnh dần (8.9 B)

Không có kiểu "sắp thua nên bật năng lực mới đánh thắng ngay". Thể chất biểu hiện bằng các dấu hiệu nhỏ, xuất hiện có phục bút từ nhiều chương: phối hợp lực tốt hơn, cơ thể có đôi lúc vận đao thuận tay hơn, sức tăng khác thường sau giao chiến nhưng mệt bất thường.

Ba **giai đoạn thức tỉnh DRAFT** trợ lý đã đề xuất:
1. **Tàng Phong Vô Thức:** thể chất ngủ say, dấu hiệu nhỏ, nam chính chỉ nghĩ bản thân hơi có ngộ tính về đao.
2. **Chiến Huyết Sơ Động:** khí huyết biến đổi khi luyện đao/giao chiến; chi phí/hiệu quả bất thường, chưa ổn định.
3. **Sơ Khai Tàng Phong:** sau tích lũy và biến cố phù hợp, thể chất thức tỉnh một phần; bắt đầu cảm nhận và vận dụng Chiến Thế/Ngưng Phong ở mức sơ khai, vẫn rất hạn chế.

**Chưa chốt:** số chương/mốc thời gian thức tỉnh, sự kiện cụ thể, ai chứng kiến, tỉ lệ tăng và tên giai đoạn.

### 20.5. Tự học điều khiển, từ tự động đến chủ động (8.11 C + 8.12 A)

Ba **giai đoạn điều khiển DRAFT**, khác với các giai đoạn thức tỉnh:
1. **Bản Năng Chiến Khởi:** Chiến Thế tự phát trong giao chiến đủ áp lực, khó chủ động bật/tắt, có thể hao khí huyết ngoài dự kiến.
2. **Tri Chiến Ngự Huyết:** nam chính tự quan sát nhịp thở, khí huyết và động tác; biết dự đoán, điều tiết một phần, nhưng chưa hoàn toàn làm chủ.
3. **Tùy Tâm Ngự Chiến:** dần chủ động kích hoạt khi giao chiến, tăng/giảm cường độ và thu hồi; **chủ động bật không đồng nghĩa ngay lập tức có tối đa chiến lực**, vẫn cần giao phong để tích lũy.

**Phương pháp đã được người dùng chọn:** tự tìm hiểu qua ghi nhận, tự so sánh thử nghiệm, những lần sai/thất bại và chiến đấu thật. **Không** được viết tình tiết trưởng lão hoặc tông chủ lập tức nhận ra tên thể chất rồi truyền dạy cách điều khiển Chiến Thế. Đồng môn/trưởng lão có thể tạo cơ hội học kỹ thuật thông thường, giao đấu, chữa thương hoặc khiến nam chính có thêm dữ liệu, nhưng **khám phá/quyết định cách điều khiển cơ chế là của chính nam chính**.

Trợ lý từng minh họa cảnh nam chính luyện hơn ba trăm nhát đao ban đêm, ghi chép trong sổ rồi tự phát hiện "biến đổi lực nhất thời" khác với "đao thức thuận tay hơn hôm qua". **Đây là cảnh thử DRAFT, không phải chi tiết chính thức**. Tên/việc hắn thực sự dùng sổ tay còn chưa chốt.

### 20.6. Công khai biểu hiện, giữ kín bản chất (8.13 C)

- Người ngoài được quyền thấy hắn càng vung đao/giao chiến càng khó đối phó. **Không bắt buộc giấu mọi dấu hiệu**, không phải cả thiên hạ đều mù quáng.
- Hắn không tự tiết lộ điều kiện kích hoạt, khả năng chuyển hóa thành tiến bộ vĩnh viễn, cơ chế tiêu hao khí huyết và **ngưỡng suy kiệt cụ thể**; danh xưng/cội nguồn thể chất cũng chưa chắc ai biết.
- Kẻ địch giỏi có thể suy luận và tìm cách khắc chế; không nên viết mọi đối thủ đều lao vào đấu sức bất chấp hiểu biết. Chiến thuật của nam chính có thể gồm **Dưỡng Chiến** (tạo giao phong hợp lý), **Ẩn Phong** (giấu mức tăng thật), **Bạo Phong** (bộc phát đao thức ở thời cơ thích hợp) — các tên này đều mới là đề xuất DRAFT.
- Mức độ người thân/đạo lữ biết bí mật đến đâu vẫn có thể phát triển theo tình tiết, **nhưng lựa chọn của người dùng KHÔNG PHẢI "bật mí cho người tin tưởng" như phương án B**.

### 20.7. Đao Tu và Thể Tu: độc lập → cộng hưởng → hợp nhất (8.14 C)

- **Giai đoạn đầu:** nam chính phải tự luyện **đao pháp/đao ý** và **gân cốt/khí huyết/thể phách** như hai con đường độc lập. Giỏi đao chưa chắc thể mạnh tương ứng; thể mạnh chưa chắc kỹ xảo đao đủ tốt.
- **Giai đoạn giữa:** Vạn Chiến Tàng Phong Thể giúp hai con đường **cộng hưởng**. Lĩnh ngộ cách phát lực mới có thể khiến thể phách dần thích nghi, thể phách tiến bộ lại cho phép thi triển đao thức khó hơn; **không tự động nâng cảnh giới đao đạo hoặc thể đạo chỉ nhờ bên kia tăng**.
- **Giai đoạn cao:** **Đao Thể Hợp Nhất** — toàn thân, khí huyết, chuyển động, đao ý và kỹ thuật xuất đao phối hợp rất sâu; đây là thành tựu vận dụng sức mạnh và đỉnh cao của con đường riêng, **không phải bảo đảm vô địch**.
- **Chưa chốt:** cảnh giới/số lần đột phá cụ thể, khi nào cộng hưởng, tên kỹ năng, đao pháp, loại đao, công pháp thể tu, hệ thống tài nguyên, cách tương tác với hệ thống tu vi chính.

### 20.8. Giới hạn cân bằng cần ưu tiên khi review

- Cường giả chênh lệch xa có thể đánh bại nam chính trước khi Chiến Thế tích đủ.
- Không nâng cấp mọi năng lực chỉ bằng chém không khí, không thắng tất cả vì kéo dài trận.
- Chiến Thế tăng **năng lực giao chiến**, không tự động đột phá tu vi chính; luyện thể cần tài nguyên, thời gian, hồi phục.
- Thương tích và hao khí huyết phải có hậu quả đáng tin; không tạo thêm giá phản phệ Đao Ngân đã bị bác bỏ.
- Nam chính vẫn có đời sống tông môn, bằng hữu, những đạo lữ và cuộc phiêu lưu, không biến thành cỗ máy chỉ thích đánh nhau.
- Những cảnh đánh nhau nên thể hiện đòn thế, nhịp, toan tính và lỗ hổng thực tế; không lặp mô típ "đánh lâu là thắng" ở mọi trận.

## 21. MỐI LIÊN HỆ VỚI TÔNG MÔN VÀ PHONG CÁCH KỂ — ĐỀ XUẤT CHƯA CHỐT

### 21.1. Vai trò tông môn — không được mâu thuẫn với lựa chọn 8.12 A

Khung đã lựa chọn để phát triển: một tông môn sắp giải tán, đại sư tỷ bị chính đạo truy sát, nhị sư tỷ từng là thiên tài luyện đan bị vu oan, trưởng lão mất tu vi, tông chủ che giấu một bí mật lớn; nhưng thân thế/tên riêng/diễn biến cụ thể CHƯA FINAL.

Các mối liên hệ **do trợ lý đề xuất, chưa phê duyệt**:
- **Đại sư tỷ:** giao đấu/đụng độ với nam chính, bộc lộ điểm yếu kỹ thuật và tạo áp lực khiến hắn học hỏi. Nàng không bắt buộc là đạo lữ.
- **Nhị sư tỷ:** kiến thức luyện đan có thể hỗ trợ hồi phục khí huyết. Không được mặc định thuốc giúp hắn không phải trả giá chiến đấu; nàng không bắt buộc là đạo lữ.
- **Trưởng lão mất tu vi:** có thể nói chuyện đời, kinh nghiệm chiến đấu phổ thông, làm bạn rượu hoặc dạy kỹ thuật cơ bản, **nhưng không chỉ điểm cách điều khiển bí mật Chiến Thế** vì người dùng đã chọn A.
- **Tông chủ:** cung cấp bối cảnh/nhiệm vụ/hỗ trợ; mục đích thu nhận các nhân vật bị truy sát vẫn chưa quyết định.
- **Các đồng môn:** là nguồn tình nghĩa, tương tác hài hước, sự kiện sinh tử để nam chính tự trưởng thành.

**Bí mật tông môn:** trước đây trợ lý đề xuất A (người oan khuất), B (thành viên thật sự nguy hiểm), C (tông chủ có kế hoạch lớn), rồi nghiêng B+C, **nhưng người dùng CHƯA CHỌN bất kỳ phương án nào**. Không tự chốt B+C.

### 21.2. Văn phong khi sáng tác thật

- **Mẫu được nhận xét "ổn"**: nguyên văn ở **mục 15**; nhân vật lên núi thấy bảng tuyển đệ tử bao ăn bao ở, tông môn rách nát, đối đáp với lão trưởng lão và bị đòi gạo. Chỉ tham chiếu **văn phong** chứ không mặc định đây là mở đầu cốt truyện chính thức.
- Không viết như lời giới thiệu phim/synopsis bìa sách. Viết cảnh cụ thể: ai ở đâu, đang làm gì, cảm giác/đối thoại/hành động và hậu quả; hé bí mật theo diễn biến, không "thuyết minh" trước.
- Nam chính hài hước tự nhiên, không biến mọi người thành ngốc; thông minh qua quyết định và hành động; các trận đấu có chiêu thức/chiến thuật và hậu quả. Tránh kể lướt những cảnh quan trọng bằng một đoạn tóm tắt.
- Những đoạn thử khác đã có trong chat (cảnh luyện đao ban đêm, cảnh đối thủ nghi ngờ càng đánh càng mạnh, cảnh gần cạn khí huyết) chỉ có giá trị minh họa. Không đưa thẳng vào bản thảo chính thức hoặc coi tên/tình tiết/nhát đao đếm được là canon.
- Mỗi chương về sau cần dễ nghe bằng TTS, lời thoại phân biệt rõ, không dồn dập thuật ngữ hoặc cảnh giới mới; giữ nhịp chương và phục bút để theo dõi lâu dài.

## 22. DANH SÁCH CHƯA CHỐT — TUYỆT ĐỐI KHÔNG TỰ BỔ SUNG THÀNH FINAL

- **Bản hồ sơ nhân vật/thể chất:** tất cả còn DRAFT. Chưa có bản hợp nhất được user review và duyệt FINAL.
- **Tên gọi:** tên truyện, tên kênh, nam chính, tông môn, các trưởng lão, sư tỷ, đạo lữ, phản diện; "Thanh Vân Tông" ở đoạn mẫu chỉ minh họa; "Vạn Chiến Tàng Phong Thể", "Đao Ngân", tên cấp Chiến Thế và giai đoạn thức tỉnh/điều khiển chỉ là đề xuất.
- **Nhân thân:** tuổi, diện mạo, gia đình, tán tu bắt đầu ở cảnh giới nào, các nghề tán tu, lý do gia nhập tông môn, có hay không biến cố bi thương, nguồn gốc thể chất.
- **Hệ thống sức mạnh chung:** hệ thống cảnh giới tu vi, đao đạo, thể đạo, trình độ vượt cấp, công pháp/đao/bảo vật, tài nguyên và nhịp đột phá; thời điểm thức tỉnh/cộng hưởng/hợp nhất.
- **Tông môn và thế giới:** bí mật tông chủ, lý do các nhân vật bị truy sát, phe chính/tà, địa lý, các arc, phản diện, đường dây bí mật dài hạn.
- **Tuyến tình cảm:** ai là đạo lữ, số lượng, quá trình phát triển, giới hạn quan hệ; không mặc nhiên mọi sư tỷ đều yêu nam chính.
- **Nội dung phát hành:** chưa có **chương 1 chính thức**, chương FINAL, audio, video, kênh hoàn thiện hoặc YPP được duyệt. Quy mô 2.000 chương chỉ là tham khảo.
- **Bằng chứng:** chưa có xác nhận đã xuất toàn bộ nguyên văn chat/prompt/review cho các bước 8.x vào `04-CREATIVE-EVIDENCE`. Không nhận vơ Git history hay file evidence chưa được chủ dự án xác nhận.

## 23. GIT, CHỨNG CỨ SÁNG TẠO VÀ TRẠNG THÁI FILE THỰC TẾ

### 23.1. Những gì được người dùng xác nhận đã commit/push

- `README.md`
- `DECISIONS.md`
- `EVIDENCE-LOG.md`
- `04-CREATIVE-EVIDENCE/README.md`
- `01-STORY-BIBLE/CREATIVE-BRIEF.md`
- `01-STORY-BIBLE/PREMISE-CANDIDATES-v1.md`
- `01-STORY-BIBLE/CHARACTER-DIRECTION-v1.md`
- **Một bản context cập nhật trước đó**, người dùng xác nhận đã commit/push vào Git, nhưng **chưa xác minh đường dẫn/tên chính xác** trong remote.

**Không có căn cứ** rằng file `01-STORY-BIBLE/PROTAGONIST-v1.md` hay `01-STORY-BIBLE/VAN-CHIEN-TANG-PHONG-THE-v1.md` đã tồn tại hoặc đã push. Cả hai từng được trợ lý đề xuất cho tương lai, không được coi là file thực tế.

### 23.2. Chuẩn lưu evidence cần duy trì

- Giữ bản gốc/hội thoại đầy đủ, không chỉ tóm tắt. Ghi cả **ý tưởng cũ bị người dùng chê "chán"**, nhận xét về văn phong synopsis, phản hồi "đoạn mẫu ... ổn", và những lựa chọn A/B/C/D theo ngày thực tế; không sửa lại lịch sử.
- Quy trình từng bản: yêu cầu của người dùng → đề xuất AI → nhận xét/chỉnh sửa → phiên bản mới → người dùng xác nhận FINAL (nếu có) → file TTS → QA audio/video → xuất bản. Có thể ghi tham chiếu commit, nhưng không tự điền hash commit/bằng chứng giả.
- Chỉ thêm mã `DEC-XXXX` hoặc `EV-XXXX` sau khi kiểm tra mã trước đã dùng để tránh trùng; đừng tự ghi "đã FINAL" nếu user chỉ chọn hướng DRAFT.
- Repo nên private; Git + nhật ký là tư liệu giải trình quá trình, không chứng minh pháp lý tuyệt đối hoặc tự bảo đảm YPP.
- Hướng dẫn Git **mỗi lần một bước**: đưa đúng file/path cần tạo/sửa, nội dung/nguồn DRAFT, rồi lệnh git add/commit/push cho đúng thay đổi; chờ người dùng báo hoàn tất mới bước tiếp theo. Không giao cùng lúc nhiều tài liệu phải thao tác.

## 24. ĐIỂM DỪNG & CÔNG VIỆC TIẾP THEO CHO SESSION MỚI

**Điểm dừng đúng:** Người dùng vừa chọn **C ở bước 8.14**: ban đầu Đao/Thể độc lập, về sau cộng hưởng, hướng tới Đao Thể Hợp Nhất. Trợ lý đề xuất bước **8.15 tổng hợp/review thiết kế Vạn Chiến Tàng Phong Thể V1**, chưa viết bản hoàn chỉnh hay lưu file Story Bible tương ứng. Sau đó người dùng yêu cầu **cập nhật file context đang đính kèm và hướng dẫn Git từng bước**.

**Việc thực hiện ngay trong session hiện tại:** Cập nhật context này thành v3.0, trả file cho người dùng; **chỉ hướng dẫn 1 thao tác Git đầu tiên: cập nhật file context trong repo và push**. Chưa làm hồ sơ phụ cùng lượt khi user chưa báo đã xong.

**Sau khi người dùng báo đã push context v3.0:**
1. Tiếp tục đúng **bước 8.15 — lập bản hồ sơ DRAFT V1** cho Vạn Chiến Tàng Phong Thể và con đường Đao Thể Song Tu, từ những lựa chọn đã ghi ở mục 19–20. Cần giữ rõ cái nào user chọn, cái nào assistant đề xuất. Đề xuất 1 file trong `01-STORY-BIBLE/` để user review, chưa tự FINAL.
2. Review tính hợp lý, cân bằng, chi tiết còn mở; không thêm năng lực/huyết mạch kỳ lạ vô cớ. Sau review mới xem xét file Git kế tiếp và cập nhật nhật ký quyết định/evidence theo từng bước.
3. Sau khi nền tảng thể chất đủ ổn, quay lại hoàn thiện hồ sơ **nam chính**, hệ thống cảnh giới, bối cảnh tông môn, nhân vật, bí mật xung đột chính, tuyến đạo lữ, các đại arc. Chỉ bắt đầu chương 1 khi chủ dự án giao rõ; chỉ audio từ bản FINAL.
4. **Không tự viết tiếp cảnh thử** ở mục 15 hoặc chương 1; không tự đổi hướng truyện hay tự kết luận đã FINAL.

## 25. PROMPT MỞ SESSION MỚI (BẢN MỚI NHẤT V3.0)

> Tôi gửi file context **v3.0 cập nhật 25/11/2026** cho dự án `SangTacTruyenTuTien`. Hãy đọc **toàn bộ**, nhưng ưu tiên **mục 18–25** (mới nhất), sau đó mục 12–17 (lịch sử và nguyên văn cảnh mẫu). Tôi đã tạo repo và commit/push bước 1–7, đồng thời lưu bản context trước đó. Hướng truyện *Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát* đã được chọn để phát triển nhưng **chưa FINAL**. Nam chính là tán tu cấp thấp, hài hước, nhân hậu, sắc bén dưới vẻ cà lơ phất phơ, muốn tiêu dao và bảo vệ người quan trọng; theo **Đao Thể Song Tu**. Chúng tôi đã chọn hướng thể chất nguyên tác *Vạn Chiến Tàng Phong Thể* với **Chiến Thế – Tàng Phong – Ngưng Phong** (tên và chi tiết đều DRAFT), càng đánh/càng chém có chất lượng càng mạnh trong trận và tiến bộ vĩnh viễn sau trận; thức tỉnh dần; **cái giá khí huyết lớn** (không dùng phản phệ Đao Ngân); ban đầu tự động rồi **tự nghiên cứu** để điều khiển; không cố giấu biểu hiện nhưng giấu cơ chế và giới hạn; **bước 8.14 đã chọn C: Đao và Thể độc lập → cộng hưởng → hợp nhất**. Tôi đã thích đoạn thử văn xuôi mục 15, nhưng chưa phải chương 1. **Đừng tự chốt FINAL; đừng viết chương chính thức, tạo audio/ảnh/video; hãy tiếp tục từ bước 8.15 (hồ sơ V1 DRAFT để review) và hướng dẫn các thay đổi Git từng bước một, đợi tôi xác nhận đã push rồi mới đến bước tiếp.**

**Nguyên tắc cập nhật tiếp theo:** Mỗi khi có lựa chọn mới ở session khác, giữ nguyên lịch sử, bổ sung ngày/phiên bản, ghi rõ mức độ DRAFT/FINAL và đường dẫn file Git mà người dùng thực sự đã push. Không diễn giải lại các đề xuất cũ thành quyết định chính thức.

---

# CẬP NHẬT V4.0 — CHỐT 7 CHƯƠNG FINAL VÀ GIAO AGENT DỰNG AUDIO TẬP 1 (25/11/2026)

> **MỤC 26–35 LÀ BẢN BÀN GIAO MỚI NHẤT.** Mọi mô tả ở mục 1–25 trái với các mục này đều là **lịch sử**, không phải trạng thái hiện hành. Không xóa phần cũ vì cần lưu quá trình sáng tạo. **Khi có sai lệch về tình tiết thực tế, mở nguyên văn 7 chương FINAL trước khi phát biểu hoặc viết tiếp.**

## 26. TÓM TẮT 60 GIÂY — ĐIỂM DỪNG THỰC TẾ

- **Dự án:** Truyện tu tiên nguyên tác Việt Nam, dùng AI hỗ trợ sáng tác; xuất bản audiobook dạng video lên YouTube, mục tiêu mỗi tập khoảng 1–3 giờ, tập đầu nhắm khoảng 2 giờ và có minh họa chuyển cảnh theo nội dung.
- **Tên kênh đã được người dùng lựa chọn trong trao đổi riêng về branding:** **Tiên Vực Ký** (đã yêu cầu avatar, ảnh bìa, watermark; lưu ý cần kiểm tra file/hình thực tế nếu tiếp tục thiết kế). Không đồng nhất tên **kênh** với tên **bộ truyện**. Việc đã tạo/đặt tên kênh không đồng nghĩa đã tải video lên.
- **Tên truyện làm việc / tiền đề:** *Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát*. Trên thumbnail Tập 1 dùng cách viết ngắn nổi bật **TÔNG MÔN BỊ TRUY SÁT**. Chưa có một quyết định riêng xác nhận tên thương mại dài là tên chính thức bất biến của toàn series, nhưng các Chương 1–7 đã FINAL theo nội dung riêng.
- **Điểm cốt lõi:** Đã sáng tác và người dùng **CHỐT FINAL TOÀN BỘ CHƯƠNG 1, 2, 3, 4, 5, 6, 7**. Đây là nội dung phải dùng nguyên văn để TTS, storyboard và mọi công việc tiếp nối. **Chương 8 chưa được giao viết/chưa có bản FINAL trong cuộc hội thoại này.**
- **Tên nam chính đã dùng trong bản FINAL:** **Tạ Hành Chu**; tông môn trong truyện **Thanh Vân Tông**. Những chỗ ở lịch sử ghi “chưa chọn tên nam chính/Thanh Vân Tông chỉ là ví dụ” là trạng thái **trước khi viết chương**, không còn đúng đối với 7 chương đã FINAL.
- **Chủ dự án đã góp ý và được sửa:** (1) Giới thiệu nhân vật bằng tên, ưu tiên “Tạ Hành Chu” hoặc “Hành Chu”, hạn chế đại từ “hắn”; (2) tuyệt đối không gọi nam chính là “người tán tu” như đại từ thay tên; (3) kiểm tra cuối chương trước/đầu chương sau để tránh lặp nguyên văn khi ghép giọng đọc; (4) không commit Git theo mỗi chỉnh sửa nhỏ.
- **Tư liệu sản xuất:** Thumbnail `thumbnail-part-1.png`; storyboard/CSV đề xuất 217 ảnh, hướng dẫn tạo ảnh, prompt agent tổng chỉ huy. Người dùng chụp ảnh Windows Explorer xác nhận file trong repo.
- **Trạng thái production thật:** **Chưa được xác nhận** giọng nữ đã tạo, số lượng ảnh/clip đã hoàn thành, thời lượng WAV, MP4 FINAL, upload YouTube hoặc YPP. **Prompt đã được cung cấp không có nghĩa agent đã chạy.**
- **Việc tiếp theo:** Có thể tiếp tục **theo dõi/QA agent đang dựng Tập 1**, yêu cầu kiểm tra file FINAL nếu người dùng cung cấp; hoặc **viết Chương 8** khi người dùng giao (phải đọc Chương 7 FINAL). Không tự bắt đầu hoạt động khác khi chỉ nhận context.

## 27. CÁC CHƯƠNG TRUYỆN ĐÃ CHỐT — NGUỒN CHUẨN

Đúng đường dẫn theo repo `SangTacTruyenTuTien` (đã thấy file trong ảnh chụp thư mục `03-MANUSCRIPTS/approved`):

| Chương | Tựa đề | File nguồn CHÍNH THỨC | Trạng thái |
|---|---|---|---|
| 1 | **Bao Ăn, Bao Ở** | `03-MANUSCRIPTS/approved/CHUONG-0001-FINAL.md` | User chốt FINAL từ DRAFT V2 |
| 2 | **Người Trong Phong Thư** | `03-MANUSCRIPTS/approved/CHUONG-0002-FINAL.md` | User chốt FINAL từ DRAFT V2 |
| 3 | **Người Trở Về Trong Sương** | `03-MANUSCRIPTS/approved/CHUONG-0003-FINAL.md` | User chốt FINAL từ DRAFT V2 |
| 4 | **Ba Lối Xuống Núi** | `03-MANUSCRIPTS/approved/CHUONG-0004-FINAL.md` | User chốt FINAL từ DRAFT V2 |
| 5 | **Bụi Tro Trên Phong Thư** | `03-MANUSCRIPTS/approved/CHUONG-0005-FINAL.md` | User chốt FINAL từ DRAFT V2 |
| 6 | **Một Bữa Cơm Trước Trận** | `03-MANUSCRIPTS/approved/CHUONG-0006-FINAL.md` | User chốt FINAL từ DRAFT V2 |
| 7 | **Thanh Vân Không Bán Người** | `03-MANUSCRIPTS/approved/CHUONG-0007-FINAL.md` | User chốt FINAL từ DRAFT V2 |

- **Chương 1:** Viết ban đầu theo phong cách văn xuôi có cảnh/hội thoại. Phản hồi user: không nên dùng “hắn” dày đặc; sửa DRAFT V2 để giới thiệu **Tạ Hành Chu** ngay đầu và dùng tên nhân vật phù hợp; user nói **“ok chốt chương 1”**.
- **Chương 2:** DRAFT V1 bị lỗi **lặp nguyên văn câu đe dọa “Trước khi trời sáng, giao người ra. Nếu không, cả núi cùng chôn.”** ở cuối Chương 1 và đầu Chương 2, gây lặp voice. Sửa cả câu lặp và câu nhắc lại không cần thiết trong DRAFT V2, **không sửa Chương 1 FINAL**; user nói **“chốt chương 2”**. Tình tiết chương: phong thư/độc châm, mối đe dọa đối với Thanh Vân Tông, cuộc đối đầu ban đêm, Kỷ Thanh La trở về bị thương.
- **Chương 3–7:** Sáng tác một đợt 5 chương DRAFT V1 để review. User góp ý bỏ “người tán tu” như đại từ chỉ Tạ Hành Chu; trợ lý báo đã sửa **25 vị trí** ở bản DRAFT V2. User nói **“chốt chương 3-7”**; 5 bản FINAL được xuất dựa trên V2. Không tự thay đổi lời văn đã duyệt.
- **Thống kê cũ:** Assistant từng ước lượng 7 chương ~19.800 “từ/tiếng” tính theo khoảng trắng, có thể gần 2 tiếng với TTS vừa phải. **Chỉ là ước tính chưa kiểm chứng bằng WAV cuối cùng**; không ép thời lượng thành 120:00 bằng cách kéo giọng đọc hay lặp cảnh.
- **Tôn trọng CANON:** Những chi tiết cụ thể như ai nói câu nào, thời điểm xuất hiện bí mật, thương tích, địa hình, thứ tự giao đấu, cliffhanger cuối Chương 7 phải **đọc nguyên bản Markdown**. Các phần mô tả tóm tắt trong context/storyboard chỉ dùng để tìm đường, không được thay thế nguồn truyện.

### 27.1. Quy ước khi viết tiếp Chương 8 trở đi

1. Mở **ít nhất toàn bộ Chương 7 FINAL**, và đọc thêm các chương trước khi cần kiểm tra sự kiện, đặc biệt các manh mối kéo dài từ Chương 1–6; không viết từ tóm tắt mơ hồ.
2. **Tạ Hành Chu** là tên gọi chính; **Hành Chu** dùng để tránh lặp tên liên tục; đôi lúc có thể lược chủ ngữ khi rõ người thực hiện. **Không dùng “người tán tu” hoặc “hắn” lặp dày làm đại từ thay nam chính**. “Tán tu” chỉ dùng khi mô tả thân phận thật.
3. Văn phong là **tiểu thuyết đang diễn ra**, không phải synopsis, giới thiệu bìa sách, voice thuyết minh trước nội dung. Hài hước qua tương tác, trận chiến có chiến thuật, thương tích và giới hạn tu vi hợp lý.
4. **Kiểm tra câu/đoạn cuối chương trước với câu/đoạn đầu chương sau** trước khi đưa TTS. Không lặp cliffhanger nguyên văn. Nếu lặp ý cần thiết, diễn đạt diễn tiến tiếp theo từ hành động và cảm giác mới, tránh “nhắc lại” như phim truyền hình.
5. Không tự thêm chi tiết trở thành CANON về cảnh giới, Vạn Chiến Tàng Phong Thể, nguồn gốc môn phái, đạo lữ nếu không được xây dựng trong cốt truyện và user duyệt. Giữ cơ chế Chiến Thế/Tàng Phong/Ngưng Phong là **thiết kế DRAFT** trừ phần đã thể hiện rõ bằng văn bản FINAL.
6. Viết **DRAFT → user review → chỉnh sửa → user chốt FINAL**. Chỉ khi FINAL mới đưa vào kho bản chuẩn và commit.

## 28. LIÊN TỤC CỐT TRUYỆN TẬP 1 — CÁC MỐC ĐÃ ĐƯỢC DÙNG ĐỂ LẬP STORYBOARD

> Phần này là **lược đồ định hướng từ nội dung các phiên trước**, không phải thay thế 7 file FINAL. Khi cần biết ai/chuyện gì/chi tiết nào xảy ra chính xác, mở bản thảo gốc. Không suy diễn các mốc thành lời thoại nguyên văn.

| Chương | Trục hình ảnh/sự kiện đã dùng cho storyboard |
|---|---|
| 1 | Tạ Hành Chu đến tông môn núi đổ nát vì bảng tuyển đệ tử **“không thu phí, bao ăn, bao ở”**; gặp Tam trưởng lão, người ở tông môn và A Thạch; xuất hiện mối đe dọa phong thư |
| 2 | Mũi kim độc và phong thư; cảnh phòng bị/giao đấu ban đêm; đại sư tỷ trở về bị thương |
| 3 | **Kỷ Thanh La** trở về, vết thương và dấu vết truy sát; **Dẫn Hương Trùng**; chuẩn bị đối phó |
| 4 | **Ba lối xuống núi**, bố trí đối phó kẻ đột nhập; chiến đấu, nhân vật **Chu Tứ** |
| 5 | Khai thác dấu vết/đối chất, thuốc và bí mật liên quan **Trạm Thanh Giản**; **mảnh đồng hình cánh chim** |
| 6 | Bữa cơm và tình nghĩa trước trận, chuẩn bị kế hoạch; **Trác Cửu** xuất hiện |
| 7 | Cao trào giao chiến với kẻ truy sát, bảo vệ đồng môn; bước ngoặt gia nhập tông môn, **dấu đóng chìm** và manh mối dẫn sang tập tiếp theo |

**Các nhân vật/tên cần giữ nhất quán trong giọng đọc và hình:** Tạ Hành Chu, Kỷ Thanh La, Vãn Ninh, A Thạch, Tam trưởng lão, Trác Cửu; có các tên riêng khác trong bản thảo và storyboard. Chỉ khẳng định quan hệ, lai lịch, tuổi và tướng mạo theo **nguyên văn FINAL**, không suy luận chỉ vì tên/giới tính/giai đoạn của câu chuyện. **Thể chất đặc biệt chưa được đánh thức hoàn toàn trong Tập 1** theo hướng xây dựng đã duyệt.

## 29. THUMBNAIL TẬP 1 VÀ ĐỊNH HƯỚNG HÌNH ẢNH

- Người dùng yêu cầu một thumbnail YouTube bắt mắt cho audio Tập 1, **bắt buộc có số 1** để phân biệt tập.
- Đã tạo hình 16:9 theo phong cách tiên hiệp điện ảnh, nhân vật nam Tạ Hành Chu mặc áo cổ phong xanh xám cầm **đao**, khí chất phóng khoáng, một nữ tu sĩ khí chất bí ẩn, sơn môn đổ nát và bầu trời đêm; trên ảnh có chữ lớn **“TÔNG MÔN BỊ TRUY SÁT”** và **“TẬP 1”**, kèm chữ nhỏ **“AUDIO TRUYỆN TU TIÊN”**.
- Trong ảnh chụp của người dùng, tài liệu thumbnail đang nằm tại **`BUILD FINAL CLIP/thumbnail-part-1.png`**. Đây là tài nguyên đầu vào đã được người dùng sắp vào thư mục dựng. **Không tự tạo lại thumbnail** nếu không có yêu cầu sửa.
- Khi cần thiết kế nhân vật nhất quán cho loạt clip, thumbnail chỉ là **tham chiếu mỹ thuật**, phải đối chiếu mô tả nhân vật và sự kiện trong FINAL. Không tự suy diễn rằng mọi hiệu ứng tím/giáp đẹp/kiếm trên ảnh là kỹ năng đã xuất hiện trong truyện.

## 30. STORYBOARD 217 ẢNH MINH HỌA — TƯ LIỆU ĐÃ BÀN GIAO

- Người dùng yêu cầu “list các ảnh để agent làm clip chuyển cảnh giữa các ảnh này liên tục khi phát audio nhằm mô tả cho cốt truyện”.
- Trợ lý đã tạo storyboard **217 cảnh/ảnh dự kiến** dựa trên 7 chương FINAL và tài liệu cho agent tạo ảnh, chuyển động, đồng bộ với lời đọc. **217 là số mục storyboard, KHÔNG PHẢI số ảnh/clip thực sự đã được render.**
- Phân bổ: **Chương 1: 37, Chương 2: 32, Chương 3: 23, Chương 4: 30, Chương 5: 27, Chương 6: 30, Chương 7: 38 = 217**.
- Các file trong `BUILD FINAL CLIP` **đã hiện trong ảnh chụp Windows Explorer**, gồm:
  - `STORYBOARD-ANH-TAP-01.md` — danh sách cảnh theo thứ tự; lời kể neo cảnh, miêu tả hình và gợi ý chuyển động.
  - `DANH-SACH-ANH-TAP-01-AGENT.csv` — bảng cho agent xử lý có cấu trúc.
  - `PROMPT-DUNG-CHUNG-CHO-AGENT.md` — quy tắc chung tạo ảnh/clip.
  - `README.md` — hướng dẫn dùng bộ dữ liệu.
  - `thumbnail-part-1.png` — thumbnail Tập 1.
- Bộ ZIP từng bàn giao trong chat: `STORYBOARD-ANH-AUDIO-TAP-01-CHO-AGENT.zip`; nhưng trong ảnh user đã **giải nén ra các file trên**. Khi session mới, ưu tiên file thực tế người dùng đang có thay vì đòi file ZIP cũ.
- **Không có timestamp chính xác trước khi làm audio.** Agent phải lấy text neo cảnh → đối chiếu với voice thực tế, không chia đều 217 ảnh theo thời gian và không tạo hình làm lộ cao trào trước lúc người kể tới.
- Để clip nhìn như phim minh họa thay vì slideshow, có thể tạo các chuyển động/hình cận cảnh/phân góc bổ sung; **không được kéo một đoạn video ngắn bằng lặp/đảo ngược hoặc chỉ zoom ảnh liên tục**.

## 31. VỊ TRÍ THƯ MỤC MÁY NGƯỜI DÙNG — ĐÃ THỂ HIỆN TRONG ẢNH CHỤP

Đường dẫn breadcrumb của Windows Explorer:

```text
Downloads > Youtube 2 > SangTacTruyenTuTien > BUILD FINAL CLIP
Downloads > Youtube 2 > SangTacTruyenTuTien > 03-MANUSCRIPTS > approved
```

Cấu trúc cần dựa vào khi hướng dẫn agent:

```text
SangTacTruyenTuTien/
├── 03-MANUSCRIPTS/
│   └── approved/
│       ├── CHUONG-0001-FINAL.md
│       ├── CHUONG-0002-FINAL.md
│       ├── CHUONG-0003-FINAL.md
│       ├── CHUONG-0004-FINAL.md
│       ├── CHUONG-0005-FINAL.md
│       ├── CHUONG-0006-FINAL.md
│       └── CHUONG-0007-FINAL.md
└── BUILD FINAL CLIP/
    ├── thumbnail-part-1.png
    ├── DANH-SACH-ANH-TAP-01-AGENT.csv
    ├── PROMPT-DUNG-CHUNG-CHO-AGENT.md
    ├── README.md
    └── STORYBOARD-ANH-TAP-01.md
```

**Không biết ký tự ổ đĩa/đường dẫn tuyệt đối từ ảnh chụp**, vì chỉ hiển thị từ thư mục `Downloads`. Agent có quyền truy cập máy cần **tự phát hiện đường dẫn đầy đủ**. ChatGPT trong session mới **không mặc nhiên đọc được ổ đĩa trên máy Windows**; muốn phân tích file thực tế, người dùng phải upload hoặc dùng công cụ có quyền kết nối.

## 32. PROMPT TỔNG CHỈ HUY ĐÃ SOẠN CHO AGENT DỰNG VIDEO FINAL

- Trong hội thoại, trợ lý đã giao **một prompt rất chi tiết** có tiêu đề **“NHIỆM VỤ: SẢN XUẤT VIDEO AUDIO TRUYỆN TU TIÊN — TẬP 1 FINAL”** (writing block trong chat, **không có xác nhận đã lưu thành file**). Nếu session mới cần chỉnh prompt, hãy yêu cầu người dùng đưa lại prompt hoặc dựa vào tóm tắt này, **không tuyên bố đã trực tiếp chạy agent**.
- **Mục tiêu:** Từ 7 chương FINAL + storyboard + thumbnail → giọng kể nữ tiếng Việt → ảnh minh họa → image-to-video/chuyển động → ghép dựng khớp voice → xuất MP4 upload YouTube.
- **YÊU CẦU GIỌNG KỂ BẮT BUỘC:** Agent **tự tạo TTS giọng NỮ tiếng Việt**, trẻ trung trưởng thành, **trong trẻo, sáng, ấm, dễ nghe, phát âm rõ chữ**, không rít/chói/giọng trẻ con; tốc độ vừa phải, ngắt nghỉ dấu câu tự nhiên, có cảm xúc theo cảnh hài/chiến đấu/bí ẩn/đồng môn. **Một giọng và một cấu hình xuyên suốt 7 chương**, không đổi giọng từng chunk, không nhầm tên nhân vật; giữ lời thoại nguyên văn, chỉ điều chỉnh biểu cảm/nhịp đọc.
- **Thứ tự dựng nên giữ:** Đọc 7 file FINAL → lọc metadata Markdown ra khỏi TTS → tạo audio theo chương → kiểm tra đối chiếu văn bản/phát âm → ghép audio liền mạch, ngắt chương tự nhiên khoảng 1,5–3 giây → dựa trên audio thực tế để gắn cảnh → tạo ảnh và clip chuyển động → đồng bộ bằng mốc lời đọc → dựng MP4 → kiểm tra bản xuất. **TTS trước để hình bám theo truyện**, không ép nhanh/chậm voice để vừa clip.
- **Các điều cấm:** Không sửa cốt truyện, không cắt/lược/đọc thiếu câu, không chèn intro quảng cáo/CTA mới; không đọc metadata DRAFT/FINAL và cú pháp Markdown; không mất/lặp chữ ở ranh giới chunk/chương; không tự chế cảnh trái truyện; không dùng 217 ảnh chỉ để đủ số; không slideshow đứng hình rung/zoom máy móc; không lặp hoặc tua ngược clip ngắn; không dùng nhạc bản quyền thiếu phép, không để nhạc át voice; không báo hoàn thành nếu chưa có file MP4 thật.
- **Phong cách ảnh:** Tiên hiệp cổ phong điện ảnh, 16:9, nhân vật đẹp nhất quán khuôn mặt/trang phục/vũ khí; Tạ Hành Chu **đao tu**, chưa có tu vi/vũ khí/công pháp vượt nội dung FINAL; Kỷ Thanh La và đồng môn giữ thương tích/trang phục theo từng sự kiện.
- **Đồng bộ:** Storyboard có câu dẫn/mốc truyện; agent nên dùng **forced alignment** hoặc so khớp đoạn đọc, kiểm tra thủ công các điểm không chắc; mỗi ảnh/clip phải xuất hiện đúng thời điểm lời kể, **không chia đều 217 mục cho 120 phút**. Tạo thêm góc máy nếu voice dài; chuyển động phù hợp cảnh (gió, sương, tay áo, bước đi, giao đấu, đường đao...).
- **Định dạng video yêu cầu:** 1920×1080, 16:9, 30 FPS, H.264 trong MP4, AAC 48 kHz, không watermark; giữ đúng thời lượng giọng đọc thực tế, **không ép đúng 120 phút**.
- **Thư mục do agent tạo:** `BUILD FINAL CLIP/WORK` (audio từng chương, ảnh, clip, project, timeline) và `BUILD FINAL CLIP/OUTPUT` (xuất thành phẩm); không sửa `approved`.
- **Đầu ra được yêu cầu (tên đề xuất trong prompt):**
  - `BUILD FINAL CLIP/OUTPUT/TONG-MON-BI-TRUY-SAT-TAP-01-FINAL.mp4`
  - `BUILD FINAL CLIP/OUTPUT/TAP-01-VOICE-FULL.wav`
  - `BUILD FINAL CLIP/OUTPUT/TAP-01-TTS-SCRIPT.txt`
  - `BUILD FINAL CLIP/OUTPUT/TAP-01-TIMELINE.csv`
  - `BUILD FINAL CLIP/OUTPUT/TAP-01-QA-REPORT.md`
- **QA cần có:** đủ 7 chương, không lặp/thiếu câu giữa các chương, phát âm đúng Tạ Hành Chu/Kỷ Thanh La/Vãn Ninh/A Thạch/Tam trưởng lão/Trác Cửu, giọng ổn định, sạch lỗi ghép, ảnh bám đúng truyện, không lặp cảnh vô lý, không black frames/lỗi codec, kiểm tra phát được MP4 từ đầu tới cuối. Có lỗi phải sửa rồi mới coi FINAL.
- **Không xác nhận đã tạo voice, ảnh hay video:** đến thời điểm ghi context, chỉ có **prompt và tài liệu đầu vào**, chưa có báo cáo agent/video xuất thực tế từ người dùng.

## 33. GIT VÀ EVIDENCE — CÁCH LÀM ĐÃ ĐƯỢC NGƯỜI DÙNG YÊU CẦU SỬA

- Người dùng phản hồi trực tiếp: **“hạn chế commit nhiều lần, chốt 1 chương rồi commit luôn cứ commit theo từng hành động vậy không hợp lý”**.
- **QUY TẮC MỚI CÓ ƯU TIÊN CAO:** Không commit riêng mỗi DRAFT V1/V2, mỗi lời góp ý, mỗi chỉnh sửa hay mỗi file lặt vặt. Sau khi user review/chốt **một chương FINAL**, có thể commit một lần gồm FINAL và bằng chứng liên quan. Khi user **chốt đồng thời Chương 3–7**, trợ lý đã hướng dẫn **một commit cho cả 5 chương**; tránh spam commit.
- Giữ các bản nháp và nhận xét để làm bằng chứng nguyên tác; có thể lưu locally trong lúc review rồi gom vào commit khi FINAL; không bỏ mất lịch sử, không chỉnh nội dung đã FINAL nếu không được giao.
- Trong hội thoại, trợ lý đã cung cấp lệnh `git add`, `git commit`, `git push` cho Chương 1, Chương 2, Chương 3–7. **Không có xác nhận cụ thể về việc các lệnh ấy đã được người dùng chạy/push thành công**. **Ảnh chụp cho thấy file đã nằm trong thư mục dự án trên máy**, không chứng minh Git remote có commit tương ứng.
- Các log bằng chứng trước đây như `DECISIONS.md`, `EVIDENCE-LOG.md`, `04-CREATIVE-EVIDENCE` đã được lập từ đầu; có thể cập nhật khi có bản FINAL và báo cáo QA sản xuất. Không invent hash Git, mã EV, cam kết YPP, ngày giờ render hoặc URL YouTube.
- **Context file này có thể lưu một lần** vào repo theo đường dẫn context đang dùng. Khi cập nhật theo lô, hướng dẫn **commit một lần có chủ đích**, không bắt user commit liên tục chỉ để hoàn tất cuộc trò chuyện.

## 34. NHỮNG VIỆC CHƯA HOÀN THÀNH VÀ HƯỚNG TIẾP TỤC

**Đã hoàn thành về mặt nội dung/đầu vào:** 7 chương đã được tác giả duyệt FINAL; thumbnail Tập 1; tài liệu storyboard 217 cảnh, CSV/README/prompt tạo ảnh; prompt tổng giao agent sản xuất giọng nữ và MP4.

**Chưa có bằng chứng hoàn thành trong chat:** File TTS/WAV, các clip image-to-video, file MP4 FINAL, QA report thực, kết quả thời lượng, xác nhận agent đã dựng, xác nhận đăng video lên YouTube, URL tập 1. Không giả định kênh đã đủ điều kiện kiếm tiền.

**Có hai nhánh công việc hợp lệ tùy câu hỏi user tiếp theo:**
1. **Production Tập 1:** Nếu user cho biết agent đã chạy hoặc gửi video/log, hãy kiểm tra sản phẩm thực tế, phát âm giọng nữ, đồng bộ ảnh, trùng lặp voice, bản quyền nhạc/TTS, thời lượng và chất lượng cảnh. Nếu user muốn cải tiến prompt, chỉ sửa đúng phần gây lỗi. Trước khi nói “video sẵn sàng đăng”, phải có file MP4 được kiểm tra thực tế và quyền dùng tài nguyên được làm rõ.
2. **Sáng tác tiếp:** Khi user yêu cầu **Chương 8** hoặc arc tiếp theo, yêu cầu mở nguyên văn Chương 7 FINAL và các chương có liên quan; viết từng chương có cảnh và mạch nối; **giữ Tạ Hành Chu**, không làm mạnh quá sớm; review rồi chốt; commit theo FINAL. Nếu user yêu cầu mở rộng Story Bible (hệ thống cảnh giới, Vạn Chiến Tàng Phong Thể, tuyến đạo lữ), có thể làm song song nhưng không được sửa hồi tố 7 chương FINAL.

**Chưa chốt ở tầng quy hoạch dài kỳ:** Hệ thống cảnh giới tổng quát, bản hồ sơ thiết kế hoàn chỉnh Vạn Chiến Tàng Phong Thể, xung đột toàn thế giới, nguồn gốc quá khứ các sư tỷ/tông chủ và số lượng đạo lữ. Không suy diễn từ ý tưởng lịch sử ở mục 18–25 thành cơ chế chính thức đã công khai trong 7 chương đầu. Tuy vậy, **những gì được viết trong 7 chương FINAL là CANON**, ngay cả khi trước đó từng nằm trong phần DRAFT thiết kế.

## 35. PROMPT NGẮN ĐỂ DÁN VÀO SESSION CHATGPT MỚI (CẬP NHẬT V4.0)

> Tôi gửi file **CONTEXT_KENH_AUDIO_TRUYEN_TU_TIEN v4.0 ngày 25/11/2026**. Hãy **đọc mục 26–35 trước**, sau đó tham khảo mục 1–25 như lịch sử. **Dự án hiện đã có 7 chương FINAL** của truyện *Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát*: các file `03-MANUSCRIPTS/approved/CHUONG-0001-FINAL.md` đến `CHUONG-0007-FINAL.md`. Nam chính **Tạ Hành Chu**, Thanh Vân Tông, Kỷ Thanh La, Vãn Ninh, A Thạch, Tam trưởng lão, Trác Cửu… Khi viết tiếp, hãy mở **nguyên văn FINAL** chứ đừng dựa vào bản tóm tắt context. Lời kể ưu tiên **Tạ Hành Chu/Hành Chu**, không dùng “người tán tu” để chỉ main, tránh lặp câu ở ranh giới chương và không tự sửa chương FINAL. **Chỉ commit Git sau khi chương được tôi chốt FINAL**, không commit theo từng sửa nháp. Tập audio số 1 đã có **thumbnail `thumbnail-part-1.png`**, storyboard/CSV **217 ảnh** và prompt tổng cho agent dựng video, yêu cầu **tự tạo giọng kể NỮ tiếng Việt trong trẻo, rõ ràng, nhất quán** rồi đồng bộ hình ảnh và xuất MP4. Các tư liệu đầu vào đã được tôi đặt ở `SangTacTruyenTuTien/BUILD FINAL CLIP`, chương FINAL ở `03-MANUSCRIPTS/approved`; **chưa xác nhận agent đã làm xong voice hay MP4**. Bạn hãy dựa đúng trạng thái này để tiếp tục công việc tôi giao, không tự viết chương hoặc tuyên bố video hoàn thành.

**Quy tắc duy trì context:** Khi kết thúc một đợt sáng tác/sản xuất có quyết định mới, hãy **append một mục cập nhật có ngày + trạng thái DRAFT/FINAL + file nguồn**, đặt mức ưu tiên mới lên đầu file; không xóa lịch sử đã duyệt, không suy đoán trạng thái Git/agent và tuyệt đối không giả mạo QA. Nên giữ thêm một `NEXT-SESSION-HANDOFF` ngắn khi dự án kéo dài hàng trăm chương, nhưng không bắt người dùng tạo/commit tài liệu mới trừ khi họ yêu cầu.

---

# CẬP NHẬT V5.0 — GITHUB ĐÃ KẾT NỐI, QUY TẮC BÀN GIAO VÀ CONTINUITY DÀI KỲ (25/11/2026)

> **ƯU TIÊN CAO NHẤT KHI MỞ SESSION MỚI: ĐỌC MỤC 36–42.** Phần 1–35 được bảo lưu làm lịch sử và tài liệu tham khảo; nếu có khác biệt về tiến độ, trạng thái kết nối hoặc quy trình, thông tin **đã kiểm chứng mới hơn** trong các mục này được ưu tiên. Bản thảo chương FINAL nguyên văn là nguồn truyện chuẩn; mọi khẳng định chưa có nguồn hoặc chỉ do nhân vật suy đoán không được nâng thành sự thật CANON.

## 36. HƯỚNG DẪN TỰ KHỞI ĐỘNG CHO MỌI SESSION MỚI — KHÔNG ĐƯỢC LÀM TẮT

**Người dùng chỉ cần upload đúng file context v5.0 này và nói muốn tiếp tục dự án; không phải dán thêm prompt dài hay tải lên hàng trăm chương.** Assistant session mới phải chủ động thực hiện những việc dưới đây, sau đó chờ nhiệm vụ cụ thể:

1. **Đọc context:** Ưu tiên mục 36–42, sau đó 26–35 và các lịch sử quyết định trong 18–25 khi cần. Đừng dùng các mục lịch sử lỗi thời để kết luận 'chưa viết chương' hoặc 'chưa đặt tên nam chính'.
2. **Kiểm tra kết nối GitHub trong session HIỆN TẠI:** Dùng công cụ GitHub đang có để truy cập chính xác `dinhngocquanghuy/SangTacTruyenTuTien`. **Không giả định** lần kết nối thành công trong session trước bảo đảm tất cả session sau có quyền giống nhau. Nếu không truy cập được, nêu rõ lỗi/quyền thiếu, yêu cầu người dùng kết nối lại hoặc cấp quyền trước khi sáng tác; không bịa từ ký ức.
3. **Xác minh repo và nội dung:** Kiểm tra nhánh chính (lần xác minh gần nhất là `main`), duyệt file liên quan trong `README.md`, `DECISIONS.md`, `EVIDENCE-LOG.md`, `01-STORY-BIBLE/` nếu tồn tại, và **đọc đủ nguyên văn** `03-MANUSCRIPTS/approved/CHUONG-0001-FINAL.md` đến `CHUONG-0007-FINAL.md` trước đợt tiếp nối ban đầu. Các file có trong GitHub đã được thử đọc thành công một phần đầu từng file ở session 25/11/2026, nhưng session mới vẫn phải tự kiểm tra.
4. **Lập sơ bộ bản đồ nhất quán từ nguồn:** Ai ở đâu, đang biết gì, quan hệ và thương tích ra sao; tu vi, vũ khí/vật phẩm, sự kiện theo thời gian, dấu hiệu thể chất; các manh mối/âm mưu mới chỉ **nghi ngờ**, chưa tiết lộ. Tham chiếu **chương và đoạn có thật**, đừng tự đặt chứng cứ hay tình tiết.
5. **Phân loại trạng thái mọi thông tin:** `CANON` (đã xuất hiện trong chương FINAL hoặc được user chốt rõ), `DRAFT` (phương án chưa duyệt), `MYSTERY` (bí mật hoặc giả thuyết chưa xác nhận), `PLANNED` (định hướng tương lai, chưa xảy ra), `UNKNOWN` (thiếu nguồn). Giữ ranh giới giữa chúng; không tự đưa DRAFT thành sự thật chỉ vì hấp dẫn.
6. **Kiểm tra điểm nối hiện tại:** Đọc cuối Chương 7 nguyên văn, đồng thời các phục bút từ chương trước; không nhắc lại nguyên văn cliffhanger ở đầu Chương 8, không làm mất thương tích, vật phẩm và hậu quả.
7. **Báo cáo ngắn:** Nêu các file đã thật sự đọc, trạng thái FINAL mới nhất, tình tiết/điểm treo quan trọng, mục chưa rõ và **một bước hợp lý tiếp theo**. **Chưa tự viết Chương 8, dựng video hay chỉnh Git** nếu người dùng chưa giao.

**Đặc biệt:** File context không phải một 'câu lệnh cho phép tự thao tác mọi thứ'. Các hoạt động ghi/sửa repository, thay đổi bí mật thế giới, sửa chương FINAL và tạo file mới cần đúng phạm vi người dùng giao. Nếu một nguồn trong GitHub mâu thuẫn với lời kể trong context, chỉ ra nguồn và sự khác nhau để người dùng quyết định khi cần.

## 37. KẾT NỐI GITHUB — TRẠNG THÁI ĐÃ XÁC MINH 25/11/2026

| Trường | Kết quả đã xác minh trong session 25/11/2026 |
|---|---|
| Dịch vụ | GitHub connector dành cho ChatGPT |
| Repository duy nhất của installation được liệt kê | `dinhngocquanghuy/SangTacTruyenTuTien` |
| Nhánh mặc định | `main` |
| Kiểu chọn repository của GitHub App | `selected` (chỉ chọn một số repository) |
| Danh sách repo trả về theo installation | Chỉ `SangTacTruyenTuTien` |
| Khả năng truy cập | Đọc được `README.md` và đã gọi đọc thành công cả bảy path `CHUONG-0001-FINAL.md` ... `CHUONG-0007-FINAL.md` |
| Quyền được trả về | `pull: true`, `push: true` (có khả năng đọc/ghi, nhưng **không được tự ghi**) |
| Visibility khi kiểm tra | `public` — đây là trạng thái ở thời điểm kiểm tra, có thể thay đổi sau này |

- **Lưu ý bảo mật:** Repo Public có thể bị người khác xem. Người dùng từng thử chuyển Private nhưng SourceTree không push được; sau đó **chủ động chọn giữ Public tạm thời**, sẽ xử lý Private sau. **Không tự đổi visibility, remote hay xác thực SourceTree** nếu người dùng không yêu cầu.
- Kết nối GitHub là **cơ chế truy xuất file**, không phải 'trí nhớ 1.000 chương' tự động. Session mới phải sử dụng công cụ đọc/tra cứu thực tế, nêu rõ những file đã đọc, và không tuyên bố quyền truy cập chắc chắn nếu không kiểm tra lại.
- Không cần yêu cầu người dùng upload lại toàn bộ 7 chương nếu repo đã truy cập được. Nếu repo không truy cập, giải quyết kết nối trước; tránh bắt user chép lại hàng trăm chương bằng tay.
- **Git lịch sử:** Đã có 7 chương FINAL trong GitHub, nhưng không suy diễn các bản DRAFT, evidence, sản phẩm video hay context mới đã được push nếu chưa kiểm chứng. Người dùng yêu cầu **chỉ một commit sau mỗi chương/đợt chương đã duyệt FINAL**, không spam commit cho thao tác nhỏ.

## 38. NGUYÊN TẮC CANON — KHÔNG CHO SESSION MỚI TỰ VIẾT LỆCH CỐT TRUYỆN

**Ưu tiên theo loại thông tin, tránh 'ghi đè lịch sử':**

1. **Nội dung truyện đã chốt:** Nguyên văn file `03-MANUSCRIPTS/approved/CHUONG-XXXX-FINAL.md` là chuẩn về những gì đã xảy ra, được nói và được mô tả trong truyện. Không sửa hồi tố 7 chương nếu người dùng không giao.
2. **Quyết định thiết kế được user xác nhận:** Trích dẫn/ghi nhận trong `DECISIONS.md`, hồ sơ Story Bible đã duyệt và context lịch sử. Đây là giới hạn cho việc viết **tương lai**, nhưng các phương án còn DRAFT chưa tự trở thành luật thế giới bất biến.
3. **Sự thật trong thế giới truyện khác với lời nhân vật:** Câu nói, suy đoán, lời đe dọa, tin đồn và phán đoán của nhân vật là **thông tin được kể**, không mặc nhiên là sự thật khách quan. Chẳng hạn, dấu đóng chìm trong Chương 7 là **manh mối**, không đủ để tự kết luận Thanh Vân Tông chắc chắn là thủ phạm.
4. **Outline/nhật ký phục bút:** Kế hoạch tương lai là `PLANNED`, có thể điều chỉnh bằng review. Chi tiết chưa tiết lộ phải có kiểm soát truy cập về mặt cốt truyện (ai biết gì, ở chương nào), tránh spoil sớm.
5. **Bản nháp AI hoặc suy luận không có nguồn:** Không được tự nâng lên CANON, không dùng để thay thế bản FINAL khi hai bên không khớp.

**Quy ước viết:** Tên nam chính **Tạ Hành Chu / Hành Chu**; tránh 'người tán tu' như đại từ và tránh lạm dụng 'hắn'. Nam chính ở giai đoạn đầu không phải cao thủ giả vờ, sử dụng đao và rèn luyện thể chất; thể chất đặc biệt chưa thức tỉnh hoàn chỉnh. Giữ hài hước, lòng nhân hậu, trí thông minh thể hiện qua hành động; có hậu quả thương tích/tu luyện. Không tiết lộ ngay bí mật đồng môn/tông chủ hoặc tự gán đạo lữ chỉ vì các tuyến romance nằm trong định hướng.

**Lỗi phải kiểm tra mỗi chương:** Lặp câu giữa ranh giới các chương; chuyển địa điểm/giờ giấc vô lý; nhân vật biết điều chưa được tiết lộ; thương tích biến mất; phục hồi/cảnh giới tăng không có nguyên nhân; thay loại vũ khí; tuổi/tên/quan hệ mâu thuẫn; tiết lộ bí mật chưa đến lúc; tên gọi chính bị đổi; tình tiết đã giải quyết bị kể như chưa xảy ra.

Nếu phát hiện mâu thuẫn trong nguồn FINAL, **báo người dùng cùng đoạn trích dẫn có thật** để xử lý, không tự chỉnh một chương đã chốt.

## 39. THIẾT KẾ CONTINUITY SYSTEM — HỆ THỐNG QUẢN LÝ 1.000+ CHƯƠNG

**Chưa có xác nhận hệ thống sau đây đã được tạo trong GitHub. Đây là kiến trúc ĐỀ XUẤT cần thiết lập từ nguyên văn 7 chương FINAL rồi cập nhật theo mỗi chương mới.** Tên thư mục/path bên dưới là gợi ý, không khẳng định đang tồn tại. Có thể tận dụng cấu trúc đang có để khỏi tạo trùng.

| Lớp dữ liệu | Chức năng | File gợi ý (chưa tạo) |
|---|---|---|
| CANON REGISTER | Các quy tắc và quyết định user chốt, phân biệt DRAFT và PLANNED | `01-STORY-BIBLE/CANON-REGISTER.md` |
| CHARACTER STATE | Hồ sơ người, trạng thái gần nhất, quan hệ, thương tích, ai biết gì | `05-CONTINUITY/CHARACTER-STATE.md` |
| CHAPTER INDEX | Mỗi chương FINAL một bản ghi ngắn, sự kiện và tham chiếu chương/đoạn | `05-CONTINUITY/CHAPTER-INDEX.md` |
| TIMELINE & POWER | Thời gian/địa điểm, cảnh giới, kỹ năng, công pháp, vật phẩm, giới hạn | `05-CONTINUITY/TIMELINE-POWER-ITEMS.md` |
| PLOT THREADS | Phục bút, bí mật, câu hỏi mở, lần gieo, lần cập nhật, lần giải đáp | `05-CONTINUITY/OPEN-PLOT-THREADS.md` |
| CURRENT STATE / HANDOFF | Điểm kết mới nhất, danh sách nguồn cần đọc và đúng bước đang chờ | `05-CONTINUITY/NEXT-CHAPTER-HANDOFF.md` |

**Các quy tắc vận hành để quy mô truyện lớn không làm sai lệch:**

- Không nén cả nghìn chương thành một đoạn tóm tắt rồi coi là đủ. **Giữ nguyên bản thảo FINAL trong GitHub**; tài liệu liên tục chỉ là chỉ mục dẫn tới nguồn, không phải bản thay thế.
- Khi có 1.000 chương, session mới đọc **CANON + CURRENT STATE + PLOT THREADS + mục lục/đoạn liên quan và 1–3 chương gần nhất** (tùy dung lượng và công việc), sau đó tìm đọc **nguyên văn các chương cũ có manh mối liên quan**. Không cần nạp tất cả 1.000 chương vào một cuộc trò chuyện.
- Với **bước khởi tạo hiện tại chỉ có 7 chương**, session mới nên đọc đủ cả 7 và dựng continuity v1 dựa trên nguồn gốc; đánh dấu `UNKNOWN` nếu một mục không có chứng cứ, không suy ra tuổi/cảnh giới chỉ từ hình ảnh bìa.
- Mỗi bản ghi phục bút nên có mã ổn định, `status: OPEN/RESOLVED`, `introduced_in`, `last_seen`, nhân vật biết gì, mô tả nội dung, và **đường dẫn/chương/câu dẫn có thật**. Chỉ có trạng thái `RESOLVED` sau khi có chương FINAL xác nhận.
- Mỗi bản ghi chương nên có `chapter_id`, tiêu đề, thời gian/địa điểm tương đối, nhân vật xuất hiện, hành động quan trọng, thay đổi cảnh giới/trạng thái/vật phẩm, thoại/ý nghĩa quan trọng, phục bút mở/đóng và `source_path`.
- Không tự đổi tên file, nhận định/chuyển tình tiết thành sự kiện mới khi lập bảng; phân biệt **thông tin người kể xác nhận** với **tin đồn/giả thuyết do nhân vật nói**.
- Theo dõi mạch nhân vật và mục tiêu **dài hạn**, nhưng kế hoạch tình tiết không được 'ép' người viết lặp mô típ hoặc làm mất nhịp truyện; mỗi lần tạo mới phải sáng tạo trên nền CANON.
- Sau mỗi chương FINAL, cập nhật dữ liệu liên tục và review kiểm tra mâu thuẫn **trước khi commit chung**. Sau 10–20 chương hoặc hết một arc, thực hiện một vòng continuity audit sâu, đối chiếu với những chương nguồn thực tế.

## 40. QUY TRÌNH SÁNG TÁC VÀ GIT TỪ CHƯƠNG 8 TRỞ ĐI

1. **Nhận yêu cầu:** User chỉ định viết Chương 8 hoặc nhóm chương; không tự viết chỉ vì đã nhận file context.
2. **Đọc trước khi viết:** Mở Chương FINAL gần nhất, continuity/canon liên quan, và truy xuất chính xác các chương cũ có nhân vật/bí mật đang tiếp diễn.
3. **Lập kiểm tra ngắn:** Xác nhận sự kiện đang treo, nhân vật biết gì, điểm bắt đầu chương tiếp và những điều cấm mâu thuẫn. Nếu người dùng muốn, có thể trình bày outline để duyệt trước khi viết.
4. **Viết DRAFT:** Văn xuôi tiểu thuyết với cảnh/đối thoại thực, theo tên nhân vật và nhịp audio, không chép lại câu cuối chương trước.
5. **Review/hiệu chỉnh:** User nhận xét; assistant cập nhật DRAFT V2/V3...; không commit theo từng lần thay đổi.
6. **Chỉ khi user nói CHỐT FINAL:** Xuất bản FINAL nguyên văn đã duyệt. Ghi nhận kết quả review, cập nhật Continuity, Chapter Index, Open Plots, Character State; kiểm tra sự mâu thuẫn và ranh giới chương.
7. **Một commit có chủ đích:** Gộp FINAL + tài liệu liên quan trong cùng commit/đợt user chốt; không push nếu chưa được user yêu cầu hoặc cho phép. Nếu connector có quyền ghi, vẫn phải hỏi/làm đúng phạm vi nhiệm vụ; không dùng quyền push để tự sửa tác phẩm.
8. **Handoff:** Ghi trạng thái hiện tại và các mục cần đọc, giúp session sau tiếp tục đúng việc, không bắt user giải thích lại.

## 41. PHÂN BIỆT TẬP AUDIO 1 VÀ TẬP 2 — KHÔNG TỰ ĐÁNH ĐỒNG

- **Tập 1** đã có **Chương 1–7 FINAL**, thumbnail nhãn `TẬP 1`, storyboard 217 cảnh, prompt agent tự sản xuất voice NỮ rõ, trong trẻo, dễ nghe và dựng video; **không có xác nhận** đã dựng WAV/MP4 hay upload YouTube thành công.
- **Tập 2** dự kiến tiếp từ **Chương 8**, số chương thực tế căn theo thời lượng TTS và mạch truyện; không mặc định 7 chương/tập là luật bắt buộc, không ép đoạn cuối cắt dở. **Chưa có Chương 8 FINAL** tại thời điểm cập nhật.
- Nếu nhận yêu cầu về **production Tập 1**, kiểm tra file thực tế do user/agent cung cấp, không lẫn với yêu cầu viết Chương 8.
- Nếu nhận yêu cầu **sáng tác Tập 2**, phải dựa trên bản thảo FINAL và continuity, không xây lại premise/nhân vật/hệ thống từ đầu hoặc đề xuất một câu chuyện khác.
- Nếu user hỏi **bước tiếp theo**, ưu tiên thiết lập **Continuity System V1 từ 7 chương FINAL** rồi mới triển khai Chương 8, trừ khi người dùng muốn đi thẳng vào sản xuất hoặc viết truyện.

## 42. CHECKLIST BÀN GIAO VÀ CÂU LỆNH MỞ SESSION MỚI (ĐÃ TÍCH HỢP)

**Bộ điều kiện cần xác nhận trong session mới:**

- [ ] Đã đọc mục 36–42 + mục 26–35 của file context này.
- [ ] Đã thử và xác nhận GitHub connector thực sự truy cập được **đúng** `dinhngocquanghuy/SangTacTruyenTuTien`.
- [ ] Đã đọc đủ 7 chương FINAL (hoặc báo rõ chương không truy cập được), thay vì đoán từ mô tả.
- [ ] Đã phân biệt các quy tắc được user chốt, đề xuất DRAFT, manh mối MYSTERY và kế hoạch PLANNED.
- [ ] Đã xác nhận Chương 7 là điểm kết hiện tại và có các phục bút cần nối sang Chương 8.
- [ ] Đã kiểm tra tài liệu Continuity có thật trên GitHub chưa; **không coi kiến trúc đề xuất trong mục 39 là file đã tạo**.
- [ ] Đã báo cáo ngắn tình trạng, rủi ro mâu thuẫn và **chỉ một bước tiếp theo**.
- [ ] **Chưa tự viết, chưa tự tạo/commit/sửa repository** khi chưa được user giao.

**Người dùng mở session mới chỉ cần gửi file context này và nhắn một câu bình thường như 'Đọc file context và tiếp tục dự án'.** Assistant phải tự hiểu và thực hiện quy trình trên, không bắt người dùng copy lại một prompt riêng. Nếu có nhiệm vụ cụ thể kèm theo (ví dụ 'thiết kế Continuity V1', 'viết Chương 8', 'kiểm tra MP4 Tập 1'), làm đúng phạm vi yêu cầu và dùng GitHub làm nguồn đối chiếu.

**Không hứa có trí nhớ hoàn hảo.** Hệ thống an toàn hơn là kết hợp bản thảo gốc + danh mục chứng cứ/canon + truy xuất các chương liên quan + QA trước FINAL. Mục tiêu là chương thứ 1.000 có thể tra đúng các sự kiện thật của những chương đầu, không để session tự bịa lại lịch sử.

---

# CẬP NHẬT V6.0 — TIÊU CHUẨN KỸ THUẬT VÀ QUY TRÌNH TẠO VOICE AUDIO ĐỒNG BỘ CHO KÊNH (26/11/2026)

> **QUY CHUẨN BẮT BUỘC CHO TOÀN BỘ CÁC TẬP TỪ TẬP 2 TRỞ ĐI:** Toàn bộ video audio truyện của kênh phải dùng chung một loại voice, cùng âm sắc, cùng tốc độ đọc 1.25x (giữ nguyên cao độ), cùng chuẩn định dạng 48kHz Stereo và cùng khoảng ngắt 2.0s giữa các chương để đảm bảo người nghe trải nghiệm như một người kể chuyện duy nhất xuyên suốt hàng trăm tập.

## 43. TIÊU CHUẨN CẤU HÌNH VOICE TTS CHÍNH THỨC

| Thông số | Giá trị chuẩn của kênh | Giải thích kỹ thuật & Lý do lựa chọn |
| :--- | :--- | :--- |
| **Engine TTS** | **Google Text-to-Speech (`gTTS`)** | Độ ổn định 100%, không bị giới hạn token / lỗi 403 WebSocket như Edge-TTS khi tạo hàng trăm file liên tục. |
| **Ngôn ngữ (`lang`)** | `vi` (Tiếng Việt) | Phát âm chuẩn tiếng Việt phổ thông, tròn vành rõ chữ, chuẩn dấu câu. |
| **Top-Level Domain (`tld`)** | `com` | Âm sắc nữ miền Bắc/Việt Nam chuẩn, trẻ trung, trong trẻo, tự nhiên, truyền cảm. |
| **Tốc độ đọc chuẩn (Playback Speed)** | **1.25x** | Tốc độ gốc 1.0x (~145 từ/phút) hơi chậm đối với truyện tiên hiệp; tốc độ 1.25x (~180–190 từ/phút) giúp nhịp kể nhanh, dứt khoát, cuốn hút và giảm cảm giác lê thê. |
| **Thuật toán tăng tốc** | **FFmpeg `atempo=1.25`** | **BẮT BUỘC DÙNG `atempo` ĐỂ GIỮ NGUYÊN CAO ĐỘ (PRESERVE PITCH)**. Tuyệt đối không đổi sample rate hay tăng pitch vì sẽ làm giọng the thé hoặc bị hiệu ứng sóc chuột (chipmunk). |
| **Định dạng âm thanh phân cảnh** | **WAV (PCM 16-bit, 48,000 Hz, Stereo)** | Lệnh chuẩn: `ffmpeg -i in.mp3 -ar 48000 -ac 2 -c:a pcm_s16le out.wav`. |
| **Định dạng Master Audio** | **WAV (PCM 16-bit, 48,000 Hz, Stereo)** | Ghép liên tục các phân cảnh và các chương theo đúng thứ tự. |
| **Độ dài khoảng ngắt giữa các chương** | **2.0 giây im lặng tuyệt đối** | Lệnh tạo: `ffmpeg -f lavfi -i anullsrc=r=48000:cl=stereo -t 2.0 -c:a pcm_s16le silence_2s.wav`. Tránh ngắt quá lâu (>3s) hoặc dính câu (<1s). |
| **Chuẩn Audio mux vào Video MP4** | **AAC, Bitrate 192 kbps, 48,000 Hz Stereo** | Lệnh mux: `-c:a aac -b:a 192k -ar 48000`. Âm thanh trong trẻo, không bị nén vỡ dải tần. |

---

## 44. QUY TRÌNH TIỀN XỬ LÝ VĂN BẢN (TEXT PREPROCESSING) TRƯỚC KHI ĐỌC

Để giọng đọc mượt mà, không đọc nhầm các ký tự rác và không gây khó chịu cho người nghe:

1. **Trích xuất từ nguồn chuẩn:** Chỉ lấy văn bản từ thư mục bản thảo đã duyệt `03-MANUSCRIPTS/approved/CHUONG-XXXX-FINAL.md`.
2. **Loại bỏ siêu dữ liệu (Metadata stripping):**
   - Xóa bỏ các dòng tiêu đề kỹ thuật: `# CHƯƠNG...`, `DRAFT`, `FINAL`, `version:`, `Trạng thái:`, ghi chú tác giả, đường dẫn file.
   - Xóa bỏ toàn bộ ký hiệu định dạng Markdown: dấu sao `*`, dấu gạch dưới `_`, dấu thăng `#`, dấu ngoặc vuông `[]`, v.v. để AI không phát âm thành chữ "sao" hay "gạch".
3. **Quy tắc đọc tiêu đề chương:**
   - **Chỉ đọc tiêu đề chương đúng một lần** ở ngay đầu phân cảnh đầu tiên của chương tương ứng (Ví dụ: `Chương 8: ... Lời mở đầu...`).
   - Tuyệt đối không lặp lại tiêu đề chương ở các phân cảnh tiếp theo trong cùng chương đó.
4. **Không tự chèn tạp âm:**
   - Tuyệt đối không tự chèn lời quảng cáo, câu kêu gọi like/subscribe/CTA, intro/outro kênh vào giữa nội dung truyện.
   - Nội dung truyện phải thuần khiết, giữ nguyên vẹn 100% lời văn và hội thoại của tác giả.
5. **Chia đoạn phân cảnh theo Storyboard (Scene Slicing):**
   - Chia văn bản theo từng phân cảnh storyboard (thường từ 1 đến 3 câu văn, khoảng 15–40 từ/cảnh).
   - Đặt tên file audio phân cảnh thống nhất theo mã ảnh: `CXX-IYYY.wav` (ví dụ `C08-I001.wav`).

---

## 45. QUY TRÌNH KỸ THUẬT CODE SẢN XUẤT VOICE (PYTHON + FFMPEG)

Quy trình sản xuất tự động 5 bước đã được kiểm chứng chuẩn xác ở Tập 1:

### Bước 1: Tạo audio từng cảnh bằng gTTS
```python
from gtts import gTTS
import os, subprocess, time

# text_content là đoạn văn bản sạch của phân cảnh
tts = gTTS(text=text_content, lang="vi", tld="com")
tts.save(f"scenes/{image_id}.mp3")

# Chuyển đổi sang WAV chuẩn 48kHz Stereo
subprocess.run([
    "ffmpeg", "-y", "-i", f"scenes/{image_id}.mp3",
    "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
    f"scenes/{image_id}.wav"
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
```

### Bước 2: Tăng tốc độ đọc lên 1.25x bằng FFmpeg `atempo=1.25`
```python
# Tăng tốc độ 1.25x giữ nguyên cao độ giọng (chạy song song ThreadPoolExecutor)
subprocess.run([
    "ffmpeg", "-y", "-i", f"scenes/{image_id}.wav",
    "-filter:a", "atempo=1.25",
    "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
    f"scenes_125/{image_id}.wav"
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
```

### Bước 3: Ghép audio theo từng chương
```python
# Tạo file concat_ch_X.txt liệt kê tất cả scenes_125 của chương
# Sau đó ghép nhanh bằng copy stream:
subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", f"concat_ch_{ch_num}.txt", "-c", "copy",
    f"chapter_{ch_num:02d}.wav"
], check=True)
```

### Bước 4: Ghép toàn bộ các chương thành Master Voice
```python
# Nối các file chapter_XX.wav với silence_2s.wav ở giữa
# silence_2s.wav: ffmpeg -y -f lavfi -i anullsrc=r=48000:cl=stereo -t 2.0 -c:a pcm_s16le silence_2s.wav
subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", "concat_full.txt", "-c", "copy",
    "OUTPUT/TAP-0X-VOICE-FULL.wav"
], check=True)
```

### Bước 5: Tự động trích xuất phụ đề YouTube (SRT & VTT)
- Phân tách từng phân cảnh thành các câu ngắn (2 đến 5 giây, tối đa 2 dòng, khoảng 10–18 từ).
- Phân bổ thời gian theo tỷ lệ số từ của từng câu dựa trên thời lượng thực tế của phân cảnh.
- Xuất song song file `.srt` và `.vtt` chuẩn UTF-8 để tải trực tiếp lên YouTube Studio.

---

## 46. DỮ LIỆU ĐỐI CHỨNG CHUẨN TỪ TẬP 1 (BENCHMARK DATA)

Dùng các thông số sau để kiểm tra chéo (sanity check) khi sản xuất Tập 2 trở đi:

- **Số chương Tập 1:** 7 chương (Chương 1 đến 7).
- **Tổng số từ tiếng Việt:** 19,790 từ (1,540 đoạn văn).
- **Số phân cảnh minh họa:** 217 scenes.
- **Thời lượng đọc ở tốc độ 1.0x:** 02:03:26 (7,406 giây) — tương đương tốc độ trung bình 160 từ/phút.
- **Thời lượng đọc ở tốc độ 1.25x:** **01:38:47** (5,927 giây) — tương đương tốc độ trung bình ~200 từ/phút (bao gồm cả ngắt nghỉ tự nhiên giữa các câu).
- **Kích thước file Master Voice WAV:** 1,085.27 MB (1.08 GB).
- **Kích thước file Video MP4 1080p (ảnh tĩnh + voice 1.25x):** 728.54 MB.
- **Độ lệch giọng:** 0% (cùng một chất giọng nữ xuyên suốt từ giây đầu tiên đến giây cuối cùng).
- **Quy chuẩn video:** 100% ảnh tĩnh đứng yên tuyệt đối (`tune: stillimage`), phong cách tiên hiệp thanh lệ, không dùng hiệu ứng lia/rung lắc.



---

# CẬP NHẬT V7.0 — CHỐT CHƯƠNG 8–14, QUY TRÌNH 80 ẢNH TĨNH, HANDOFF TẬP 3 (26/11/2026)

## 47. TRẠNG THÁI THỰC TẾ VÀ QUYẾT ĐỊNH MỚI

- Người dùng yêu cầu viết liền mạch Chương 8–14 để duyệt Tập 2. Assistant đã viết đủ bảy chương dạng văn xuôi tiểu thuyết trong chat; người dùng nói nguyên văn **“ok chốt chương 8-14, cho tôi file để commit push lên git”**. Đây là phê duyệt FINAL ngày 26/11/2026, không còn DRAFT.
- Đã bàn giao ZIP `TAP-02-CHUONG-08-14-FINAL.zip`, chứa đúng 7 file dưới `03-MANUSCRIPTS/approved/`. Không tự viết lại văn bản đã duyệt. Bản ZIP được kiểm tra lại khi cập nhật context này. Tổng số từ từng được báo 17.037 (đếm khoảng trắng phần truyện, không phải số từ ngôn ngữ học); thời lượng TTS Tập 2 chưa đo, không ép 2 giờ.
- Trong session này GitHub connector `get_repo` đã trả kết quả truy cập đúng repo `dinhngocquanghuy/SangTacTruyenTuTien`, default branch `main`, visibility **public tại thời điểm kiểm tra**, không phải private như đề xuất lịch sử. Đã fetch bảy file FINAL 1–7; Chương 7 đọc đầy đủ, kết quả các chương khác có phần bị giới hạn hiển thị nên không khẳng định audit đủ toàn văn. Các chương 8–14 được bàn giao để user tự commit/push; chưa có xác nhận user đã push thành công, chưa kiểm tra remote có 8–14 hay chưa. Không tự đổi visibility.
- Đã tạo thumbnail Tập 2 đúng tiêu đề rút gọn “TÔNG MÔN BỊ TRUY SÁT”, nhãn “TẬP 2”. Bản đầu ghi “Từ Phàm Tu Tiên” là SAI tên và bị user bác bỏ. Chỉ dùng bản sửa `tông_môn_bị_truy_sát_tập_2.png`. Tên đầy đủ của truyện vẫn là **Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát**, kênh **Tiên Vực Ký**.
- Tập 2: đã bàn giao tài liệu sản xuất và SEO, **không có chứng cứ nghiệm thu video/audio, 80 ảnh, URL upload, hoặc kết quả YouTube**. Yêu cầu title/mô tả/tag không tự động chứng minh đã đăng.
- Tập 3: user chỉ định **Chương 15–21** là phạm vi tiếp theo. Chưa sáng tác/chưa FINAL/chưa có storyboard/voice/video/thumbnail Tập 3. Khi được giao viết, triển khai đủ bảy chương liên tục, không chỉ outline hoặc synopsis, không dừng sau một chương.

## 48. DANH MỤC NGUỒN FINAL TẬP 2

| Chương | Tiêu đề | Nguồn chuẩn |
|---|---|---|
| 8 | Món nợ của đệ tử mới | `03-MANUSCRIPTS/approved/CHUONG-0008-FINAL.md` |
| 9 | Dược phô dưới trấn | `03-MANUSCRIPTS/approved/CHUONG-0009-FINAL.md` |
| 10 | Người hái thuốc không trở về | `03-MANUSCRIPTS/approved/CHUONG-0010-FINAL.md` |
| 11 | Thanh đao đầu tiên | `03-MANUSCRIPTS/approved/CHUONG-0011-FINAL.md` |
| 12 | Đao chưa đủ nhanh | `03-MANUSCRIPTS/approved/CHUONG-0012-FINAL.md` |
| 13 | Một đao đổi đường sống | `03-MANUSCRIPTS/approved/CHUONG-0013-FINAL.md` |
| 14 | Vị khách trước sơn môn | `03-MANUSCRIPTS/approved/CHUONG-0014-FINAL.md` |

SHA-256 của các file trong ZIP tại lúc cập nhật (để đối chiếu bản chuẩn, không phải Git commit hash):

- `03-MANUSCRIPTS/approved/CHUONG-0008-FINAL.md`: `965a51b7a575097afd59b638a96125ac7f53a1119b9a762cf98491bdc9360e21`
- `03-MANUSCRIPTS/approved/CHUONG-0009-FINAL.md`: `841f115e33a00211f122c071e323dfd6f424aebe44f1ac155b30ede769881665`
- `03-MANUSCRIPTS/approved/CHUONG-0010-FINAL.md`: `bdcc168fe47bdcf26ca2c2dd0774682ca41c8c856295fa47db4396f7588d142b`
- `03-MANUSCRIPTS/approved/CHUONG-0011-FINAL.md`: `ab7bd91a85aa92a628a007ec37578344f586730d3869f058c0796dcb610fcfa2`
- `03-MANUSCRIPTS/approved/CHUONG-0012-FINAL.md`: `0632ed9ba7c6d31a48dd7769e22fb9a70e49f1779b58336435ec506492fd1936`
- `03-MANUSCRIPTS/approved/CHUONG-0013-FINAL.md`: `517db2a011d85214862657a382364582d026c432407db6137e376fcee0ea3a04`
- `03-MANUSCRIPTS/approved/CHUONG-0014-FINAL.md`: `a148ae8dd164533658a4fa41f84deb37a1999ba12fed0c8d4747ec1793b1bd92`


## 49. CONTINUITY TẬP 2 — CHỈ MỤC TRA NGUYÊN VĂN

| Chương | Diễn biến đã duyệt | Trạng thái/điểm nối |
|---|---|---|
| 8 | A Thạch đánh thức Hành Chu; Vãn Ninh thay băng, dặn không giao đấu/vận khí huyết mạnh 3 ngày; khí huyết ổn định hơn dự kiến. Kỷ Thanh La cần thuốc dẫn, cho Hành Chu xem dấu đóng chìm trên giấy dầu vì chàng mới đến, chưa nói với Tam trưởng lão và Vãn Ninh. Chu Tứ nhắc quán Hồi Phong, cảnh báo nơi treo đèn hình chim và việc theo dõi người mua thuốc. | Hành Chu và Vãn Ninh xuống núi; đao cũ gãy, vỏ rỗng. |
| 9 | Bách Thảo Đường, Lưu chưởng quầy: Hàn Lộ Tử bị mua sạch 3 ngày trước; hai dược phô khác tương tự; thuốc bị chặn có chủ ý là suy luận của nhân vật. Kẻ áo nâu vá đen theo dõi; hai người đổi đường, mua nón. Hành Chu bán hai đoạn đao gãy để bù tiền mua đao thép thô bản dày hơi ngắn, nặng, vỏ gỗ cũ; giữ dây gai chuôi cũ. Lão Đỗ chỉ Hắc Tùng Cốc có Hàn Lộ Tử, nhưng có người chiếm khe đá. | Có đường lấy thuốc ngoài dược phô nhưng bị canh. |
| 10 | Lão Đỗ vẽ đường vòng, nhờ tìm cháu Đỗ Bình 16 tuổi, áo vá hình lá. Hai người phát hiện trại canh giam người, tìm thuốc trước. Hầu hết Hàn Lộ Tử bị hái/nhổ; tìm được 5 quả xanh trắng nguyên vẹn trong khe hẹp. Hành Chu nhặt thẻ sắt rỉ có rãnh giữa, vết xước, gần hình khắc ba nét móc vào nhau trên đá; không cảm nhận linh lực. Đao mới để ngoài khe bị hai kẻ canh phát hiện. | Bị chặn lối ra. |
| 11 | Hành Chu giả vờ yếu, gọi Vãn Ninh là muội muội để qua mặt; nàng hất bột thuốc, chàng giành lại đao, chế trụ hai kẻ canh. Vết thương sườn rỉ máu, thay băng; đối phương có thẻ gỗ ký hiệu đường thẳng cắt vòng tròn, không phải cánh chim. Chúng nhận tiền làm việc, thân phận/chủ thuê chưa rõ. Trói lại, để bánh, không giết. Vãn Ninh vòng sau lều; Hành Chu đánh lạc hướng lính canh. | Tiếng động từ lều khiến kế hoạch lộ. |
| 12 | Vãn Ninh cắt vải lều, giải thoát bốn người: ba người hái thuốc và nam trung niên; Đỗ Bình sốt, chân bị thương, miếng vá hình lá. Hành Chu chặn côn/kiếm, dần thích nghi đao nặng nhưng hao khí huyết; bị thương cánh tay, vai. Thủ lĩnh áo đen dùng trường kiếm mạnh hơn rõ rệt. Hành Chu không cố kích sức mạnh chưa hiểu; Vãn Ninh hỗ trợ bột thuốc, cả nhóm chạy qua suối, tới cầu gỗ mục. | Hành Chu giữ đầu cầu để người khác qua. |
| 13 | Hành Chu không đánh thắng thủ lĩnh; tìm cơ hội thoát, chém đoạn gỗ nứt, cầu sập, Vãn Ninh kéo chàng lên và giữ đao. Thủ lĩnh sống, đe dọa tìm lại. Đỗ Bình được đưa về với gia gia. Hà Thuận, người vận chuyển dược liệu được cứu, kể thấy thùng gỗ niêm phong, hình như có hình chim (chưa chắc); giấy thông hành ghi “Thanh Giản Trạm”, chưa khẳng định đồng nhất Trạm Thanh Giản. Hành Chu từ chối tiền dành chữa thương của cháu, nhận lương khô/dược liệu lão Đỗ tặng; không tiết lộ tên tông môn. Vãn Ninh hứa một quả trứng. | Về trấn lúc tối, chuẩn bị trở lại núi. |
| 14 | Trở về núi trong đêm, Vãn Ninh phối thuốc, Kỷ Thanh La uống và ho máu sẫm; độc tính bắt đầu giảm, chưa giải hết, cấm vận linh lực. Bữa cháo có trứng, Hành Chu chia A Thạch và Vãn Ninh. Quấn dây gai cũ lên đao mới, ghi chép dấu hiệu khí huyết/thích nghi đao, tránh thử khi bị thương; thẻ sắt vẫn vô phản ứng. Sáng sau kể manh mối cho Kỷ Thanh La, hai người hỏi Tam trưởng lão về dấu chìm. Lão nói rất giống con dấu tông môn từng dùng, không biết hiện ở đâu, một số đồ thất lạc nhiều năm trước; dặn chờ tông chủ. Ba ngày sau Hành Chu tập nhẹ dưới gốc cây phía tây. Khách áo xám tóc điểm bạc, gậy trúc/tay nải lớn mang thư tới, là người Tam trưởng lão nhận ra và bất ngờ còn sống. | Khách kể ba tháng trước có kẻ mang con dấu cũ, tự xưng đệ tử Thanh Vân Tông, để lại thẻ gỗ cháy một góc. Tam trưởng lão nhìn hàng chữ sau thẻ, run tay; thân phận người mang thẻ và nội dung thư chưa công bố. |

### 49.1. Điểm kết Chương 14 — trích nguyên văn để nối Chương 15

> Cuối cùng, lão nhân ngẩng đầu.
>
> “Người mang tấm thẻ này… thật sự còn sống?”
>
> Người đàn ông áo xám đáp:
>
> “Đó chính là điều ta muốn biết.”

Chương 15 phải tiếp nối diễn biến mới tại sơn môn/mái hiên, hoặc chuyển cảnh có lý do rõ; **không đọc lại nguyên văn cliffhanger trên**. Hành Chu nghe được lời khách nói vì đứng dưới mái hiên sau khi cho A Thạch vào bếp; không tự khẳng định chàng đọc được hàng chữ trên mặt sau thẻ hoặc thư. Tam trưởng lão và khách đang nói riêng; A Thạch không còn đứng cạnh họ. Tông chủ vẫn chưa xuất hiện trong 14 chương. Không suy đoán thân phận khách là tông chủ hoặc người mang thẻ là người đã chết thực sự.

## 50. CHARACTER STATE, VẬT PHẨM VÀ PHỤC BÚT CẦN GIỮ

- **Tạ Hành Chu:** đệ tử mới, tu sĩ thấp cấp, đao/thể song tu; chưa công bố cảnh giới cụ thể/đột phá mới. Thương sườn và tay từ Tập 1, bị thương thêm cánh tay trái, vai, mu bàn tay trong Tập 2; cuối Ch14 đã dưỡng thương ba ngày, được luyện nhẹ, chưa hồi phục hoàn toàn. Càng giao chiến càng thích nghi động tác; luồng nóng trong ngực/cánh tay, khí huyết hao mạnh; tự nhận biết giới hạn và chủ động dừng. Ch14 đã ghi chép trên mảnh giấy cũ, không phải sách công pháp. Chưa biết tên Vạn Chiến Tàng Phong Thể và cơ chế đầy đủ. Không để cao nhân giải thích hộ năng lực. Không tự nhảy cảnh giới.
- **Vãn Ninh:** người am hiểu thuốc, nhị sư tỷ; vệt đỏ cổ tay còn đau/nóng khi nấu thuốc, chưa giải thích. Cùng Hành Chu vượt hiểm, lo lắng, tức giận vì chàng liều mạng, có sự quan tâm tăng dần. Chưa xác lập đạo lữ hay tình yêu công khai. Đã giúp giữ đao và kéo Hành Chu lên bờ. Không có kiếm/pháp thuật mới được xác lập.
- **Kỷ Thanh La:** đại sư tỷ, vai bị độc thương, Hàn Lộ Tử giúp phối thuốc làm độc giảm, không hồi phục tức thì; còn giữ giấy dầu với bản sao ký hiệu cánh chim ở mặt sau (Ch6). Biết dấu chìm, biết lời Hà Thuận qua Hành Chu, đã cùng hỏi Tam trưởng lão. Chưa biết sự thật về thủ phạm.
- **Tam trưởng lão:** nhận ra dấu giống con dấu cũ của tông môn, nói không biết nơi hiện tại và chưa biết việc vận chuyển người; có quá khứ chưa kể. Nhận ra khách áo xám, bất ngờ ông còn sống, nhận thư và thẻ cháy, run tay khi đọc hàng chữ. Lời nói nhân vật không đồng nghĩa sự thật khách quan; chưa đủ chứng cứ kết luận ông phản bội/giấu tội.
- **A Thạch:** trẻ nhỏ, gọi Hành Chu tiểu sư huynh, còn chăm chim sẻ; không biến thành người trưởng thành/chiến binh. Được đưa vào bếp khi khách nói chuyện riêng.
- **Chu Tứ:** người nuôi Dẫn Hương Trùng của Thạch Ưng Hội, được giữ trong kho, đã được cho ăn, cung cấp manh mối Hồi Phong/đèn chim/thuốc. Chưa có tình tiết thả hoặc giết sau Ch8; không tự khẳng định đã rời tông.
- **Trác Cửu:** rời núi cuối Ch7 với mảnh đồng thật hình cánh chim; không xuất hiện trực tiếp trong Tập 2. Không nhầm với thủ lĩnh áo đen ở Hắc Tùng Cốc.
- **Lưu chưởng quầy:** dược thương Bách Thảo Đường, quen Vãn Ninh. **Lão Đỗ/Đỗ Bình:** ông cháu hái thuốc, đã đoàn tụ; Đỗ Bình cần dưỡng thương. **Hà Thuận:** vận chuyển dược liệu, nhân chứng được cứu, có thể tìm ở trấn, không biết trong thùng có gì. Hai người hái thuốc còn lại không có tên chốt.
- **Thủ lĩnh áo đen:** dùng trường kiếm, mạnh hơn Hành Chu, sống sót ở bờ bên kia khi cầu gãy, hứa truy tìm. Hai kẻ canh khe bị trói còn sống; không xác lập kết cục các thuộc hạ. Ký hiệu đường thẳng cắt vòng tròn của thẻ gỗ là manh mối chưa giải.
- **Khách áo xám:** nam tóc điểm bạc, áo vải xám, gậy trúc, tay nải lớn, từng đến Thanh Vân Tông nhiều năm trước; chưa tên, chưa thân phận. Mang thư của người quen cũ, nói tận mắt thấy một việc, chưa rõ nội dung. Không tự đặt tên vào CANON trước khi chương mới được duyệt.

### Sổ vật phẩm và mystery (mã gợi ý để cập nhật continuity, chưa phải ID có sẵn trong repo)

| Mã | Vật phẩm / bí ẩn | Tình trạng |
|---|---|---|
| P01 | Giấy dầu Trạm Thanh Giản, ký hiệu cánh chim thêm nét chéo và dấu chìm Thanh Vân Tông | Kỷ Thanh La giữ; danh sách nhòe; chưa giải quyết. |
| P02 | Mảnh đồng hình cánh chim | Trác Cửu đã lấy cuối Ch7; bản sao hình trên giấy dầu còn. |
| P03 | Con dấu cũ | Tam trưởng lão nhận ra dấu giống đồ tông môn từng dùng; khách nói có người mang tới 3 tháng trước; chưa biết ai giữ hiện tại. |
| P04 | Thẻ gỗ đệ tử Hành Chu | Được trao Ch7; vẫn treo bên hông cuối Ch14. |
| P05 | Thẻ gỗ cháy một góc | Khách áo xám giao Tam trưởng lão cuối Ch14; mặt sau có hàng chữ chưa tiết lộ; không đồng nhất với thẻ sắt. |
| P06 | Thẻ sắt rỉ / hình khắc ba nét móc | Hành Chu nhặt Ch10, giữ trong tay nải, xem Ch14 không phản ứng; chưa rõ công dụng/chủ sở hữu. Không tự biến thành pháp bảo phát sáng. |
| P07 | Ký hiệu thẳng cắt vòng tròn | Trên thẻ gỗ của kẻ canh khe; Hành Chu/Vãn Ninh đã nhìn thấy; chủ thuê chưa rõ. Không khẳng định thẻ được giữ sau trận nếu chưa đối chiếu nguyên văn. |
| P08 | Hàn Lộ Tử và vụ mua sạch thuốc | 5 quả hái được; dùng phối thuốc Ch14, lượng còn lại chưa xác nhận chính xác sau toàn bộ liệu trình; động cơ và người thu mua chưa xác định. |
| P09 | Đao cũ / đao mới | Đao cũ bán thép Ch9; giữ dây gai, quấn lên đao mới Ch14. Đao mới bản dày hơi ngắn, nặng, thô, vỏ gỗ cũ; không có tên riêng/cấp bậc pháp khí. |
| P10 | Thùng gỗ niêm phong / Thanh Giản Trạm | Hà Thuận chỉ nhìn thoáng ký hiệu chim, không biết hàng; tên nơi trên giấy thông hành có thể cùng Trạm Thanh Giản nhưng chưa xác minh. |
| P11 | Vệt đỏ cổ tay Vãn Ninh | Còn đau nóng, chưa lý giải. |
| P12 | Khí huyết Hành Chu | Dấu hiệu đang tự nghiên cứu, chưa thức tỉnh hoàn toàn, không lộ tên thể chất. |
| P13 | Tông chủ và quá khứ tông môn | Vẫn vắng mặt; lý do đồ vật thất lạc, người mang thẻ cháy, khách và thư đều chưa giải. |

Các bản ghi trên là chỉ mục từ nội dung đã duyệt, **không phải sự xác nhận hệ thống continuity đã được tạo/commit**. Kiểm tra nguyên văn nếu cần câu thoại, số lượng, thứ tự hoặc chi tiết cụ thể. Không giải hết các mystery trong một arc; kế hoạch Ch15–21 chưa được user duyệt tình tiết.

## 51. QUY CHUẨN MỚI VỀ SỐ ẢNH VÀ STORYBOARD — GHI ĐÈ 300 ẢNH

User phản hồi: “tôi chỉ cần khi 2 nhân vật đang nói chuyện với nhau thì để ảnh đúng 2 nhân vật đó nói chuyện với nhau suốt hội thoại, khi 2 nhân vật đánh nhau thì làm tượng trưng tầm 2 - 3 hình hoặc nếu đánh lâu thì tầm 5 hình được rồi, không cần mô tả quá chi tiết chỉ cần ảnh mô tả đúng với câu là được”. Đã chọn kế hoạch 80 ảnh cho Tập 2; **không cố định 80 là luật bất biến cho mọi tập**, nhưng mặc định khoảng 75–85 theo mạch, không quay về 217/300 nếu không có yêu cầu. Một ảnh có thể giữ cả hội thoại dài vài phút. Một nhóm nhân vật/địa điểm ổn định = một ảnh; thay bối cảnh, thành phần, hành động quan trọng mới đổi. Giao đấu ngắn 2–3, dài tối đa khoảng 5, không minh họa mỗi nhát đao. Cảnh bí mật 1–2. Không chia đều thời gian.

Bộ thực tế Tập 2: Ch8 9 ảnh (001–009), Ch9 10 (010–019), Ch10 10 (020–029), Ch11 10 (030–039), Ch12 12 (040–051), Ch13 12 (052–063), Ch14 17 (064–080). Đây là phân bổ **chính thức thay kế hoạch 9/10/10/12/14/13/12** và thay kế hoạch 300 ảnh. `C08-I001.png` đến `C14-I080.png`, global order liên tục; không lấy danh sách thử 10 ảnh đầu cũ thay CSV.

CSV có 18 cột: `scene_id,chapter,global_order,image_file,anchor_text,occurrence,description,status,character_refs,character_design,location_id,environment_design,weapon_continuity,image_prompt,negative_prompt,source_file,source_paragraph_index,transition_rule`. Mỗi anchor là câu/đoạn bắt đầu thật trong FINAL; occurrence/paragraph index dùng để phân biệt câu lặp; kiểm tra coverage, thứ tự, tên file và đúng nguồn. Status lúc bàn giao `PENDING_GENERATION`, không đồng nghĩa ảnh đã sinh. Tập 3 tạo CSV mới từ Ch15–21 FINAL, không dùng anchor Tập 2, dùng mã C15-I001… theo số lượng thực tế. Prompt tự đủ chi tiết để agent tạo từng ảnh không cần tự bịa, gồm nhóm nhân vật, vị trí, tư thế, cảm xúc, thương thế, binh khí, khung cảnh, ánh sáng, bố cục, negative prompt.

## 52. QUY CHUẨN MỸ THUẬT VÀ CÁC LỖI PHẢI TRÁNH

- User muốn ảnh **huyền huyễn/tiên hiệp điện ảnh đẹp, ngầu, nam tuấn tú, nữ xinh đẹp thanh lệ**; phong cách bán hiện thực/realistic 3D concept art, chi tiết tóc/vải, ánh sáng có chiều sâu, nhân vật rõ trên màn hình điện thoại. 16:9, ưu tiên 1920×1080 hoặc cao hơn, không méo hình, không logo/text/mã ảnh/watermark. Mỗi file là một ảnh độc lập, không collage/comic panels/cắt ảnh ghép; tên file trên đĩa, không in lên hình. Không dùng thumbnail trong timeline.
- Trước khi tạo ảnh, lập character bible, reference sheet riêng (không tính vào 80 ảnh); nếu engine hỗ trợ dùng cùng reference/model/seed/style, nếu không thì dùng mô tả cố định và kiểm tra từng ảnh. Không gửi toàn bộ CSV vào một prompt sinh ảnh. Tạo từng dòng độc lập, kiểm tra rồi lưu đúng mã, sai thì tạo lại đúng dòng, không báo hoàn thành nếu sai. Chỉ đưa agent tạo ảnh khi có công cụ tạo ảnh thật.
- Tạ Hành Chu: thiết kế hình 20–25 tuổi, Đông Á tuấn tú, mặt góc cạnh, tóc đen dài buộc cao dây vải, thân hình săn chắc, áo xanh xám/lam trầm giản dị, đai nâu/giày đen, băng trắng ngà theo thương thế; không giáp quý/vương miện/sẹo mặt vĩnh viễn. Đao tu không phải kiếm tu. Vãn Ninh: nữ trưởng thành 20–25 (ước lệ hình), mặt trái xoan, tóc đen búi nửa đầu trâm gỗ, áo xanh ngọc nhạt kín đáo, đai xanh sẫm, giỏ trúc khi cần; vệt cổ tay chỉ khi phù hợp. Kỷ Thanh La: nữ trưởng thành 22–27 (ước lệ hình), sắc sảo, tóc đen, hắc y đen than viền xám, băng vai, sắc mặt nhợt khi dưỡng thương. A Thạch: bé trai nhỏ gầy, khoảng 8–10 (ước lệ hình), mắt to, tóc búi nhỏ rối, áo nâu đất rộng, quần xám. Tam trưởng lão: khoảng 65–75 (ước lệ hình), tóc bạc rối/râu ngắn, đạo bào xám cũ, hồ lô rượu nâu. Tuổi/màu sắc/thẩm mỹ chỉ là thiết kế hình, không tự nâng thành CANON nếu truyện chưa xác nhận.
- Thanh Vân Tông phải nghèo, cổng gỗ hỏng, mái điện thủng, tường đổ, sân cũ; không cung điện nguy nga, ngai vàng, đội đệ tử đông. Phòng phía tây nhỏ, giường tre/bàn gỗ/cửa sổ không khít; bếp mộc; kho cũ. Hắc Tùng Cốc rừng thông rậm, khe đá ẩm lạnh, suối nhỏ, cầu gỗ mục; Hàn Lộ Tử quả nhỏ xanh trắng không phát sáng. Thẻ đệ tử bằng gỗ, thẻ sắt rỉ không phát sáng. Không vẽ tông chủ khi chưa xuất hiện, không tự thêm yêu thú/hiệu ứng linh lực/đao quang quá mức. Duy trì tiến trình vũ khí, thương tích và vật phẩm đúng từng chương.
- **Các lần thử trực tiếp tạo 10 ảnh đầu đã thất bại nhiều lượt:** tool sinh tông môn nguy nga, tông chủ/ngai vàng, đệ tử lạ, ngọc bội, đao nguyên vẹn khi đã gãy, hào quang, A Thạch thành người lớn, Kỷ Thanh La sai giới tính; cuối cùng sinh bảng 10 ô có chữ mã. User rất không hài lòng, nói “tạo fail hoài”, yêu cầu **chuyển sang agent tự tạo theo CSV thật chi tiết**. Không tái sử dụng các ảnh lỗi, không tính vào 80 ảnh, không tiếp tục tự sinh ảnh hàng loạt nếu user chưa giao lại. Hai ảnh thử thay băng trước đó cũng không được xác nhận là tài sản chính thức. Mục tiêu là agent nhận hướng dẫn độc lập từng cảnh, không cần user sửa prompt từng lần.

## 53. CRITICAL — VOICE, HARD CUT, QA VIDEO (QUY CHUẨN BẮT BUỘC CHO TẬP 3+)

### Nguồn voice và pipeline
- Repo local `SangTacTruyenTuTien/03-MANUSCRIPTS/approved/`, branch `main` GitHub `https://github.com/dinhngocquanghuy/SangTacTruyenTuTien`. Khi giao agent Tập 3, **liệt kê chính xác 7 file CHUONG-0015-FINAL.md … CHUONG-0021-FINAL.md**, chỉ khi chúng tồn tại/đã duyệt. Không giả định đường dẫn tuyệt đối Windows (agent tự tìm trong Downloads/Youtube 2 nếu cần). Nếu thiếu local, kiểm tra remote; thiếu cả hai thì báo lỗi không tự viết thay.
- Chỉ đọc tiêu đề chương đúng một lần + nguyên văn nội dung truyện. Loại metadata, Markdown, dấu phân cách, dòng hết chương kỹ thuật, ghi chú review; không dùng DRAFT, không đọc lại Ch1–14, không chèn CTA/intro/outro/recap. CSV/anchor_text chỉ để đồng bộ, tuyệt đối không đọc prompt/description/anchor thành lời bổ sung.
- Xuất `TAP-03-TTS-SCRIPT.txt` (đối chiếu đủ chữ, thứ tự, không lặp/thiếu). Google gTTS `lang="vi", tld="com"`, giọng nữ Việt như Tập 1; FFmpeg `atempo=1.25` giữ pitch, PCM s16le 48000 Hz stereo, nghỉ 2.0 giây giữa chương. Không đổi engine/giọng/tốc độ, không thay sample rate để tăng tốc. Cache theo nội dung/cấu hình, retry có giới hạn khi lỗi mạng, tiếp tục đoạn thiếu, nghe kiểm tra phát âm tên riêng. gTTS là chuẩn thực hành của kênh, không đảm bảo dịch vụ luôn hoạt động/âm sắc không đổi; nếu lỗi không tự chuyển engine.
- Tách lời kể theo câu/đoạn nhỏ để tạo audio và đo bằng ffprobe hoặc số mẫu PCM. Ghép đúng thứ tự, giữ nguyên câu, chỉ thêm im lặng giữa chương. Ghi mốc start/end thực tế sau atempo; dùng forced alignment hoặc đối chiếu đoạn chứa anchor, không ước lượng toàn tập bằng số từ. Có thể tạo voice trước khi ảnh xong; không render FINAL nếu thiếu ảnh. Xuất SRT/VTT UTF-8 riêng, 2–5 giây/cue tham khảo, tối đa 2 dòng, kiểm tra thời gian thực; không burn-in. Nếu dùng tỷ lệ từ trong đoạn để ước lượng cue, cần kiểm tra và chỉnh, không coi là timestamp chính xác tuyệt đối.
- Tổng thời lượng video theo master voice thực tế, không kéo dài/thu ngắn để đủ 2 giờ. Không tự thêm nhạc nền, hiệu ứng âm thanh, intro/outro, quảng cáo hay chữ trên ảnh.

### Mệnh lệnh nguyên tắc của user: ẢNH TĨNH TUYỆT ĐỐI

User nói agent hay làm ảnh rung lắc/giật giật, nhìn rất khó chịu; yêu cầu **cấm tuyệt đối**, kể cả chuyển động nhỏ. Đây là CRITICAL mức ưu tiên cao nhất, không được tự sáng tạo để “sinh động hơn”. Mỗi ảnh đứng yên như mở PNG trên màn hình, từ frame đầu đến cuối. Cấm camera shake, jitter, zoom in/out, Ken Burns, pan/tilt, parallax/2.5D, xoay/nghiêng/trượt, nhấp nháy/thay đổi sáng, biến dạng, AI image-to-video (tóc/áo/mắt/mây/sương), mọi keyframe/hiệu ứng mặc định làm chuyển động. Chỉ resize/padding cố định, không zoompan hoặc biểu thức thay đổi theo thời gian. FFmpeg có thể `-loop 1`, `-tune stillimage`, 30fps; lặp frame tĩnh để đủ thời lượng là được, không lặp/tua clip chuyển động.

**Chỉ HARD CUT:** chuyển trực tiếp ảnh A → B đúng mốc anchor trong voice, không fade/crossfade/dissolve, không black frame, không slide/zoom/shake transition. Voice liên tục qua chuyển cảnh; trong 2 giây nghỉ giữa chương vẫn giữ ảnh trước tới lúc chương mới bắt đầu. Không chia đều thời lượng ảnh. Hội thoại giữ một ảnh xuyên suốt; tránh spoil bằng ảnh trước khi lời kể đến. Làm timeline gồm ID, đường dẫn ảnh, anchor, start/end, duration, mốc chương; kiểm tra không gap/overlap, tổng khớp WAV (làm tròn frame có kiểm soát, không cộng dồn lệch).

### QA và định dạng
- Render test ít nhất 3 ảnh trước khi render cả tập. So sánh frame đầu/giữa/cuối mỗi cảnh, vị trí/tỷ lệ/độ sáng/nội dung phải giống nhau trừ sai số nén nhỏ; dùng so sánh pixel/SSIM hoặc kiểm tra frame difference, xem trực tiếp các ranh giới. Nếu phát hiện rung/giật/chuyển động, sửa và render lại. Không báo FINAL nếu còn lỗi. Kiểm tra đủ file PNG độc lập, đúng tên, đúng thứ tự, không tái sử dụng ảnh lỗi, không black frame, voice không mất/lặp, codec phát được.
- MP4 1920×1080, 16:9, 30fps, H.264, yuv420p tương thích, `tune stillimage`, AAC 192 kbps 48kHz stereo. Xuất WAV master, TXT voice, CSV timeline, SRT/VTT, QA report và MP4 thực tế. Tập 3 có thể dùng `BUILD FINAL CLIP/TAP-03/WORK` và `OUTPUT` riêng để không ghi đè Tập 1–2 (đường dẫn đề xuất, chưa tồn tại). Tên đề xuất `TONG-MON-BI-TRUY-SAT-TAP-03-FINAL.mp4`, `TAP-03-VOICE-FULL.wav`, `TAP-03-TTS-SCRIPT.txt`, `TAP-03-TIMELINE.csv`, `TAP-03-QA-REPORT.md`, phụ đề cùng tên video. Không tự commit/push/upload.

## 54. DANH SÁCH TÀI LIỆU ĐÃ BÀN GIAO TẬP 2

| File | Chức năng / trạng thái |
|---|---|
| `TAP-02-CHUONG-08-14-FINAL.zip` | 7 chương FINAL, giải nén vào root repo |
| `HUONG-DAN-AGENT-TAP-02.zip` | Bộ hướng dẫn ban đầu gồm PROMPT-GIAO-AGENT.md, HUONG-DAN-KY-THUAT.md, README.md, STORYBOARD-SCHEMA.csv; **còn kế hoạch 300 ảnh, đã bị thay thế phần số ảnh** |
| `BO-STORYBOARD-80-ANH-TAP-02.zip` | Bộ chính thức 80 ảnh, gồm hai file dưới |
| `STORYBOARD-SCHEMA-TAP-02-80-ANH.csv` | 80 cảnh thực tế, prompt/anchor/continuity, không phải file schema mẫu |
| `HUONG-DAN-TAO-80-ANH-TAP-02.md` | Character bible 17 nhóm, địa điểm, binh khí, negative prompt, workflow |
| `tông_môn_bị_truy_sát_tập_2.png` | Thumbnail sửa đúng tên, không dùng làm ảnh trong video |

**Prompt agent mới nhất** nằm trong chat: writing block 78342 (bản sửa cuối, 7 mục, CRITICAL ảnh tĩnh/HARD CUT/QA), sau đó block 83921 bổ sung **mục 0 nguồn kịch bản**. Hai block phải được kết hợp, không chỉ gửi block 78342 thiếu đường dẫn. Chưa có xác nhận đã ghi phiên bản hợp nhất vào file .md cũ; vì vậy hướng dẫn mục 53 của context này ghi đè mọi quy định mâu thuẫn. Tập 3 nên tạo một prompt tổng hoàn chỉnh ngay từ đầu, ghi cụ thể 7 file FINAL, CSV mới, character bible, voice và QA; không bắt user ghép nhiều prompt thủ công.

## 55. SEO TẬP 2 ĐÃ SOẠN VÀ QUY TẮC GIT/EVIDENCE

Title đề xuất chính (chưa xác nhận user đã chọn/đăng): `Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát | Tập 2: Bí Mật Thanh Vân Tông | Audio Tu Tiên`. Hai lựa chọn khác: `Tông Môn Bị Thiên Hạ Truy Sát – Tập 2 | Một Đao Đổi Đường Sống | Audio Truyện Tu Tiên`; `Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát | Tập 2: Kẻ Đáng Lẽ Đã Chết` (title thứ ba chỉ là hook SEO, không phải CANON rằng người mang thẻ đã chết). Mô tả đã soạn trong block 68245: mở bằng tông môn nghèo, đao gãy, hai sư tỷ; hành trình tìm thuốc Hắc Tùng Cốc, đao mới, khách bí ẩn; liệt kê tên Ch8–14, thông tin truyện nguyên sáng, kênh Tiên Vực Ký, AI hỗ trợ voice/ảnh, CTA và hashtag. Tag block 68246 gồm tên truyện, tông môn bị truy sát, Tiên Vực Ký, Tạ Hành Chu, Thanh Vân Tông, audio truyện tu tiên/tiên hiệp/huyền huyễn, đao thể song tu, vạn chiến tàng phong thể, truyện nguyên sáng. Tập 3 tạo mới 3 title/mô tả/tag theo nội dung FINAL, không spoil quá mức, kiểm tra giới hạn YouTube khi cần, không copy nội dung Tập 2 thay tên tập.

- User ưu tiên lưu text nguyên tác và lịch sử Git làm bằng chứng sáng tác; voice/MP4 có thể tái tạo từ bản thảo còn lưu. Không coi WAV/MP4 là bắt buộc phải push lên Git; lưu local nếu cần QA. Việc có text Git không đảm bảo YouTube chấp nhận YPP; giữ lịch sử sáng tác, quyết định, quyền tài nguyên trung thực.
- Lệnh đã bàn giao cho Ch8–14 (chạy Git Bash tại root repo):

```bash
git add 03-MANUSCRIPTS/approved/CHUONG-000[89]-FINAL.md 03-MANUSCRIPTS/approved/CHUONG-001[0-4]-FINAL.md
git status
git commit -m "Approve chapters 8-14 FINAL for audiobook episode 2"
git push origin main
```

- Chưa xác nhận lệnh đã chạy. Với Ch15–21 chỉ sau khi user chốt FINAL mới gom một commit cho cả lô + continuity/evidence nếu được yêu cầu. Không spam commit mỗi DRAFT, không tự sửa FINAL, không giả tạo timestamp/hash hoặc ghi nhận QA chưa làm. File context v7.0 này chưa push lên GitHub.

## 56. HANDOFF THỰC HÀNH — TẬP 3 CHƯƠNG 15–21

1. Đọc mục 47–56 trước; dùng connector đúng repo, kiểm tra bản thảo 8–14 trên remote; nếu chưa có, dùng ZIP được duyệt (hoặc yêu cầu đúng nguồn thiếu), không viết dựa vào tóm tắt thay cho nguyên văn. Đọc ít nhất toàn Ch14, các chương 8–13 và phục bút Ch1–7 có liên quan. Kiểm tra continuity file có thực tế hay không, không tạo/commit tự động.
2. Khi user yêu cầu viết Tập 3: viết **đầy đủ bảy chương 15–21 DRAFT**, liền mạch một arc, phát triển bí ẩn khách áo xám/thẻ cháy/dấu cũ có kiểm soát. Chưa có outline chính thức; những quyết định mới phải xây dựng qua hành động và chờ user duyệt. Duy trì hài hước, tình nghĩa, tiến bộ tu luyện đao/thể, nguy hiểm có hậu quả, kỳ ngộ và tuyến tình cảm có chiều sâu. Không lặp thoại/mô típ cứu người ở Hắc Tùng Cốc chỉ để kéo dài. Giữ tên Tạ Hành Chu/Hành Chu, hạn chế “hắn”, không dùng “người tán tu” làm đại từ. Không ép dung lượng bằng câu lặp; tham chiếu Tập 1 19.790 từ và Tập 2 khoảng 17.037, mục tiêu nghe khoảng 1–3 giờ theo TTS thực tế.
3. Sau review, chỉ khi user nói chốt thì xuất 7 file Markdown `CHUONG-0015-FINAL.md`…`CHUONG-0021-FINAL.md` trong ZIP đúng cấu trúc approved; giữ nguyên văn, metadata ngày chốt, kiểm tra ranh giới, cập nhật continuity/evidence, hướng dẫn một commit. Nếu phát hiện lỗi trong FINAL cũ, báo với nguyên văn chứng cứ, không sửa hồi tố.
4. Khi user yêu cầu production: tạo thumbnail TẬP 3 đúng tên truyện, phong cách nhất quán. Lập storyboard khoảng 80 ảnh tùy mạch thực tế, prompt chi tiết từng dòng theo mục 51–52; agent tự tạo theo CSV (không tự tạo trực tiếp hàng loạt sau lịch sử fail). Giao prompt tổng theo mục 53, 7 đường dẫn FINAL chính xác, voice trước/timestamp thật/ảnh tĩnh tuyệt đối/hard cut/QA. Chỉ xác nhận sản phẩm khi có bằng chứng thực tế.
5. Khi user yêu cầu SEO: 3 title, mô tả copy-post, tag giới hạn phù hợp, đúng Ch15–21, tên truyện/kênh; không bịa thời lượng/URL/trạng thái đăng.

**Câu mở session mới không cần dài:** “Đọc context này, tiếp tục Tập 3 từ Chương 15 đến 21.” Assistant phải hiểu đã chốt Ch1–14, không viết lại Tập 2, không hỏi lại voice/ảnh tĩnh/quy chuẩn mỹ thuật, và phân biệt nhiệm vụ đọc context với yêu cầu sáng tác cụ thể. Nếu user chỉ muốn nắm context, báo xác minh và chờ giao việc. Nếu yêu cầu viết, làm ngay bản thảo dựa trên nguồn thực tế. Không hứa làm nền hoặc bảo user chờ kết quả tương lai.


---

# CẬP NHẬT V8.0 — TẬP 3 FINAL, HANDOFF TẬP 4 (29/11/2026)

## 57. Tiến độ và nguồn chuẩn

- Trong session này đã sáng tác đủ Ch15–21 DRAFT V1. User yêu cầu bỏ hết dấu ngoặc kép vì agent đọc thành tiếng; sau đó xác nhận “ok chốt kịch bản 15-21, bạn đưa tôi file lưu vào folder và commit”. Đã bàn giao `TAP-03-CHUONG-15-21-FINAL.zip`, cấu trúc `03-MANUSCRIPTS/approved/CHUONG-0015-FINAL.md` … `CHUONG-0021-FINAL.md`.
- Đã kiểm tra lại ZIP thực tế khi lập context: 7 file UTF-8, ZIP không lỗi CRC, không có dấu ngoặc kép thẳng/cong, tổng 11.128 đơn vị đếm theo khoảng trắng không tính tiêu đề. Đây là tập ngắn hơn Tập 1 (19.790) và Tập 2 (~17.037). Không sửa/kéo dài hồi tố vì user đã chốt.
- Ảnh Explorer xác nhận đủ 7 tên file ở `Downloads/Youtube 2/SangTacTruyenTuTien/03-MANUSCRIPTS/approved`. Không chứng minh nội dung local trùng byte ZIP hoặc remote đã push. Đã đọc Ch14 từ GitHub trong session, chưa xác minh Ch15–21 remote. Không tuyên bố đã commit. Lệnh đã giao (Git Bash tại root repo):

```bash
git add 03-MANUSCRIPTS/approved/CHUONG-001[5-9]-FINAL.md 03-MANUSCRIPTS/approved/CHUONG-002[01]-FINAL.md
git status
git commit -m "Approve chapters 15-21 FINAL for audiobook episode 3"
git push origin main
```

- User đã yêu cầu 10 ảnh minh họa trực tiếp (thay vì storyboard 80 ảnh cho tập này), đã tạo đủ 10 ảnh độc lập, đổi tên và xác nhận chúng có trên máy qua ảnh Explorer. Đã tạo thumbnail. Đã giao prompt production, chưa nhận báo cáo Agent hay file thành phẩm. Chưa soạn SEO Tập 3 trong session này.
- Quy tắc bằng chứng: chỉ commit khi FINAL được duyệt, gom cả 7 chương một lần nếu duyệt cùng lúc. Ưu tiên lưu text nguyên tác và lịch sử sáng tạo, không bắt buộc commit WAV/MP4. Không tự sửa bản FINAL, không tự ghi hash/ngày push/QA giả.

## 58. Continuity từng chương Tập 3 (đối chiếu với nguyên văn ở mục 65)

| Chương | Tên | Diễn biến chuẩn |
|---|---|---|
| 15 | Người trở về từ quá khứ | Khách áo xám tên Lục Văn Sơn. Người giấu mặt gặp ông ba tháng trước, biết nhà cũ phía bắc Trường Phong Thành và món nợ 30 linh thạch, nhưng không trả lời câu hỏi nơi uống rượu trước khi rời tông. Mang hộp đồng quấn 3 dây đen, mảnh ngọc trắng nứt khắc chữ Minh, thư hẹn sau bảy ngày nước Bạch Khê đổi dòng. Vãn Ninh kiểm tra hộp; Tam trưởng lão nhận ra ngọc của người từng sống ở tông, không nói tên. Lục ở dưới chân núi, từng bị theo dõi. Trưởng lão hẹn dạy đao giờ Mão. |
| 16 | Một đao cũng chưa đủ | Tam trưởng lão dùng cành cây chỉ ra lỗi chân, hông, vai, chuyển trọng tâm, thu đao; Hành Chu luyện cơ bản, giảm tiêu hao, tự ghi nhận khác biệt giữa khí huyết khi luyện và khi thực chiến. Vãn Ninh chữa cổ tay Hành Chu, vệt đỏ của nàng đậm hơn. Lục gửi tin có người lạ ở Bạch Khê và thu mua bản đồ. |
| 17 | Bạch Khê cốc | Kỷ Thanh La đưa bản đồ, ở lại cùng A Thạch vì độc thương chưa khỏi, cho Hành Chu túi bột nhiễu mùi. Bốn người đi: Hành Chu, Vãn Ninh, Tam trưởng lão, Lục Văn Sơn. Có hai đường chính và đường nhỏ phía nam. Theo dõi ba kẻ tìm cửa đá, trú mái đá, phát hiện dấu đao; đêm mưa thấy ánh sáng và tiếng kim loại. |
| 18 | Những vết đao trên vách đá | Nước đổi dòng, nhóm năm người lộ cửa đá nhưng không mở được; ba người áo đen tới tranh chấp, cả nhóm rút. Hành Chu thấy ba nét chỉ đường dưới dấu đao, tìm hang sau dây leo; tự suy luận tổ hợp ba nhát, thử động tác, không có linh quang. Tìm cuốn ghi chép luyện thể bị ẩm, thiếu trang, không được luyện bừa. Có kẻ phát hiện cửa hang. |
| 19 | Lấy đao mở đường | Lục dùng gậy trúc tước kiếm, Hành Chu gạt đòn và áp dụng tổ hợp ba nhát với nam nhân mặt dài. Vãn Ninh dùng bột cay giúp rút lui. Hành Chu giữ lối hẹp, bị kiếm sượt vai, khí huyết nóng lên, vận đao thuận hơn nhưng sau đó đau ngực/suy kiệt, chủ động rút, Lục hỗ trợ. Vãn Ninh băng vai. Nhận ra cửa đá có thể không phải mục tiêu thực; bản đồ có nét mực chỉ đường cũ phía nam. |
| 20 | Bí mật dưới cây cầu cũ | Cầu đá rêu phủ, ký hiệu ba ngọn núi là dấu chỉ đường cũ của Thanh Vân Tông. Vãn Ninh tìm viên đá có dấu mòn, Lục đẩy, Tam trưởng lão lấy ống trúc bịt sáp và thư mới. Thư: Ngọc chỉ là tín vật. Đừng tới cửa đá. Có người đang dùng danh nghĩa Thanh Vân Tông thu gom tu sĩ. Hãy tìm người giữ sổ tại bến Bạch Lộ. Bến phía đông Trường Phong Thành. Vãn Ninh phát tác vệt đỏ, tay lạnh, chưa muốn nói; Hành Chu tôn trọng, yêu cầu báo khi đau. Trưởng lão biết một phần. Hành Chu nghiên cứu ghi chép, không luyện bừa, hứa sau này mua thuốc cho nàng. Cả nhóm quay về, Lục xuống núi dò tin. |
| 21 | Ngày đầu tiên của con đường cường giả | Cả nhóm trở về, đại sư tỷ được kể lại chuyện; Hành Chu quyết định rèn luyện trước khi xuống núi. Tập nâng đá, chân/lưng, đứng tấn, chạy bậc thềm, luyện ba động tác với gậy gỗ dưới hướng dẫn trưởng lão. Thấy hồi phục hơi nhanh hơn, chưa biết nguyên nhân. Hành Chu mang canh nóng cho Vãn Ninh; nàng yêu cầu đừng đứng lại một mình khi nguy hiểm, chàng đồng ý. Sáng ngày thứ bảy sau khi về Bạch Khê, Lục gửi một thiếu phụ tới tông bằng tín vật. Phu quân mất tích gần hai tháng, nhận việc vận chuyển tại Bạch Lộ hẹn 10 ngày công hậu; giấy nhận việc có tên thương đội, tiền ứng và dấu chim dang cánh; mảnh giấy nhận ba ngày trước bảo tìm Thanh Vân Tông, đừng tới quan phủ. Nàng hỏi phu quân ở đâu; Hành Chu kéo ghế, mời kể từ đầu, A Thạch đi lấy nước. |

## 59. Trạng thái nhân vật/vật phẩm tại cuối Ch21

- Tạ Hành Chu: đệ tử Thanh Vân Tông, đao tu + thể tu giai đoạn đầu, dùng đao bản dày nặng hơi ngắn, dây gai cũ quấn chuôi; không có tên đao, cấp pháp khí hoặc đột phá cảnh giới mới. Vai bị kiếm sượt ở Ch19 đã băng; sau bảy ngày có luyện tập, không khẳng định lành hoàn toàn. Biết phối hợp ba nhát (mở đường, ép đổi vị trí, tập trung lực), chưa đặt tên đao pháp; chưa hoàn thiện. Tự ghi chép khí huyết, chủ động dừng khi quá tải; không biết tên thể chất. Không biến dấu hiệu thành thức tỉnh hoàn toàn, không tự ban công pháp/đao ý hay nhảy cảnh giới.
- Vãn Ninh: nhị sư tỷ luyện đan/chữa thương; vệt đỏ cổ tay lan dài, phát tác ở cầu đá, tay lạnh, dùng thuốc mang theo và đỡ hơn. Chưa nói nguyên nhân, nói hiện tại không phải vấn đề dược liệu. Tam trưởng lão biết một phần. Quan tâm Hành Chu rõ hơn, gọi Hành Chu, dặn đừng một mình cản địch; chưa là đạo lữ, chưa tỏ tình. Không biến nàng chỉ thành người chữa thương/đối tượng tình cảm.
- Kỷ Thanh La: đại sư tỷ, độc thương giảm nhưng chưa hoàn toàn hồi phục, có thể đi lại; ở lại tông cùng A Thạch khi nhóm đi Bạch Khê; giữ giấy dầu có dấu đóng chìm. Không tự cho nàng vận dụng toàn lực hay khỏi hẳn.
- Tam trưởng lão: từng có tu vi cao, hiện hạn chế vận dụng linh lực, có kinh nghiệm dạy đao và thân pháp cơ bản; biết dấu chỉ đường ba ngọn núi, nhận ra mảnh ngọc chữ Minh, không tiết lộ danh tính chủ cũ. Không biết toàn bộ sự thật, không trực tiếp giảng cơ chế thể chất của Hành Chu.
- Lục Văn Sơn: khách áo xám, tóc điểm bạc, gậy trúc, tay nải lớn; quen trưởng lão từ trước, từng được người liên quan cứu mạng (không kết luận danh tính); hỗ trợ nhóm rút khỏi Bạch Khê. Cuối tập đã xuống núi thu thập tin, gửi thiếu phụ tới, không có mặt trong cảnh cuối theo nguyên văn. Mức độ đáng tin chưa xác định; Kỷ Thanh La từng dặn không quá tin ông.
- A Thạch: ở tông với đại sư tỷ, vẫn hồn nhiên, chim sẻ và chuyện ăn bánh; cuối Ch21 đi lấy nước cho thiếu phụ.
- Tông chủ: chưa trở về; Trác Cửu chưa xuất hiện trong tập này, mảnh đồng hình cánh chim vẫn là phục bút cũ chưa giải. Thẻ sắt rỉ Hành Chu giữ từ Ch14 chưa có phản ứng, chưa được giải thích ở Tập 3.
- Vật chứng mới: hộp đồng, ngọc trắng nứt chữ Minh, thẻ gỗ cháy từ Ch14, phong thư, bản đồ có đường phía nam, cuốn sách luyện thể ẩm hỏng (nhóm mang về, Hành Chu nghiên cứu hình vẽ), thư dưới cầu trong ống trúc, hai giấy của thiếu phụ. Không tự gán ngọc là pháp bảo phát sáng/chìa khóa mở cửa đá; thư nói chỉ là tín vật. Số lượng bột/thuốc còn lại không xác định.

## 60. Phục bút và hướng Tập 4 — CHƯA CHỐT TÌNH TIẾT MỚI

Điểm nối chính xác: Ch21 kết thúc khi thiếu phụ vừa ngồi xuống chuẩn bị kể, A Thạch đi lấy nước, mọi người nhận ra có kẻ cố tình lôi Thanh Vân Tông vào vụ việc. Ch22 nên mở bằng hành động hoặc lời kể tiếp theo của thiếu phụ, không chép lại câu cuối Ch21, không recap dài. Đọc nguyên văn phần cuối tại mục 65 trước khi viết.

Các câu hỏi còn mở:
- Thiếu phụ và phu quân chưa có tên; chưa xác định người chồng còn sống, chết hay bị giam, nghề nghiệp/tu vi, tên thương đội cụ thể, ai tuyển và ai gửi giấy. Giấy có dấu chim là đầu mối, chưa chứng minh cùng tổ chức với Trạm Thanh Giản/Trác Cửu.
- Người giữ sổ ở bến Bạch Lộ là ai, sổ ghi gì, vì sao có thể tiếp cận, người gửi thư dưới cầu là ai. Bến Bạch Lộ phía đông Trường Phong Thành là hướng điều tra, chưa tới trong truyện.
- Ai dùng danh nghĩa Thanh Vân Tông thu gom tu sĩ; con dấu cũ thật/giả, người mang thẻ cháy và mảnh ngọc chữ Minh là ai; cửa đá Bạch Khê chứa gì; nhóm áo đen và nhóm tìm cửa đá thuộc thế lực nào. Không biến suy đoán của nhân vật thành sự thật đã xác nhận.
- Mảnh đồng của Trác Cửu, dấu chim, giấy dầu, Hàn Lộ Tử bị mua sạch, thùng gỗ niêm phong, Trạm Thanh Giản/Thanh Giản Trạm, Hà Thuận, thẻ sắt rỉ, quá khứ Vãn Ninh/Kỷ Thanh La/tông chủ vẫn cần phát triển có kiểm soát.
- Đề xuất DRAFT cho arc 22–28: nghe thiếu phụ kể và xác minh giấy tờ; chuẩn bị xuống bến Bạch Lộ với lý do cấp bách nhưng không lao vào tự sát; khai thác môi trường bến hàng, thương đội, người giữ sổ bằng quan sát, trí tuệ và giao tiếp; thêm thử thách tu luyện/chiến đấu có hậu quả và tiến triển tình cảm. Không bắt buộc theo đề xuất này, chưa phải outline được duyệt. Không giải hết bí mật trong một tập, không lặp công thức tìm hang/giải cứu người hái thuốc.
- Hành Chu phải có tiến bộ thực sự qua tu luyện và thực chiến, giữ hài hước, nhân hậu, sắc bén; sử dụng Tạ Hành Chu/Hành Chu, không gọi thay bằng “người tán tu”. Thiết kế thể chất dựa mục 19–20 của context: thức tỉnh dần, tự nghiên cứu, tiêu hao khí huyết, đao/thể ban đầu độc lập rồi cộng hưởng; thuật ngữ chưa xuất hiện trong FINAL không được tiết lộ tùy tiện. Không áp dụng các cơ chế khác trái lựa chọn đã ghi ở file.
- Khi được yêu cầu viết, tạo đủ 7 chương Ch22–28 DRAFT văn xuôi tiểu thuyết, không synopsis. Tham chiếu độ dài Tập 1–2, tránh ngắn quá như Tập 3 nếu nội dung có thể phát triển tự nhiên; không kéo dài bằng đối thoại lặp, không ép thời lượng. Chỉ chốt sau review.

## 61. CRITICAL — Định dạng truyện sạch cho TTS, áp dụng từ Tập 3 trở đi

User nói: “bỏ hết giấu " đi, đưa vô agent nó tạo voice nó đọc luôn cả ngoặc kép, cay thì thôi”. Quy tắc mới: KHÔNG dùng dấu ngoặc kép thẳng hoặc cong bao quanh lời thoại, kể cả bản DRAFT. Viết lời thoại xuống dòng riêng, làm rõ người nói qua lời kể; không thay bằng gạch đầu dòng/ký hiệu đặc biệt. Giữ dấu câu tiếng Việt để ngắt nghỉ tự nhiên. Bản FINAL chỉ có tiêu đề chương dạng `Chương 22: ...` và văn bản truyện sạch, không Markdown, metadata, dấu sao, dòng hết chương kỹ thuật, ghi chú review hoặc CTA trong nội dung voice. Không sửa từ ngữ/cốt truyện khi làm sạch. Các chương FINAL cũ không tự chỉnh hồi tố; agent có thể làm sạch bản sao input TTS. Kiểm tra nối chương không lặp/thiếu câu. Ghi chú DRAFT/review đặt ngoài bản text đọc.

## 62. Tài nguyên hình Tập 3 và timeline đúng yêu cầu user

Thư mục local được xác nhận bằng ảnh Explorer: `Downloads/Youtube 2/SangTacTruyenTuTien/BUILD FINAL CLIP/Part3`. Chưa biết đường dẫn tuyệt đối/ổ đĩa; agent tự tìm. User đổi tên 10 ảnh theo thứ tự đã thống nhất:

| File mới | Tên ảnh gốc | Nội dung / mốc bắt đầu đề xuất |
|---|---|---|
| 1.png | twilight_heroes_of_the_ruined_sect.png | Mở Ch15, toàn cảnh tông môn |
| 2.png | ancient_secrets_beneath_the_cloud_emblem.png | Ch15, Lục lấy hộp đồng |
| 3.png | dawn_saber_training_in_ruined_courtyard.png | Mở Ch16, luyện đao |
| 4.png | journey_to_the_misty_citadel.png | Ch17, nhóm lên đường |
| 5.png | rainy_ambush_at_bạch_khê_valley.png | Cuối Ch17, phát hiện người lạ làm việc trong đêm, sang Ch18 |
| 6.png | echoes_of_the_ancient_saber_sequence.png | Ch18, tìm hang đá |
| 7.png | twilight_saber_clash_in_the_mountain_pass.png | Mở Ch19, giao chiến |
| 8.png | discovery_at_bạch_khê_bridge.png | Mở Ch20, cầu đá và Vãn Ninh phát tác |
| 9.png | a_warm_bowl_at_dusk.png | Ch21, mang canh nóng tới phòng Vãn Ninh |
| 10.png | wuxia_conspiracy_over_ancient_maps.png | Cuối Ch21, thiếu phụ xuất hiện, giữ đến hết voice |

- User đã sửa rõ: “không phải 10s một ảnh, mà phải là hiển thị ảnh cho tới khi voice nói không còn liên quan nữa thì chuyển tiếp qua ảnh kế, nghĩa là suốt tập 3 mỗi ảnh trong 10 ảnh sẽ chỉ hiển thị 1 lần hiểu chưa”. Đây là quy tắc có ưu tiên cao nhất về timeline. Prompt đầu hiểu sai thành slideshow 10s lặp vòng đã bị thay thế hoàn toàn.
- Đúng 10 đoạn ảnh, 9 hard cut, thứ tự số tự nhiên 1→10, mỗi ảnh xuất hiện một lần duy nhất, không quay lại, không chia đều, không giới hạn 10s. Giữ ảnh hiện tại qua đoạn trung gian không có hình riêng và 2 giây nghỉ chương; chuyển khi nội dung voice tới mốc phù hợp ảnh kế. Mốc phải đo từ audio thật sau atempo, không tự bịa timestamp. Các ảnh có chi tiết minh họa thừa (ví dụ A Thạch/Kỷ Thanh La trên cầu, Lục ở cảnh cuối, nhiều bóng Hành Chu trong hang, kiến trúc xa/đao quang); ảnh không phải CANON, không sửa truyện cho khớp hình.
- Thumbnail đã tạo: `bí_mật_bạch_khê_tập_3.png`, tỷ lệ gần 16:9, chữ BÍ MẬT BẠCH KHÊ / TÔNG MÔN BỊ TRUY SÁT / TẬP 3; Hành Chu, Vãn Ninh, trưởng lão, ngọc, cửa đá. Không dùng thumbnail vào timeline, không coi ngọc phát sáng trong thumbnail là tình tiết truyện. Chưa xác nhận người dùng lưu thumbnail ở đường dẫn nào. Tập 4 làm thumbnail mới khi được giao, số TẬP 4 rõ, chữ đẹp dễ đọc trên mobile.
- Với Tập 4, có thể đề xuất tiếp phương án 10 ảnh độc lập nếu user muốn giữ workflow mới; số lượng cụ thể chưa được xác nhận cho Tập 4. Không tự quay về 80/300 ảnh hay tạo ảnh nếu chưa giao. Duy trì nhất quán thiết kế nhân vật và phong cách điện ảnh tiên hiệp, ảnh riêng không collage, không chữ/watermark trong ảnh timeline.

## 63. Prompt production mới nhất — Tập 3, tham chiếu cho Tập 4

Prompt hoàn chỉnh đã giao trong writing block 83521 bản sửa cuối. Các quy tắc bắt buộc:
- Nguồn đọc: đúng 7 file FINAL Ch15–21 ở approved, không đọc DRAFT hay tập cũ; làm sạch như mục 61. Google gTTS lang=vi, tld=com, slow=False, giọng nữ tiếng Việt trong trẻo rõ chữ nhất quán (gTTS không có tham số chọn giới tính cố định, cần nghe đối chiếu giọng trước; không tự thay engine). Tạo voice trước, cache đoạn, retry giới hạn, kiểm tra phát âm. FFmpeg `atempo=1.25` đúng một lần, giữ pitch; PCM s16le 48000 Hz stereo; nghỉ 2 giây giữa chương. Không tự tăng tốc lần hai. Tên riêng cần nghe: Tạ Hành Chu, Vãn Ninh, Kỷ Thanh La, A Thạch, Tam trưởng lão, Lục Văn Sơn, Bạch Khê, Bạch Lộ, Thanh Vân Tông.
- Timeline theo mục 62, timestamp đo theo PCM/ffprobe/forced alignment sau tăng tốc. Ảnh tĩnh tuyệt đối như mở PNG: cấm rung, giật, zoom, pan, tilt, Ken Burns, jitter, parallax, 2.5D, xoay, nhấp nháy sáng, tóc/áo/mây chuyển động, keyframe, zoompan, AI image-to-video. Resize/padding cố định giữ tỷ lệ, không crop nhân vật. Chỉ hard cut, không fade/crossfade/dissolve/slide/flash/black frame. Voice liên tục. Không nhạc/SFX/intro/outro/CTA/logo/watermark/chữ/phụ đề burn-in/ảnh bổ sung.
- MP4 H.264 1920×1080 16:9, 30fps, yuv420p, CRF18–20, tune stillimage, AAC 192kbps 48kHz stereo, faststart; video kết thúc cùng voice trong sai số làm tròn frame. Không ép thời lượng.
- File FINAL phải lưu TRỰC TIẾP tại `BUILD FINAL CLIP/Part3`, cùng cấp 1.png–10.png, không đặt trong OUTPUT. Tên `TONG-MON-BI-TRUY-SAT-TAP-03-FINAL.mp4`. Các file cùng thư mục: `TAP-03-VOICE-FULL.wav`, `TAP-03-TTS-SCRIPT.txt`, `TAP-03-TIMELINE.csv`, `TAP-03-QA-REPORT.md`, `TONG-MON-BI-TRUY-SAT-TAP-03-FINAL.srt` và `.vtt`. WORK có thể dùng cho file tạm. Không ghi đè PNG, không sửa approved, không tự commit/push.
- QA: kiểm tra đủ 7 chương, không đọc dấu ngoặc kép/Markdown, không mất/lặp câu, đúng tốc độ, giọng nhất quán, kiểm tra tên riêng; render test trước, so sánh frame đầu/giữa/cuối từng đoạn để xác minh tĩnh, kiểm tra 9 ranh giới, không black frame, timeline không gap/overlap, video/audio kết thúc cùng lúc, phụ đề riêng khớp voice. Báo cáo đường dẫn tuyệt đối, dung lượng, thời lượng thực, mốc start/end từng ảnh, số chuyển cảnh, lỗi và cách sửa. Chưa có bằng chứng QA thực tế nên không báo đã dựng.
- Tập 4 chỉ thay input thành Ch22–28 FINAL sau duyệt, thư mục ảnh/output theo user cung cấp thực tế (không tự khẳng định Part4 tồn tại), tên file TAP-04 tương ứng. Không hỏi lại tốc độ/giọng/quy tắc tĩnh; không dựng trước khi chốt bản truyện.

## 64. Handoff session mới và việc còn thiếu

Câu user có thể dùng: “Đọc context này, nắm tiến độ rồi sáng tác Tập 4 từ Chương 22 đến 28 cho tôi review.” Khi chỉ yêu cầu nắm context, không tự sáng tác. Khi yêu cầu sáng tác, kiểm tra repo và đọc nguyên văn FINAL gần nhất. Nếu remote chưa có Ch15–21, mục 65 là bản nguyên văn trích trực tiếp từ ZIP đã bàn giao, không cần bắt user tải lại nếu đủ. Ưu tiên remote đã xác minh nếu có khác biệt; báo mâu thuẫn, không âm thầm sửa. Kiểm tra các phục bút Ch1–14 bằng repo khi cần. Chưa có outline Tập 4 được duyệt; mọi tình tiết mới là DRAFT. Sau khi user chốt, xuất ZIP 7 file đúng approved, sạch ngoặc kép, hướng dẫn một commit; không tự push. Tạo ảnh/thumbnail/production/SEO chỉ khi yêu cầu. Tập 3 chưa xác nhận đăng YouTube, chưa có URL/thời lượng thực/SEO, chưa xác nhận push. Context v8.0 chưa push.

## 65. BẢN NGUYÊN VĂN DỰ PHÒNG CHƯƠNG 15–21 FINAL

Nguồn: trích nguyên văn 7 file trong `TAP-03-CHUONG-15-21-FINAL.zip` đã bàn giao, kiểm tra ZIP và UTF-8 ngày 29/11/2026. Đây là nội dung được duyệt, không phải bản tóm tắt. Các heading bên ngoài khối code chỉ phục vụ context, không đưa vào TTS. Nếu GitHub chưa có chương mới, có thể dùng nguyên văn này để bảo đảm nối truyện. Không đọc toàn bộ context vào voice.

### CHUONG-0015-FINAL.md

```text
Chương 15: Người trở về từ quá khứ

Trong nhà bếp, A Thạch đang kiễng chân tìm thứ gì đó trên giá gỗ.

Tạ Hành Chu bước vào, kéo một chiếc ghế đặt cạnh cửa rồi ngồi xuống.

Đệ tìm gì vậy?

Trà.

Đệ biết pha trà từ bao giờ?

Tam trưởng lão nói có khách tới thì phải pha trà.

Hành Chu nhìn chiếc hũ nhỏ phủ đầy bụi trên giá.

Vậy đệ có biết lần cuối cùng bổn môn mua trà là khi nào không?

A Thạch lắc đầu.

Ta cũng không biết. Nhưng nhìn lớp bụi kia, có lẽ vị khách ngoài cửa còn trẻ hơn số trà trong hũ.

A Thạch vội rụt tay lại.

Tạ Hành Chu bật cười, đứng dậy lấy hũ trà xuống. Bên trong chỉ còn một ít lá khô đã vụn nát.

Chàng ngửi thử, sau đó quyết định lấy nước nóng thay trà.

Dù sao cũng không thể để vị khách vừa tới uống xong rồi phải nhờ Vãn Ninh cứu chữa.

Ngoài sân, Tam trưởng lão đã dẫn người đàn ông áo xám vào căn phòng phía đông. Đó vốn là nơi dùng để tiếp khách, nhưng bởi mái nhà bị dột nên đã lâu không có người sử dụng.

Tạ Hành Chu bưng hai bát nước nóng tới.

Cửa phòng vẫn mở.

Tam trưởng lão ngồi bên bàn, trước mặt đặt phong thư và tấm thẻ gỗ cháy xém.

Người đàn ông áo xám đang tháo chiếc tay nải trên vai.

Đa tạ tiểu huynh đệ.

Ông nhận bát nước từ tay Hành Chu, uống một ngụm rồi nhìn xuống đáy bát.

Trà của quý tông khá đặc biệt.

Tạ Hành Chu nghiêm túc đáp:

Đây là phương pháp pha trà cao thâm của bổn môn. Bỏ đi hình thức, chỉ giữ lại bản chất.

Bản chất?

Nước.

Người đàn ông ngẩn ra, sau đó bật cười.

Tam trưởng lão trừng mắt.

Tiểu tử, ngươi không có việc gì làm sao?

Có chứ. Vãn bối còn phải đi luyện đao. Chỉ là vị tiền bối này từ xa tới, ta nghĩ ít nhất cũng nên hỏi quý danh.

Người đàn ông đặt bát xuống.

Ta họ Lục, tên Văn Sơn. Trước kia từng qua lại với Thanh Vân Tông.

Vãn bối Tạ Hành Chu.

Lục Văn Sơn nhìn chàng thêm một lát.

Tạ tiểu huynh đệ, ngươi nhập môn được bao lâu rồi?

Chưa lâu.

Có biết trước đây Thanh Vân Tông là nơi thế nào không?

Hành Chu nhìn lên mái nhà.

Nghe nói trước đây mái ngói còn nguyên vẹn.

Lục Văn Sơn lại cười.

Lần này, ngay cả Tam trưởng lão cũng phải quay mặt đi.

Nhưng nụ cười nhanh chóng biến mất khi ánh mắt Lục Văn Sơn rơi xuống tấm thẻ gỗ.

Lão bằng hữu, chuyện năm đó đã qua nhiều năm. Ta vốn không muốn nhắc lại. Chỉ là lần này, người tìm ta biết một số chuyện mà người ngoài không thể biết.

Tam trưởng lão hỏi:

Chuyện gì?

Vị trí căn nhà cũ của ta ở phía bắc Trường Phong Thành. Cả việc năm đó ta từng thiếu ngươi ba mươi linh thạch.

Lão nhân nhíu mày.

Biết những chuyện ấy không có nghĩa hắn là chủ nhân tấm thẻ.

Ta hiểu.

Lục Văn Sơn lấy từ tay nải ra một mảnh giấy khác.

Người đó còn nhờ ta chuyển một món đồ tới chỗ cũ.

Tam trưởng lão nhìn mảnh giấy.

Trên đó chỉ có vài nét mực đơn giản, vẽ một dãy núi và một dòng suối.

Phía dưới là hai chữ.

Bạch Khê.

Sắc mặt lão nhân càng trở nên khó coi.

Tạ Hành Chu nhận thấy bàn tay đang cầm bát nước của ông hơi siết lại.

Ngươi đã mang đồ tới đó?

Chưa.

Vì sao?

Bởi vì ta không tin hắn.

Lục Văn Sơn thở dài.

Người từng cứu mạng ta năm đó, cho dù có hóa thành tro, ta cũng muốn nhận lại. Nhưng kẻ xuất hiện ba tháng trước không chịu để lộ khuôn mặt. Hắn biết rất nhiều chuyện cũ, lại không trả lời được một câu hỏi mà ta đặt ra.

Câu hỏi gì?

Ta hỏi hắn, trước khi rời Thanh Vân Tông, chúng ta đã uống rượu ở đâu.

Tam trưởng lão im lặng.

Lục Văn Sơn tiếp tục:

Hắn không trả lời. Chỉ bảo ta đừng hỏi những chuyện không cần thiết.

Tạ Hành Chu nhìn hai người.

Vậy món đồ hắn giao cho tiền bối đâu?

Lục Văn Sơn chỉ vào chiếc tay nải.

Ở đây.

Ông lấy ra một chiếc hộp đồng dài hơn một gang tay. Hộp không có khóa, nhưng giữa nắp và thân hộp được quấn bằng ba sợi dây màu đen.

Ta chưa mở.

Tam trưởng lão đưa tay định cầm lấy.

Tạ Hành Chu bất chợt lên tiếng:

Trưởng lão, khoan đã.

Lão nhân quay sang.

Lại chuyện gì?

Người ta có thể đưa một tấm thẻ gỗ cũ tới để khiến người mất bình tĩnh. Một chiếc hộp không rõ bên trong chứa gì, tốt nhất vẫn nên để nhị sư tỷ kiểm tra trước.

Tam trưởng lão nhìn chiếc hộp.

Sau một lúc, ông chậm rãi thu tay về.

Đi gọi Vãn Ninh.

Vãn Ninh đến không lâu sau đó.

Nàng mang theo một đôi đũa trúc, vài mảnh vải sạch và một bình sứ nhỏ.

Tạ Hành Chu nhìn những món đồ trên bàn.

Nhị sư tỷ, chúng ta định mở hộp hay chuẩn bị ăn cơm?

Ngươi muốn thử trước không?

Ta cảm thấy nên để người có chuyên môn thực hiện.

Vãn Ninh không để ý tới chàng nữa.

Nàng dùng đũa trúc gạt từng sợi dây đen sang một bên, quan sát lớp bụi bám trên mặt hộp, sau đó nghiêng đầu ngửi nhẹ.

Có mùi dầu bảo quản kim loại. Chưa thấy dấu hiệu của độc dược thông thường.

Nàng mở nắp.

Bên trong không có linh quang, không có ám khí.

Chỉ có một mảnh ngọc trắng đã nứt và một cuộn giấy nhỏ.

Tam trưởng lão vừa nhìn thấy mảnh ngọc đã đứng bật dậy.

Chiếc ghế phía sau đổ xuống đất.

Vãn Ninh ngẩng đầu.

Trưởng lão?

Lão nhân không trả lời.

Ông cẩn thận cầm mảnh ngọc lên, dùng ngón tay vuốt dọc theo vết nứt.

Trên bề mặt mảnh ngọc có khắc một chữ nhỏ.

Minh.

Tạ Hành Chu chưa từng thấy Tam trưởng lão có vẻ mặt như vậy.

Ngày thường, ngay cả khi sơn môn bị người ta tấn công, lão nhân vẫn có thể buông vài câu đùa cợt. Nhưng lúc này, đôi mắt đục ngầu của ông dường như chứa đựng điều gì đó rất nặng nề.

Trưởng lão biết chủ nhân của nó? Hành Chu hỏi.

Biết.

Là ai?

Tam trưởng lão đặt mảnh ngọc xuống.

Một người từng sống ở đây.

Ông không nói thêm.

Vãn Ninh mở cuộn giấy.

Trên đó viết một hàng chữ.

Sau bảy ngày, nước Bạch Khê đổi dòng. Người muốn tìm lại chuyện cũ, hãy mang ngọc tới.

Lục Văn Sơn nói:

Ta vốn định tự mình tới Bạch Khê. Nhưng trên đường đến đây, ta phát hiện có người theo dõi.

Có biết là ai không? Tam trưởng lão hỏi.

Không. Ta đã đổi đường hai lần mới cắt được chúng.

Tạ Hành Chu chống cằm.

Biết chuyện cũ của tông môn, có con dấu, có thẻ đệ tử, lại cố ý đưa tin cho trưởng lão. Người này hoặc thật sự muốn giúp chúng ta, hoặc đang chuẩn bị một cái bẫy rất công phu.

Vãn Ninh nhìn chàng.

Ngươi nghĩ khả năng nào lớn hơn?

Với vận khí của bổn môn gần đây, ta cảm thấy khả năng thứ hai đáng được tôn trọng hơn.

Tam trưởng lão không phản bác.

Ông cất mảnh ngọc và cuộn giấy vào hộp.

Chuyện này tạm thời không được truyền ra ngoài.

Lục Văn Sơn gật đầu.

Ta sẽ ở lại dưới chân núi vài ngày. Nếu có tin gì mới, ta sẽ tìm cách báo cho ngươi.

Tạ Hành Chu lập tức nói:

Tiền bối không ở lại đây sao? Bổn môn có nhiều phòng trống lắm.

Lục Văn Sơn nhìn mái nhà.

Có phòng nào không dột không?

Hành Chu suy nghĩ hồi lâu.

Tiền bối thích ngủ gần bếp không?

Lục Văn Sơn quyết định xuống núi.

Chiều hôm ấy, sau khi khách rời đi, Tam trưởng lão một mình đứng trước chính điện.

Tạ Hành Chu mang chiếc ghế vừa sửa tới đặt bên cạnh ông.

Ngồi một chút đi.

Lão nhân nhìn chàng.

Ngươi muốn hỏi chuyện gì?

Không muốn hỏi nữa.

Hiếm thấy.

Hành Chu ngồi xuống bậc thềm.

Trưởng lão không muốn nói, ta hỏi nhiều cũng chẳng có ích gì. Chỉ là nếu người định tới Bạch Khê một mình, tốt nhất nên nói với chúng ta trước.

Tam trưởng lão khẽ hừ.

Ngươi cho rằng lão phu già đến mức không tự lo được cho mình?

Không.

Tạ Hành Chu nhìn khoảng sân cũ.

Ta chỉ cảm thấy người trong một tông môn, nếu có chuyện thì nên cùng nhau nghĩ cách. Nếu trưởng lão xảy ra chuyện, ai sẽ sửa mái nhà?

Lão nhân bật cười.

Tiểu tử vô lương tâm.

Hành Chu cũng cười.

Một lúc lâu sau, Tam trưởng lão mới nói:

Bạch Khê từng là nơi đệ tử Thanh Vân Tông xuống núi lịch luyện.

Hiện tại thì sao?

Đã bỏ hoang nhiều năm.

Có nguy hiểm không?

Có.

Tạ Hành Chu gật đầu.

Vậy trước khi đi, chúng ta phải chuẩn bị thật kỹ.

Tam trưởng lão nhìn chàng.

Lão phu đã nói sẽ cho ngươi đi sao?

Chưa.

Vậy ngươi chuẩn bị làm gì?

Hành Chu vỗ nhẹ lên chuôi đao.

Chuẩn bị để đến lúc người không còn lựa chọn nào tốt hơn, sẽ nhớ tới vãn bối.

Lão nhân nhìn thanh đao bên hông chàng.

Cuối cùng, ông đứng dậy.

Ngày mai, giờ Mão, tới sân phía tây.

Làm gì?

Luyện đao.

Tạ Hành Chu chớp mắt.

Có thể đổi thành giờ Thìn không?

Không.

Vậy giờ Mão có bao cơm sáng không?

Tam trưởng lão xách hồ lô rượu bỏ đi.

Tạ Hành Chu nhìn bóng lưng ông, khóe miệng hơi cong lên.

Chàng biết lão nhân vẫn còn rất nhiều điều chưa muốn nói.

Nhưng ít nhất, từ ngày mai, Hành Chu có thể bắt đầu làm một việc thiết thực hơn là ngồi chờ bí mật tự tìm tới cửa.

Chàng cần trở nên mạnh hơn.
```

### CHUONG-0016-FINAL.md

```text
Chương 16: Một đao cũng chưa đủ

Trời còn chưa sáng hẳn, một tiếng gõ cửa đã vang lên trong căn phòng phía tây.

Tạ Hành Chu kéo chăn trùm kín đầu.

Tiếng gõ lại vang lên.

Tiểu tử, dậy.

Trưởng lão, người tu đạo phải thuận theo tự nhiên.

Ra ngoài.

Hiện tại tự nhiên đang bảo ta ngủ.

Cánh cửa gỗ bị đẩy ra.

Tam trưởng lão đứng bên ngoài, trên tay cầm một gáo nước lạnh.

Tạ Hành Chu lập tức bật dậy.

Vãn bối đã tỉnh!

Lão nhân hài lòng gật đầu.

Nửa khắc sau, Hành Chu đứng giữa sân phía tây, hai tay cầm thanh đao mới.

Sương sớm phủ trên mặt đất. Những ngọn cỏ dưới chân còn đọng nước.

Tam trưởng lão đặt ba khúc gỗ trước mặt chàng.

Chém đi.

Tạ Hành Chu bước lên, nâng đao bổ xuống.

Khúc gỗ đầu tiên tách làm hai.

Chàng quay đầu nhìn lão nhân.

Thế nào?

Khó coi.

Nụ cười trên mặt Hành Chu cứng lại.

Tam trưởng lão chỉ xuống đất.

Chân trái đặt quá xa. Khi đao rơi xuống, vai ngươi dùng sức trước hông. Nếu khúc gỗ kia là người sống, chỉ cần tránh sang bên một bước, ngươi sẽ tự để lộ sườn.

Tạ Hành Chu nhìn lại vị trí chân mình.

Làm lại.

Khúc gỗ thứ hai bị chém đôi.

Vẫn khó coi.

Khúc thứ ba cũng không thoát khỏi số phận tương tự.

Tam trưởng lão lắc đầu.

Ngươi đang dùng sức để bổ gỗ, không phải dùng đao.

Vậy đao dùng để làm gì?

Để đưa sức lực của ngươi tới nơi cần đến.

Lão nhân nhặt một cành cây dưới đất.

Xuất đao về phía ta.

Hành Chu nhìn cành cây khô trong tay ông.

Trưởng lão, thanh đao này khá nặng.

Ta biết.

Vãn bối không chịu trách nhiệm nếu người bị thương đâu.

Bớt nói nhảm.

Tạ Hành Chu không dám thật sự dùng toàn lực. Chàng tiến lên một bước, xoay cổ tay đưa đao ngang qua.

Cành cây trong tay Tam trưởng lão chạm nhẹ vào mặt đao.

Lưỡi đao lệch hướng.

Ngay sau đó, đầu cành cây đã chạm vào cổ Hành Chu.

Chàng đứng sững.

Tam trưởng lão thu tay.

Lại.

Lần thứ hai, Hành Chu đổi hướng giữa chừng.

Cành cây vẫn dễ dàng gạt thanh đao ra ngoài.

Lần thứ ba, chàng cố thu hẹp động tác, không để lộ khoảng trống quá lớn.

Lần này, Tam trưởng lão phải lùi nửa bước.

Nhưng đầu cành cây vẫn chạm được vào vai chàng.

Sau hơn hai mươi lần, Tạ Hành Chu ngồi bệt xuống đất.

Không đánh nữa.

Vì sao?

Vãn bối cảm thấy mình đang bị một cành củi sỉ nhục.

Tam trưởng lão cười khà khà.

Ngươi có sức, phản ứng cũng không chậm. Nhưng trước kia phải tự mưu sinh, gặp chuyện gì thì dùng cách đó. Những động tác thừa tích lũy lâu ngày đã thành thói quen.

Hành Chu thở ra.

Vậy sửa thế nào?

Trước tiên, học cách đứng cho vững.

Lão nhân dùng cành cây vạch hai đường trên đất.

Đặt chân vào đây. Hạ trọng tâm xuống. Không cần gồng vai.

Tạ Hành Chu làm theo.

Giữ nguyên.

Một lát sau, hai đùi chàng bắt đầu đau nhức.

Trưởng lão.

Gì?

Bổn môn có thù với hai chân ta sao?

Giữ nguyên.

Khi mặt trời vượt khỏi dãy núi, Tạ Hành Chu cuối cùng cũng được phép đứng thẳng.

Hai chân chàng run lên.

Tam trưởng lão ném cành cây vào đống củi.

Ngày mai tiếp tục.

Hành Chu nhìn theo lão nhân.

Bỗng nhiên, chàng nhớ ra một việc.

Trưởng lão! Cơm sáng!

Ở trong bếp!

Tạ Hành Chu lập tức cảm thấy hai chân mình đã hồi phục được ba phần.

Vãn Ninh đang giã thuốc khi Hành Chu bước vào.

Nàng ngẩng đầu nhìn dáng đi của chàng.

Bị thương ở đâu?

Lòng tự trọng.

Vậy không cần chữa.

Hành Chu ngồi xuống chiếc ghế cạnh bếp.

Nhị sư tỷ, tỷ thật sự không định an ủi ta một chút sao?

Vãn Ninh đặt trước mặt chàng một bát cháo.

Ăn đi. Sau đó ta kiểm tra vết thương ở cổ tay.

Tạ Hành Chu lập tức cầm thìa.

Bát cháo hôm nay đặc hơn thường ngày.

Bên trong còn có một ít thịt thái nhỏ.

Chàng nhìn Vãn Ninh với vẻ kinh ngạc.

Bổn môn phát tài rồi?

Lão Đỗ gửi một ít thịt khô lên.

Vậy phải cảm tạ lão Đỗ.

Ngươi đừng ăn nhanh quá.

Hành Chu vừa ăn vừa kể lại chuyện bị Tam trưởng lão đánh bại bằng cành cây.

Vãn Ninh nghe xong, khóe môi khẽ nhếch.

Trưởng lão từng có tu vi rất cao. Dù hiện tại không thể vận dụng linh lực như trước, kinh nghiệm của người vẫn còn.

Tạ Hành Chu gật đầu.

Ta cũng nghĩ vậy. Chỉ không biết trước đây người mạnh đến mức nào.

Vãn Ninh im lặng.

Nàng tiếp tục nghiền thuốc.

Hành Chu không hỏi thêm.

Ăn xong, chàng đưa cổ tay cho nàng kiểm tra.

Vãn Ninh tháo lớp băng, ấn nhẹ vào vùng gân cốt.

Còn đau không?

Một chút.

Vậy không được luyện đao quá lâu.

Tạ Hành Chu nhìn cổ tay nàng.

Khi cúi người lấy thuốc, tay áo Vãn Ninh hơi trượt xuống. Vết đỏ dưới da vẫn còn đó, dường như đậm hơn vài ngày trước.

Còn tỷ?

Vãn Ninh lập tức kéo tay áo xuống.

Ta không sao.

Nhị sư tỷ, câu này nghe quen lắm.

Nàng nhìn chàng.

Quen thế nào?

Ta thường nói mỗi lần bị thương. Sau đó tỷ đều mắng ta.

Vãn Ninh không đáp.

Tạ Hành Chu thu lại nụ cười.

Nếu cần giúp đỡ, tỷ cứ nói. Ta không biết luyện đan, nhưng chạy chân, hái thuốc, bổ củi hay thử thuốc đều có thể.

Thử thuốc?

Cái cuối cùng phải xem giá cả.

Vãn Ninh bật cười.

Nàng băng lại cổ tay cho chàng.

Đợi khi nào ngươi không cần ta chữa thương nữa rồi hãy nói chuyện giúp ta.

Hành Chu nhìn nút thắt trên lớp băng.

Vậy ta sẽ cố gắng.

Ba ngày tiếp theo, sân phía tây thường xuyên vang lên tiếng đao chém gió.

Tam trưởng lão không truyền cho Tạ Hành Chu công pháp cao thâm nào.

Ông chỉ yêu cầu chàng sửa từng động tác nhỏ.

Cách đặt chân.

Cách chuyển trọng tâm.

Cách dùng lực từ hông và lưng.

Cách thu đao mà không để thân thể mất cân bằng.

Ban đầu, Hành Chu cảm thấy những yêu cầu ấy quá đơn giản.

Nhưng đến ngày thứ ba, khi chàng chém xuống một khúc gỗ có kích thước tương tự trước kia, lưỡi đao xuyên qua thớ gỗ nhẹ nhàng hơn rõ rệt.

Không cần dùng hết sức.

Cổ tay cũng không đau như trước.

Tạ Hành Chu đứng nhìn vết cắt.

Chàng thử lại.

Kết quả tương tự.

Một cảm giác vui sướng khó tả dâng lên trong lòng.

Trước kia, Hành Chu từng nghĩ muốn một đao mạnh hơn thì phải dùng nhiều sức hơn.

Bây giờ chàng mới nhận ra, sức lực bị lãng phí trong từng động tác có lẽ còn nhiều hơn mình tưởng.

Buổi tối, sau khi mọi người đã nghỉ ngơi, Tạ Hành Chu lại lấy tờ giấy ghi chép ra.

Chàng bổ sung thêm một dòng.

Thay đổi cách vận lực có thể giảm tiêu hao khí huyết.

Hành Chu suy nghĩ rồi viết tiếp.

Khí huyết nóng lên khi thực chiến và khi luyện tập không hoàn toàn giống nhau. Cần tìm nguyên nhân.

Chàng đặt bút xuống.

Nếu sự biến đổi trong cơ thể thật sự có liên quan tới những lần xuất đao và giao chiến, vậy việc cải thiện kỹ thuật dùng đao có thể giúp chàng duy trì trạng thái ấy lâu hơn.

Nhưng đây vẫn chỉ là suy đoán.

Tạ Hành Chu không định dùng thân thể chưa hồi phục hoàn toàn để kiểm chứng.

Chàng cất giấy, chuẩn bị đi ngủ.

Bỗng nhiên, bên ngoài vang lên tiếng bước chân.

A Thạch chạy tới cửa.

Tiểu sư huynh! Có người gửi thư!

Tạ Hành Chu nhìn đứa trẻ.

Lại thư?

Chàng cảm thấy từ ngày nhập môn, hai chữ này chưa từng mang tới chuyện tốt.

A Thạch đưa ra một mảnh giấy được gấp nhỏ.

Có một người bán củi đưa cho đệ ở chân núi. Người đó bảo Lục tiền bối nhờ chuyển.

Hành Chu mở giấy.

Bên trong chỉ có ba dòng.

Bạch Khê xuất hiện người lạ.

Có kẻ đang thu mua bản đồ đường núi.

Ta sẽ tới Thanh Vân Tông vào ngày mai.

Tạ Hành Chu nhìn về phía chính điện.

Thời gian bảy ngày ghi trong cuộn giấy sắp hết.

Chàng đứng dậy, cài thanh đao bên hông.

A Thạch, đi gọi trưởng lão.

Có chuyện gì sao?

Hành Chu xoa đầu đứa trẻ.

Có lẽ bổn môn sắp phải đi tìm một ít đồ thất lạc.
```

### CHUONG-0017-FINAL.md

```text
Chương 17: Bạch Khê cốc

Trên bàn ăn sáng hôm sau, Kỷ Thanh La đặt một tấm bản đồ cũ xuống.

Nàng đã có thể đi lại bình thường, nhưng sắc mặt vẫn chưa hoàn toàn hồi phục.

Đây là đường núi phía đông. Bạch Khê nằm sau hai ngọn núi này.

Tạ Hành Chu cúi xuống quan sát.

Có bao nhiêu đường vào?

Trước kia có hai. Một đường dọc theo suối, một đường đi qua sườn núi.

Tam trưởng lão lấy ngón tay chỉ vào khoảng trống trên bản đồ.

Còn một đường nhỏ phía nam. Đã nhiều năm không có người sử dụng, không biết hiện tại còn đi được hay không.

Lục Văn Sơn ngồi đối diện ông.

Ta đã tới gần Bạch Khê hôm qua. Có ít nhất hai nhóm người xuất hiện quanh thung lũng.

Trang phục thế nào?

Một nhóm mang kiếm, không có dấu hiệu môn phái. Nhóm còn lại giả làm thương nhân, mang theo khá nhiều dụng cụ dò tìm.

Tạ Hành Chu hỏi:

Có ai xuống đáy cốc chưa?

Chưa thấy.

Vậy có thể họ cũng đang đợi một thời điểm nào đó.

Kỷ Thanh La nhìn cuộn giấy đặt trên bàn.

Ngày nước Bạch Khê đổi dòng.

Tam trưởng lão gật đầu.

Ở đầu nguồn có một hồ nước tự nhiên. Mỗi khi mưa lớn, nước tràn qua vách đá phía đông, dòng chảy bên dưới sẽ thay đổi. Một số khu vực vốn chìm dưới nước có thể lộ ra.

Vậy người gửi thư biết rất rõ địa hình nơi đó, Hành Chu nói.

Đúng.

Mọi người im lặng.

Cuối cùng, Tam trưởng lão quyết định chỉ tới thăm dò ngoại vi.

Kỷ Thanh La muốn đi cùng, nhưng Vãn Ninh lập tức phản đối.

Độc thương của tỷ chưa khỏi. Nếu gặp địch, tỷ có thể không vận dụng được bao nhiêu linh lực.

Ta biết đường.

Trưởng lão cũng biết.

Kỷ Thanh La nhìn nàng.

Vãn Ninh không nhượng bộ.

Tạ Hành Chu đặt một chiếc bánh xuống trước mặt đại sư tỷ.

Tỷ ở lại bảo vệ sơn môn. Trách nhiệm này quan trọng không kém.

Kỷ Thanh La liếc chàng.

Ngươi đang dỗ trẻ con?

Không. A Thạch chỉ cần nửa cái bánh là đủ.

A Thạch lập tức ngẩng đầu.

Đệ muốn cả cái!

Bầu không khí quanh bàn dịu đi đôi chút.

Sau cùng, nhóm tới Bạch Khê gồm Tam trưởng lão, Lục Văn Sơn, Tạ Hành Chu và Vãn Ninh.

Kỷ Thanh La ở lại cùng A Thạch.

Trước khi rời sơn môn, nàng gọi Hành Chu tới.

Đừng quá tin Lục Văn Sơn.

Tạ Hành Chu khẽ gật đầu.

Ta hiểu.

Còn nữa, nếu gặp người có tu vi vượt xa mình, lập tức rút lui. Không được cậy vào chút bản lĩnh mới học.

Hành Chu nghiêm túc chắp tay.

Đệ xin ghi nhớ lời đại sư tỷ.

Kỷ Thanh La nhìn chàng một lúc.

Sau đó nàng lấy từ bên cạnh giường ra một túi vải nhỏ.

Bên trong có một ít bột làm nhiễu mùi. Nếu gặp Dẫn Hương Trùng hoặc thứ tương tự, có thể dùng tạm thời.

Tạ Hành Chu nhận lấy.

Đa tạ đại sư tỷ.

Kỷ Thanh La quay mặt đi.

Trở về nguyên vẹn là được.

Đường tới Bạch Khê khó đi hơn Hành Chu tưởng.

Sau khi vượt qua ngọn núi đầu tiên, cả nhóm phải men theo một vách đá dài phủ đầy dây leo.

Tam trưởng lão đi chậm nhưng bước chân rất chắc.

Lục Văn Sơn dẫn đường phía trước.

Vãn Ninh mang theo một giỏ thuốc nhỏ, còn Tạ Hành Chu phụ trách phần hành lý nặng nhất.

Đi được nửa ngày, chàng bắt đầu nghi ngờ mục đích thực sự của chuyến đi.

Trưởng lão.

Hử?

Có phải bổn môn thiếu phu khuân vác nên mới cho ta theo không?

Ngươi nghĩ nhiều rồi.

Tạ Hành Chu vừa định cảm động thì lão nhân nói tiếp:

Phu khuân vác còn phải trả tiền.

Hành Chu quay sang Vãn Ninh.

Nhị sư tỷ, tỷ nghe thấy chưa?

Nàng đưa cho chàng một túi nước.

Uống đi rồi tiếp tục.

Hành Chu nhận lấy.

Vẫn là nhị sư tỷ thương ta nhất.

Vãn Ninh bước nhanh về phía trước, không trả lời.

Đến giữa buổi chiều, tiếng nước chảy bắt đầu vọng lên từ dưới thung lũng.

Bạch Khê hiện ra giữa hai vách núi cao.

Dòng nước trong đến mức có thể nhìn thấy những viên đá trắng dưới đáy.

Phía xa, sương mỏng bao phủ những tán cây mọc sát vách núi.

Tam trưởng lão đứng lại.

Ông nhìn cảnh vật trước mắt hồi lâu.

Nơi này thay đổi nhiều quá.

Lục Văn Sơn chỉ về phía một bãi đất trống.

Trước kia ở đó có một căn nhà gỗ.

Đã sập rồi.

Tạ Hành Chu nhìn những tảng đá lớn nằm rải rác.

Chàng không biết Thanh Vân Tông từng có bao nhiêu người, cũng không biết nơi đây đã chứng kiến chuyện gì.

Nhưng vẻ mặt của Tam trưởng lão khiến chàng hiểu rằng Bạch Khê không chỉ là một địa điểm cũ.

Cả nhóm tiếp tục đi dọc theo suối.

Chưa được bao xa, Tạ Hành Chu bỗng giơ tay.

Dừng lại.

Lục Văn Sơn quay đầu.

Phát hiện gì?

Hành Chu chỉ vào một bụi cây cạnh đường.

Một nhánh cây mới gãy, vết gãy còn xanh.

Trên bùn có dấu chân chồng lên nhau.

Có người đi qua đây không lâu.

Tam trưởng lão nhìn quanh.

Vào rừng.

Bốn người rời khỏi đường mòn, ẩn sau một cụm đá lớn.

Không lâu sau, tiếng nói chuyện từ phía trước truyền tới.

Ba người đàn ông mặc áo vải màu nâu đang men theo suối.

Một người cầm bản đồ, hai người còn lại mang kiếm.

Chỗ này cũng không có.

Cứ đánh dấu lại. Đêm nay nước sẽ lên, ngày mai quay lại xem.

Đại ca nói chỉ cần tìm được cửa đá, những việc còn lại không cần chúng ta lo.

Tạ Hành Chu nghiêng đầu nhìn Tam trưởng lão.

Lão nhân khẽ nhíu mày.

Ba người kia nhanh chóng đi xa.

Lục Văn Sơn thì thầm:

Chính là nhóm ta nhìn thấy hôm qua.

Vãn Ninh hỏi:

Cửa đá là gì?

Tam trưởng lão nhìn về phía sâu trong thung lũng.

Ở Bạch Khê từng có một số nơi dùng để cất dụng cụ và vật tư lịch luyện. Có thể chúng đang tìm một trong những nơi ấy.

Hành Chu nhìn dòng suối.

Nếu biết chúng tìm cửa đá, chúng ta không cần vội tìm trước.

Lục Văn Sơn quay sang.

Ý ngươi là?

Chúng ta có thể xem chúng tìm được gì.

Tam trưởng lão suy nghĩ một lúc rồi gật đầu.

Cả nhóm quyết định tìm chỗ nghỉ kín đáo, đợi tới đêm.

Khi mặt trời khuất sau vách núi, nhiệt độ trong Bạch Khê giảm xuống rất nhanh.

Bốn người trú dưới một mái đá tự nhiên.

Vãn Ninh lấy ra một ít lương khô, chia cho mọi người.

Tạ Hành Chu nhận phần của mình, nhai chậm rãi.

Trong lúc ấy, chàng nhìn thấy trên vách đá đối diện có một số đường khắc rất nông.

Ban đầu Hành Chu tưởng đó chỉ là vết nứt.

Nhưng càng nhìn, chàng càng cảm thấy chúng giống dấu vết do binh khí để lại.

Có đường dài, có đường ngắn.

Một vài vết chém sâu hơn những vết còn lại.

Tạ Hành Chu bước tới, đưa tay chạm vào bề mặt đá.

Trưởng lão, trước đây có người luyện đao ở đây sao?

Tam trưởng lão nhìn những dấu vết.

Có lẽ vậy. Nơi này từng có nhiều đệ tử qua lại.

Hành Chu đứng trước vách đá, thử tưởng tượng hướng lưỡi đao đã chém xuống.

Một vết chém kéo dài từ trên xuống dưới, nhưng phần sâu nhất lại nằm gần cuối đường đao.

Chàng nhớ tới lời Tam trưởng lão về cách đưa sức lực tới đúng vị trí.

Bàn tay Hành Chu vô thức đặt lên chuôi đao.

Vãn Ninh lên tiếng phía sau:

Ngươi không được luyện đao ở đây.

Ta chỉ nhìn thôi.

Lần trước ngươi cũng nói chỉ thử một chút.

Hành Chu đành thu tay.

Chàng ghi nhớ vài vết chém đặc biệt trong đầu.

Nếu có cơ hội, Hành Chu muốn tìm hiểu kỹ hơn.

Đêm xuống.

Mưa bắt đầu rơi trên những tán cây phía xa.

Tiếng nước trong khe suối ngày càng lớn.

Tạ Hành Chu đang ngồi tựa lưng vào vách đá thì nghe thấy một âm thanh khác thường.

Không phải tiếng nước.

Cũng không phải tiếng gió.

Đó là tiếng kim loại va vào đá.

Chàng lập tức đứng dậy.

Ở phía bên kia dòng suối, giữa màn mưa, một đốm sáng nhỏ xuất hiện.

Rồi thêm một đốm nữa.

Tam trưởng lão bước tới bên cạnh Hành Chu.

Hai người cùng nhìn về phía ấy.

Có người đang làm việc giữa đêm.

Và vị trí của chúng chính là nơi dòng nước Bạch Khê sắp rút xuống.
```

### CHUONG-0018-FINAL.md

```text
Chương 18: Những vết đao trên vách đá

Mưa kéo dài đến gần sáng.

Dòng suối trước mặt bỗng trở nên đục ngầu.

Nước từ đầu nguồn đổ xuống, va vào những tảng đá lớn rồi tách sang một khe sâu phía đông.

Phần lòng suối sát vách núi dần lộ ra.

Tạ Hành Chu cùng mọi người đứng sau cụm cây rậm, quan sát nhóm người phía đối diện.

Có năm người.

Hai kẻ đang dùng dụng cụ cạy những viên đá mắc giữa các khe nứt.

Một người khác cầm đuốc, soi vào mặt vách.

Khi lớp bùn đất bị gạt đi, một đường viền hình chữ nhật xuất hiện.

Tam trưởng lão khẽ hít vào.

Đúng là cửa đá.

Lục Văn Sơn hỏi nhỏ:

Ngươi biết bên trong có gì không?

Không. Ta chưa từng tới vị trí này.

Một trong năm người lấy ra một vật hình tròn, đặt lên phần lõm giữa cửa.

Không có chuyện gì xảy ra.

Kẻ đó thử xoay vài lần rồi tức giận ném vật trong tay xuống đất.

Không phải cái này!

Những người còn lại tiếp tục tìm kiếm quanh cửa.

Tạ Hành Chu quan sát một lúc.

Chúng biết vị trí, nhưng không biết cách mở.

Vãn Ninh gật đầu.

Có lẽ thiếu chìa khóa.

Tam trưởng lão vô thức chạm vào chiếc hộp đồng giấu trong áo.

Hành Chu nhìn thấy động tác ấy.

Trưởng lão, chưa nên lấy đồ ra.

Lão nhân thu tay lại.

Cả nhóm tiếp tục chờ.

Khoảng nửa canh giờ sau, từ phía thượng nguồn xuất hiện thêm ba bóng người.

Những kẻ mới tới mặc áo đen, đứng đầu là một nam nhân cao lớn mang trường kiếm.

Hắn không nói chuyện với nhóm đang tìm cửa.

Chỉ nhìn quanh rồi lạnh lùng hỏi:

Ai cho các ngươi tới đây?

Người cầm đuốc lập tức rút kiếm.

Bạch Khê không thuộc về các ngươi.

Nam nhân áo đen không đáp.

Hắn phất tay.

Hai người phía sau lập tức tiến lên.

Tiếng binh khí va chạm vang vọng giữa thung lũng.

Tạ Hành Chu kéo Vãn Ninh lùi sâu hơn vào bụi cây.

Chúng ta đi thôi.

Lục Văn Sơn ngạc nhiên.

Không đợi nữa?

Chờ thêm có thể xem được một trận đánh hay. Nhưng nếu chúng phát hiện chúng ta, người nằm dưới đất có khi lại là mình.

Tam trưởng lão đồng ý.

Cả nhóm men theo đường cũ, rút khỏi khu vực cửa đá.

Khi đi ngang qua mái đá đã nghỉ đêm trước, Tạ Hành Chu bất ngờ dừng bước.

Chàng nhìn những vết đao trên vách.

Một dòng nước mưa chảy qua mặt đá, cuốn đi lớp đất mỏng bám bên dưới.

Ở giữa các dấu chém xuất hiện ba đường khắc nhỏ.

Hành Chu tiến lại gần.

Ba đường ấy không giống vết đao.

Chúng có độ sâu gần như bằng nhau, tạo thành hình mũi tên hướng sang bên trái.

Trưởng lão.

Tam trưởng lão quay đầu.

Chỗ này có dấu chỉ đường.

Lão nhân nhìn một lúc, sau đó đi theo hướng mũi tên.

Phía sau bụi dây leo mọc sát vách là một khe đá hẹp.

Tạ Hành Chu dùng vỏ đao gạt cây sang bên.

Một luồng khí mát từ trong khe thoát ra.

Lục Văn Sơn lấy đuốc.

Vào xem?

Tam trưởng lão gật đầu.

Lối đi chỉ đủ cho một người nghiêng thân bước qua.

Sau hơn mười bước, bên trong đột nhiên mở rộng.

Đó là một hang đá nhỏ, nền đất khá khô ráo.

Giữa hang đặt một bệ đá thấp.

Bên cạnh có vài mảnh gốm vỡ, một chiếc giá gỗ đã mục và những thanh sắt bị rỉ sét.

Tạ Hành Chu đi tới vách trong.

Trên đó có rất nhiều dấu chém.

Khác với bên ngoài, những vết chém này được sắp xếp thành từng cụm.

Một số cụm gồm ba vết.

Một số cụm gồm năm vết.

Khoảng cách giữa chúng có quy luật rõ ràng.

Tam trưởng lão đưa đuốc tới gần.

Nơi này từng có người luyện đao.

Hành Chu hỏi:

Là người của Thanh Vân Tông sao?

Không thể xác định.

Tạ Hành Chu không thất vọng.

Chàng đứng trước cụm ba vết chém, quan sát từ nhiều góc độ.

Vết đầu tiên ngắn và nông.

Vết thứ hai nghiêng xuống.

Vết cuối cùng dài hơn, phần cuối ăn sâu vào đá.

Hành Chu nhớ tới những lần bản thân bị Tam trưởng lão dùng cành cây đánh lệch hướng.

Nếu nhát đao đầu tiên chỉ để mở đường, nhát thứ hai ép đối phương thay đổi vị trí, vậy nhát thứ ba mới là nơi toàn bộ sức lực được đưa tới.

Chàng không chắc người để lại những vết chém có suy nghĩ như vậy hay không.

Nhưng cách giải thích ấy khiến Hành Chu nảy ra một ý tưởng.

Chàng rút đao.

Vãn Ninh lập tức nhìn sang.

Tạ Hành Chu vội nói:

Không chém đá. Ta chỉ thử động tác.

Chàng đứng cách vách một khoảng, chậm rãi đưa đao ra trước.

Thu.

Chuyển bước.

Chém xuống.

Ngay lần đầu tiên, động tác đã không thuận lợi.

Lưỡi đao quá nặng, khi chuyển hướng giữa nhát thứ hai và thứ ba, cổ tay Hành Chu phải chịu lực lớn.

Chàng dừng lại.

Thay đổi vị trí bàn chân.

Làm lại.

Lần này, Hành Chu không cố xoay đao bằng cổ tay. Chàng dùng chuyển động của hông để dẫn lưỡi đao đi theo một đường cong nhỏ.

Động tác trở nên liền mạch hơn.

Tam trưởng lão đứng nhìn.

Đừng vội.

Hành Chu gật đầu.

Chàng thực hiện lần thứ ba.

Sau đó là lần thứ tư.

Không có hào quang bất thường.

Không có linh lực bùng phát.

Nhưng Hành Chu cảm nhận được thanh đao trong tay không còn nặng nề như trước.

Chàng bật cười.

Thú vị.

Vãn Ninh đi tới.

Thấy thứ gì tốt sao?

Có lẽ chỉ là một cách dùng đao khác.

Ngươi vui đến vậy?

Tạ Hành Chu cất đao.

Trước đây muốn học đao pháp của người khác phải trả tiền. Hôm nay không mất một đồng nào.

Vãn Ninh lắc đầu.

Lục Văn Sơn tìm thấy một chiếc hòm gỗ nhỏ dưới bệ đá.

Chiếc hòm đã mục gần hết.

Bên trong chỉ còn vài mảnh vải và một cuốn sách bị ẩm.

Tam trưởng lão cẩn thận mở sách.

Phần lớn trang giấy đã dính chặt vào nhau. Những chữ còn nhìn rõ cũng không hoàn chỉnh.

Tạ Hành Chu cúi xuống.

Trên một trang có hình người đang đứng tấn, bên cạnh là những đường chỉ hướng vận lực.

Công pháp?

Tam trưởng lão lắc đầu.

Giống ghi chép luyện thể hơn.

Ông lật sang một trang khác.

Không đầy đủ. Không được tùy tiện luyện theo.

Hành Chu gật đầu.

Chàng biết những thứ thất truyền nhiều năm chưa chắc đã là bảo vật. Một phương pháp luyện thể thiếu mất phần quan trọng có thể khiến người tu luyện tổn thương kinh mạch.

Nhưng chàng vẫn muốn giữ lại để nghiên cứu.

Vãn Ninh lấy một mảnh vải sạch, giúp Tam trưởng lão bọc cuốn sách.

Đúng lúc ấy, Lục Văn Sơn đang đứng gần cửa hang bất ngờ tắt đuốc.

Có người.

Mọi người lập tức im lặng.

Tiếng bước chân vang lên bên ngoài khe đá.

Vết chân mới.

Một giọng nói trầm thấp truyền tới.

Có người vừa vào đây.

Tạ Hành Chu nhẹ nhàng rút đao.

Tam trưởng lão ra hiệu cho Vãn Ninh đứng lui về phía trong.

Lục Văn Sơn cầm gậy trúc, nấp cạnh cửa.

Bên ngoài, người nọ tiếp tục nói:

Kiểm tra.

Một lưỡi kiếm chậm rãi xuyên qua bụi dây leo.

Tạ Hành Chu siết chặt chuôi đao.

Những động tác vừa luyện trước vách đá hiện lên trong đầu.

Chàng chưa từng sử dụng chúng để giao chiến thật sự.

Nhưng có vẻ cơ hội thử nghiệm đã tới sớm hơn dự kiến.
```

### CHUONG-0019-FINAL.md

```text
Chương 19: Lấy đao mở đường

Người đầu tiên vừa bước vào khe đá đã nhìn thấy Lục Văn Sơn.

Hắn giật mình, lập tức nâng kiếm.

Gậy trúc trong tay Lục Văn Sơn đập vào cổ tay hắn.

Thanh kiếm rơi xuống đất.

Tạ Hành Chu tiến lên, dùng sống đao ép người nọ vào vách.

Đừng động.

Kẻ đó còn chưa kịp kêu thì phía ngoài đã vang lên tiếng quát.

Có địch!

Hai người khác lập tức lao tới.

Lục Văn Sơn kéo tên vừa bị tước kiếm sang bên, tránh để hắn chắn lối đi.

Tam trưởng lão nói:

Không thể ở lại đây. Ra ngoài!

Tạ Hành Chu đi trước.

Khe đá quá hẹp, thanh đao bản dày khó xoay ngang.

Chàng phải giữ lưỡi đao nghiêng trước thân, vừa tiến vừa quan sát.

Một mũi kiếm đột nhiên đâm tới từ bên ngoài.

Hành Chu nghiêng người.

Mũi kiếm sượt qua tay áo.

Thay vì vung đao thật mạnh để phản kích, chàng dùng một động tác ngắn gạt thanh kiếm sang bên, sau đó bước lên chiếm khoảng trống.

Kẻ tấn công không ngờ chàng tiến nhanh như vậy.

Hắn vội lùi khỏi cửa hang.

Tạ Hành Chu nhân cơ hội lao ra ngoài.

Mưa đã tạnh, nhưng mặt đất vẫn trơn trượt.

Trước cửa có bốn người.

Hai trong số đó là những kẻ chàng từng thấy bên cửa đá.

Một nam nhân mặt dài nhìn Hành Chu.

Các ngươi tìm được gì trong hang?

Tạ Hành Chu đáp:

Củi mục, đá vụn. Nếu các vị thích, cứ vào lấy.

Nam nhân không tin.

Giao tay nải ra!

Trong đó có lương khô. Các vị định cướp cả cơm của người khác?

Bớt nói nhảm!

Nam nhân rút kiếm.

Tạ Hành Chu thở dài.

Vì mấy cái bánh mà động thủ, thật không có tiền đồ.

Thanh kiếm lao tới.

Hành Chu lập tức thu lại vẻ cười cợt.

Chàng xoay hông, dùng mặt đao đỡ kiếm.

Lực va chạm truyền vào cánh tay.

Đối phương không yếu.

Chỉ qua một lần giao phong, Hành Chu đã biết sức mạnh của hắn không kém mình.

Nếu đấu trực diện lâu dài, chàng chưa chắc chiếm được lợi thế.

Nam nhân mặt dài đổi hướng kiếm, đâm liên tiếp về phía ngực và bụng.

Tạ Hành Chu lùi hai bước.

Chàng nhớ tới những dấu đao trong hang.

Nhát thứ nhất mở đường.

Hành Chu gạt kiếm sang phải.

Nhát thứ hai ép đối thủ thay đổi vị trí.

Chàng chém nghiêng, buộc nam nhân phải lùi chân trái.

Nhát thứ ba tập trung sức lực.

Tạ Hành Chu chuyển bước, xoay hông, đưa lưỡi đao từ dưới lên.

Nam nhân mặt dài biến sắc.

Hắn vội dùng kiếm đỡ.

Một tiếng kim loại chói tai vang lên.

Đối phương lùi liền ba bước, cổ tay run rẩy.

Tạ Hành Chu cũng cảm thấy cánh tay mình tê dại.

Nhưng chàng không khỏi vui mừng.

Ba động tác vẫn còn thô vụng.

Nhịp chuyển tiếp chưa đủ nhanh.

Tuy nhiên, hiệu quả tốt hơn cách chém dồn dập trước kia.

Ở bên cạnh, Lục Văn Sơn đã đưa Tam trưởng lão và Vãn Ninh ra khỏi khe đá.

Hai kẻ còn lại muốn xông tới chặn đường.

Lục Văn Sơn vung gậy, buộc một tên phải lùi lại.

Vãn Ninh ném một gói bột xuống đất.

Mùi cay nồng lập tức lan ra.

Người cầm kiếm gần nhất ho sặc sụa.

Đi về phía suối! Tam trưởng lão quát.

Tạ Hành Chu không ham chiến.

Chàng chém thêm một đao ép nam nhân mặt dài lùi lại rồi quay người chạy theo mọi người.

Nhưng đối phương không chịu bỏ qua.

Đuổi theo!

Cả nhóm chạy dọc bờ suối.

Phía trước là một khoảng đất hẹp nằm giữa vách núi và dòng nước.

Tam trưởng lão đi tới đó thì bất ngờ trượt chân.

Lục Văn Sơn vội đỡ ông.

Tạ Hành Chu quay đầu.

Những kẻ truy đuổi đã tới gần.

Chàng nhìn khoảng đất hẹp, lập tức nói:

Mọi người đi trước!

Vãn Ninh quay lại.

Ngươi định làm gì?

Giữ đường.

Không được cố quá sức!

Tạ Hành Chu gật đầu.

Chàng đứng chắn giữa hai tảng đá lớn.

Ở vị trí này, đối phương chỉ có thể tiến lên từng người.

Nam nhân mặt dài lao tới đầu tiên.

Kiếm và đao lại va vào nhau.

Lần này, Hành Chu không còn đủ khoảng trống để liên tục né tránh.

Chàng phải đỡ nhiều hơn.

Một đường kiếm sượt qua vai.

Máu lập tức thấm ra áo.

Tạ Hành Chu cắn răng, dùng chân đạp mạnh vào mặt đất, xoay đao ép đối phương lùi lại.

Khí huyết trong cơ thể dần nóng lên.

Cảm giác quen thuộc ấy lại xuất hiện.

Mỗi lần giao phong, Hành Chu dường như hiểu rõ hơn trọng lượng của thanh đao.

Những động tác ban đầu còn gượng gạo bắt đầu trở nên thuận tay.

Chàng thử giảm bớt sức lực trong hai lần giao phong đầu, chỉ tập trung lực vào nhát phản kích cuối cùng.

Nam nhân mặt dài càng đánh càng kinh ngạc.

Hắn rõ ràng đã khiến đối thủ bị thương.

Vậy mà thanh đao trước mặt ngày càng khó gạt ra.

Ngươi dùng tà thuật gì?

Tạ Hành Chu thở mạnh.

Nếu ta biết tà thuật, việc đầu tiên sẽ là khiến ngươi im miệng.

Đối phương nổi giận, vận lực đâm thẳng tới.

Hành Chu gạt kiếm.

Xoay bước.

Chém.

Nam nhân mặt dài mất thăng bằng, ngã vào một tảng đá cạnh đường.

Tạ Hành Chu không đuổi theo.

Chàng lập tức quay người.

Cảm giác nóng trong ngực đã bắt đầu chuyển thành đau nhức.

Nếu tiếp tục giao chiến, tình trạng suy kiệt có thể lặp lại.

Hành Chu chạy được một đoạn thì nghe tiếng động phía sau.

Một kẻ khác đã vượt qua nam nhân mặt dài, cầm kiếm đuổi tới.

Chàng vừa định xoay người thì một cây gậy trúc từ bên cạnh xuất hiện.

Gậy đập mạnh vào thanh kiếm.

Lục Văn Sơn đứng chắn trước mặt kẻ truy đuổi.

Đi đi!

Tạ Hành Chu không chần chừ.

Lục Văn Sơn vừa đánh vừa lùi, nhanh chóng theo chàng rời khỏi lối hẹp.

Đến khi cả nhóm thoát khỏi thung lũng, trời đã gần trưa.

Tạ Hành Chu ngồi xuống bên một gốc cây, lồng ngực phập phồng.

Vãn Ninh lập tức kéo áo trên vai chàng ra.

Vết thương không sâu, nhưng vẫn cần xử lý.

Ngươi lại bị thương.

Hành Chu nhìn nàng.

Lần này chỉ một vết.

Ngươi còn thấy tự hào?

Có tiến bộ.

Vãn Ninh dùng thuốc rắc lên vết thương.

Tạ Hành Chu lập tức hít mạnh.

Nhị sư tỷ, nhẹ tay!

Đừng nhúc nhích.

Chàng đành ngồi yên.

Lục Văn Sơn uống một ngụm nước, nhìn Hành Chu với vẻ khác lạ.

Đao pháp của ngươi học từ ai?

Vừa học được một chút từ trưởng lão.

Còn ba nhát liên tiếp vừa rồi?

Tạ Hành Chu thành thật đáp:

Nhìn mấy vết đao trong hang rồi tự nghĩ ra.

Lục Văn Sơn im lặng hồi lâu.

Ngươi có ngộ tính khá tốt.

Hành Chu mỉm cười.

Tiền bối quá khen. Nếu có thể đổi ngộ tính lấy linh thạch, vãn bối sẽ vui hơn nhiều.

Tam trưởng lão lắc đầu.

Ông lấy chiếc hộp đồng ra kiểm tra.

Mảnh ngọc vẫn còn nguyên.

Những người vừa rồi có lẽ không biết mục đích thực sự của kẻ gửi thư. Chúng chỉ đang tìm kiếm thứ gì đó ở Bạch Khê.

Lục Văn Sơn nói:

Vậy chúng ta đã mất cơ hội kiểm tra cửa đá.

Tạ Hành Chu nhìn về hướng thung lũng.

Chưa chắc.

Ý ngươi là?

Người gửi thư biết trưởng lão sẽ tới. Nếu mục đích chỉ là dẫn chúng ta đến cửa đá kia, vậy tại sao lại để nhiều nhóm người khác biết vị trí trước?

Không ai trả lời ngay.

Hành Chu tiếp tục:

Có thể thứ chúng ta cần tìm không nằm sau cánh cửa mà những kẻ kia đang tranh giành.

Tam trưởng lão nhìn chàng.

Sau đó, ông lấy mảnh giấy vẽ bản đồ ra.

Cả nhóm đã đi theo dòng suối chính.

Nhưng trên tờ giấy, bên cạnh dòng nước còn có một nét mực rất nhỏ kéo về phía sườn núi phía nam.

Nét mực ấy trước đó gần như bị bỏ qua.

Lục Văn Sơn nhìn kỹ.

Đường cũ?

Tam trưởng lão chậm rãi gật đầu.

Có một cây cầu đá ở hướng đó. Nếu nó chưa sập, có thể đi vòng về phía sau Bạch Khê.

Tạ Hành Chu thở dài.

Xem ra hôm nay lại không được ăn cơm đúng giờ.

Vãn Ninh buộc lớp băng cuối cùng trên vai chàng.

Ngươi nghỉ thêm một lát rồi mới đi.

Hành Chu nhìn nàng.

Lần này, chàng ngoan ngoãn gật đầu.
```

### CHUONG-0020-FINAL.md

```text
Chương 20: Bí mật dưới cây cầu cũ

Cây cầu đá nằm giữa hai sườn núi thấp, bị dây leo che phủ gần như hoàn toàn.

Một phần lan can đã đổ xuống vực.

Nhưng mặt cầu vẫn còn nguyên.

Tam trưởng lão đứng ở đầu cầu, nhìn những viên đá xám đã phủ đầy rêu.

Trước kia, mỗi khi tới Bạch Khê, đệ tử trong tông thường đi đường này.

Tạ Hành Chu nhìn xuống khe sâu bên dưới.

Các vị tiền bối thật sự rất thích chọn đường khó đi.

Đường này ngắn hơn nửa ngày.

Vậy cũng có lý.

Hành Chu lập tức bước lên.

Vãn Ninh nắm lấy tay áo chàng.

Chậm thôi.

Tạ Hành Chu nhìn bàn tay nàng.

Nhị sư tỷ lo ta rơi xuống sao?

Ta lo ngươi làm sập cầu.

Hành Chu đặt tay lên ngực.

Lời này khiến ta tổn thương hơn cả vết kiếm vừa rồi.

Vãn Ninh buông tay, đi theo phía sau.

Lục Văn Sơn và Tam trưởng lão bước tới giữa cầu.

Ở đó có một khối đá lớn hơn những viên còn lại.

Tam trưởng lão cúi xuống, gạt lớp rêu trên mặt đá.

Một ký hiệu nhỏ dần hiện ra.

Không phải hình chim.

Mà là hình ba ngọn núi nối tiếp nhau.

Lão nhân nhìn ký hiệu, vẻ mặt lập tức thay đổi.

Vẫn còn.

Lục Văn Sơn tiến lại.

Ngươi nhận ra?

Là dấu hiệu chỉ đường cũ của Thanh Vân Tông.

Tam trưởng lão nhìn sang hai bên.

Ngày trước, khi đệ tử xuống núi gặp nguy hiểm, có thể để lại tin tức ở những nơi mang dấu này.

Tạ Hành Chu hỏi:

Vậy có chỗ giấu đồ?

Lão nhân gật đầu.

Cả nhóm bắt đầu kiểm tra quanh chân cầu.

Sau một lúc, Vãn Ninh phát hiện một viên đá nhỏ nằm sâu dưới lan can, bề mặt có dấu mài mòn khác với những viên xung quanh.

Lục Văn Sơn dùng gậy trúc đẩy thử.

Viên đá dịch chuyển.

Bên trong là một hốc nhỏ.

Tam trưởng lão đưa tay vào.

Ông lấy ra một ống trúc đã được bịt kín bằng sáp.

Không ai nói gì.

Lão nhân mở ống.

Bên trong có một mảnh giấy cuộn chặt.

Giấy còn khá mới.

Trên đó viết:

Ngọc chỉ là tín vật. Đừng tới cửa đá.

Có người đang dùng danh nghĩa Thanh Vân Tông thu gom tu sĩ.

Hãy tìm người giữ sổ tại bến Bạch Lộ.

Tam trưởng lão đọc đi đọc lại.

Lục Văn Sơn nhíu mày.

Bến Bạch Lộ nằm ở phía đông Trường Phong Thành.

Tạ Hành Chu nhìn nét chữ.

Người để lại lời nhắn biết chúng ta sẽ mang mảnh ngọc tới đây.

Có thể hắn là người gửi thư.

Cũng có thể là một kẻ khác.

Hành Chu chỉ vào dòng cuối.

Người giữ sổ là ai? Sổ gì? Nếu không nói rõ, đến bến Bạch Lộ chúng ta vẫn phải tự tìm.

Tam trưởng lão cất tờ giấy.

Ít nhất đã có một địa điểm.

Đúng lúc ấy, Vãn Ninh đột nhiên đưa tay giữ lấy lan can.

Sắc mặt nàng trở nên tái nhợt.

Tạ Hành Chu lập tức đỡ lấy nàng.

Nhị sư tỷ?

Vãn Ninh khẽ lắc đầu.

Không sao.

Nhưng bàn tay đang nắm lấy tay áo chàng lạnh bất thường.

Hành Chu không để nàng đứng tiếp.

Chàng dìu Vãn Ninh tới đầu cầu, tìm một tảng đá sạch để nàng ngồi xuống.

Cho ta xem cổ tay.

Vãn Ninh im lặng.

Nhị sư tỷ.

Lần này, giọng Hành Chu không còn ý đùa cợt.

Một lúc sau, nàng chậm rãi kéo tay áo lên.

Vệt đỏ dưới da đã lan dài hơn trước.

Tạ Hành Chu nhìn nó.

Đau từ khi nào?

Không lâu.

Đã mấy ngày rồi?

Vãn Ninh tránh ánh mắt chàng.

Hành Chu thở dài.

Vậy là không phải không lâu.

Tam trưởng lão bước tới.

Ông nhìn cổ tay nàng, vẻ mặt trầm xuống.

Lại phát tác?

Vãn Ninh gật đầu.

Tạ Hành Chu nhìn hai người.

Trưởng lão biết chuyện này?

Biết một phần.

Có thể chữa không?

Tam trưởng lão im lặng.

Vãn Ninh lên tiếng trước:

Ta đang tìm cách.

Hành Chu ngồi xuống trước mặt nàng.

Cần dược liệu gì?

Hiện tại không phải vấn đề dược liệu.

Vậy là vấn đề gì?

Vãn Ninh nhìn chàng.

Trong mắt nàng có chút do dự.

Có một số chuyện, ta chưa muốn nói.

Tạ Hành Chu không hỏi tiếp.

Chàng lấy túi nước đưa cho nàng.

Được. Khi nào tỷ muốn nói, ta sẽ nghe.

Vãn Ninh nhận lấy túi nước.

Hành Chu tiếp tục:

Nhưng từ bây giờ, nếu tỷ cảm thấy không khỏe thì phải nói. Chuyện giấu bệnh không được tính vào bí mật cá nhân.

Nàng nhìn chàng.

Ngươi đang ra lệnh cho ta?

Không dám.

Vậy là gì?

Lời đề nghị chân thành của một người rất có kinh nghiệm bị thương.

Vãn Ninh không nhịn được cười.

Một lát sau, nàng khẽ nói:

Ta biết rồi.

Cả nhóm quyết định không tiếp tục điều tra trong ngày hôm ấy.

Họ tìm một nơi kín gió nghỉ ngơi.

Vãn Ninh uống thuốc mang theo, sắc mặt dần tốt hơn.

Tạ Hành Chu ngồi cách nàng không xa, lặng lẽ lau thanh đao.

Lục Văn Sơn và Tam trưởng lão đang nói chuyện ở phía đối diện.

Hành Chu nhìn bề mặt lưỡi đao.

Trong trận chiến vừa rồi, chàng đã tiến bộ.

Không chỉ bởi sự biến đổi kỳ lạ của khí huyết, mà còn bởi cách dùng đao được sửa đổi trong mấy ngày qua.

Chàng bắt đầu hiểu một điều.

Muốn trở nên mạnh mẽ, không thể chỉ trông chờ vào sức lực tăng lên trong lúc giao chiến.

Nếu thân thể không đủ khỏe, khí huyết sẽ cạn kiệt.

Nếu kỹ thuật dùng đao không đủ tốt, sức mạnh có tăng cũng sẽ bị lãng phí.

Tạ Hành Chu lấy tờ giấy ghi chép ra.

Chàng viết lại những cảm nhận trong trận chiến, đánh dấu những thời điểm khí huyết nóng lên và những lúc cơ thể bắt đầu suy yếu.

Sau đó Hành Chu mở cuốn sách luyện thể bị hư hỏng lấy được trong hang.

Chàng chỉ quan sát những hình vẽ còn nguyên, không thử vận hành bất kỳ phương pháp nào.

Một vài động tác trong sách có vẻ liên quan đến cách rèn luyện phần lưng và chân.

Đó chính là những nơi Tam trưởng lão thường nhắc tới khi sửa đao pháp cho chàng.

Hành Chu quyết định sau khi trở về sẽ cùng lão nhân xem xét kỹ.

Chàng đang định cất sách thì Vãn Ninh ngồi xuống bên cạnh.

Ngươi đang xem gì?

Một thứ có thể giúp ta khỏe hơn.

Đừng luyện bừa.

Ta biết.

Tạ Hành Chu nghiêng đầu nhìn nàng.

Nhị sư tỷ, tỷ thấy nếu ta trở thành một cường giả, có thể kiếm được nhiều linh thạch không?

Có lẽ.

Vậy sau này tỷ cần thuốc gì, ta mua hết.

Vãn Ninh hơi ngẩn người.

Hành Chu cười.

Nhưng tiền thuốc chữa thương cho ta trước đây thì có thể miễn được không?

Nàng quay mặt đi.

Không.

Giảm một nửa?

Không.

Ba thành?

Vãn Ninh đứng dậy.

Tạ Hành Chu nhìn bóng lưng nàng.

Nhị sư tỷ, chuyện gì cũng có thể thương lượng mà!

Nàng không quay lại.

Nhưng bước chân nhẹ hơn lúc trước rất nhiều.

Trời gần tối, Tam trưởng lão quyết định trở về Thanh Vân Tông.

Lục Văn Sơn sẽ xuống núi sau khi đưa mọi người tới nơi an toàn, tìm cách thu thập tin tức về bến Bạch Lộ.

Trước lúc rời đi, Tạ Hành Chu quay lại nhìn cây cầu đá lần cuối.

Chàng vẫn chưa biết ai để lại lời nhắn.

Cũng chưa biết vì sao người đó phải dẫn Tam trưởng lão đi một vòng lớn như vậy.

Nhưng những kẻ xuất hiện ở cửa đá, con dấu cũ, những người bị bắt và bến Bạch Lộ dường như đang dần nối lại với nhau.

Hành Chu có cảm giác phía sau tất cả những chuyện ấy còn một bàn tay khác.

Một bàn tay đã kiên nhẫn sắp xếp mọi thứ từ rất lâu.
```

### CHUONG-0021-FINAL.md

```text
Chương 21: Ngày đầu tiên của con đường cường giả

Khi Thanh Vân Tông hiện ra phía cuối con đường núi, Tạ Hành Chu lập tức cảm thấy bụng mình đói hơn.

A Thạch đang đứng trước cổng.

Vừa thấy mọi người, đứa trẻ chạy tới.

Tiểu sư huynh! Nhị sư tỷ!

Tạ Hành Chu dang tay.

Có nhớ ta không?

A Thạch gật đầu thật mạnh.

Có!

Hành Chu còn chưa kịp cảm động thì đứa trẻ đã hỏi:

Huynh có mua bánh về không?

Chàng chậm rãi thu tay lại.

Tình nghĩa đồng môn thật mong manh.

A Thạch nhìn túi hành lý.

Không có sao?

Có hai cái lương khô.

Cũng được!

Tạ Hành Chu đưa túi cho đứa trẻ.

Kỷ Thanh La từ trong sân bước ra.

Nàng nhìn mọi người, ánh mắt dừng lại trên lớp băng mới ở vai Hành Chu.

Lại đánh nhau?

Tạ Hành Chu cười.

Chỉ giao lưu đao kiếm với mấy vị bằng hữu mới quen.

Bọn họ đâu?

Có lẽ vẫn đang nhớ thương ta.

Kỷ Thanh La không hỏi tiếp.

Nàng nhìn Vãn Ninh.

Muội không sao chứ?

Vãn Ninh gật đầu.

Về phòng rồi nói.

Kỷ Thanh La lập tức hiểu rằng chuyến đi không đơn giản.

Sau bữa tối, mọi người tập trung trong chính điện.

Tam trưởng lão đặt mảnh ngọc, tờ giấy và tấm bản đồ lên bàn.

Lục Văn Sơn đã xuống núi trước khi trời tối.

Kỷ Thanh La nghe kể toàn bộ những gì xảy ra ở Bạch Khê, từ nhóm người tìm cửa đá đến lời nhắn dưới cây cầu.

Khi nghe tới việc thu gom tu sĩ, nàng lập tức lấy tờ giấy dầu vẫn luôn giữ bên mình.

Những người ở Trạm Thanh Giản có thể đã được chuyển tới nơi khác.

Tam trưởng lão gật đầu.

Bến Bạch Lộ là một địa điểm đáng nghi. Nhưng chưa thể chắc chắn.

Tạ Hành Chu quan sát hai tờ giấy.

Nếu thật sự có một danh sách ghi lại những người bị đưa đi, người giữ sổ có thể biết nhiều hơn chúng ta.

Kỷ Thanh La hỏi:

Ngươi định tới đó?

Không phải ngay bây giờ.

Hành Chu chỉ vào vai mình.

Ta vừa trải qua một trận chiến không mấy dễ chịu. Nếu tới một nơi nguy hiểm hơn với bản lĩnh hiện tại, có khi còn chưa tìm thấy sổ đã bị người ta ghi tên vào đó.

Tam trưởng lão bật cười.

Cuối cùng cũng biết mình yếu.

Vãn bối luôn biết. Chỉ là bình thường không thích nói ra.

Kỷ Thanh La nhìn chàng.

Vậy ngươi muốn làm gì?

Tu luyện.

Câu trả lời khiến mọi người hơi bất ngờ.

Tạ Hành Chu bình tĩnh nói tiếp:

Trong mấy ngày qua, chúng ta gặp phải quá nhiều người không rõ lai lịch. Mỗi lần muốn tìm hiểu một chuyện lại phải đánh nhau. Nếu cứ như vậy, sớm muộn cũng gặp phải kẻ mà chúng ta không thể chống đỡ.

Chàng đặt tay lên chuôi đao.

Trước khi tiếp tục xuống núi, ta muốn có thêm một chút khả năng tự bảo vệ mình.

Tam trưởng lão nhìn Hành Chu hồi lâu.

Sau đó ông gật đầu.

Được.

Sáng hôm sau, Tạ Hành Chu chủ động thức dậy trước khi Tam trưởng lão tới gọi.

Chàng thay quần áo, mang đao ra sân phía tây.

Khi lão nhân xuất hiện, Hành Chu đã đứng tấn dưới gốc cây.

Tam trưởng lão nhìn mặt trời còn chưa mọc.

Tiểu tử, ngươi uống nhầm thuốc sao?

Tạ Hành Chu không nhúc nhích.

Vãn bối quyết định từ hôm nay sẽ chăm chỉ tu luyện.

Được bao lâu?

Ít nhất tới bữa sáng.

Lão nhân bật cười.

Sau đó hai người bắt đầu buổi luyện tập.

Lần này, Tam trưởng lão không yêu cầu Hành Chu chém gỗ.

Ông đặt một viên đá lớn giữa sân.

Nhấc lên.

Tạ Hành Chu cúi xuống, dùng hai tay ôm viên đá.

Nặng hơn chàng tưởng.

Chàng cố nâng lên ngang bụng.

Giữ nguyên.

Không lâu sau, hai cánh tay bắt đầu run.

Tam trưởng lão đứng bên cạnh điều chỉnh tư thế.

Đừng dồn toàn bộ sức lên vai. Hạ thấp trọng tâm. Dùng chân và lưng.

Tạ Hành Chu làm theo.

Viên đá vẫn rất nặng, nhưng áp lực trên hai cánh tay giảm đi đôi chút.

Sau khi đặt đá xuống, Hành Chu phải nghỉ một lúc mới lấy lại hơi thở.

Tam trưởng lão đưa cho chàng một cây gậy gỗ.

Luyện lại ba động tác ngươi tự nghĩ ra trong hang.

Hành Chu nhận gậy.

Chàng thực hiện từng động tác chậm rãi.

Lão nhân quan sát, thỉnh thoảng chỉ ra một vài sai sót.

Nhát thứ hai không cần đi xa như vậy.

Chân phải thu lại một chút.

Đúng rồi. Nếu đối phương lùi, ngươi không nhất thiết phải đuổi theo.

Tạ Hành Chu kiên nhẫn sửa từng điểm.

Chàng không đặt tên cho ba động tác ấy.

Hiện tại chúng còn quá thô sơ để được gọi là một bộ đao pháp.

Nhưng đây là lần đầu tiên Hành Chu tự tìm ra một cách phối hợp các đòn thế, rồi cải thiện nó bằng thực chiến và luyện tập.

Cảm giác ấy khác hẳn việc học thuộc một chiêu thức có sẵn.

Chàng muốn tiếp tục.

Những ngày sau đó, sinh hoạt ở Thanh Vân Tông dần trở lại bình thường.

Kỷ Thanh La tiếp tục dưỡng thương.

Vãn Ninh nghiên cứu thuốc.

A Thạch quét sân, chăm sóc chim sẻ và thỉnh thoảng tìm cách trốn việc.

Tam trưởng lão sửa mái nhà, uống rượu và dạy Hành Chu luyện tập.

Còn Tạ Hành Chu, ngoài những việc thường ngày, bắt đầu dành nhiều thời gian hơn cho việc rèn luyện thân thể.

Ban đầu chàng chỉ nâng đá, chạy trên những bậc thềm và thực hiện các động tác đứng tấn.

Sau đó mới chuyển sang luyện đao.

Mỗi khi thân thể xuất hiện dấu hiệu quá tải, Hành Chu chủ động dừng lại.

Chàng không muốn lặp lại sai lầm dùng cạn khí huyết trong những trận chiến trước.

Một buổi chiều, Hành Chu đứng giữa sân, hoàn thành nhát đao cuối cùng.

Mồ hôi đã thấm ướt áo.

Chàng thu đao, ngồi xuống dưới bóng cây.

Hơi thở dần ổn định.

Trong cơ thể có một luồng ấm áp rất nhẹ lưu chuyển.

Không mãnh liệt như khi giao chiến.

Cũng không khiến Hành Chu đột nhiên có được sức mạnh kinh người.

Nhưng sau khi nghỉ ngơi, chàng nhận ra sự mệt mỏi đã giảm nhanh hơn một chút so với những ngày đầu luyện tập.

Hành Chu không biết đó là kết quả của việc rèn luyện thân thể hay liên quan đến sự biến đổi khí huyết kỳ lạ.

Chàng chỉ biết một điều.

Cơ thể mình đang thay đổi.

Từng chút một.

Tạ Hành Chu lấy giấy ghi chép, viết xuống những cảm nhận trong ngày.

Sau đó, chàng ngẩng đầu nhìn khoảng sân đầy lá rụng.

Một ý nghĩ bất chợt xuất hiện.

Nếu một ngày nào đó, chàng có thể dùng thanh đao này mà không cần lo lắng bản thân sẽ cạn sức giữa trận chiến thì tốt biết bao.

Nếu một ngày nào đó, Thanh Vân Tông không còn phải sợ những kẻ gửi thư đe dọa thì tốt biết bao.

Nếu một ngày nào đó, Vãn Ninh không cần giấu cổ tay đang đau dưới lớp áo...

Tạ Hành Chu khẽ thở ra.

Chàng cất giấy.

Đứng dậy.

Cầm đao.

Và bắt đầu thêm một lượt luyện tập nhẹ nhàng nữa.

Đêm ấy, Vãn Ninh đang sắp xếp những lọ thuốc trong phòng thì nghe tiếng gõ cửa.

Nàng mở cửa.

Tạ Hành Chu đứng bên ngoài, tay cầm một chiếc bát.

Nhị sư tỷ, ăn tối chưa?

Rồi.

Vậy ăn thêm một chút.

Bên trong bát là một ít canh nóng.

Vãn Ninh nhận ra mùi vị khá quen thuộc.

Ngươi nấu?

Đúng.

Nàng nhìn chàng với vẻ nghi ngờ.

Có thể uống được không?

Tạ Hành Chu đau lòng đáp:

Nhị sư tỷ, giữa chúng ta chẳng lẽ không có chút tin tưởng nào?

Vãn Ninh nhận bát, nếm thử một ngụm.

Vị canh nhạt, nhưng không khó uống.

Cũng được.

Hành Chu lập tức vui vẻ.

Ta đã thử trước rồi. Nếu có độc thì hiện tại tỷ đang đứng trước một thi thể biết nói.

Vãn Ninh bật cười.

Nàng mang bát vào phòng.

Tạ Hành Chu định quay về thì nghe nàng gọi.

Hành Chu.

Chàng quay lại.

Vãn Ninh đứng bên cửa, dưới ánh đèn dầu.

Sau này, nếu có chuyện nguy hiểm, đừng lúc nào cũng đứng lại một mình.

Tạ Hành Chu nhìn nàng.

Ta không thích nhìn người khác bị thương.

Ta cũng vậy.

Nàng nói rất khẽ.

Hành Chu im lặng trong chốc lát.

Sau đó, chàng mỉm cười.

Được. Ta nhớ rồi.

Vãn Ninh gật đầu, khép cửa.

Tạ Hành Chu đứng ngoài hành lang thêm một lúc.

Chàng bỗng cảm thấy đêm nay gió núi dường như không lạnh như mọi ngày.

Sáng ngày thứ bảy sau khi trở về từ Bạch Khê, Lục Văn Sơn gửi tin tới Thanh Vân Tông.

Lần này không phải một phong thư.

Mà là một người.

Đó là một thiếu phụ mặc áo vải, mang theo chiếc giỏ trúc cũ. Nàng đứng trước sơn môn, vẻ mặt mệt mỏi, hai bàn tay có nhiều vết chai.

A Thạch dẫn nàng vào sân.

Tam trưởng lão nhận ra tín vật do Lục Văn Sơn gửi kèm.

Ngươi từ bến Bạch Lộ tới?

Thiếu phụ gật đầu.

Lục tiên sinh bảo ta có thể tìm người giúp đỡ ở đây.

Kỷ Thanh La bước tới.

Ngươi gặp chuyện gì?

Thiếu phụ cúi đầu.

Phu quân của ta mất tích gần hai tháng trước.

Nàng lấy từ trong giỏ ra một tờ giấy nhỏ.

Trước khi biến mất, chàng nhận việc vận chuyển hàng tại bến Bạch Lộ. Người thuê nói chỉ cần làm việc trong mười ngày sẽ được trả công hậu hĩnh.

Tam trưởng lão nhận tờ giấy.

Tạ Hành Chu đứng bên cạnh nhìn xuống.

Đó là một giấy nhận việc thông thường, phía dưới ghi tên thương đội và số tiền ứng trước.

Nhưng ở góc dưới cùng có một dấu mực rất nhỏ.

Hình một con chim đang dang cánh.

Kỷ Thanh La lập tức bước tới gần.

Ngươi còn giữ giấy tờ nào khác không?

Thiếu phụ gật đầu.

Nàng run rẩy lấy ra một mảnh giấy đã nhàu nát.

Cái này có người lén đưa cho ta ba ngày trước.

Tạ Hành Chu nhận lấy.

Trên giấy chỉ có một dòng chữ.

Muốn gặp phu quân, đừng tới quan phủ. Hãy tìm người của Thanh Vân Tông.

Mọi người đồng loạt im lặng.

Tam trưởng lão nhìn tờ giấy, bàn tay dần siết chặt.

Kỷ Thanh La lấy tờ giấy dầu của mình ra, đặt cạnh hai mảnh giấy mới.

Vãn Ninh khẽ hỏi:

Vì sao lại bảo nàng tới tìm chúng ta?

Không ai có câu trả lời.

Thiếu phụ nhìn từng người, giọng nghẹn lại.

Các vị... có biết phu quân của ta đang ở đâu không?

Tạ Hành Chu nhìn đôi mắt đỏ hoe của nàng.

Chàng không thể hứa sẽ tìm được người.

Cũng không thể nói rằng mọi chuyện nhất định sẽ tốt đẹp.

Hành Chu kéo một chiếc ghế tới.

Đại tẩu, ngồi xuống trước đi. Kể cho chúng ta nghe từ đầu, đừng bỏ sót bất kỳ chuyện gì.

Thiếu phụ chậm rãi ngồi xuống.

A Thạch chạy vào bếp lấy nước.

Ngoài sân, gió thổi qua tấm biển Thanh Vân Tông cũ kỹ.

Tạ Hành Chu đưa mắt nhìn thanh đao bên hông.

Chàng vốn định dành thêm một khoảng thời gian để tu luyện.

Nhưng có những người không thể chờ được lâu như vậy.

Lần này, bí mật của Thanh Vân Tông không còn chỉ liên quan đến quá khứ của những người trong tông.

Nó đã bắt đầu kéo những người vô tội vào vòng xoáy.

Và ở một nơi nào đó, có kẻ đang cố tình khiến Thanh Vân Tông bước vào cuộc chơi.
```
