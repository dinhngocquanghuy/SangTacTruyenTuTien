# STORYBOARD HÌNH ẢNH — AUDIO TRUYỆN TU TIÊN — TẬP 01

**Trạng thái:** Kịch bản hình ảnh để agent tạo ảnh và dựng video; KHÔNG phải bản sửa nội dung truyện.
**Nguồn nội dung:** 7 file `CHUONG-0001-FINAL.md` đến `CHUONG-0007-FINAL.md` trong `03-MANUSCRIPTS/approved/` của dự án `SangTacTruyenTuTien`.
**Tình trạng audio:** Chưa có audio final hay bảng thời gian lời thoại nên không gán timestamp giả. Mỗi shot có một **mốc văn bản** để agent khớp sau khi có TTS.

**Số ảnh nền/ảnh chính:** 217 ảnh độc lập, chia theo trình tự truyện. **Mục tiêu video:** khoảng 2 giờ, phụ thuộc voice thực tế.

## A. Nguyên tắc hình ảnh và liên tục nhân vật

- **Khung hình:** 16:9, ưu tiên 1920×1080 hoặc 2560×1440, không watermark, không logo, không chữ nổi trong ảnh. Riêng thumbnail đã được tạo trước là ảnh xuất bản, không thay cho toàn bộ hình minh họa.
- **Phong cách:** minh họa điện ảnh tiên hiệp cổ trang, chi tiết tranh fantasy nhưng giữ hiện thực của một tông môn nghèo nàn, tường mục, kho gạo rỗng; ánh sáng thay đổi theo dòng thời gian trong truyện.
- **Tạ Hành Chu:** nam trẻ khoảng 20, tóc đen dài buộc giản dị, áo xanh vải thô đã bạc, tay nải cũ, trường đao **một lưỡi** cũ và vỏ bọc da sờn. Tính cách tự nhiên, láu lỉnh; không mặc long bào hay giáp thần, không dùng thần khí tỏa sáng.
- **Vãn Ninh:** nữ trẻ trong áo xanh mộc mạc, là người giữ kho và chữa thương, ánh mắt nghiêm, băng/chỉ/thuốc, **cổ tay có vệt đỏ** tiến triển qua các chương; không tự đổi màu áo.
- **Kỷ Thanh La:** đại sư tỷ xinh đẹp với phong thái lạnh lùng, tóc đen dài; khi trở về mặc **áo đen**, vai trúng độc, cầm **kiếm gãy**; càng về sau yếu vì thương tích. Đừng biến nàng thành người khỏe mạnh chiến đấu liên tục.
- **Tam trưởng lão:** ông lão tóc bạc, đạo bào xám cũ, hồ lô rượu, sau dùng **cây chổi** để cầm cự; không đột nhiên khôi phục tu vi phát ra thiên địa dị tượng.
- **A Thạch:** bé trai mặc áo vải giản dị, gắn với **rổ chim sẻ bị thương**; kích thước phù hợp trẻ em, không biến thành thanh niên qua các ảnh.
- **Trác Cửu:** đối thủ của Chương 6–7, nam trưởng thành mặc áo xám tro, **kiếm hẹp**; hai thuộc hạ có **cung** và **trường côn bọc sắt**.
- **Chu Tứ:** người mang túi da chứa **Dẫn Hương Trùng**, sau bị bắt sống và trói; phân biệt với sát thủ áo nâu dùng phi tiêu.
- **Đạo cụ cần nhất quán:** cổng tông môn hỏng, chuông đồng cũ, hồ lô, trường đao cũ (đến cuối Chương 7 mới gãy), tấm phù vàng cuối cùng, mảnh đồng gãy hình cánh chim, phong thư dấu son đỏ, thẻ đệ tử bằng gỗ.
- **Địa hình cố định:** sân chính điện, bếp, kho, phòng người bệnh, bậc lên núi; phía sau bếp có 3 lối (khe suối, vườn rau/nhà kho, rừng trúc). Không đổi vị trí các khu vực ở từng ảnh.
- **Ranh giới cốt truyện:** không vẽ Vạn Chiến Tàng Phong Thể đã thức tỉnh, không cho Tạ Hành Chu đánh ra luồng sáng khổng lồ hoặc một mình hạ Trác Cửu.
- **Không spoil:** mảnh đồng và giấy dầu chỉ xuất hiện đúng ở đoạn truyện tiết lộ; ảnh dấu đóng chìm cuối Chương 7 là cảnh chốt, không xuất hiện ở phần trước.

## B. Quy trình dựng video từ ảnh

1. Đọc transcript TTS theo đúng thứ tự FINAL Chương 1→7; bỏ dòng metadata và các nhãn `Hết chương — FINAL` khỏi lời đọc nếu không muốn phát âm.
2. Tìm `voice_cue` của mỗi ảnh trong văn bản chương tương ứng rồi căn vị trí của cue theo **audio thực tế** (forced alignment hoặc đối chiếu waveform). Không tự giả định mỗi chương dài bằng nhau.
3. Tạo ảnh theo `image_direction`; dùng ảnh thumbnail đã có làm tham chiếu phong cách, **không nhất thiết lấy hình nhân vật thumbnail làm thiết kế tuyệt đối** vì thumbnail dùng trang phục/vũ khí cách điệu hơn bản truyện.
4. Với mỗi ảnh chính, dựng 2–4 biến thể hình động (góc rộng, trung, cận; thay đổi bố cục/cử động môi trường hợp lý). Không được kéo ảnh tĩnh hàng chục giây chỉ bằng zoom tiến-lùi liên tục. Nếu âm thoại kéo dài, tạo thêm shot mới cùng sự kiện.
5. Chuyển cảnh ưu tiên hard cut theo dấu câu/hành động; dissolve rất ngắn cho đổi bối cảnh hoặc hồi tưởng. Audio giọng kể chạy **liên tục**, không reset/nhảy câu khi thay ảnh.
6. Không tái sử dụng một ảnh trong hai đoạn không liên quan. Giữ riêng scene của từng chương và ảnh theo ID; rà soát các boundary cuối Chương N – đầu Chương N+1.
7. Trước khi xuất bản: rà khớp câu đọc với hình, kiểm tra dấu thời gian sau khi có giọng, phát âm tên nhân vật, lỗi chữ giả/biến dạng ngón tay, sai số lượng đạo cụ, sai chân tay, weapon continuity, fps và audio không lặp.

## C. Danh sách ảnh chi tiết (theo mốc truyện)

### Chương 1 — Bao ăn, bao ở (37 ảnh)

**C01-I001 — Toàn cảnh**
- **Mốc voice:** §0 — “Mặt trời ngả về phía tây, những vệt nắng cuối cùng vắt ngang con đường núi gập ghềnh.”
- **Ảnh:** Chiều muộn, núi rừng xanh ngắt, con đường đá quanh co lên một đỉnh núi xa, nắng vàng xiên qua mây.
- **Động/chuyển:** Máy quay trượt nhẹ dọc con đường, bóng lá lay theo gió.

**C01-I002 — Trung cảnh**
- **Mốc voice:** §1 — “Tạ Hành Chu đang leo từng bậc đá. Người tán tu trẻ tuổi mặc áo xanh, trên vai đeo tay nải bạc màu, bên hông giắt mộ…”
- **Ảnh:** Tạ Hành Chu áo xanh giản dị, tay nải bạc màu, trường đao cũ đeo hông, vừa leo bậc đá vừa ngậm cọng cỏ.
- **Động/chuyển:** Máy quay theo bước chân ngang sườn núi, tóc áo phất nhẹ.

**C01-I003 — Cận cảnh**
- **Mốc voice:** §3 — “Dẫu vậy, mỗi lần nhấc chân, Hành Chu đều đặt bước rất chắc. Những bậc đá phủ rêu trơn, một khi đã giẫm hụt, Hành Ch…”
- **Ảnh:** Giày Hành Chu đặt chắc lên bậc đá phủ rêu, quan sát những chỗ trơn trước khi bước.
- **Động/chuyển:** Cắt cận chân và vệt rêu, đổi nét vào ánh mắt tỉnh táo.

**C01-I004 — Toàn cảnh**
- **Mốc voice:** §5 — “Trên bia khắc ba chữ: Thanh Vân Tông.”
- **Ảnh:** Bia đá cổ phủ rêu ở lối rẽ dẫn lên Thanh Vân Tông, cỏ dại và dây leo.
- **Động/chuyển:** Máy quay tiến chậm tới bia đá, sương mỏng qua thân bia.

**C01-I005 — Chi tiết**
- **Mốc voice:** §6 — “Bên cạnh có tấm bảng gỗ xiêu vẹo, buộc vào cọc bằng sợi dây thừng mới hơn nhiều so với tấm bảng.”
- **Ảnh:** Tấm bảng gỗ tuyển người xiêu vẹo với ý chính bao ăn bao ở, không yêu cầu render chữ rõ trong ảnh.
- **Động/chuyển:** Tia nắng di chuyển trên mặt bảng, ngón tay gạt bụi.

**C01-I006 — Cận mặt**
- **Mốc voice:** §12 — “Hành Chu nhìn hàng chữ bao ăn, bao ở thêm lần nữa. Sợ đọc nhầm, Tạ Hành Chu còn đưa tay lau lớp bụi trên mặt bảng.”
- **Ảnh:** Tạ Hành Chu sáng mắt vì đọc thông báo bao ăn bao ở, khóe môi cười tinh quái.
- **Động/chuyển:** Chuyển nét từ tấm bảng lên nụ cười tự nhiên.

**C01-I007 — Hồi tưởng**
- **Mốc voice:** §15 — “Ở chân núi, Tạ Hành Chu từng nghe ông chủ quán trà nhắc tới Thanh Vân Tông. Khi ấy, ông chủ vừa rót nước vừa cười, …”
- **Ảnh:** Quán trà đơn sơ dưới chân núi; ông chủ quán vừa rót trà vừa nhắc tông môn đang sa sút.
- **Động/chuyển:** Hơi nước từ chén trà bay lên, chuyển sáng mềm sang đường núi.

**C01-I008 — Toàn cảnh**
- **Mốc voice:** §18 — “Bởi vì vừa leo hết những bậc đá cuối cùng, Tạ Hành Chu đã nhìn thấy sơn môn.”
- **Ảnh:** Sơn môn Thanh Vân Tông đổ nát với cổng gỗ mục, tường sụp, chính điện thủng ngói, quạ đậu mái.
- **Động/chuyển:** Máy quay mở rộng từ bậc thềm lên toàn bộ sơn môn.

**C01-I009 — Cận mặt**
- **Mốc voice:** §24 — “Ngẫm nghĩ một chút, Hành Chu nói:”
- **Ảnh:** Tạ Hành Chu nhìn cảnh đổ nát, nụ cười tắt dần, vẻ tiếc nuối hài hước.
- **Động/chuyển:** Lá khô lăn qua chân, máy quay nghiêng nhẹ theo ánh nhìn.

**C01-I010 — Trung cảnh**
- **Mốc voice:** §27 — “Giọng nói bất ngờ vang lên sau lưng.”
- **Ảnh:** Tam trưởng lão tóc bạc áo xám xuất hiện bên gốc cây, một tay cầm hồ lô rượu.
- **Động/chuyển:** Máy quay vòng nhẹ sau vai Tạ Hành Chu, lộ ông lão.

**C01-I011 — Hai người**
- **Mốc voice:** §30 — ““Vãn bối nghe danh quý tông đã lâu, đặc biệt tới xin bái nhập môn hạ.””
- **Ảnh:** Tạ Hành Chu chắp tay hành lễ rất lễ phép, Tam trưởng lão cầm hồ lô quan sát nghi ngờ.
- **Động/chuyển:** Chuyển nét giữa hai gương mặt, áo bào lay nhẹ.

**C01-I012 — Chi tiết hài**
- **Mốc voice:** §39 — “Cả hai cùng ngoảnh đầu.”
- **Ảnh:** Một viên ngói rơi vỡ trước hai người trong khi họ giữ vẻ nghiêm trang.
- **Động/chuyển:** Cận viên ngói vỡ, bụi bay chậm, cắt phản ứng bất lực.

**C01-I013 — Hai người**
- **Mốc voice:** §45 — “Một già một trẻ nhìn nhau, đều cảm thấy người đối diện rất hiểu chuyện.”
- **Ảnh:** Ông lão cười khoái chí vì câu nịnh khéo, Tạ Hành Chu cười đáp bên cổng rách.
- **Động/chuyển:** Góc thấp nhẹ làm nổi hai gương mặt đang hợp ý.

**C01-I014 — Trung cảnh**
- **Mốc voice:** §50 — ““Vãn bối đi đường xa, quả thật hơi đói. Có thể dùng cơm trước được không?””
- **Ảnh:** Tạ Hành Chu ôm bụng đói, ngập ngừng hỏi chuyện ăn cơm; ông lão ngẩn ra.
- **Động/chuyển:** Máy quay lia từ bụng đói sang hồ lô rượu.

