# HƯỚNG DẪN KỸ THUẬT DỰNG AUDIO TRUYỆN — TẬP 2

Phiên bản 1.0 · 26/11/2026 · Tiên Vực Ký

## 1. Phạm vi và nguồn chuẩn

- Tên truyện: **Tông Môn Của Những Kẻ Bị Thiên Hạ Truy Sát**. Nhãn ngắn trên thumbnail: **TÔNG MÔN BỊ TRUY SÁT — TẬP 2**. Không đổi thành Từ Phàm Tu Tiên.
- Nguồn nội dung duy nhất: bảy file dưới đây, đã chốt FINAL ngày 26/11/2026. Nếu chưa có trong repo local, chủ dự án có ZIP `TAP-02-CHUONG-08-14-FINAL.zip`. Giải nén đúng cấu trúc, không ghi đè file khác mà không kiểm tra. Nếu local và ZIP khác nhau, báo khác biệt và dừng trước khi sản xuất.
- Chuẩn kỹ thuật kế thừa file `CONTEXT_KENH_AUDIO_TRUYEN_TU_TIEN(8).md`, v6.0, mục 43–46. Tập 1: 19.790 từ tính theo khoảng trắng, master WAV 01:38:47 tại 1.25x, khoảng 200 từ/phút. Đây là benchmark, không phải giới hạn cứng.
- Tập 2 khoảng 17 nghìn từ, dự kiến khoảng 85–95 phút nếu nhịp tương tự Tập 1, cần đo bằng WAV. Không cố kéo dài tới 120 phút.
- Chưa có bộ 300 ảnh. Không tự tạo, dùng ảnh mạng, tái dùng ảnh Tập 1 hoặc dựng MP4 giả để lấp thiếu. Có thể làm hết voice và dữ liệu đồng bộ ở giai đoạn A.

| Chương | File trong `03-MANUSCRIPTS/approved/` | Tiêu đề |
|---|---|---|
| 8 | CHUONG-0008-FINAL.md | Món nợ của đệ tử mới |
| 9 | CHUONG-0009-FINAL.md | Dược phô dưới trấn |
| 10 | CHUONG-0010-FINAL.md | Người hái thuốc không trở về |
| 11 | CHUONG-0011-FINAL.md | Thanh đao đầu tiên |
| 12 | CHUONG-0012-FINAL.md | Đao chưa đủ nhanh |
| 13 | CHUONG-0013-FINAL.md | Một đao đổi đường sống |
| 14 | CHUONG-0014-FINAL.md | Vị khách trước sơn môn |

## 2. Thư mục và chống ghi đè

Tự xác định đường dẫn tuyệt đối, không giả định ổ C: hoặc D:. Tạo thư mục riêng cho Tập 2 (tên đề xuất), không đụng đến `BUILD FINAL CLIP/OUTPUT` của Tập 1.

```text
SangTacTruyenTuTien/
├── 03-MANUSCRIPTS/approved/       # CHỈ ĐỌC
└── BUILD FINAL CLIP TAP 02/
    ├── INPUT/
    │   ├── STORYBOARD-TAP-02.csv   # chủ dự án giao sau
    │   ├── IMAGES/                # 300 ảnh, giao sau
    │   └── thumbnail-part-2.png    # ảnh bìa riêng, không đưa vào timeline
    ├── WORK/
    │   ├── TEXT/                  # 7 chương sạch + manifest
    │   ├── TTS_MP3/
    │   ├── WAV_100/
    │   ├── WAV_125/
    │   ├── CHAPTER_AUDIO/
    │   ├── TIMELINE/
    │   ├── IMAGES_NORMALIZED/
    │   ├── VIDEO_SEGMENTS/
    │   ├── LOGS/
    │   └── scripts/
    └── OUTPUT/
```

Kiểm tra `python --version`, `ffmpeg -version`, `ffprobe -version`, khả năng ghi file, dung lượng trống và kết nối gTTS. Dùng virtual environment nếu cần cài `gTTS`; không thay đổi môi trường hệ thống ngoài phạm vi. Ghi phiên bản công cụ, cấu hình, SHA-256 của từng file FINAL và trạng thái công việc. Chỉ sử dụng quyền truy cập đã có. Không lưu token, credential vào log hoặc Git.

