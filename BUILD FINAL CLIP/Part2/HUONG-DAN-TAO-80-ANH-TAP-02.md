# HƯỚNG DẪN AGENT TẠO 80 ẢNH — TẬP 2

**Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát | Tiên Vực Ký | Chương 8–14 FINAL**

Nguồn: bảy file FINAL trong TAP-02-CHUONG-08-14-FINAL.zip. CSV mới giữ 8 cột gốc và bổ sung các cột mô tả/prompt. Đây là storyboard sản xuất, không sửa truyện. Tuổi ước lệ, màu sắc và chi tiết mỹ thuật chưa được nêu trong truyện là thiết kế tham chiếu hình ảnh, không phải CANON.

## Mệnh lệnh bắt buộc
- Thay toàn bộ yêu cầu 300 ảnh trong hướng dẫn dựng cũ bằng đúng 80 ảnh trong CSV mới. Không tự bổ sung ảnh, không tự đổi thứ tự. Không dùng ảnh lỗi từ các lần tạo trước.
- Tạo từng ảnh độc lập bằng công cụ tạo ảnh thật; 80 file PNG ngang 16:9, ưu tiên 1920×1080 hoặc độ phân giải cao hơn. Không tạo bảng 10 ô rồi crop, không ảnh ghép, không in tên file vào ảnh.
- Tạo reference sheet riêng cho các nhân vật chính trước, dùng làm input tham chiếu nếu engine hỗ trợ; reference sheet không được tính vào 80 ảnh hoặc timeline. Khóa seed/model/style nếu có; dùng cùng ảnh reference đã duyệt cho mọi lần xuất hiện. Không thay khuôn mặt giữa cảnh. Nếu engine không hỗ trợ reference, dùng mô tả cố định nguyên văn trong CSV, đối chiếu bằng mắt sau từng ảnh.
- Đọc image_prompt của đúng một dòng, không gửi toàn bộ CSV vào một lượt sinh ảnh. Không ghép nhiều prompt vào một yêu cầu sinh ảnh. Tạo từng ảnh, kiểm tra rồi mới lưu chính xác image_file. Nếu sai, tạo lại đúng dòng đó; không dùng ảnh gần đúng thay thế.
- Bố cục ưu tiên toàn/trung cảnh đủ thấy nhân vật và địa điểm; cận cảnh chỉ khi vật phẩm hoặc cảm xúc là trọng tâm. Hội thoại giữ chung một khung hình, không bắt buộc minh họa từng câu.
- Không tự tạo nhân vật tông chủ, đám đông đệ tử Thanh Vân, yêu thú, ngọc bội hoặc pháp thuật phát sáng. Thanh Vân Tông rất nghèo, Hành Chu chưa mạnh.
- Tên file chỉ là mã trên ổ đĩa; không chữ trong ảnh. Ảnh thumbnail không được dùng làm phân cảnh.

## Thiết kế hình ảnh chung
Một ảnh độc lập ngang 16:9, 1920×1080 trở lên (nếu engine không hỗ trợ đúng thì xuất tỷ lệ 16:9 gần nhất, không kéo méo). Minh họa tiên hiệp huyền huyễn điện ảnh bán hiện thực/realistic 3D concept art cao cấp, gương mặt Đông Á đẹp tự nhiên, tóc và vải chi tiết, ánh sáng điện ảnh có chiều sâu, màu lam trầm và xanh ngọc hài hòa, bố cục rõ, nhân vật đủ lớn để xem trên điện thoại, tay chân đúng giải phẫu, không phô trương sức mạnh ngoài truyện. Chỉ một khung hình, không collage, không viền, không chữ, không mã ảnh, không logo, không watermark.