**C01-I015 — Cảnh đối thoại**
- **Mốc voice:** §56 — ““Tam trưởng lão! Người lại đem gạo trong kho đổi rượu phải không?””
- **Ảnh:** Tiếng nữ tử từ chính điện gọi chuyện gạo đổi rượu; Tam trưởng lão bối rối giấu hồ lô.
- **Động/chuyển:** Một chuyển cảnh nhanh từ cửa điện sang vẻ lúng túng ông lão.

**C01-I016 — Trung cảnh**
- **Mốc voice:** §64 — “Người từ chính điện bước ra là một nữ tử áo xanh nhạt.”
- **Ảnh:** Vãn Ninh áo xanh nhã nhặn nhưng nghiêm nghị bước tới ở sân, nhìn khách mới và hồ lô rượu.
- **Động/chuyển:** Máy quay ngang qua vai Vãn Ninh, hậu cảnh chính điện hư hỏng.

**C01-I017 — Toàn cảnh nhóm**
- **Mốc voice:** §81 — ““Trong kho chỉ còn hai nắm gạo. Củi ướt chưa chẻ. Tường phía đông đổ từ tháng trước. Ngươi muốn ăn cơm, trước hết p…”
- **Ảnh:** Vãn Ninh chỉ kho gạo trống, củi ướt, tường đổ; Tạ Hành Chu và trưởng lão nghe chuyện.
- **Động/chuyển:** Máy quay di chuyển chậm qua từng vật dụng thiếu thốn.

**C01-I018 — Hai người**
- **Mốc voice:** §102 — ““Được rồi. Có lẽ chúng ta hiểu nhầm nhau.””
- **Ảnh:** Tạ Hành Chu đề nghị làm việc sửa sang đổi lấy chỗ ở; Vãn Ninh cân nhắc với vẻ cảnh giác.
- **Động/chuyển:** Từ hai người đối diện chuyển sang dụng cụ sửa nhà.

**C01-I019 — Không gian**
- **Mốc voice:** §120 — “Bên trong có một chiếc giường tre, một cái bàn gỗ và một cửa sổ đóng không khít. Ít nhất mái còn nguyên, trên giườn…”
- **Ảnh:** Căn phòng khách nghèo có giường tre, bàn gỗ lung lay và cửa sổ hở.
- **Động/chuyển:** Ánh sáng qua khe cửa, khung hình tĩnh trang nhã.

**C01-I020 — Cận cảnh**
- **Mốc voice:** §123 — “Khi Tạ Hành Chu bê cái bàn ra ngoài để sửa chân, từ góc sân bỗng vang lên tiếng sột soạt.”
- **Ảnh:** A Thạch xuất hiện nơi góc sân, che giấu chim sẻ bị thương trong hai bàn tay.
- **Động/chuyển:** Máy quay hạ thấp ngang tầm đứa trẻ, cánh chim khẽ run.

**C01-I021 — Chi tiết**
- **Mốc voice:** §135 — “Con chim sẻ có sợi chỉ mảnh quấn quanh khớp cánh. Hành Chu không giật mạnh, chỉ mượn con dao nhỏ cắt từng đoạn rồi …”
- **Ảnh:** Tạ Hành Chu cẩn thận cắt sợi chỉ quấn cánh chim sẻ, dùng mảnh vải sạch băng lỏng.
- **Động/chuyển:** Cận ngón tay khéo léo, chim khẽ động cánh.

**C01-I022 — Hai người**
- **Mốc voice:** §141 — ““Ta họ Tạ, tên Hành Chu.””
- **Ảnh:** Tạ Hành Chu tự giới thiệu tên với A Thạch; đứa bé nhìn chàng đầy tò mò.
- **Động/chuyển:** Góc ngang, nét mặt đứa trẻ dịu lại.

**C01-I023 — Toàn cảnh nhóm**
- **Mốc voice:** §162 — “Tam trưởng lão ôm hồ lô rượu ngồi trước bàn, vẻ mặt vô cùng bình thản. Nữ tử áo xanh đặt bát xuống trước mặt lão hơ…”
- **Ảnh:** Bữa cháo loãng giữa phòng bếp cũ, Tam trưởng lão ôm hồ lô, Vãn Ninh đặt bát, A Thạch ngồi cạnh Hành Chu.
- **Động/chuyển:** Máy quay trôi nhẹ quanh bàn, hơi cháo bốc lên.

**C01-I024 — Cận chi tiết**
- **Mốc voice:** §174 — “Trên cổ tay nàng có một vệt đỏ mảnh, trông như vết bỏng. Lúc nàng vươn tay, vệt đỏ ấy lóe lên rồi biến mất dưới ống…”
- **Ảnh:** Vết đỏ khác thường dưới ống tay áo nơi cổ tay Vãn Ninh khi nàng múc cháo.
- **Động/chuyển:** Chuyển nét kín đáo sang vết đỏ rồi về ánh mắt Hành Chu.

**C01-I025 — Trung cảnh**
- **Mốc voice:** §186 — ““À, chiều nay có người dưới trấn lên tìm tông chủ.””
- **Ảnh:** A Thạch nói có người áo nâu để lại phong thư ngoài cổng; người lớn lập tức chú ý.
- **Động/chuyển:** Ánh đèn bếp bập bùng, các gương mặt đổi sắc.

**C01-I026 — Cận cảnh**
- **Mốc voice:** §192 — “Nữ tử vừa mở ra đã biến sắc.”
- **Ảnh:** Vãn Ninh mở phong thư có dấu son đỏ và biến sắc, ngón tay nắm giấy trắng bệch.
- **Động/chuyển:** Máy quay tiến gần bàn tay siết lá thư.

**C01-I027 — Hai người**
- **Mốc voice:** §198 — ““Tạ công tử.” Nàng quay sang Tạ Hành Chu. “Nếu ngươi chỉ muốn tìm nơi ăn ở, sáng mai tốt nhất nên xuống núi. Ba ngà…”
- **Ảnh:** Vãn Ninh khuyên Tạ Hành Chu sáng mai xuống núi; chàng đắn đo nhưng không hoảng loạn.
- **Động/chuyển:** Đổi góc qua vai, nền bếp tối dần.

**C01-I028 — Toàn cảnh**
- **Mốc voice:** §219 — “Khi sân đã vắng người, Hành Chu lấy thanh đao cũ bên hông ra.”
- **Ảnh:** Đêm trên sân Thanh Vân Tông, Hành Chu rút đao luyện một mình dưới bóng trăng.
- **Động/chuyển:** Máy quay đi ngang theo từng nhịp đao, bụi sân tung nhẹ.

**C01-I029 — Chi tiết động tác**
- **Mốc voice:** §225 — “Đến nhát thứ bốn mươi, mồ hôi bắt đầu thấm vào cổ áo.”
- **Ảnh:** Đao cũ chém liên tiếp, mồ hôi trên cổ áo; không có quang hiệu siêu năng lực.
- **Động/chuyển:** Chuyển cận chuôi đao và cánh tay mỏi.

**C01-I030 — Trung cảnh căng thẳng**
- **Mốc voice:** §234 — “Tạ Hành Chu ngừng bước.”
- **Ảnh:** Tạ Hành Chu nghe động sau dãy nhà, ngừng luyện đao và áp sát vách tây quan sát.
- **Động/chuyển:** Máy quay ẩn sau cột cùng hướng nhìn chàng.

**C01-I031 — Góc nhìn nhân vật**
- **Mốc voice:** §243 — “Trong tay kẻ đó có một ống trúc ngắn.”
- **Ảnh:** Người áo tối đứng ngoài cổng trong bóng đêm, tay giấu ống trúc bắn độc châm.
- **Động/chuyển:** Máy quay nhìn xuyên khe tường, bóng người chìm trong sương.

**C01-I032 — Trung cảnh**
- **Mốc voice:** §249 — “Là A Thạch.”
- **Ảnh:** A Thạch bất ngờ tiến vào vùng nguy hiểm, tay ôm chiếc rổ chim sẻ.
- **Động/chuyển:** Máy quay chuyển nhanh từ đứa bé sang ống trúc nguy hiểm.

**C01-I033 — Hành động**
- **Mốc voice:** §258 — “Hành Chu cúi xuống nhặt một hòn sỏi, búng nhẹ vào cái chum sành đựng nước mưa cách đó mấy bước.”
- **Ảnh:** Tạ Hành Chu búng hòn sỏi làm động chiếc chum sành để đánh lạc hướng sát thủ.
- **Động/chuyển:** Hòn sỏi chạm chum, rung động và góc nhìn sát thủ quay đi.

**C01-I034 — Hành động**
- **Mốc voice:** §264 — “Phựt!”
- **Ảnh:** Mũi kim đen phóng vào sân, Tạ Hành Chu vung đao chém đứt sợi chỉ liên quan tới cuộc tập kích.
- **Động/chuyển:** Đường chuyển động của lưỡi đao sắc gọn, không quay chậm phô trương.

**C01-I035 — Toàn cảnh**
- **Mốc voice:** §270 — “Một tiếng cười lạnh vang lên ngoài cổng.”
- **Ảnh:** Bóng kẻ đột nhập lùi vào rừng tối, sân tông môn vẫn tiêu điều dưới trăng.
- **Động/chuyển:** Bóng người khuất sau cây, lá bay qua nền tối.

**C01-I036 — Hai người**
- **Mốc voice:** §282 — “Tạ Hành Chu quay đầu.”
- **Ảnh:** Vãn Ninh nhìn dấu vết đao, Tam trưởng lão đứng sau không còn vẻ say, Tạ Hành Chu giả vờ bình thản.
- **Động/chuyển:** Máy quay từ vết chém lên ánh mắt dò xét của Vãn Ninh.

**C01-I037 — Cận vật chứng**
- **Mốc voice:** §288 — “Bởi vì trên phong thư đang mở, dưới dấu son màu đỏ, chỉ có một dòng chữ:”
- **Ảnh:** Phong thư mở với dấu son đỏ, nét đe dọa trên giấy, không tạo chữ ngẫu nhiên trên màn hình.
- **Động/chuyển:** Cận giấy và dấu son, ánh đèn rung nhẹ rồi chuyển tối.

### Chương 2 — Người Trong Phong Thư (32 ảnh)

**C02-I001 — Không gian**
- **Mốc voice:** §0 — “Gió đêm luồn qua khoảng sân trống. Mũi kim đen vẫn rung khe khẽ nơi thân cột, để lại một vệt sẫm trên thớ gỗ. A Thạ…”
- **Ảnh:** Sân núi ban đêm, mũi kim đen rung trong cột, A Thạch ôm rổ chim đứng phía sau.
- **Động/chuyển:** Máy quay tiến chậm từ mũi kim tới đứa trẻ lo sợ.

**C02-I002 — Chi tiết**
- **Mốc voice:** §9 — ““Đừng chạm vào!” Tạ Hành Chu lập tức lên tiếng.”
- **Ảnh:** Tam trưởng lão định chạm mũi kim, Tạ Hành Chu giơ tay ngăn lại ngay.
- **Động/chuyển:** Chuyển nét từ bàn tay trưởng lão sang kim đen.

**C02-I003 — Cận chi tiết**
- **Mốc voice:** §11 — “Tạ Hành Chu nhặt một nhánh củi dưới đất, dùng đầu nhánh củi khẽ gạt vào thân kim. Một giọt chất lỏng màu tím đen rị…”
- **Ảnh:** Nhánh củi gạt kim độc, giọt chất lỏng tím đen nhỏ xuống khiến cỏ non úa.
- **Động/chuyển:** Giọt độc rơi, cỏ quăn lại chân thực, không biến thành phép thuật rực rỡ.

**C02-I004 — Trung cảnh**
- **Mốc voice:** §18 — ““Tam trưởng lão, đưa A Thạch vào trong.””
- **Ảnh:** Tam trưởng lão dẫn A Thạch khỏi sân nguy hiểm, ngoái nhìn Hành Chu.
- **Động/chuyển:** Máy quay dõi theo hai người qua hiên đổ nát.

**C02-I005 — Hai người**
- **Mốc voice:** §27 — ““Ngươi định xem gì?””
- **Ảnh:** Tạ Hành Chu cùng Vãn Ninh bàn về vị trí sát thủ còn ẩn, ánh mắt hướng rặng nhà phía tây.
- **Động/chuyển:** Máy quay đổi góc qua vai, nửa khuôn mặt ở bóng tối.

**C02-I006 — Chi tiết**
- **Mốc voice:** §48 — “Dưới chân trụ có một dấu bùn nhỏ. Đất ở đó khô, nhưng vết giày còn ẩm. Một người vừa đứng sát chân tường không lâu.…”
- **Ảnh:** Dấu giày bùn còn ẩm nơi chân trụ khô, hướng vào trong sân.
- **Động/chuyển:** Cận mặt đất cùng vệt bùn, ánh đèn lướt qua.