## 3. Giai đoạn A — tạo voice trước khi có 300 ảnh

### 3.1. Tiền xử lý văn bản (bắt buộc giữ nguyên nội dung)

Đọc UTF-8. Với định dạng bảy file hiện có: lấy tên chương từ dòng `**Chương N: ...**`, lấy phần thân truyện sau dòng phân cách `---` đầu tiên, bỏ dòng kết `**Hết chương N — FINAL**`. Bỏ các dấu phân cảnh đứng riêng (`***`, `---`) và ký hiệu trình bày Markdown, nhưng giữ chữ, dấu câu, lời thoại và thứ tự. Không bỏ dòng thoại vì nhầm với gạch đầu dòng. Không bỏ chữ in nghiêng/đậm, chỉ bỏ ký hiệu bao ngoài. Không dùng regex xóa mọi dấu gạch hoặc dấu ngoặc trong nội dung. Không tự thay tên, viết lại câu, cắt phần trùng ý, thêm lời kể.

Chèn duy nhất `Chương N: [tên chương]` đầu mỗi chương. Không đọc tên truyện lặp lại, ghi chú, metadata FINAL/APPROVED, đường dẫn, ngày duyệt, hoặc câu kết kỹ thuật. Không chèn CTA, lời quảng cáo, intro/outro hoặc recap. Giữ nguyên các tiếng tượng thanh có trong truyện như Keng!, Rắc!.

Xuất `WORK/TEXT/C08.txt` đến `C14.txt` và `OUTPUT/TAP-02-TTS-SCRIPT.txt`. Trích đoạn đầu/cuối mỗi chương vào báo cáo đối chiếu. Kiểm tra cuối chương 7 không bị thêm vào đầu chương 8, và không lặp/thiếu chữ ở sáu ranh giới tiếp theo.

### 3.2. Chia voice độc lập với ảnh

Do ảnh chưa có, không đặt tên audio theo mã ảnh dự đoán. Tách ở ranh giới câu hoặc đoạn thoại tự nhiên thành các chunk `C08-U0001`, `C08-U0002`...; U là đơn vị voice. Có thể dùng khoảng 1–3 câu/đơn vị, điều chỉnh để không cắt câu, không ngắt giữa tên riêng. Giữ mỗi đơn vị có văn bản liên tục, không trùng lặp. Nếu đoạn quá dài, chia theo dấu câu; không chia cứng theo số ký tự. Nếu đoạn cực ngắn, có thể ghép với câu tiếp theo khi cùng ngữ cảnh. Không thêm khoảng nghỉ nhân tạo vào từng chunk.

Lưu manifest gồm `chapter, unit_id, start_char, end_char, text, text_sha256, audio_path, duration_samples, start_sample, end_sample, status`. Offset ký tự là chỉ số Unicode 0-based, end exclusive trong file Cxx.txt; có thể phân vùng cả khoảng trắng ở ranh giới nhưng không làm mất chữ. Nối các đoạn theo offset phải tái tạo được văn bản sạch đầy đủ, đối chiếu tự động trước khi tạo TTS. Giữ thứ tự theo số, không sort chuỗi không padding.

Sau khi có storyboard, nhiều U có thể ứng với một ảnh, hoặc một U có thể chứa ranh giới ảnh. Không ép cứ một file WAV là một ảnh. Nếu cần cắt trong U, dùng alignment theo câu/lời nói thực tế (xem mục 5). Không tạo lại toàn bộ voice chỉ vì số ảnh thay đổi.

### 3.3. Voice chuẩn duy nhất