## Character bible — giữ nguyên xuyên suốt
- **HC** — Tạ Hành Chu: nam thanh niên Đông Á khoảng 20–25 tuổi (thiết kế hình), khuôn mặt tuấn tú góc cạnh, mày đen thẳng, mắt nâu đen sắc nhưng hay cười, tóc đen dài buộc cao bằng dây vải đơn giản; thân hình săn chắc vừa phải; áo vải xanh xám/lam trầm nhiều lớp, thắt lưng vải nâu, giày vải đen, không giáp quý, không vương miện. Vết thương sườn và tay từ Tập 1, băng vải trắng ngà; không sẹo mặt vĩnh viễn.
- **VN** — Vãn Ninh: nữ trưởng thành Đông Á khoảng 20–25 tuổi, thanh tú, mặt trái xoan, mắt nâu đen, tóc đen dài búi nửa đầu gọn bằng trâm gỗ, áo cổ phong xanh ngọc nhạt kín đáo, tay áo thực dụng, đai vải xanh sẫm, giỏ trúc dược liệu khi đi ngoài; không vũ khí kiếm, không trang sức cầu kỳ, vệt đỏ cổ tay chỉ lộ khi truyện nói.
- **KL** — Kỷ Thanh La: nữ trưởng thành Đông Á khoảng 22–27 tuổi, đẹp lạnh lùng, mặt thanh sắc nét, mắt đen, tóc đen dài buộc nửa đầu đơn giản; hắc y đen than viền xám, băng trắng ngà kín vai bị thương, sắc mặt nhợt; nằm hoặc tựa phản khi dưỡng thương. Không biến thành nam, không tóc bạc, không áo trắng, không dùng kiếm nguyên vẹn.
- **AS** — A Thạch: bé trai Đông Á khoảng 8–10 tuổi (thiết kế hình), nhỏ gầy, mặt tròn dễ thương, mắt đen to, tóc đen búi nhỏ hơi rối, áo vải nâu đất rộng, quần xám, giày vải; tuyệt đối không người lớn, không râu, không chiến đấu.
- **EL** — Tam trưởng lão: lão nhân Đông Á khoảng 65–75 tuổi, tóc bạc rối búi thấp, râu bạc ngắn, mặt nhăn hiền và tinh nghịch, đạo bào xám cũ, hồ lô rượu nâu bên hông; không trang phục tông chủ, không ngai vàng, không hào quang.
- **CT** — Chu Tứ: nam trưởng thành Đông Á 30–40 tuổi, gầy, mặt hốc hác cảnh giác, tóc búi thấp rối, áo nâu xám cũ, bị giữ trong kho; không áo sang, không phải Trác Cửu.
- **SPY** — Kẻ theo dõi: nam trưởng thành tóc búi, áo nâu bình thường với một miếng vá đen rõ trên tay áo, nét mặt kín đáo; không mặt nạ.
- **LU** — Lưu chưởng quầy: lão dược thương tóc hoa râm, râu ngắn, áo vải nâu nhạt, dáng gầy, bình thường.
- **SM** — Thợ rèn: nam trung niên vai rộng, tóc đen búi, tay áo xắn hoặc để trần cánh tay, tạp dề da sẫm, không vũ khí trang trí.
- **DO** — Lão Đỗ: ông lão hái thuốc khoảng 65–75 tuổi, tóc bạc thưa búi thấp, râu lưa thưa, mặt nhăn hiền, áo nâu bạc màu, dáng gầy.
- **DB** — Đỗ Bình: thiếu niên nam 16 tuổi, gầy, tóc đen búi nhỏ, áo vải nâu nhạt có miếng vá hình lá, chân bị thương băng kín sau chữa; không râu, không cường giả.
- **HA** — Hà Thuận: nam trung niên khoảng 40 tuổi, tóc búi gọn, áo vải thương nhân màu xám nâu sạch và chỉnh tề hơn người hái thuốc, không vũ khí.
- **HERB** — Hai người hái thuốc phụ: một nam lớn tuổi và một người trưởng thành, áo vải thô nâu/xám, dáng mệt, không vũ khí; giữ ngoại hình giống nhau qua các cảnh.
- **G2** — Hai tên canh khe đá: nam trưởng thành áo vải sẫm, tên thứ nhất đai xám, tên thứ hai dùng dao ngắn; khuôn mặt khác nhau, không giáp, không mặt nạ.
- **GUARD** — Nhóm canh trại: nam trưởng thành áo nâu/xám sẫm thô, một tên chắc người cầm trường côn gỗ, một tên gầy cầm kiếm thẳng, các tên phụ chỉ xuất hiện đúng số ghi ở cảnh.
- **BOSS** — Thủ lĩnh áo đen: nam trưởng thành cao lớn khoảng 35–45 tuổi, mặt nghiêm lạnh, tóc đen búi cao, hắc y đen trơn thắt đai sẫm, trường kiếm thẳng hai lưỡi, không mặt nạ, không giáp vàng, không mắt đỏ hay ma khí.
- **VIS** — Vị khách áo xám: nam trung niên lớn tuổi, tóc đen điểm bạc buộc gọn, nét mặt trầm, áo vải xám bình thường, gậy trúc và tay nải lớn; khác Tam trưởng lão, không hồ lô rượu, không trang phục tông chủ.