**C02-I007 — Không gian**
- **Mốc voice:** §54 — “Hành Chu ngẩng đầu nhìn bóng tối sau dãy nhà.”
- **Ảnh:** Lối tối phía sau dãy nhà Thanh Vân Tông, cỏ mọc hoang và bóng tường chắn.
- **Động/chuyển:** Máy quay trượt dọc mép tường, tiếng lá chỉ là gợi ý motion.

**C02-I008 — Cận cảnh**
- **Mốc voice:** §60 — “Nữ tử rút từ tay áo một tấm phù giấy màu vàng. Trên mặt phù có mấy nét mực đỏ đã nhạt, giống như từng bị ngâm nước.…”
- **Ảnh:** Vãn Ninh rút tấm phù giấy vàng mực đỏ đã nhạt nhưng ngừng dùng vì sợ lộ vị trí.
- **Động/chuyển:** Phù giấy khẽ rung trong tay, ánh linh lực chỉ lóe mờ.

**C02-I009 — Cận mặt**
- **Mốc voice:** §72 — “Nụ cười trên mặt Tạ Hành Chu nhạt dần. Hành Chu nhìn về khoảng sân phía tây, nơi cái bàn gỗ đã sửa chân đang đặt cạ…”
- **Ảnh:** Tạ Hành Chu ngắm khoảng sân phía tây, nét mặt tỉnh táo khi tính kế.
- **Động/chuyển:** Máy quay chuyển nét từ mắt sang bàn gỗ và đống củi.

**C02-I010 — Trong phòng**
- **Mốc voice:** §81 — “Khi Tạ Hành Chu và nữ tử áo xanh bước vào, đứa trẻ lập tức ngẩng đầu.”
- **Ảnh:** A Thạch ngẩng lên khi Hành Chu và Vãn Ninh trở lại gian bếp.
- **Động/chuyển:** Ánh nến ấm đối lập bóng tối ngoài hiên.

**C02-I011 — Hai người**
- **Mốc voice:** §87 — ““Sợ cũng không sao.” Tạ Hành Chu mở tay nải, lấy ra một chiếc bánh khô. “Ta cũng sợ. Sợ nhất là chết trước khi ăn h…”
- **Ảnh:** Tạ Hành Chu chia bánh khô trấn an A Thạch, chim sẻ nằm yên trong rổ.
- **Động/chuyển:** Cận bánh khô trao tay và nét mặt dịu của A Thạch.

**C02-I012 — Toàn cảnh nhóm**
- **Mốc voice:** §96 — ““Đêm nay phải đưa A Thạch xuống khe suối.””
- **Ảnh:** Vãn Ninh, Tam trưởng lão và Hành Chu bàn chuyện đưa A Thạch xuống khe suối.
- **Động/chuyển:** Máy quay từ mặt bàn tới cổng núi tối ngoài cửa.

**C02-I013 — Hai người**
- **Mốc voice:** §105 — ““Thế là cô nương định một mình giữ cổng?” Tạ Hành Chu hỏi.”
- **Ảnh:** Vãn Ninh kiên quyết muốn giữ cổng, Tạ Hành Chu nghiêng đầu hỏi lại.
- **Động/chuyển:** Góc đối thoại căng thẳng nhưng kiềm chế.

**C02-I014 — Góc nhìn ẩn nấp**
- **Mốc voice:** §129 — “Dưới mái hiên tối om, Tạ Hành Chu nín thở.”
- **Ảnh:** Tạ Hành Chu nấp dưới hiên tối, đặt tay trên chuôi đao, chờ bóng kẻ địch.
- **Động/chuyển:** Máy quay thấp sau cột, màn sương lướt sân.

**C02-I015 — Toàn cảnh**
- **Mốc voice:** §138 — “Kẻ đó dừng trước cửa sổ phía nam, nhìn bóng người đang di chuyển trong phòng.”
- **Ảnh:** Sát thủ áo đen men đến cửa sổ phía nam, nhìn bóng người làm mồi phía trong.
- **Động/chuyển:** Máy quay đi theo bóng sát thủ ở phía ngoài cửa sổ.

**C02-I016 — Hành động**
- **Mốc voice:** §141 — “Phập!”
- **Ảnh:** Bẫy bất ngờ kích hoạt ở khu vực bàn gỗ, mũi đâm chệch mục tiêu.
- **Động/chuyển:** Cắt góc ngắn vào bẫy rồi phản ứng sát thủ.

**C02-I017 — Hành động**
- **Mốc voice:** §147 — “Đối phương phản ứng cực nhanh, lách người tránh được mép bàn. Nhưng ngay khoảnh khắc ấy, một nắm tro bếp bay thẳng …”
- **Ảnh:** Tạ Hành Chu hất tro bếp vào mặt địch thủ giữa sân, lợi dụng bụi che tầm nhìn.
- **Động/chuyển:** Tro xám bùng thành mây, chuyển camera ngang tầm đấu.

**C02-I018 — Chi tiết binh khí**
- **Mốc voice:** §150 — “Keng!”
- **Ảnh:** Đoản nhận sát thủ va chạm trường đao cũ, tia lửa mỏng từ kim loại.
- **Động/chuyển:** Cận va chạm thực tế, giữ vị trí vũ khí nhất quán.

**C02-I019 — Hành động**
- **Mốc voice:** §156 — “Hành Chu không cố đỡ cứng. Lùi sát chân bàn, Tạ Hành Chu hạ thấp đao, chém vào cổ tay cầm binh khí của đối thủ.”
- **Ảnh:** Hành Chu hạ đao đánh về cổ tay đối phương, tránh đọ sức trực diện.
- **Động/chuyển:** Máy quay xoay theo tay kiếm, chuyển động ngắn rõ.

**C02-I020 — Hành động**
- **Mốc voice:** §159 — “Tạ Hành Chu nghiêng đầu, dùng sống đao ép ngang cánh tay đối phương. Hai người va mạnh vào cột hiên. Vết thương bên…”
- **Ảnh:** Hai người đụng mạnh cột hiên, Tạ Hành Chu ôm vết thương bên sườn.
- **Động/chuyển:** Chuyển góc thấp, bụi gỗ rơi nhẹ.

**C02-I021 — Hành động**
- **Mốc voice:** §165 — “Lần này, Tạ Hành Chu không chém vào tay. Lưỡi đao bổ thấp xuống cạnh bậc cửa, buộc kẻ lạ phải thu chân.”
- **Ảnh:** Tạ Hành Chu ép địch lùi về bậc cửa, lưỡi đao chém thấp buộc đối phương đổi thế.
- **Động/chuyển:** Máy quay theo chân bước và mũi đao trên nền đá.

**C02-I022 — Cận cảnh**
- **Mốc voice:** §174 — “Nàng không cầm đao kiếm. Trong tay chỉ có một tấm phù giấy màu vàng đã chuẩn bị từ trước.”
- **Ảnh:** Vãn Ninh đứng sau, tấm phù vàng trong tay đã sẵn sàng.
- **Động/chuyển:** Nét từ phù giấy chuyển lên ánh mắt kiên quyết.

**C02-I023 — Hành động**
- **Mốc voice:** §177 — “Tấm phù bùng lên ánh lửa trắng, chiếu sáng toàn bộ khoảng sân. Kẻ lạ đưa tay che mắt, vội vàng nhảy lùi về phía bức…”
- **Ảnh:** Tấm phù bùng ánh sáng trắng, sát thủ che mắt nhảy lùi khỏi sân.
- **Động/chuyển:** Ánh trắng chiếu mái ngói cũ rồi dịu về đêm.

**C02-I024 — Toàn cảnh**
- **Mốc voice:** §183 — “Rồi bóng đen biến mất trong rừng.”
- **Ảnh:** Bóng sát thủ thoát vào rừng sâu, sân núi tạm lặng.
- **Động/chuyển:** Máy quay giữ cổng trong khung, bóng khuất sau sương.

**C02-I025 — Chăm sóc**
- **Mốc voice:** §189 — ““Để ta xem.””
- **Ảnh:** Vãn Ninh xem và băng vết thương bên sườn Hành Chu ở gian bếp.
- **Động/chuyển:** Cận dải băng quấn, hai nhân vật tập trung.

**C02-I026 — Trong phòng**
- **Mốc voice:** §207 — “Tam trưởng lão mang tới cho Tạ Hành Chu một bát nước nóng.”
- **Ảnh:** Tam trưởng lão đưa cho Hành Chu bát nước nóng sau trận đêm.
- **Động/chuyển:** Hơi nước lượn trước gương mặt mỏi mệt.

**C02-I027 — Hai người**
- **Mốc voice:** §222 — ““Ta đã hứa với A Thạch sẽ giữ giúp con chim. Chưa trả được, đi sao đành.””
- **Ảnh:** Hành Chu nhắc lời hứa giữ chim cho A Thạch khi trưởng lão thắc mắc vì sao chưa rời núi.
- **Động/chuyển:** Cận rổ chim rồi trở lại ánh nhìn Hành Chu.

**C02-I028 — Trung cảnh**
- **Mốc voice:** §234 — “Ngoài hiên, tiếng bước chân vang lên.”
- **Ảnh:** Vãn Ninh tới hiên bếp lúc gần sáng; mọi người bàn về người đang vắng mặt.
- **Động/chuyển:** Ánh rạng đông tràn dần qua cửa sổ.

**C02-I029 — Cận vật**
- **Mốc voice:** §249 — “Không phải tiếng ai đập cửa. Âm thanh đến từ chuông đồng cũ treo bên trụ đá, chiếc chuông đã nhiều năm không ai dùn…”
- **Ảnh:** Chuông đồng cũ treo trên trụ đá bất ngờ kêu khi sương sáng phủ cổng.
- **Động/chuyển:** Máy quay tiến tới chuông rung nhẹ, sương bay.

**C02-I030 — Toàn cảnh**
- **Mốc voice:** §252 — “Tạ Hành Chu đặt tay lên chuôi đao. Vết thương bên sườn đau nhói, nhưng Hành Chu vẫn bước ra trước hiên, đứng ở vị t…”
- **Ảnh:** Tạ Hành Chu bước ra hiên, tay trên chuôi đao, nhìn xuống bậc thềm sương sớm.
- **Động/chuyển:** Camera nhìn qua vai Hành Chu xuống lối núi.

**C02-I031 — Toàn cảnh nhân vật**
- **Mốc voice:** §255 — “Nữ tử ngẩng đầu, nhìn tấm biển Thanh Vân Tông xiêu vẹo, rồi bật cười khẽ.”
- **Ảnh:** Kỷ Thanh La áo đen đứng dựa trụ đá, vai máu, tay cầm trường kiếm gãy, vệt máu kéo dài trên bậc.
- **Động/chuyển:** Máy quay từ lưỡi kiếm gãy lên khuôn mặt tái nhợt.

**C02-I032 — Hành động cảm xúc**
- **Mốc voice:** §258 — ““Các người lại để cửa nhà thành ra thế này?””
- **Ảnh:** Vãn Ninh lao xuống bậc thềm gọi đại sư tỷ; Kỷ Thanh La gượng cười dù đang chảy máu.
- **Động/chuyển:** Chuyển cận nét hoảng hốt và nụ cười yếu.

### Chương 3 — Người Trở Về Trong Sương (23 ảnh)

**C03-I001 — Hành động**
- **Mốc voice:** §0 — “Vãn Ninh vừa chạy đến bậc đá thứ ba, nữ tử áo đen đã khuỵu xuống.”
- **Ảnh:** Kỷ Thanh La khuỵu trên bậc đá, Vãn Ninh vội đỡ, Tạ Hành Chu lao tới giữ họ khỏi ngã.
- **Động/chuyển:** Máy quay ngang theo động tác đỡ người, vải đen tung nhẹ.

**C03-I002 — Cận nhân vật**
- **Mốc voice:** §6 — ““Người mới?””
- **Ảnh:** Cận Kỷ Thanh La đẹp lạnh lùng, mặt tái và tóc rối, nhìn Hành Chu như hỏi người mới là ai.
- **Động/chuyển:** Chuyển nét từ tay đỡ sang ánh mắt cảnh giác.

**C03-I003 — Toàn cảnh**
- **Mốc voice:** §12 — “Tam trưởng lão đã ra tới hiên. Lão vừa nhìn thấy nữ tử áo đen liền im bặt, chiếc hồ lô trong tay khẽ va vào lan can…”
- **Ảnh:** Tam trưởng lão từ hiên chạy ra khi nhận ra Thanh La, hồ lô rượu rung trên tay.
- **Động/chuyển:** Máy quay theo bước chân vội không còn giả say.

**C03-I004 — Trong phòng**
- **Mốc voice:** §21 — “Tạ Hành Chu đặt nữ tử áo đen ngồi tựa vào thành giường. Lúc rút tay về, Hành Chu mới phát hiện áo mình đã thấm máu …”
- **Ảnh:** Đại sư tỷ được đặt trên giường, áo đen thấm máu, Hành Chu cũng có băng sườn.
- **Động/chuyển:** Ánh sáng sớm xuyên khe cửa, vải băng dịch theo cử động.