| Tham số | Giá trị bắt buộc |
|---|---|
| Engine | Google gTTS |
| Ngôn ngữ | vi |
| TLD | com |
| Slow | False |
| Âm sắc | Giọng nữ tiếng Việt như Tập 1; kiểm tra bằng nghe đối chứng |
| Tốc độ | 1.25x, áp dụng đúng một lần |
| Bộ lọc | FFmpeg `atempo=1.25` (giữ cao độ) |
| WAV gốc và WAV 1.25x | PCM s16le, 48000 Hz, 2 kênh |
| Nghỉ giữa chương | 2.0 giây im lặng, đúng 6 khoảng |
| Audio MP4 | AAC, 192 kbps, 48000 Hz, stereo |

Không đổi sang Edge-TTS, giọng khác, `tld` khác, `slow=True` hay dùng `asetrate` để tăng tốc. Không tăng tốc thêm ở editor hoặc khi mux. Không thêm nhạc nền, hiệu ứng âm thanh, reverb, hoặc xử lý đổi giọng khi chưa có yêu cầu. Nếu gTTS lỗi mạng/rate limit, retry có giới hạn và resume; không chuyển engine âm thầm. gTTS không bảo đảm luôn giữ cùng phiên bản giọng từ phía dịch vụ, vì vậy phải nghe mẫu đối chiếu với Tập 1 trước khi render hàng loạt; không tuyên bố 0% sai lệch nếu chưa kiểm chứng.

### 3.4. Quy trình Python + FFmpeg tham chiếu

Agent cần hiện thực hóa script có resume, log lỗi và kiểm tra exit code. Mẫu dưới đây minh họa một đơn vị, không phải script chạy toàn bộ pipeline.

```python
from pathlib import Path
from gtts import gTTS
import subprocess, time

unit_id = 'C08-U0001'
# text = nội dung thật từ manifest, không phải ví dụ hoặc placeholder
root = Path('WORK')
mp3 = root / 'TTS_MP3' / f'{unit_id}.mp3'
wav100 = root / 'WAV_100' / f'{unit_id}.wav'
wav125 = root / 'WAV_125' / f'{unit_id}.wav'
for p in (mp3, wav100, wav125):
    p.parent.mkdir(parents=True, exist_ok=True)

def run(*args):
    subprocess.run(list(args), check=True)

def make_unit(text):
    tmp = mp3.with_suffix('.tmp.mp3')
    for attempt in range(4):
        try:
            gTTS(text=text, lang='vi', tld='com', slow=False).save(str(tmp))
            # Giải mã thử để phát hiện MP3 rỗng/hỏng trước khi chấp nhận
            run('ffmpeg', '-v', 'error', '-xerror', '-i', str(tmp), '-f', 'null', '-')
            tmp.replace(mp3)
            break
        except Exception:
            tmp.unlink(missing_ok=True)
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)
    run('ffmpeg', '-y', '-i', str(mp3), '-ar', '48000', '-ac', '2',
        '-c:a', 'pcm_s16le', str(wav100))
    run('ffmpeg', '-y', '-i', str(wav100), '-af', 'atempo=1.25',
        '-ar', '48000', '-ac', '2', '-c:a', 'pcm_s16le', str(wav125))
```

Tạo mẫu nghe đầu Chương 8, một đoạn hội thoại và một đoạn giao đấu để so với Tập 1 nếu có WAV/MP4 local. QA về âm sắc, độ rõ, tốc độ, ngắt nghỉ trước khi chạy toàn bộ. TTS có thể chạy tuần tự hoặc số worker thấp; FFmpeg chuyển đổi có thể song song có kiểm soát. Không gửi hàng trăm request cùng lúc. Cache theo hash văn bản + engine + lang + tld + slow + tốc độ + phiên bản pipeline. Chỉ reuse file đã kiểm tra hợp lệ và đúng hash. Khi sửa một đơn vị, tính lại toàn bộ offset phía sau.

Kiểm tra file WAV bằng `ffprobe` và Python `wave`: `nchannels=2`, `sampwidth=2`, `framerate=48000`, `nframes>0`. Thời lượng chính xác = nframes/48000. Kiểm tra decode và phát hiện file im lặng bất thường, clipping, phần đầu/cuối bị cắt. So sánh WAV_125/WAV_100 gần 0,8 (sai số nhỏ do thuật toán và padding), không dùng tỷ lệ này thay cho đo thực tế.