## Location bible
- **PHONG** — Phòng phía tây Thanh Vân Tông: nhỏ, vách gỗ cũ, giường tre, bàn gỗ chân sửa, cửa sổ không khít, đèn dầu, ít đồ, không trang trí xa hoa.
- **BENH** — Gian phòng sau bếp Thanh Vân Tông: phản gỗ thấp, chăn vải thô, bàn nhỏ đựng bát thuốc, cửa sổ hẹp, vách gỗ cũ, ánh sáng dịu.
- **KHO** — Kho cũ Thanh Vân Tông: ván gỗ thô, vài bao tải, nền đất/đá, khe sáng nhỏ, không ngục đá hoành tráng.
- **GATE** — Sơn môn Thanh Vân Tông nhỏ nghèo: một cánh cổng gỗ mất nửa bên, hai trụ đá nghiêng, cỏ dại, mái chính điện thủng ngói, biển gỗ cũ; chỉ vài căn nhà, không đại điện nguy nga, không đoàn đệ tử.
- **YARD** — Sân Thanh Vân Tông: sân đá cũ nứt, cỏ dại, cây phía tây, mái ngói thủng, tường vỡ, không quảng trường lớn, không cung điện.
- **PATH** — Đường núi quanh co, bậc đá phủ rêu, thông, sương tự nhiên, núi thấp xa xa; không cung điện nổi, không thác nước khổng lồ.
- **TOWN** — Trấn cổ phong nhỏ: nhà gỗ mái ngói, phố đá, sạp hàng dân dã, người dân áo vải, không thành phố hiện đại, không cung đình.
- **SHOP** — Bách Thảo Đường: dược phô nhỏ với hộc thuốc gỗ, cân tay, giỏ dược liệu và lọ sứ, ánh sáng cửa phố, không đèn hình chim.
- **OLD** — Cửa hàng đồ cũ trong trấn: vải, nón tre, đồ gỗ, cửa sổ hẹp nhìn hẻm đá; không biển hiệu chữ vô nghĩa.
- **FORGE** — Lò rèn nhỏ: đe sắt, búa, than hồng, bàn gỗ, vài binh khí thô; ánh lửa ấm, không xưởng vũ khí thần thánh.
- **DOHOME** — Nhà lão Đỗ: căn nhà gỗ đất nhỏ cuối đường đất phía bắc trấn, bó dược liệu khô treo trước sân, bàn gỗ đơn giản.
- **FOREST** — Hắc Tùng Cốc: rừng thông rậm giữa hai núi thấp, nền lá thông, đất ẩm, rêu đá, suối nhỏ; ánh sáng xuyên tán, không yêu thú, không cung điện.
- **CAMP** — Bãi trại trong Hắc Tùng Cốc: nền đất phẳng nhỏ giữa rừng thông, lều vải thô duy nhất sát bụi cây, đống lửa, nồi sắt, bao lớn, không doanh trại hoành tráng.
- **CREVICE** — Khe đá lạnh: hai vách đá gần nhau, rêu ẩm, dòng nước nhỏ, vũng trong, lối vào hẹp đủ một người nghiêng thân; không hang pha lê.
- **CAVE** — Hốc đá sau khe hẹp: không gian nhỏ tối, tia sáng yếu từ khe phía trên, đá ẩm, bụi cây lá xanh nhạt, không hồ lớn, không tinh thể phát sáng.
- **TENT** — Bên trong lều vải thô nhỏ: cọc gỗ, nền đất, ánh sáng qua đường rạch, không ngục tù kiên cố.
- **BRIDGE** — Cầu gỗ nhỏ mục qua dòng suối lạnh có đá, hai thanh gỗ chịu lực và vài ván cũ, bờ thấp có cây thông; không cầu dây khổng lồ, không vực sâu.
- **KITCHEN** — Bếp Thanh Vân Tông: bếp lửa nhỏ, nồi đất/sắt, bàn gỗ, bát sứ cũ, củi, đèn dầu; nghèo nhưng ấm cúng, không bàn tiệc hoặc lò luyện đan xa hoa.