**C03-I005 — Cận thương tích**
- **Mốc voice:** §45 — “Vãn Ninh cắt lớp vải quanh vai nàng, động tác rất nhẹ. Dưới áo là một vết chém sâu, miệng vết thương có màu tím sẫm…”
- **Ảnh:** Vãn Ninh mở lớp vải vai Kỷ Thanh La thấy vết thương tím sẫm và đầu kim sát xương.
- **Động/chuyển:** Máy quay cận vết thương vừa phải, không máu me phô trương.

**C03-I006 — Trong phòng**
- **Mốc voice:** §51 — ““Thực Mạch Sa.””
- **Ảnh:** Vãn Ninh nhận biết độc Thực Mạch Sa; Hành Chu lắng nghe, Tam trưởng lão lo lắng.
- **Động/chuyển:** Khung tam giác nhân vật quanh giường bệnh.

**C03-I007 — Chăm sóc**
- **Mốc voice:** §60 — “Câu ấy bật ra quá nhanh. Vãn Ninh khựng lại, cắn môi, cúi đầu lấy túi kim mảnh từ tay áo.”
- **Ảnh:** Vãn Ninh chuẩn bị kim khâu, thuốc và băng; Kỷ Thanh La chịu đau trong im lặng.
- **Động/chuyển:** Cận dụng cụ y thuật xưa, hơi thở căng.

**C03-I008 — Hai người**
- **Mốc voice:** §66 — ““Tạ đại ca, đại sư tỷ có chết không?””
- **Ảnh:** A Thạch lo lắng hỏi Hành Chu liệu đại sư tỷ có qua khỏi.
- **Động/chuyển:** Cận ánh mắt đứa trẻ và bàn tay Hành Chu xoa đầu.

**C03-I009 — Cận cảm xúc**
- **Mốc voice:** §75 — ““Người như vậy hẳn rất đáng được cứu.””
- **Ảnh:** A Thạch kể Thanh La hay mua kẹo cho mình; Hành Chu nhận ra tình cảm trong tông.
- **Động/chuyển:** Ánh nắng sớm làm mềm gương mặt hai người.

**C03-I010 — Chi tiết manh mối**
- **Mốc voice:** §78 — “Một thứ mùi như vỏ quýt bị đốt, lẫn với hương cỏ khô. Hành Chu cúi xuống ngửi áo mình. Mùi ấy đậm hơn ở phần tay áo…”
- **Ảnh:** Hành Chu ngửi thấy mùi vỏ quýt cháy lẫn cỏ khô trên tay áo vừa đỡ Thanh La.
- **Động/chuyển:** Máy quay theo tay áo đưa lên mũi rồi cắt qua chậu thuốc.

**C03-I011 — Hai người**
- **Mốc voice:** §93 — ““Hứa.””
- **Ảnh:** Hành Chu hứa với A Thạch sẽ cứu đại sư tỷ; đứa trẻ ôm rổ chim và phần bánh nhỏ.
- **Động/chuyển:** Góc thấp thân mật, nền bếp ấm.

**C03-I012 — Toàn cảnh**
- **Mốc voice:** §99 — “Đến lúc nước sôi, trời đã sáng hẳn.”
- **Ảnh:** Sáng hẳn, gian bếp Thanh Vân Tông với nồi nước sôi trên bếp củi và thuốc thiếu thốn.
- **Động/chuyển:** Hơi nước bốc lên, máy quay dọc bàn thuốc.

**C03-I013 — Cận vật**
- **Mốc voice:** §111 — ““Dẫn Hương Diệp.””
- **Ảnh:** Lá Dẫn Hương Diệp với mùi thơm đặc biệt nằm cạnh mảnh vải nhiễm hương.
- **Động/chuyển:** Cận gân lá, côn trùng nhỏ bay mờ ngoài khung.

**C03-I014 — Hồi tưởng**
- **Mốc voice:** §120 — ““Trên đường trở về, có người bắn trúng vai ta bằng một mũi tên tẩm thuốc. Ta tưởng thứ bám trên áo chỉ là cỏ rừng.””
- **Ảnh:** Đường núi lúc Thanh La bị truy sát, một mũi tên tẩm thuốc cắm vào vai áo đen.
- **Động/chuyển:** Hồi tưởng ngắn hơi giảm bão hòa, không thêm nhân vật lạ.

**C03-I015 — Toàn cảnh**
- **Mốc voice:** §132 — ““Không chắc lừa được.” Tạ Hành Chu buộc dây vào chân sào. “Nhưng nếu có thứ gì tới, chí ít chúng ta biết nơi nó tìm…”
- **Ảnh:** Tạ Hành Chu treo áo xám làm mồi trên sào ở dãy nhà phía tây, bố trí dây kéo.
- **Động/chuyển:** Máy quay quét từ sào sang vị trí ẩn nấp cạnh tường.

**C03-I016 — Chi tiết**
- **Mốc voice:** §138 — “Tạ Hành Chu buộc nút dây cuối cùng, thử kéo một cái. Cây sào nghiêng sang trái, chiếc áo khẽ lay động như có người …”
- **Ảnh:** Tạ Hành Chu thử kéo dây khiến áo rách trên sào lay động như có người.
- **Động/chuyển:** Cận sợi dây căng rồi mở ra chiếc áo mồi.

**C03-I017 — Trung cảnh**
- **Mốc voice:** §144 — “Đang cười, Tạ Hành Chu chợt thấy Tam trưởng lão đưa tay đặt lên bên sườn. Lão ho một tiếng rất nhỏ, rồi chống tay v…”
- **Ảnh:** Tam trưởng lão che cơn ho, đặt tay bên sườn; Hành Chu nhận ra trạng thái bất thường.
- **Động/chuyển:** Chuyển nét từ bàn tay trưởng lão sang mắt Hành Chu.

**C03-I018 — Cận vật**
- **Mốc voice:** §153 — “Nó chỉ lớn hơn hạt đậu một chút, hai cánh mỏng rung rất nhanh. Con bọ bay vòng quanh lu nước, lượn qua mái hiên, rồ…”
- **Ảnh:** Con Dẫn Hương Trùng nhỏ với hai cánh mỏng bay quanh lu nước rồi đổi hướng.
- **Động/chuyển:** Macro con trùng, cánh rung, không phóng đại như quái thú.

**C03-I019 — Toàn cảnh**
- **Mốc voice:** §156 — “Một con thứ hai xuất hiện.”
- **Ảnh:** Hai con trùng dò hương hướng về dãy nhà phía tây, cây cỏ rung lạ bên mé rừng.
- **Động/chuyển:** Máy quay bám nhẹ theo quỹ đạo côn trùng.

**C03-I020 — Góc nhìn**
- **Mốc voice:** §159 — “Những cành cỏ ở đó vừa rung lên một nhịp ngắn. Không phải gió, bởi ngọn cỏ bên cạnh vẫn đứng yên.”
- **Ảnh:** Trong cỏ rừng phía tây có cành rung khác hướng gió, báo kẻ truy đuổi đang nấp.
- **Động/chuyển:** Camera ẩn sau bụi trúc, quan sát khe tường.

**C03-I021 — Trung cảnh**
- **Mốc voice:** §162 — “Tạ Hành Chu đặt con dao xuống bàn.”
- **Ảnh:** Tạ Hành Chu đặt dao xuống bàn báo khách đã đến, Vãn Ninh lập tức căng thẳng.
- **Động/chuyển:** Máy quay từ bàn bếp sang lối cửa sau.

**C03-I022 — Hai người**
- **Mốc voice:** §171 — ““Ngươi tên gì?””
- **Ảnh:** Kỷ Thanh La cố gượng dậy hỏi tên Hành Chu, chàng khuyên nàng nằm yên giữ vết khâu.
- **Động/chuyển:** Cận nét mặt Thanh La pha cảnh giác và nể phục.

**C03-I023 — Góc nhìn kết**
- **Mốc voice:** §180 — “Tạ Hành Chu lùi đến cửa sau, hạ giọng:”
- **Ảnh:** Tạ Hành Chu lùi về cửa sau, cảnh báo tránh sân phía tây, quyết xem địch mắc bẫy ra sao.
- **Động/chuyển:** Máy quay bám sau lưng ra mé tường tối.

### Chương 4 — Ba Lối Xuống Núi (30 ảnh)

**C04-I001 — Toàn cảnh**
- **Mốc voice:** §0 — “Ở mé rừng phía tây, hai bóng người đang nằm sát mặt đất.”
- **Ảnh:** Hai sát thủ nằm sát cỏ nơi mé rừng phía tây nhìn về áo xám trên sào.
- **Động/chuyển:** Máy quay thấp xuyên lá cỏ, chiều sáng u ám.

**C04-I002 — Chi tiết**
- **Mốc voice:** §1 — “Một kẻ áo nâu đưa tay che mắt, chăm chú nhìn chiếc áo xám treo trên cây sào. Kẻ còn lại đeo một túi da bên hông, từ…”
- **Ảnh:** Kẻ áo nâu nắm phi tiêu ba cạnh; đồng bọn đeo túi da chứa Dẫn Hương Trùng.
- **Động/chuyển:** Chuyển cận giữa phi tiêu và túi trùng động đậy.

**C04-I003 — Cận hành động**
- **Mốc voice:** §8 — “Hành Chu rút một sợi dây nhỏ buộc ở đầu cột, kéo nhẹ.”
- **Ảnh:** Tạ Hành Chu ẩn sau cột kéo nhẹ sợi dây, áo mồi trên sào rung.
- **Động/chuyển:** Máy quay theo dây tới áo vải xám.

**C04-I004 — Hành động**
- **Mốc voice:** §12 — “Một mũi xuyên qua vạt áo, cắm vào bó rơm dưới chân sào. Chưa tới một nhịp thở sau, mũi thứ hai đã bay tới, hướng th…”
- **Ảnh:** Hai phi tiêu ghim xuyên chiếc áo giả và bó rơm, nơi đáng lẽ có cổ người.
- **Động/chuyển:** Phi tiêu phóng vút chính xác, vải rách phất mạnh.

**C04-I005 — Theo chân**
- **Mốc voice:** §15 — “Tạ Hành Chu không kéo dây nữa. Mặc cho chiếc áo đổ xuống, chàng khom lưng chạy men theo vách nhà. Phía trước có một…”
- **Ảnh:** Hành Chu khom chạy men vách nhà qua lu nước nứt, gạch vỡ, ba bậc hiên.
- **Động/chuyển:** Máy quay theo thấp ngang hông, không rung hỗn loạn.

**C04-I006 — Hai hướng**
- **Mốc voice:** §17 — “Một kẻ leo qua bức tường thấp. Kẻ còn lại chạy vòng về sau dãy nhà, định chặn đường thoát của người trúng tiêu.”
- **Ảnh:** Một kẻ vượt tường thấp, kẻ đeo túi trùng vòng sau dãy nhà để chặn đường.
- **Động/chuyển:** Máy quay từ trên cao ghi rõ địa hình hai hướng.

**C04-I007 — Trong bếp**
- **Mốc voice:** §20 — “Trong bếp, Vãn Ninh đang dùng chày nghiền một nắm lá thuốc. Tiếng chân chạy ngoài sân khiến nàng dừng tay.”
- **Ảnh:** Vãn Ninh nghiền thuốc bằng chày nghe tiếng động, A Thạch ôm chim chạy vào phòng.
- **Động/chuyển:** Chuyển nét từ chày thuốc sang cửa bếp.

**C04-I008 — Hai người**
- **Mốc voice:** §25 — ““Lấy kiếm cho ta.””
- **Ảnh:** Kỷ Thanh La nằm trên phản với kiếm gãy cạnh giường, Vãn Ninh ngăn nàng lấy kiếm.
- **Động/chuyển:** Máy quay ngang qua bàn tay đặt lên chuôi kiếm.

**C04-I009 — Hành động vật thể**
- **Mốc voice:** §40 — “Tạ Hành Chu vừa làm nghiêng chiếc lu nứt.”
- **Ảnh:** Tạ Hành Chu làm đổ lu nứt chứa cát đá, chặn một lối giữa sân.
- **Động/chuyển:** Máy quay theo lu lăn và đá cát bung ra.

**C04-I010 — Chi tiết bẫy**
- **Mốc voice:** §49 — “Chân vừa giẫm xuống, đất lún nhẹ.”
- **Ảnh:** Sát thủ áo nâu tránh dây cản nhưng giẫm trúng nền lá che thùng gỗ lật.
- **Động/chuyển:** Cận chân sụt và gương mặt mất thăng bằng.

**C04-I011 — Đối đầu**
- **Mốc voice:** §52 — “Thanh đao cũ chém từ dưới lên, không nhắm vào cổ mà nhắm cổ tay đang chống đất. Kẻ áo nâu vội thu tay, nghiêng ngườ…”
- **Ảnh:** Hành Chu áp sát chém đao từ dưới lên vào cổ tay địch, áo nâu rách toạc.
- **Động/chuyển:** Máy quay trung cảnh giữ rõ tư thế hai người.