### 3.5. Ghép chương và master

Tạo khoảng nghỉ 2 giây ở định dạng giống WAV:

```bash
ffmpeg -y -f lavfi -i anullsrc=r=48000:cl=stereo -t 2.0 -c:a pcm_s16le silence_2s.wav
```

Nối các WAV_125 trong từng chương theo manifest; sau đó nối C08, silence, C09, silence, ... C14. Dùng FFmpeg concat demuxer với danh sách `file '...'` (escape đường dẫn đúng) và `-c copy` nếu tất cả stream đồng nhất, hoặc Python `wave` ghi nối PCM theo thứ tự. Không nối byte nguyên file WAV vì mỗi file có header riêng. Không thêm khoảng nghỉ sau chương 14; không ghép lại cùng chunk hai lần. Mỗi khoảng nghỉ đúng 96.000 sample frames. Giữ pause tự nhiên trong TTS; không trim tất cả khoảng lặng bằng threshold vì có thể cắt âm nhẹ.

Ví dụ FFmpeg:

```bash
ffmpeg -y -f concat -safe 0 -i concat_ch_08.txt -c copy chapter_08.wav
ffmpeg -y -f concat -safe 0 -i concat_full.txt -c copy TAP-02-VOICE-FULL.wav
```

Đo nframes của master và kiểm tra bằng tổng nframes của tất cả U + 6 × 96.000. Nếu lệch, tìm nguyên nhân trước khi tiếp tục. Xuất chương riêng C08–C14 trong WORK; master lưu OUTPUT. Lập `TAP-02-VOICE-UNITS.csv` với mốc bắt đầu/kết thúc tuyệt đối tính từ sample, kể cả 6 khoảng nghỉ (loại `CHAPTER_PAUSE`). Dùng các số nguyên sample làm nguồn chính xác, thời gian giây chỉ để hiển thị.

### 3.6. Phụ đề SRT và VTT

Tạo phụ đề từ nguyên văn sạch, không từ bản tóm tắt. Dùng forced alignment nếu agent có công cụ phù hợp tiếng Việt; có thể chia câu theo tỷ lệ số từ trong từng U như Tập 1 nếu chưa có alignment, nhưng phải ghi rõ là ước tính và kiểm tra nghe các ranh giới. Không chia đều toàn video. Tối đa hai dòng, khoảng 10–18 từ/cue và 2–5 giây là mục tiêu linh hoạt; đoạn thoại ngắn có thể ngắn hơn. Không gộp câu qua chương, không tách tên riêng nếu tránh được, không đặt phụ đề trong 2 giây im lặng. UTF-8, timestamp tăng dần, không chồng lấn, không vượt thời lượng master. SRT `HH:MM:SS,mmm`; VTT có header `WEBVTT`, dùng dấu chấm. Xuất file riêng để upload YouTube, không burn-in trừ khi chủ dự án yêu cầu.

### 3.7. QA voice và trạng thái chờ hình

Đối chiếu 7 tiêu đề đúng một lần, toàn bộ văn bản, số chunk, hash, dấu câu, tên riêng. Nghe đầu/cuối mỗi chương, toàn bộ các điểm ghép có nghi vấn, đoạn hội thoại, giao đấu; rà soát phát âm Tạ Hành Chu, Vãn Ninh, Kỷ Thanh La, A Thạch, Tam trưởng lão, Chu Tứ, Trác Cửu, Hàn Lộ Tử, Thanh Diệp Thảo, Hắc Tùng Cốc, Đỗ Bình, Hà Thuận, Trạm Thanh Giản. Không tự sửa chính tả bản FINAL; nếu cần điều chỉnh đầu vào phát âm mà vẫn giữ cùng lời, ghi rõ bản gốc/đầu vào TTS và xin duyệt khi thay đổi từ ngữ. Ghi báo cáo lỗi và cách sửa; không gọi ASR là bằng chứng tuyệt đối (ASR cũng có thể nhầm).