## Vật phẩm và continuity
- Đao cũ: trường đao thép mộc, chuôi quấn dây gai; đã gãy làm hai ở cuối Chương 7. C08 đến trước khi mua đao ở C09 không có đao nguyên vẹn. Sau mua là đao bản dày hơi ngắn, mặt thô, vỏ gỗ cũ; không nhầm với trường kiếm hai lưỡi của thủ lĩnh. Trong C10 khi vào hốc đá đao để ngoài, C11 đối thủ giữ đao rồi Hành Chu giành lại. C13 Vãn Ninh giữ đao lúc cứu Hành Chu. C14 quấn dây gai cũ lên cuối chuôi.
- Tấm thẻ đệ tử Hành Chu: gỗ nhỏ mép tròn, không ngọc bội. Thẻ gỗ cháy góc của khách chỉ xuất hiện cuối C14, không nhầm với thẻ sắt rỉ trong hốc đá C10 hoặc thẻ gỗ ký hiệu vòng tròn bị cắt ở C11.
- Tờ giấy dầu Kỷ Thanh La: nhàu, chữ nhòe, dấu đóng chìm mờ khi ánh sáng chiếu nghiêng; không triện đỏ lớn, không giấy phát sáng. Tránh tạo chữ giả rõ nét; nếu cần chữ chính xác thì hậu kỳ riêng, không để model tự viết.
- Hàn Lộ Tử: năm quả nhỏ xanh trắng, lá xanh nhạt, đọng nước, hộp gỗ nhỏ. Không trái khổng lồ hay phát sáng. Vãn Ninh giữ hộp đến khi về tông phối thuốc.
- Thương thế Hành Chu liên tục: ban đầu băng sườn/tay, sau giao đấu áo rách và vết máu nhẹ; C14 thay áo sạch nhưng vẫn băng, ba ngày sau mới tập nhẹ. Kỷ Thanh La vẫn băng vai sau uống thuốc.