**C04-I012 — Hành động**
- **Mốc voice:** §54 — “Đối phương phản ứng rất nhanh. Hai chân vừa đứng vững, một luồng linh lực đã quấn quanh phi tiêu thứ hai. Ánh sáng …”
- **Ảnh:** Phi tiêu ánh linh lực xanh lục bay sát cột gỗ, Hành Chu nấp tránh kịp.
- **Động/chuyển:** Chuyển động tuyến tính của phi tiêu, ánh xanh rất nhẹ.

**C04-I013 — Hành động hài**
- **Mốc voice:** §64 — “Kẻ áo nâu hừ lạnh, vung tay ném tiếp một mũi phi tiêu. Tạ Hành Chu nghe tiếng gió đã cúi đầu. Mũi phi tiêu lướt qua…”
- **Ảnh:** Phi tiêu sát thủ làm vỡ một viên ngói mái đã rách, Hành Chu tức giận nhìn lên.
- **Động/chuyển:** Mảnh ngói rơi, cắt cận vẻ phẫn nộ hài hước.

**C04-I014 — Góc nhìn**
- **Mốc voice:** §68 — “Một tiếng huýt sáo ngắn vang từ bên kia sân.”
- **Ảnh:** Tiếng huýt sáo báo kẻ thứ hai đã tới hậu viện, Hành Chu và sát thủ đồng thời quay đầu.
- **Động/chuyển:** Chuyển nét qua hai góc nhìn trái phải.

**C04-I015 — Sơ đồ cảnh thật**
- **Mốc voice:** §78 — “Đường sau bếp chia thành ba ngả.”
- **Ảnh:** Ba đường sau bếp: khe suối trơn, vườn rau dẫn kho, lối rừng trúc hẹp.
- **Động/chuyển:** Máy quay từ cao chuyển ngang từng lối, không overlay số giả.

**C04-I016 — Chi tiết bẫy**
- **Mốc voice:** §82 — “Ở lối khe suối, Tạ Hành Chu rải đá tròn từ bờ nước lên bậc lên xuống. Đá ấy không gây thương tích, nhưng người muốn…”
- **Ảnh:** Đá tròn rải trên lối suối ướt, chuông mẻ treo dây phơi gần vườn rau.
- **Động/chuyển:** Cận vật liệu bẫy đơn sơ, nước chảy và chuông khẽ rung.

**C04-I017 — Hành động**
- **Mốc voice:** §85 — “Kẻ đeo túi trùng vừa vòng qua khu nhà phía sau đã thấy lối khe suối. Hắn định chạy xuống, nhưng bàn chân giẫm lên đ…”
- **Ảnh:** Kẻ đeo túi trùng trượt chân bên suối rồi giật mình vì tiếng chuông trong vườn rau.
- **Động/chuyển:** Máy quay theo bước hụt, sau đó cắt chuông rung.

**C04-I018 — Đuổi bắt**
- **Mốc voice:** §89 — “Một bóng áo xanh lướt qua.”
- **Ảnh:** Một bóng áo xanh vụt vào lối rừng trúc, kẻ đeo túi lao theo.
- **Động/chuyển:** Máy quay tracking ngang giữa các thân trúc.

**C04-I019 — Hai người**
- **Mốc voice:** §98 — “Tạ Hành Chu chậm rãi bước ra sau bụi trúc, tay vẫn đặt lên chuôi đao.”
- **Ảnh:** Tạ Hành Chu bước ra sau bụi trúc đối diện sát thủ đeo túi trùng.
- **Động/chuyển:** Góc đối diện cân bằng, đao cũ luôn ở bên hông.

**C04-I020 — Hành động**
- **Mốc voice:** §106 — “Kẻ đeo túi lao tới. Lưỡi đoản đao vạch một đường chéo nhắm cổ. Tạ Hành Chu nghiêng người, dùng đao đỡ ở phía ngoài.…”
- **Ảnh:** Đoản đao đối phương chém chéo tới cổ, Hành Chu gạt bằng trường đao rồi lùi tránh.
- **Động/chuyển:** Máy quay giữ toàn thân động tác, không biến vũ khí.

**C04-I021 — Chi tiết bẫy**
- **Mốc voice:** §112 — “Đầu dây còn lại đang giữ một thân trúc non bị uốn cong sát mặt đất. Nút giữ vừa tuột, thân trúc bật ngang. Nó không…”
- **Ảnh:** Thân trúc non uốn cong bật ngang nhắm trúng túi trùng của sát thủ.
- **Động/chuyển:** Máy quay từ nút dây tuột sang thân trúc bật.

**C04-I022 — Hành động**
- **Mốc voice:** §114 — “Tạ Hành Chu chờ đúng lúc ấy, hạ thấp người, dùng sống đao đánh mạnh vào cổ tay phải của đối thủ.”
- **Ảnh:** Tạ Hành Chu đánh sống đao vào cổ tay phải, làm đoản đao rơi xuống đất.
- **Động/chuyển:** Cận tay và vũ khí rơi, tránh bạo lực đồ họa.

**C04-I023 — Hành động**
- **Mốc voice:** §117 — “Kẻ đeo túi chưa kịp giơ tay kia, chân đã bị Tạ Hành Chu quét ngang bằng cán đao. Cả người ngã ngửa, lưng đập xuống …”
- **Ảnh:** Kẻ đeo túi ngã lưng xuống nền đất trúc nhưng vẫn ôm chặt túi da.
- **Động/chuyển:** Camera theo ngã vừa đủ, giữ nguyên vị trí nhân vật.

**C04-I024 — Cận đối đầu**
- **Mốc voice:** §118 — “Tạ Hành Chu lập tức đặt mũi đao lên sát cổ hắn.”
- **Ảnh:** Tạ Hành Chu đặt mũi đao sát cổ kẻ bị bắt, mặt tái do vết thương ở sườn.
- **Động/chuyển:** Chuyển nét từ mũi đao lên hơi thở nặng nhọc.

**C04-I025 — Toàn cảnh**
- **Mốc voice:** §135 — “Khi Tam trưởng lão tới, kẻ đeo túi đã bị trói hai tay bằng dây gai. Tạ Hành Chu không trói quá chặt, nhưng nút buộc…”
- **Ảnh:** Tam trưởng lão tới hỗ trợ trói tù binh bằng dây gai, Hành Chu giữ sườn áo rỉ máu.
- **Động/chuyển:** Máy quay ngang theo ông lão tới sân trúc.

**C04-I026 — Cận kỹ thuật**
- **Mốc voice:** §143 — “Tam trưởng lão kéo người bị trói đứng dậy. Kẻ đó định vùng, lão liền ho một tiếng. Cả người lão có vẻ run rẩy, nhưn…”
- **Ảnh:** Tam trưởng lão giữ cổ tay tù binh bằng thế khóa tinh tế dù dáng ngoài già yếu.
- **Động/chuyển:** Cận bàn tay và nút dây, Hành Chu kín đáo quan sát.

**C04-I027 — Hai người**
- **Mốc voice:** §146 — “Vãn Ninh đứng bên hiên, sắc mặt tái đi khi thấy Tạ Hành Chu lại chảy máu.”
- **Ảnh:** Vãn Ninh thấy vết máu mới trên áo Hành Chu và nổi giận vì vừa băng lại đêm trước.
- **Động/chuyển:** Cận ánh mắt tức giận và nụ cười gượng của Hành Chu.

**C04-I028 — Trong phòng**
- **Mốc voice:** §152 — “Kỷ Thanh La đã ngồi dậy trên phản trong gian bếp. Nhìn kẻ bị bắt, đôi mắt nàng lạnh đi.”
- **Ảnh:** Kỷ Thanh La ngồi tựa phản, nhận ra dấu Thạch Ưng Hội trên kẻ bị bắt.
- **Động/chuyển:** Máy quay từ mảnh áo nâu đến mắt nàng lạnh đi.

**C04-I029 — Đối chất**
- **Mốc voice:** §166 — “Tạ Hành Chu ngồi xuống bậc thềm, lấy mảnh vải sạch ép lên vết thương bên sườn.”
- **Ảnh:** Tạ Hành Chu ngồi bậc cửa ép vải vào sườn, hỏi tù binh muốn người hay muốn vật.
- **Động/chuyển:** Máy quay thấp ngang bậc thềm, tù binh bị trói phía trước.

**C04-I030 — Cảnh kết**
- **Mốc voice:** §181 — “Ngoài sơn môn, từ trong rừng bỗng vang lên một tiếng còi dài.”
- **Ảnh:** Tiếng còi dài từ rừng làm tù binh tái mặt, mọi người nhìn ra cổng.
- **Động/chuyển:** Máy quay tiến từ nét mặt Chu Tứ sang khoảng rừng xa.

### Chương 5 — Bụi Tro Trên Phong Thư (27 ảnh)

**C05-I001 — Cận cảm xúc**
- **Mốc voice:** §0 — “Tiếng còi trong rừng tắt đi. Người bị trói quỳ cạnh bậc cửa bỗng co rúm vai, hai môi tái nhợt.”
- **Ảnh:** Chu Tứ quỳ cạnh bậc cửa, co rúm khi nghe tiếng còi từ rừng.
- **Động/chuyển:** Máy quay sát gương mặt trắng bệch, ánh sáng ngày mờ.

**C05-I002 — Hành động**
- **Mốc voice:** §8 — “Tạ Hành Chu lập tức đưa cán đao ngang miệng hắn.”
- **Ảnh:** Tạ Hành Chu nhanh tay dùng cán đao chặn miệng Chu Tứ để hắn không cắn viên độc.
- **Động/chuyển:** Cắt gọn giữa bàn tay và động tác chặn.

**C05-I003 — Cận vật**
- **Mốc voice:** §14 — “Tam trưởng lão cau mày, giữ lấy gáy tù binh. Tạ Hành Chu dùng một mảnh vải quấn quanh ngón tay, kiểm tra rất cẩn th…”
- **Ảnh:** Viên sáp đen nhỏ được lấy khỏi kẽ răng Chu Tứ và đặt lên đĩa gốm.
- **Động/chuyển:** Macro hạt sáp trên đĩa, Vãn Ninh lùi ra thận trọng.

**C05-I004 — Thẩm vấn**
- **Mốc voice:** §27 — “Kẻ bị trói tên là Chu Tứ.”
- **Ảnh:** Chu Tứ bị trói trong phòng; Kỷ Thanh La, Hành Chu, Vãn Ninh hỏi chuyện Thạch Ưng Hội.
- **Động/chuyển:** Máy quay đổi góc vừa phải trong không gian hẹp.

**C05-I005 — Hồi tưởng**
- **Mốc voice:** §31 — ““Bên ngoài trạm đá cũ ở chân núi.””
- **Ảnh:** Trạm đá cũ dưới chân núi nơi kẻ che mặt từng giao việc cho Chu Tứ.
- **Động/chuyển:** Cảnh sương mờ, nhân vật che mặt giữ bí ẩn, không lộ danh tính.

**C05-I006 — Cận phản ứng**
- **Mốc voice:** §36 — ““Năm mươi linh thạch hạ phẩm.””
- **Ảnh:** Chu Tứ nói tiền thưởng năm mươi linh thạch hạ phẩm, Hành Chu kinh ngạc hài hước.
- **Động/chuyển:** Cận ánh mắt to và tay đếm số theo thói quen.

**C05-I007 — Đối thoại căng thẳng**
- **Mốc voice:** §48 — ““Người đàn bà ấy phải sống,” cuối cùng hắn nói. “Còn vật trong tay nàng, không được mở.””
- **Ảnh:** Chu Tứ thú nhận phải bắt sống nữ tử mang vật không được mở, Thanh La khẽ siết tấm chăn.
- **Động/chuyển:** Chuyển nét từ tù binh sang bàn tay Thanh La.

**C05-I008 — Toàn cảnh**
- **Mốc voice:** §56 — “Tạ Hành Chu không hỏi ngay. Thay vào đó, Hành Chu đề nghị Tam trưởng lão nhốt Chu Tứ vào gian kho bỏ trống, cho nướ…”
- **Ảnh:** Chu Tứ bị đưa vào gian kho trống, Tam trưởng lão canh giữ, Hành Chu không muốn giết tù binh đã bắt.
- **Động/chuyển:** Máy quay theo bước chân qua cửa kho cũ.

**C05-I009 — Trong bếp**
- **Mốc voice:** §61 — “Buổi trưa, chiếc nồi cuối cùng của Thanh Vân Tông nấu một thứ nước canh mà nhìn kỹ mới thấy vài cọng rau.”
- **Ảnh:** Bữa canh rau loãng, chiếc nồi trống gần hết và mấy cái bát cũ trên bàn.
- **Động/chuyển:** Hơi nóng mỏng bốc lên, ánh trưa nghiêng cửa.