Bàn giao voice + SRT/VTT + mốc U + QA. Nếu thiếu storyboard/ảnh, ghi `VOICE_READY_WAITING_IMAGES` (chỉ khi voice đã kiểm tra đạt); nếu voice còn lỗi thì `VOICE_QA_PENDING` hoặc `BLOCKED`, nêu lý do. **Dừng trước bước render FINAL.**

## 4. Giai đoạn B — nhận đủ 300 ảnh do chủ dự án cung cấp sau

### 4.1. Quy cách hình ảnh và continuity

Mỗi ảnh là một phân cảnh độc lập 16:9, ưu tiên 1920×1080 hoặc cao hơn, phong cách tiên hiệp huyền huyễn điện ảnh, nhân vật đẹp, ngầu, nhưng không tự nâng tu vi hoặc thêm hiệu ứng sức mạnh không có trong truyện. Không chữ, watermark, khung ghép nhiều cảnh. Bộ nhân vật tham chiếu chủ dự án sẽ giao cùng ảnh. Kiểm tra Tạ Hành Chu dùng đao bản rộng (không phải kiếm), ban đầu đao cũ đã gãy, sau khi mua ở trấn mới có đao nặng; Vãn Ninh áo xanh ngọc, Kỷ Thanh La hắc y, A Thạch là trẻ nhỏ, Tam trưởng lão tóc bạc áo xám. Giữ nguyên khuôn mặt, phục trang và vết thương theo diễn biến, không cho Kỷ Thanh La khỏi độc hoàn toàn hoặc Hành Chu thức tỉnh thể chất hoàn chỉnh. Hình ảnh đẹp không được làm sai cốt truyện.

Chỉ tiếp nhận ảnh được người dùng giao; không lấy ảnh minh họa hoặc thumbnail thay thế. Đọc storyboard và kiểm tra đủ 300 mã duy nhất, mỗi mã một ảnh. Kiểm tra trùng hash, trùng hình rõ rệt, file không giải mã được, sai tỷ lệ, sai nhân vật/địa điểm. Báo danh sách lỗi và chờ bản thay thế; không dùng một ảnh cho nhiều mã để đủ số lượng. Ảnh tham chiếu nhân vật và thumbnail không tính vào 300 ảnh timeline.

### 4.2. Phân bổ dự kiến

| Chương | Số ảnh dự kiến | Trọng tâm hình ảnh |
|---|---:|---|
| 8 | 35 | Dưỡng thương, đao gãy, tờ giấy dầu, Chu Tứ, rời núi |
| 9 | 40 | Chợ, Bách Thảo Đường, bị theo dõi, lò rèn, lão Đỗ |
| 10 | 40 | Hắc Tùng Cốc, trại giam, khe đá, Hàn Lộ Tử, thẻ sắt |
| 11 | 45 | Đối đầu tại khe đá, lấy lại đao, chuẩn bị giải cứu |
| 12 | 50 | Giải cứu Đỗ Bình, giao đấu, nam tử áo đen, chạy tới cầu |
| 13 | 50 | Đoạn cầu gãy, thoát hiểm, manh mối xe hàng, về trấn |
| 14 | 40 | Về tông, sắc thuốc, bữa ăn, tu luyện, con dấu, khách lạ |
| Tổng | 300 | Phân bổ chính thức theo storyboard được chủ dự án giao |

Đây là phân bổ dự kiến đã trao đổi, không phải storyboard hoàn chỉnh. Có thể điều chỉnh khi chủ dự án duyệt storyboard cuối; agent không tự đổi số lượng hay bỏ cảnh. Chương 14 dài hơn, cần lưu ý tránh giữ ảnh quá lâu ở cao trào. Thời gian mỗi ảnh do diễn biến thực tế quyết định, không do bảng số lượng quyết định.

### 4.3. Chuẩn mã cảnh và manifest hình