## Đồng bộ voice và ảnh
1. Giữ chuẩn Tập 1: gTTS lang=vi, tld=com, slow=False; FFmpeg atempo=1.25 giữ cao độ, WAV PCM s16le 48kHz stereo, ngắt 2 giây giữa chương, AAC 192kbps trong MP4. Không sửa nguyên văn FINAL; chỉ bỏ metadata, dấu Markdown và dòng Hết chương, đọc tên chương một lần.
2. Tìm anchor_text đúng chương và occurrence trong văn bản sạch; source_paragraph_index là chỉ số đoạn bắt đầu từ 0 trong Markdown gốc khi tách bằng hai newline, dùng để định vị khi cần, không phải timestamp. Anchor nằm ở đầu đoạn chuyển cảnh, ảnh có thể mô tả tình tiết chính trong đoạn ngay sau anchor; tuyệt đối không chuyển sang biến cố của cảnh sau. Nếu hình làm lộ hành động đáng kể trước lời kể, dời điểm cut tới câu hành động thực sự bắt đầu và ghi lý do vào timeline, không đổi thứ tự.
3. Dùng timestamp từ audio thực tế hoặc forced alignment; nếu chưa có timestamp chính xác, chia TTS theo anchor của 80 cảnh hoặc theo các chunk nhỏ hơn rồi cộng thời lượng WAV đã atempo. Không lấy số từ để giả làm timestamp chính xác. Không thay giọng/tốc độ giữa cảnh. Không cắt audio làm mất tiếng, không chèn khoảng nghỉ riêng cho mỗi ảnh.
4. Cảnh đầu mỗi chương bắt đầu ngay tại tiêu đề chương; 2 giây nghỉ giữa chương giữ ảnh cuối chương trước. Từ anchor kế tiếp hard cut sang ảnh tương ứng; cảnh cuối giữ đến hết voice. Mỗi ảnh được giữ nguyên suốt đoạn hội thoại/giao đấu tương ứng, không chia đều thời lượng, không zoom/rung/lia, không fade đen.
5. Nếu thiếu ảnh hoặc sai ảnh: báo rõ mã và sửa trước khi render FINAL. Xuất timeline CSV gồm scene_id, image_file, start_ms, end_ms, duration_ms, anchor_text, QA_status. Không tự render FINAL khi chưa đủ ảnh đạt chuẩn.

## Nghiệm thu từng ảnh (PASS/FAIL)
- Đúng tên file, đúng tỷ lệ, một ảnh độc lập, đủ nét, không chữ, không viền.
- Đúng số người cần xuất hiện, đúng tuổi/giới tính/trang phục; A Thạch là trẻ nhỏ, Kỷ Thanh La là nữ hắc y.
- Đúng vũ khí và ai đang cầm, đúng thương thế, đúng thời điểm ngày/đêm, đúng địa hình, không tiết lộ bí mật.
- Không tông chủ, ngai vàng, cung điện xa hoa, pháp bảo phát sáng, ngẫu nhiên thêm nhân vật; kiểm tra giải phẫu tay/mặt và bố cục.
- So ảnh với reference và ảnh trước/sau; chỉ lưu file chính thức khi PASS. Nếu lỗi, tạo lại độc lập bằng prompt của chính cảnh; không crop collage hoặc đổi mã ảnh khác để lấp.
- Kiểm tra 80 tên file duy nhất và timeline tăng dần, không khoảng trống/đè thời gian, thời lượng video bằng master audio trong sai số một frame. Render 1920×1080 30fps H.264, tune stillimage, yuv420p, AAC 192kbps 48kHz stereo, faststart. Xuất SRT/VTT riêng nếu cần, không đốt phụ đề vào ảnh khi chưa yêu cầu.

## Thư mục đề xuất
BUILD FINAL CLIP/TAP-02/IMAGES/ chứa 80 PNG theo mã. Đặt CSV và hướng dẫn này tại BUILD FINAL CLIP/TAP-02/. Lưu bản reference ở REFERENCE/, ảnh lỗi ở REJECTED/, không để lẫn trong IMAGES/. Không commit hoặc upload YouTube nếu chưa được yêu cầu.

## Phân bổ
- Chương 8: 9 ảnh
- Chương 9: 10 ảnh
- Chương 10: 10 ảnh
- Chương 11: 10 ảnh
- Chương 12: 12 ảnh
- Chương 13: 12 ảnh
- Chương 14: 17 ảnh
- Tổng 80 ảnh. Chưa tạo ảnh, chưa tạo voice, chưa có timestamp thực tế.