**C05-I010 — Cận vật**
- **Mốc voice:** §67 — “Tạ Hành Chu vừa nói vừa lấy từ trong tay nải ra mấy đồng tiền cuối cùng, đặt cạnh nồi. A Thạch tròn mắt.”
- **Ảnh:** Tạ Hành Chu lấy những đồng tiền cuối cùng trong tay nải đặt cạnh nồi cho mọi người mua gạo.
- **Động/chuyển:** Cận các đồng tiền lăn nhẹ trên mặt gỗ.

**C05-I011 — Hài hước**
- **Mốc voice:** §72 — “Ngay phía sau, lão nhân đang lén mở hồ lô bỗng ho sặc sụa.”
- **Ảnh:** Tam trưởng lão đang lén mở hồ lô rượu nghe Hành Chu trêu chuyện đổi tiền lấy rượu.
- **Động/chuyển:** Cắt cận hồ lô bị giấu sau lưng ông.

**C05-I012 — Hai người**
- **Mốc voice:** §80 — “Vãn Ninh nhìn Tạ Hành Chu, khóe môi cuối cùng cũng cong lên. Nụ cười rất nhanh, nhưng A Thạch lập tức reo:”
- **Ảnh:** Vãn Ninh lần đầu hé cười khi Hành Chu nói cho mượn tiền chỉ lấy lãi bằng bát cơm đầy.
- **Động/chuyển:** Ánh sáng trưa làm dịu nét mặt Vãn Ninh.

**C05-I013 — Toàn cảnh**
- **Mốc voice:** §86 — “Sau khi thay băng, Tạ Hành Chu được Vãn Ninh dẫn ra một vạt đất sau bếp.”
- **Ảnh:** Vãn Ninh dẫn Hành Chu tới vách đá ẩm sau bếp tìm Thanh Diệp Thảo.
- **Động/chuyển:** Máy quay lướt qua rãnh nước nhỏ và rêu xanh.

**C05-I014 — Chi tiết**
- **Mốc voice:** §91 — “Hai người đi không xa, chỉ tới chân vách đá sau bếp, nơi những giọt nước từ khe đá chảy xuống một rãnh nhỏ. Tạ Hành…”
- **Ảnh:** Hành Chu nhổ nhầm lá thuốc, Vãn Ninh giữ cổ tay và chỉ mặt dưới lá có lông.
- **Động/chuyển:** Cận hai bàn tay, lá thuốc rõ đặc tính.

**C05-I015 — Cận manh mối**
- **Mốc voice:** §99 — “Vãn Ninh thả tay ra. Tạ Hành Chu chợt nhìn thấy vệt đỏ trên cổ tay nàng, đã lan thêm một chút so với đêm trước.”
- **Ảnh:** Vết đỏ trên cổ tay Vãn Ninh lan dài dưới ống tay áo khi nàng cúi nhặt thuốc.
- **Động/chuyển:** Chuyển nét từ cây cỏ lên vết bỏng đỏ.

**C05-I016 — Cảnh cảm xúc**
- **Mốc voice:** §108 — ““Cô nương không cần chữa cả thiên hạ. Hôm nay cứu được người trước mắt đã giỏi lắm rồi.””
- **Ảnh:** Hành Chu nhẹ nhàng trấn an Vãn Ninh về việc không thể chữa lành tất cả mọi người.
- **Động/chuyển:** Máy quay trung cảnh hai người bên vách đá, nước chảy nền.

**C05-I017 — Chi tiết**
- **Mốc voice:** §113 — “Tạ Hành Chu không nhìn theo. Hành Chu tiếp tục nhặt đủ sáu cây thuốc, đặt tất cả vào chiếc khăn đã trải sẵn.”
- **Ảnh:** Sáu cây Thanh Diệp Thảo được bọc trong khăn vải, hai người chậm bước trở về.
- **Động/chuyển:** Máy quay theo bó thuốc trong tay, ánh trưa dần dịu.

**C05-I018 — Trong phòng**
- **Mốc voice:** §116 — “Kỷ Thanh La đang ngồi tựa bên cửa sổ khi hai người trở lại.”
- **Ảnh:** Kỷ Thanh La áo sạch tóc buộc cao ngồi bên cửa sổ, đặt mảnh đồng bị bẻ gãy lên bàn.
- **Động/chuyển:** Máy quay tiến từ cửa sổ tới bàn gỗ.

**C05-I019 — Cận vật**
- **Mốc voice:** §117 — “Nàng đã thay áo sạch, mái tóc đen được buộc cao. Gương mặt vẫn tái, nhưng khí sắc khá hơn buổi sáng. Trên bàn trước…”
- **Ảnh:** Mảnh đồng nhỏ mép gãy, hình cánh chim khắc trên bề mặt; giấy dầu nhàu nằm cạnh.
- **Động/chuyển:** Cận họa tiết cánh chim, tránh chữ không có trong truyện.

**C05-I020 — Hồi tưởng**
- **Mốc voice:** §125 — ““Có những xe hàng không chở hàng.””
- **Ảnh:** Những xe hàng niêm phong đi qua trạm Thanh Giản, bên trong là người bị nhốt chứ không phải hàng.
- **Động/chuyển:** Chuyển cảnh ký ức mờ, chỉ gợi bóng người trong thùng kín.

**C05-I021 — Hồi tưởng**
- **Mốc voice:** §131 — ““Bọn chúng giấu người trong những thùng xe niêm phong, dùng giấy thông hành của thương hội để qua trạm kiểm soát. T…”
- **Ảnh:** Kỷ Thanh La đột nhập trạm kiểm soát và cứu được một số người bị nhốt, một số người không kịp cứu.
- **Động/chuyển:** Hình tượng hóa kín đáo, không thêm chiến tích siêu năng lực.

**C05-I022 — Cận cảm xúc**
- **Mốc voice:** §136 — ““Ta đến muộn.””
- **Ảnh:** Kỷ Thanh La cúi đầu trước tờ giấy dầu, nỗi ân hận hiện lên qua ánh mắt.
- **Động/chuyển:** Máy quay chậm tới ngón tay siết mép đồng bài.

**C05-I023 — Hai người**
- **Mốc voice:** §152 — ““Ngoài kia có người gọi ta là ma nữ. Họ không hoàn toàn nói sai. Ở trạm đó, ta giết một tên quản sự đã buông vũ khí…”
- **Ảnh:** Thanh La thừa nhận từng chém quản sự đã buông vũ khí; Hành Chu lắng nghe không vội phán xét.
- **Động/chuyển:** Góc đối thoại gần, không minh họa trực diện cảnh giết.

**C05-I024 — Chi tiết điều tra**
- **Mốc voice:** §165 — “Đầu giờ chiều, Tạ Hành Chu đem phong thư đêm trước ra sân, đặt dưới nắng.”
- **Ảnh:** Tạ Hành Chu đặt phong thư dưới nắng, dùng than chà giấy hứng để kiểm tra vết lún bút.
- **Động/chuyển:** Cận lớp giấy, than và dấu son đỏ.

**C05-I025 — Cận manh mối**
- **Mốc voice:** §173 — “Ở góc dưới phong thư, dưới lớp dấu son, hiện ra một vệt lún ngắn như nét chữ bị xóa. Không thể đọc thành từ, chỉ đủ…”
- **Ảnh:** Vệt lún như nét chữ bị xóa ẩn dưới dấu son của phong thư, không hiện ký tự rõ.
- **Động/chuyển:** Máy quay đổi góc chiếu nghiêng để vết lún lộ ra.

**C05-I026 — Trong kho**
- **Mốc voice:** §180 — “Tạ Hành Chu tới nơi. Chu Tứ ngồi dựa tường, mồ hôi đầm đìa dù trời không nóng.”
- **Ảnh:** Chu Tứ mồ hôi đầm đìa xin gặp Hành Chu, ngập ngừng tiết lộ người thuê muốn diệt khẩu.
- **Động/chuyển:** Máy quay từ bóng cửa kho tới mặt tù binh.

**C05-I027 — Cảnh kết**
- **Mốc voice:** §187 — ““Ta không biết hắn là ai. Nhưng buổi giao người ở trạm đá không phải để nhận thưởng. Là để bịt miệng tất cả.””
- **Ảnh:** Hành Chu nhìn nắng chiều chạm mép sân, hiểu buổi giao người ở trạm đá là bẫy giết tất cả.
- **Động/chuyển:** Máy quay sau vai Hành Chu ra khoảng sân nắng nghiêng.

### Chương 6 — Một Bữa Cơm Trước Trận (30 ảnh)

**C06-I001 — Trong bếp**
- **Mốc voice:** §0 — “Tạ Hành Chu rời nhà kho, đi một vòng quanh sân rồi dừng trước chiếc nồi đang đặt trên bếp.”
- **Ảnh:** Tạ Hành Chu khuấy chiếc nồi canh nguội gần trống, suy tính trước trận.
- **Động/chuyển:** Cận muôi khuấy nước và ánh mắt suy tư.

**C06-I002 — Hai người**
- **Mốc voice:** §8 — ““Chúng ta phải đưa đại sư tỷ đi.””
- **Ảnh:** Vãn Ninh muốn đưa Thanh La xuống khe suối; Hành Chu hỏi ai đủ sức mang theo người bị thương.
- **Động/chuyển:** Chuyển góc đối thoại tại cửa bếp.

**C06-I003 — Toàn cảnh nhóm**
- **Mốc voice:** §18 — ““Ta làm sao?” Giọng ông lão vang từ cửa bếp.”
- **Ảnh:** Tam trưởng lão vào bếp, mọi người tranh luận nên đi hay ở lại giữ núi.
- **Động/chuyển:** Máy quay xoay nhỏ quanh chiếc bàn cũ.

**C06-I004 — Cận hài**
- **Mốc voice:** §24 — ““Ăn cơm.””
- **Ảnh:** Hành Chu quyết phải ăn trước khi đối đầu, Tam trưởng lão tròn mắt.
- **Động/chuyển:** Cận gương mặt Hành Chu nghiêm túc một cách buồn cười.

**C06-I005 — Hai người**
- **Mốc voice:** §30 — “Tạ Hành Chu quay sang nhìn đứa trẻ.”
- **Ảnh:** A Thạch chỉ số khoai còn giấu, Tam trưởng lão nhìn ngượng vì từng nướng trộm.
- **Động/chuyển:** Chuyển cận rổ khoai rồi gương mặt lúng túng.

**C06-I006 — Trong phòng**
- **Mốc voice:** §45 — “Tạ Hành Chu đưa chiếc ghế có chân mới sửa tới.”
- **Ảnh:** Tạ Hành Chu mang ghế đã sửa cho Thanh La đang nghỉ, hai người nói chuyện giữa căn phòng cũ.
- **Động/chuyển:** Ánh cửa sổ chiều mỏng trên mặt ghế gỗ.

**C06-I007 — Hai người**
- **Mốc voice:** §55 — “Tạ Hành Chu nhìn con đường núi ngoài cổng.”
- **Ảnh:** Thanh La hỏi vì sao Hành Chu vẫn đùa trước hiểm nguy; chàng nhìn về đường núi.
- **Động/chuyển:** Máy quay từ gương mặt sang khe cửa nhìn ra núi.

**C06-I008 — Toàn cảnh bữa cơm**
- **Mốc voice:** §59 — “Bữa cơm hôm ấy có khoai hấp, rau dại và một bát canh loãng. Tam trưởng lão ngậm một miếng khoai, vừa ăn vừa than kh…”
- **Ảnh:** Bữa khoai hấp, rau dại, canh loãng gồm Hành Chu, Vãn Ninh, Thanh La, trưởng lão, A Thạch.
- **Động/chuyển:** Máy quay chậm quanh bàn, cảm giác đoàn kết trước bão.

**C06-I009 — Chi tiết ấm áp**
- **Mốc voice:** §61 — “Tạ Hành Chu bẻ miếng khoai nhỏ đưa sang cho Kỷ Thanh La.”
- **Ảnh:** Hành Chu bẻ phần khoai nhỏ đưa Thanh La đang bị thương.
- **Động/chuyển:** Cận miếng khoai trao tay và nét mặt Thanh La.

**C06-I010 — Chi tiết**
- **Mốc voice:** §64 — “Vãn Ninh ăn chậm hơn mọi người. Đôi lúc nàng đưa tay chạm cổ tay bị bỏng rồi lại vội rút xuống. Tạ Hành Chu nhìn th…”
- **Ảnh:** Vãn Ninh xoa cổ tay bỏng, Hành Chu đưa bát nước nóng mà không hỏi thêm.
- **Động/chuyển:** Hơi nước qua hai người, nhịp yên tĩnh.

**C06-I011 — Cận đạo cụ**
- **Mốc voice:** §67 — ““Muốn cô nương cho mượn một tấm phù.””
- **Ảnh:** Vãn Ninh đưa tấm phù giấy vàng cuối cùng cho Hành Chu bàn chuyện dụ địch.
- **Động/chuyển:** Cận lá phù, không thêm phù văn rực rỡ quá mức.