Tên file: `C08-I001.png`, `C08-I002.png`... số ảnh bắt đầu lại từ 001 ở từng chương. Dùng mã trong storyboard làm khóa, không sort file theo thời gian tạo hoặc tên mô tả. Chấp nhận JPG nếu manifest ghi đúng tên. Manifest phải có `scene_id, chapter, global_order, image_file, anchor_text, occurrence, description, status`. Anchor là câu/đoạn nguyên văn xuất hiện đúng tại thời điểm ảnh phải lên; nếu lặp, thêm occurrence và đối chiếu offset. Có thể bổ sung `start_char` nếu storyboard dùng đúng văn bản Cxx.txt. Không bịa timestamp trước khi có master WAV. File mẫu `STORYBOARD-SCHEMA.csv` chỉ minh họa cấu trúc, không phải danh sách 300 cảnh.

## 5. Đồng bộ 300 ảnh với voice — phần bắt buộc quan trọng nhất

Mục tiêu: người kể vừa chuyển đến cảnh nào thì hình mô tả cảnh đó xuất hiện. Không chia tổng thời lượng cho 300 rồi kéo mỗi ảnh bằng nhau. Không đổi hình giữa câu nếu làm lộ tình tiết; không để cảnh giao đấu xuất hiện từ khi nhân vật còn đang ăn sáng. Khi văn bản chuyển sang đối thoại mới, hành động mới, địa điểm mới, hoặc đối tượng được nhắc đến lần đầu, sử dụng ảnh phù hợp theo cue chính thức.

### 5.1. Tạo bảng thời điểm chính xác

1. Đọc từng anchor từ storyboard, tìm trong văn bản sạch theo chương và occurrence. Nếu anchor không khớp tuyệt đối, kiểm tra dấu Markdown đã bỏ, không tự chọn một câu tương tự. Báo trường hợp không xác định.
2. Ánh xạ offset văn bản sang U tương ứng. Nếu anchor trùng đầu U, lấy start_sample của U (đối chiếu phần im lặng đầu nếu cần). Nếu nằm giữa U, dùng forced alignment theo tiếng Việt hoặc nghe audio và đánh dấu timestamp. Có thể ước lượng ban đầu theo số từ trong U nhưng phải kiểm tra thủ công các cue trước khi FINAL. Không dùng thời gian ước lượng như mốc đã xác minh.
3. Ảnh đầu chương 8 xuất hiện từ 00:00:00; ảnh đầu mỗi chương sau xuất hiện khi tiêu đề chương đó bắt đầu đọc. Giữ ảnh cuối chương trước trong đúng 2 giây nghỉ, không chèn đen, không chuyển hình sang chương sau sớm.
4. Mỗi ảnh giữ đến lúc bắt đầu ảnh kế tiếp. Ảnh cuối Chương 14 giữ tới cuối master WAV. Không có khoảng trống, overlap hay ảnh chạy sai thứ tự. Nếu hai cue trùng timestamp, rà lại nội dung và thống nhất điều chỉnh storyboard; không render ảnh thời lượng bằng 0.
5. Xuất `TAP-02-TIMELINE.csv` với `global_order,scene_id,chapter,image_file,anchor_text,start_sample,end_sample,start_sec,end_sec,duration_sec,start_frame,end_frame,alignment_method,qa_status`. `end_sample` là exclusive. Tổng thời lượng hình phải bằng master khi làm tròn tới frame. Mọi cảnh phải có mốc được xác minh và trạng thái QA.

Ví dụ logic (không phải timestamp thật của Tập 2):

```text
C08-I001 | 0.000s → 18.400s | Cảnh Hành Chu tỉnh giấc, A Thạch cạnh giường
C08-I002 | 18.400s → 35.700s | Cảnh chuyển sang chi tiết thanh đao gãy
C08-I003 | 35.700s → ...    | Cảnh tiếp theo theo storyboard chính thức
```

Thời lượng tham khảo: giao đấu có thể ngắn khoảng 8–15 giây, đối thoại 20–35 giây, di chuyển 25–40 giây, nội tâm 25–45 giây. Đây không phải luật cứng, vì với 300 ảnh và khoảng 85–95 phút, trung bình chỉ khoảng 17–19 giây/ảnh. Nếu một ảnh giữ quá lâu hoặc chuyển quá nhanh, xem xét anchor và kiểm tra nội dung, không ép khớp con số.

### 5.2. Kiểm soát lỗi trôi thời gian