**C06-I012 — Sơ đồ bàn**
- **Mốc voice:** §75 — “Chàng đề nghị đặt chiếc hộp gỗ có chứa mảnh đồng thật ở chính điện, giữ Chu Tứ trong gian nhà phía tây như thể Than…”
- **Ảnh:** Hộp gỗ chứa đồng bài thật đặt giữa bàn, giấy dầu làm chứng bên cạnh, mọi người bàn kế.
- **Động/chuyển:** Máy quay từ hộp đến các gương mặt dè dặt.

**C06-I013 — Đối thoại quyết định**
- **Mốc voice:** §81 — ““Ta biết. Nhưng nếu cả núi chết ở đây, giữ được miếng đồng cũng chẳng còn ai nói chuyện ở Trạm Thanh Giản. Bản ghi …”
- **Ảnh:** Hành Chu nói giữ vật không quan trọng bằng mạng người và bản ghi, Thanh La cân nhắc.
- **Động/chuyển:** Máy quay cận mắt Thanh La rồi tay đẩy mảnh đồng.

**C06-I014 — Chi tiết kế hoạch**
- **Mốc voice:** §96 — “Tạ Hành Chu dùng đầu đũa vẽ mấy đường lên lớp bụi của mặt bàn. Trước chính điện là sân rộng; bên trái có lu nước nứ…”
- **Ảnh:** Hành Chu dùng đũa vẽ địa hình sân, lu nứt, tường thấp, bếp và rừng trúc trên lớp bụi bàn.
- **Động/chuyển:** Máy quay overhead từ bản vẽ tới cửa sân.

**C06-I015 — Trong bếp**
- **Mốc voice:** §100 — ““Ngươi định để A Thạch ở đâu?””
- **Ảnh:** A Thạch được bố trí trú phía sau bếp với Kỷ Thanh La, thanh kiếm gãy đặt bên giường.
- **Động/chuyển:** Máy quay qua cửa phòng, không thêm người ngoài.

**C06-I016 — Toàn cảnh**
- **Mốc voice:** §113 — “Khi mặt trời chạm đỉnh núi phía tây, tiếng bước chân vang lên ngoài sơn môn.”
- **Ảnh:** Nắng chiều chạm đỉnh núi, ba kẻ Thạch Ưng Hội xuất hiện ngoài cổng Thanh Vân Tông.
- **Động/chuyển:** Máy quay từ cổng ra bậc thềm dài, ngược sáng.

**C06-I017 — Giới thiệu phản diện**
- **Mốc voice:** §115 — “Một nam tử mặc áo xám tro bước lên bậc thềm, bên hông đeo trường kiếm hẹp. Sau lưng hắn có hai người, một người dùn…”
- **Ảnh:** Trác Cửu áo xám tro cầm kiếm hẹp đứng đầu, sau là cung thủ và kẻ dùng trường côn bọc sắt.
- **Động/chuyển:** Máy quay góc thấp vừa phải, nhóm ba người rõ vũ khí.

**C06-I018 — Hai người**
- **Mốc voice:** §123 — “Trác Cửu nhìn Hành Chu, ánh mắt dừng tại vết thương bên sườn.”
- **Ảnh:** Trác Cửu quan sát Hành Chu đang băng sườn; Hành Chu cười nhạt che đau.
- **Động/chuyển:** Góc đối diện qua sân, gió lật áo.

**C06-I019 — Cận đạo cụ**
- **Mốc voice:** §132 — ““Đồ đâu?””
- **Ảnh:** Hộp gỗ đặt như vật trao đổi ở chính điện, Trác Cửu không rời mắt khỏi nó.
- **Động/chuyển:** Máy quay tiến chậm tới hộp từ phía Trác Cửu.

**C06-I020 — Đối thoại**
- **Mốc voice:** §141 — ““Đúng. Một đứa trẻ chẳng biết gì, giết nó cũng chẳng tăng thêm linh thạch.””
- **Ảnh:** Tạ Hành Chu đàm phán để bảo vệ A Thạch và những người không liên quan, Trác Cửu giễu cợt.
- **Động/chuyển:** Luân chuyển góc máy hai đối thủ, bối cảnh cổng hỏng.

**C06-I021 — Hành động bất ngờ**
- **Mốc voice:** §153 — “Tạ Hành Chu đã tính tới việc có người dùng cung. Nhưng Hành Chu không nhìn thấy mũi tên đầu tiên được buông khỏi dâ…”
- **Ảnh:** Mũi tên đầu tiên từ cung thủ bay ngang sân về khu bếp.
- **Động/chuyển:** Đường tên rõ hướng, không chậm quá mức.

**C06-I022 — Nguy hiểm**
- **Mốc voice:** §156 — “Mũi tên cắm phập vào cánh cửa sau bếp, chỉ cách A Thạch vừa ló mặt ra một gang tay.”
- **Ảnh:** Mũi tên cắm phập cửa bếp chỉ cách A Thạch ló đầu ra một gang tay.
- **Động/chuyển:** Cận mũi tên rung trên cửa, đứa trẻ hốt hoảng.

**C06-I023 — Đối đầu mở**
- **Mốc voice:** §159 — “Trác Cửu ra tay ngay khoảnh khắc ấy.”
- **Ảnh:** Trác Cửu rút kiếm hẹp lao về phía Hành Chu, đối thủ nâng đao cũ lên đỡ.
- **Động/chuyển:** Máy quay ngang, đường kiếm và đao phân biệt rõ.

**C06-I024 — Cận áp lực**
- **Mốc voice:** §165 — “Cổ tay Tạ Hành Chu đau buốt.”
- **Ảnh:** Cổ tay Hành Chu đau buốt khi kiếm đối phương ép mạnh, vết thương sườn căng.
- **Động/chuyển:** Cận gân tay và vết băng thấm máu nhẹ.

**C06-I025 — Hai trận song song**
- **Mốc voice:** §174 — “Ở ngoài sân, Tam trưởng lão quật cây chổi về phía người cầm côn, ép đối phương tránh sang một bên. Lão không dùng l…”
- **Ảnh:** Tam trưởng lão dùng chổi đỡ người cầm côn; phía xa Hành Chu giữ Trác Cửu.
- **Động/chuyển:** Máy quay chuyển tiêu cự trước sau trong cùng sân.

**C06-I026 — Trong bếp**
- **Mốc voice:** §180 — ““Lấy tấm phù của muội. Đừng đánh vào Trác Cửu.””
- **Ảnh:** Thanh La yếu sức nhắc Vãn Ninh dùng phù cuối nhưng không đánh thẳng Trác Cửu.
- **Động/chuyển:** Cận tấm phù vàng và gương mặt hai sư tỷ.

**C06-I027 — Hành động**
- **Mốc voice:** §189 — “Một đao chém ngang.”
- **Ảnh:** Đao Hành Chu chém ngang rồi chuyển nhanh theo nhịp kiếm Trác Cửu.
- **Động/chuyển:** Máy quay theo vũ khí, giữ kết nối không gian.

**C06-I028 — Chi tiết tu luyện**
- **Mốc voice:** §195 — “Tạ Hành Chu ghi nhớ điều ấy.”
- **Ảnh:** Hành Chu nhận ra thói quen chân trái và cổ tay của Trác Cửu, học ngay trong trận.
- **Động/chuyển:** Cận bước chân đối thủ và ánh mắt Hành Chu quan sát.

**C06-I029 — Hiệu ứng cực nhẹ**
- **Mốc voice:** §198 — “Hành Chu không biết vì sao. Và cũng chẳng có thời gian tìm hiểu.”
- **Ảnh:** Đường đao Hành Chu gọn dần dù hơi thở gấp và khí huyết cạn, không có hào quang bùng nổ.
- **Động/chuyển:** Máy quay ghi liên tiếp động tác dứt khoát, biểu hiện mệt rõ.

**C06-I030 — Cảnh cliffhanger**
- **Mốc voice:** §207 — “Một người trước mặt, một mũi tên sau lưng. Vết thương ở sườn lại rỉ máu, còn trong ngực như có lửa đốt.”
- **Ảnh:** Hành Chu bị Trác Cửu ép trước mặt, cung thủ phía sau đã lắp mũi tên thứ hai, nụ cười biến mất.
- **Động/chuyển:** Góc rộng thể hiện thế gọng kìm, dừng ở mắt Hành Chu.

### Chương 7 — Thanh Vân Không Bán Người (38 ảnh)

**C07-I001 — Hành động tiếp nối**
- **Mốc voice:** §0 — “Mũi tên thứ hai rời dây cung đúng lúc một vệt sáng trắng bùng lên từ cửa bếp.”
- **Ảnh:** Mũi tên thứ hai bay lệch khi ánh sáng phù trắng bùng lên từ cửa bếp.
- **Động/chuyển:** Máy quay theo quỹ đạo tên lệch, ánh phù lóe đúng thời điểm.

**C07-I002 — Trung cảnh**
- **Mốc voice:** §2 — “Vãn Ninh dựa vào cửa, tay phải vẫn giữ tư thế vừa ném phù. Tấm phù cuối cùng trong tay nàng cháy sạch, tro xám bay …”
- **Ảnh:** Vãn Ninh dựa cửa bếp, phù cuối cháy thành tro, vết đỏ trên cổ tay kéo dài tới khuỷu.
- **Động/chuyển:** Cận tro phù cuốn theo gió, ánh mắt lo lắng.

**C07-I003 — Hành động**
- **Mốc voice:** §6 — “Kiếm hẹp đâm thẳng vào ngực. Tạ Hành Chu nghiêng người, dùng sống đao gạt mũi kiếm sang một bên. Kim loại cọ nhau p…”
- **Ảnh:** Tạ Hành Chu dùng sống đao cũ gạt mũi kiếm hẹp Trác Cửu khỏi ngực.
- **Động/chuyển:** Máy quay ngang theo va chạm, tia sáng kim loại nhỏ.

**C07-I004 — Cận vũ khí**
- **Mốc voice:** §12 — “Keng!”
- **Ảnh:** Trác Cửu đánh thẳng vào vết nứt trường đao, một mảnh thép nhỏ văng đi.
- **Động/chuyển:** Cận vết nứt lan trên lưỡi đao, kim loại rung.

**C07-I005 — Cận nhân vật**
- **Mốc voice:** §15 — “Nhưng Tạ Hành Chu nhìn rõ tay mình đang run.”
- **Ảnh:** Tay Hành Chu run vì khí huyết tiêu hao, mặt tái và vết sườn rỉ máu.
- **Động/chuyển:** Máy quay từ bàn tay đến gương mặt gắng gượng.

**C07-I006 — Song song**
- **Mốc voice:** §21 — “Tam trưởng lão chống cây chổi xuống đất, thở dốc.”
- **Ảnh:** Tam trưởng lão thở dốc cầm chổi gỗ trước kẻ cầm côn bọc sắt.
- **Động/chuyển:** Góc thấp trung cảnh, giữ đối thủ rõ trong khung.

**C07-I007 — Hành động**
- **Mốc voice:** §27 — “Tam trưởng lão nhân cơ hội quật cán chổi vào khuỷu tay hắn. Đòn đánh không mạnh, nhưng trúng đúng khớp. Người nọ đa…”
- **Ảnh:** Ông lão đánh trúng khuỷu tay đối thủ bằng cán chổi nhưng bị ép lùi ở bậc cửa.
- **Động/chuyển:** Máy quay theo cán chổi, không phóng đại sức mạnh.

**C07-I008 — Trong bếp**
- **Mốc voice:** §35 — “Kỷ Thanh La rút nửa thanh kiếm gãy đặt bên cạnh phản. Đầu ngón tay nàng trắng bệch vì dùng sức, nhưng ánh mắt vẫn k…”
- **Ảnh:** Thanh La cầm nửa thanh kiếm gãy bên phản, xin Vãn Ninh đưa tới cửa sổ nhìn cung thủ.
- **Động/chuyển:** Máy quay theo tay nắm lưỡi kiếm, ánh mắt quyết tâm.

**C07-I009 — Đối đầu tâm lý**
- **Mốc voice:** §41 — “Trác Cửu không phải kẻ ngu ngốc. Hắn đã nhìn ra Tạ Hành Chu có lối đánh rất khác tán tu bình thường: lúc đầu vụng v…”
- **Ảnh:** Trác Cửu nhận ra Hành Chu càng đánh gọn hơn nhưng máu và sức cũng giảm.
- **Động/chuyển:** Máy quay đổi góc đối diện hai khuôn mặt, thở dốc.

**C07-I010 — Chi tiết**
- **Mốc voice:** §49 — “Địch nhân có thể nhìn thấy mình yếu đi, nhưng chưa chắc biết thời điểm nào mình sẽ hết sức. Còn Trác Cửu mỗi lần nh…”
- **Ảnh:** Trác Cửu liếc liên tục chiếc hộp trên bàn thờ trong chính điện, bộc lộ mục tiêu.
- **Động/chuyển:** Máy quay theo ánh mắt tới hộp gỗ.

**C07-I011 — Hành động**
- **Mốc voice:** §51 — “Tạ Hành Chu chợt đổi hướng, lao thẳng vào cửa điện.”
- **Ảnh:** Hành Chu bất ngờ đổi hướng lao về cửa chính điện, Trác Cửu đuổi sát phía sau.
- **Động/chuyển:** Camera theo từ sân vào cửa điện, chuyển liên tục.

**C07-I012 — Chi tiết bẫy**
- **Mốc voice:** §56 — “Chiếc hộp gỗ văng lên.”
- **Ảnh:** Tạ Hành Chu dùng chuôi đao đánh mép bàn thờ, chiếc hộp gỗ bắn lên không.
- **Động/chuyển:** Máy quay cận hộp gỗ bật lên, không quay siêu chậm quá lâu.

**C07-I013 — Hành động**
- **Mốc voice:** §59 — “Hành Chu không chém vào đầu đối thủ. Chàng chuyển đao rất thấp, bổ về phía chân trái đang đặt lên ngưỡng cửa. Trác …”
- **Ảnh:** Trác Cửu chụp hộp, Hành Chu bổ thấp ép chân trái đối thủ rút lại.
- **Động/chuyển:** Máy quay từ hộp xuống đôi chân di chuyển.

**C07-I014 — Cận bẫy**
- **Mốc voice:** §60 — “Từ phía sau, một sợi dây gai vốn buộc dọc lan can bị Tạ Hành Chu đá bật khỏi nút giữ.”
- **Ảnh:** Nút dây gai dọc lan can bị Hành Chu đá bật, thanh xà mục ở mái hiên sắp đổ.
- **Động/chuyển:** Máy quay bám nút dây tuột rồi chuyển tới thanh xà.

**C07-I015 — Hành động môi trường**
- **Mốc voice:** §63 — “Rầm!”
- **Ảnh:** Thanh xà gỗ rơi ầm chắn lối hai người, bụi ngói phủ mặt sân.
- **Động/chuyển:** Bụi gỗ và ngói rơi, giữ liên tục vị trí cửa điện.

**C07-I016 — Cận đau đớn**
- **Mốc voice:** §67 — “Tạ Hành Chu ở bên kia xà, tay chống đao, mặt tái mét.”
- **Ảnh:** Hành Chu chống đao thở gấp sau xà gỗ, cố đùa để che cơn đau.
- **Động/chuyển:** Máy quay cận mồ hôi, tiếng thở chỉ là định hướng.

**C07-I017 — Nguy hiểm**
- **Mốc voice:** §72 — “Người cầm cung bước ra giữa sân, giơ mũi tên thẳng về phía cửa chính điện.”
- **Ảnh:** Cung thủ ra giữa sân căng dây nhắm vào cửa chính điện.
- **Động/chuyển:** Máy quay ngang theo cây cung kéo căng.

**C07-I018 — Hành động**
- **Mốc voice:** §74 — “Hắn vừa kéo căng dây, một vệt sáng lạnh lẽo bỗng lóe lên từ cửa sổ bếp.”
- **Ảnh:** Nửa thanh kiếm gãy từ cửa sổ bếp bay ngang trúng tay áo cung thủ, cán cung rơi xuống.
- **Động/chuyển:** Máy quay từ cửa sổ theo quỹ đạo kiếm gãy đến tay áo.

**C07-I019 — Trong bếp**
- **Mốc voice:** §78 — “Trong bếp, Kỷ Thanh La khuỵu xuống.”
- **Ảnh:** Kỷ Thanh La khuỵu xuống, máu đen thấm băng vai; Vãn Ninh vội đỡ.
- **Động/chuyển:** Chuyển cận hai sư tỷ, biểu cảm căng thẳng.

**C07-I020 — Toàn cảnh**
- **Mốc voice:** §87 — “Tam trưởng lão chống chổi đứng lên.”
- **Ảnh:** Tam trưởng lão chống chổi đứng lên giữa sân, Trác Cửu chém liên tiếp vào thanh xà.
- **Động/chuyển:** Góc rộng cho thấy hai phe cùng kiệt sức.

**C07-I021 — Cận đạo cụ**
- **Mốc voice:** §92 — “Đường nứt trên lưỡi đao cũ chạy dài tới gần sống đao.”
- **Ảnh:** Vết nứt trường đao chạy tới gần sống đao, chiếc hộp nằm bên chân Hành Chu.
- **Động/chuyển:** Máy quay cận đao nứt rồi chuyển hộp.

**C07-I022 — Hành động**
- **Mốc voice:** §97 — “Tạ Hành Chu dùng chân đá chiếc hộp ra trước.”
- **Ảnh:** Hành Chu dùng chân đá hộp gỗ về phía Trác Cửu, không còn đủ sức kéo dài trận.
- **Động/chuyển:** Máy quay theo hộp lướt nền đá.

**C07-I023 — Trung cảnh biểu tượng**
- **Mốc voice:** §105 — ““Ta không bán người.””
- **Ảnh:** Hành Chu cầm thanh đao gần gãy đứng chắn lối vào, kiên quyết không giao Kỷ Thanh La.
- **Động/chuyển:** Góc đối diện trang nghiêm vừa phải, không biến thành thần lực.

**C07-I024 — Toàn cảnh**
- **Mốc voice:** §111 — “Trác Cửu nhìn quanh.”
- **Ảnh:** Trác Cửu nhìn cung thủ bị thương và người cầm côn do dự, cân nhắc rút lui.
- **Động/chuyển:** Máy quay từ Trác Cửu nhìn quanh toàn sân.

**C07-I025 — Cận vật**
- **Mốc voice:** §117 — “Bên trong là một mảnh đồng bị bẻ gãy, khắc hình cánh chim.”
- **Ảnh:** Trác Cửu nạy mở hộp gỗ thấy mảnh đồng bị bẻ gãy có hình cánh chim.
- **Động/chuyển:** Cận họa tiết cánh chim và ánh mắt kiểm tra.

**C07-I026 — Toàn cảnh**
- **Mốc voice:** §121 — “Trác Cửu siết chặt hộp gỗ, lùi về phía cổng. Người cầm côn đỡ người bị thương đi theo.”
- **Ảnh:** Trác Cửu cầm hộp rút khỏi cổng, người cầm côn dìu cung thủ bị thương đi theo.
- **Động/chuyển:** Máy quay từ sau bóng ba kẻ rời xuống bậc đá.

**C07-I027 — Cận kết trận**
- **Mốc voice:** §129 — “Keng!”
- **Ảnh:** Thanh đao cũ rơi xuống nền đá và gãy đôi sau khi địch khuất.
- **Động/chuyển:** Cận đường gãy và bàn tay Hành Chu buông lỏng.

**C07-I028 — Trung cảnh**
- **Mốc voice:** §131 — “Tạ Hành Chu ngồi phịch xuống bậc cửa, nhăn mặt.”
- **Ảnh:** Tạ Hành Chu ngồi phịch trên bậc cửa, tái mét nhưng vẫn nói đùa vì đao gãy.
- **Động/chuyển:** Máy quay hạ dần ngang tầm mặt, Tam trưởng lão bước tới.

**C07-I029 — Toàn cảnh**
- **Mốc voice:** §141 — “Đêm hôm ấy, Thanh Vân Tông không đốt đèn trong sân.”
- **Ảnh:** Đêm xuống Thanh Vân Tông tối đèn, những người sống sót nghỉ trong các gian nhà cũ.
- **Động/chuyển:** Máy quay trôi nhẹ qua mái điện và sân lặng.

**C07-I030 — Chăm sóc**
- **Mốc voice:** §144 — “Tạ Hành Chu được băng lại vết thương bên sườn và cánh tay. Trong lúc Vãn Ninh buộc nút cuối cùng, Hành Chu vừa đau …”
- **Ảnh:** Vãn Ninh băng vết thương sườn và cánh tay cho Hành Chu trong phòng sáng đèn.
- **Động/chuyển:** Cận dải băng mới, ánh đèn dầu mềm.

**C07-I031 — Hai người**
- **Mốc voice:** §153 — ““Tiểu tử, lão phu hỏi ngươi lần cuối. Có muốn gia nhập không?””
- **Ảnh:** Tam trưởng lão nghiêm túc hỏi Hành Chu có muốn gia nhập Thanh Vân Tông chính thức.
- **Động/chuyển:** Máy quay qua bàn gỗ, hồ lô rượu đặt sang bên.

**C07-I032 — Hài hước**
- **Mốc voice:** §171 — ““Lão phu sẽ đi mua gạo.””
- **Ảnh:** Tạ Hành Chu mặc cả chuyện lịch dậy sớm và gạo ăn với trưởng lão, cả hai bất lực nhìn nhau.
- **Động/chuyển:** Khung hai người với biểu cảm đối lập.

**C07-I033 — Cận vật**
- **Mốc voice:** §189 — “Lão nhân nhìn tấm thẻ gỗ trên bàn. Một lát sau, ông lão đẩy thẻ đến trước mặt Tạ Hành Chu.”
- **Ảnh:** Tam trưởng lão đẩy tấm thẻ đệ tử bằng gỗ cũ tới trước mặt Hành Chu.
- **Động/chuyển:** Cận bàn tay và thẻ gỗ mòn cạnh.

**C07-I034 — Cảnh ấm áp**
- **Mốc voice:** §195 — “Từ ngoài cửa, A Thạch chạy vào, vui đến mức suýt làm đổ chiếc rổ.”
- **Ảnh:** A Thạch vui mừng chạy vào gọi Hành Chu là sư huynh, chiếc rổ chim suýt đổ.
- **Động/chuyển:** Máy quay theo đứa bé chạy, nụ cười hai người.

**C07-I035 — Toàn cảnh nhóm**
- **Mốc voice:** §205 — “A Thạch cười khanh khách.”
- **Ảnh:** Thanh Vân Tông có tiếng cười hiếm hoi trong đêm, gian phòng nghèo ấm áp dưới ánh đèn.
- **Động/chuyển:** Máy quay mở rộng qua cửa phòng ra sân trăng.

**C07-I036 — Cận manh mối**
- **Mốc voice:** §209 — “Nàng lấy mảnh giấy dầu từ dưới gối ra, nhìn những hàng chữ đã nhòe. Đoạn danh sách cuối cùng bị nước làm lem gần hế…”
- **Ảnh:** Kỷ Thanh La một mình đọc mảnh giấy dầu cũ trước ngọn đèn khuya.
- **Động/chuyển:** Cận ngón tay trải giấy và ngọn đèn chao.

**C07-I037 — Cực cận**
- **Mốc voice:** §211 — “Đó không phải ký hiệu cánh chim trên đồng bài.”
- **Ảnh:** Dấu đóng chìm Thanh Vân Tông hiện ở mép dưới giấy dầu khi Thanh La nghiêng về phía đèn.
- **Động/chuyển:** Ánh sáng xiên làm dấu chìm hiện lên, không render chữ sai.

**C07-I038 — Cảnh kết bí ẩn**
- **Mốc voice:** §216 — “Kỷ Thanh La nhìn về phía dãy phòng phía tây, nơi Tạ Hành Chu vừa nhận thẻ đệ tử. Ba chữ đóng chìm trên tờ giấy đã ở…”
- **Ảnh:** Kỷ Thanh La lặng người nhìn về phía phòng tây của Hành Chu qua cửa sổ, chuông đồng ngoài sân rung rất khẽ.
- **Động/chuyển:** Máy quay lùi từ ánh mắt đến cửa sổ và sân đêm, fade to black.

## D. Cách agent chia số lượng clip theo audio thật

Tập 1 dự kiến khoảng 120 phút, nhưng chỉ cố định sau khi đo voice thật. Bộ ảnh ở trên là **anchor scenes** chứ không phải số clip video cuối cùng.
Ví dụ 120 phút = 7.200 giây. Nếu agent dùng 3 cảnh máy khác nhau cho mỗi ảnh/scene và trung bình 12–16 giây/cảnh, có thể xây khoảng 450–600 video shot; thiếu hình mới phải bổ sung scene từ đúng đoạn truyện, không kéo dài một ảnh bằng những vòng zoom lặp.
Cần giữ toàn bộ **thời gian theo audio thực tế**; chỉ tạo animation của những hành động được lời kể nhắc tới. Mọi thay đổi thêm hành động mới vào nội dung FINAL phải được người dùng duyệt.

## E. File liên quan

- `DANH-SACH-ANH-TAP-01-AGENT.csv`: dữ liệu máy đọc được với image ID, chương, thứ tự, chỉ số đoạn, cue tiếng Việt, mô tả ảnh, chuyển động và trạng thái.
- `PROMPT-DUNG-CHUNG-CHO-AGENT.md`: prompt triển khai quy tắc nhân vật, tạo ảnh, diễn hoạt và dựng toàn audio.