- Dùng sample frames 48.000 Hz làm đồng hồ gốc; không cộng các giá trị giây đã làm tròn 2 chữ số.
- Đổi mốc tuyệt đối sang frame video 30 fps. Ví dụ mỗi frame tương ứng 1.600 audio sample frames; làm tròn mốc bắt đầu nội bộ tới frame gần nhất, mốc cuối dùng ceil để không mất audio. Mốc đầu = 0. Mỗi đoạn có số frame = frame kết thúc trừ frame bắt đầu. Tính từ mốc tuyệt đối, không làm tròn từng duration độc lập.
- Không render bằng cách cắt/ghép lại audio ở mỗi ảnh. Chỉ dùng master audio duy nhất trong lần mux cuối. Không crossfade voice khi chuyển ảnh.
- Kiểm tra mọi ranh giới ảnh với voice và tối thiểu đầu/cuối mỗi chương; đặc biệt Hàn Lộ Tử, thẻ sắt, đoàn người bị giam, cầu gãy, thẻ đệ tử cũ. Không đưa hình hé lộ manh mối trước câu kể.

## 6. Dựng MP4 ảnh tĩnh (không hiệu ứng)

### 6.1. Hình ảnh

100% ảnh đứng yên. Chuyển cảnh bằng hard cut tại mốc đã xác minh. Không Ken Burns, zoom, pan, rung, camera movement, chuyển động AI, fade đen hay crossfade chồng hai ảnh. Không lặp, tua ngược, nháy hình, logo hoặc watermark. Không chèn thumbnail đầu video. Không kéo giãn ảnh làm méo nhân vật.

Chuẩn hóa về 1920×1080 RGB hoặc yuv420p, SAR 1:1. Ưu tiên ảnh nguồn đúng 16:9; nếu lệch tỷ lệ đáng kể, báo cần thay ảnh; chỉ scale/crop nhẹ có kiểm tra không cắt nhân vật hoặc chi tiết quan trọng. Không tạo viền đen/mờ nếu ảnh có thể chuẩn hóa đúng. Không tự retouch nhân vật. Lưu bản chuẩn hóa trong WORK, giữ nguyên ảnh gốc.

### 6.2. Phương án FFmpeg ổn định cho video dài

Render từng đoạn ảnh thành video không âm thanh với đúng số frame theo timeline, sau đó concat video và mux master audio một lần. Dễ resume nếu lỗi ở một cảnh, tránh filter graph 300 input. Tất cả đoạn phải cùng codec, resolution, fps, pixel format, timebase và cấu hình encoder. Ví dụ mỗi đoạn có N frame, chạy bằng Python subprocess với N thật:

```bash
ffmpeg -y -loop 1 -framerate 30 -i C08-I001.png -vf "scale=1920:1080,setsar=1" -frames:v N -c:v libx264 -preset medium -tune stillimage -crf 20 -pix_fmt yuv420p -r 30 -an C08-I001.mp4
```

Chỉ áp dụng scale trên ảnh đã đúng 16:9 hoặc đã chuẩn hóa trước. `N` là placeholder phải thay bằng số nguyên frame, không chạy nguyên chữ N. `crf 20` và `preset medium` là đề xuất; có thể điều chỉnh theo dung lượng/máy, không hạ chất lượng rõ rệt. Không ép bitrate video theo dung lượng Tập 1. Kiểm tra decode mỗi đoạn; cache theo ảnh, số frame và cấu hình encoder. Tạo danh sách concat theo `global_order` (đường dẫn hợp lệ), dùng `-c copy` nếu đồng nhất:

```bash
ffmpeg -y -f concat -safe 0 -i concat_video.txt -c copy TAP-02-VIDEO-SILENT.mp4
ffmpeg -y -i TAP-02-VIDEO-SILENT.mp4 -i TAP-02-VOICE-FULL.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -ar 48000 -ac 2 -movflags +faststart TONG-MON-BI-TRUY-SAT-TAP-02-FINAL.mp4
```

Không dùng `-shortest` để che lỗi thời lượng. Timeline video cần đủ tới cuối audio (có thể dài hơn tối đa một frame do ceil; chấp nhận padding AAC ở mức codec nếu không mất lời). Kiểm tra stream durations và nghe câu cuối. Nếu độ lệch vượt khoảng một frame cộng padding codec hợp lý, sửa timeline hoặc quy trình render; không cắt audio. Chỉ đổi tên từ bản tạm sang FINAL sau QA. Không để file đang encode mang nhãn FINAL.

## 7. Bàn giao đầu ra

Giai đoạn A (trước khi có ảnh):

- `TAP-02-VOICE-FULL.wav` — PCM 16-bit, 48 kHz stereo, 1.25x.
- `TAP-02-TTS-SCRIPT.txt` — nguyên văn sạch 7 chương, tiêu đề đọc một lần.
- `TAP-02-VOICE-UNITS.csv` — mốc thực tế từng U và khoảng nghỉ.
- `TONG-MON-BI-TRUY-SAT-TAP-02-FINAL.srt` và `.vtt` — nội dung phụ đề đã QA voice (có thể giữ nhãn pending nếu chưa đạt QA; không coi là video hoàn thành).
- `TAP-02-QA-REPORT.md` — trạng thái, thông số và lỗi còn lại.

Giai đoạn B (đủ 300 ảnh): bổ sung `TAP-02-TIMELINE.csv`, `TONG-MON-BI-TRUY-SAT-TAP-02-FINAL.mp4`, báo cáo QA cuối cùng và thumbnail riêng nếu chủ dự án đã giao. Không push file WAV/MP4/ảnh lên Git trừ yêu cầu riêng.

## 8. Nghiệm thu cuối cùng (không được bỏ qua)

- [ ] Bảy file nguồn FINAL, hash ghi lại, không sửa nguồn; không thiếu/lặp nội dung; đúng tiêu đề và thứ tự.
- [ ] Giọng nữ gTTS vi/com, atempo đúng 1.25 một lần, cao độ không đổi, WAV 48kHz stereo s16le, đủ 6 khoảng nghỉ 2 giây.
- [ ] Đã nghe kiểm tra phát âm và điểm nối; ghi rõ những gì kiểm tra bằng nghe thực tế và những gì chỉ kiểm tra tự động.
- [ ] SRT/VTT đọc được, cue không overlap, bám lời kể; mốc ước tính đã rà lại hoặc ghi rõ phần chưa xác minh.
- [ ] Đủ 300 mã ảnh riêng biệt, đúng thứ tự, đúng diễn biến, không lỗi giải mã; storyboard và ảnh chính thức đã nhận.
- [ ] Timeline bao phủ toàn bộ master, không gap/overlap, không lộ cảnh trước voice, không trôi đồng bộ.
- [ ] Video 1920×1080, 30 fps, H.264, yuv420p, SAR 1:1; AAC stereo 48kHz 192 kbps mục tiêu. Không zoom/rung, không nhạc/CTA tự thêm, không black frames ngoài ý muốn.
- [ ] MP4 giải mã toàn bộ bằng `ffmpeg -v error -xerror -i <file> -f null -`; dùng ffprobe xác minh thông số. Kiểm tra hình và nghe các mốc đầu/giữa/cuối, tất cả ranh giới chương và cue nghi vấn. Không báo đã nghe toàn bộ nếu chỉ nghe mẫu.
- [ ] Câu cuối “Đó chính là điều ta muốn biết.” không bị cắt, ảnh cuối khớp, không có outro tự thêm.
- [ ] Báo cáo file path thực, dung lượng, thời lượng WAV/MP4, độ lệch, số ảnh, số U, số subtitle cue, lỗi phát hiện/sửa, trạng thái và giới hạn kiểm tra.

Trạng thái cuối: `FINAL_READY` chỉ khi tất cả điều kiện nghiệm thu bắt buộc đạt. Nếu thiếu ảnh, `VOICE_READY_WAITING_IMAGES`; nếu còn lỗi, `QA_PENDING`/`BLOCKED` với danh sách lỗi cụ thể. Không bịa kết quả, không tự đăng video.
