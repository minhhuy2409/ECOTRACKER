# 🌍 Eco Tracker - Nền tảng Mạng xã hội Gamification vì Môi trường

**Eco Tracker** là một ứng dụng web mạng xã hội đột phá kết hợp giữa bảo vệ môi trường và **Gamification (Trò chơi hóa)**, hướng tới mục tiêu thúc đẩy cộng đồng xây dựng và duy trì thói quen sống xanh một cách tự nhiên và thú vị. Thay vì những lời kêu gọi khô khan, Eco Tracker biến hành trình bảo vệ môi trường thành một trò chơi nhập vai thực tế đầy lôi cuốn, nơi mỗi hành động nhỏ của bạn đều được ghi nhận, tôn vinh và xếp hạng.

Ứng dụng được xây dựng trên nền tảng **Python 3.13+** và **Django 5+** (sử dụng cấu trúc Django 6.0.6 hiện đại), kết hợp cùng hệ thống giao diện UI/UX cao cấp hỗ trợ chế độ Light/Dark Mode mượt mà bằng CSS thuần (Vanilla CSS) và JavaScript tối ưu.

---

## 🌟 Ý tưởng sản phẩm (Product Concept)
Trong thời đại biến đổi khí hậu và ô nhiễm môi trường đang trở thành vấn đề toàn cầu, việc chuyển đổi sang lối sống bền vững là vô cùng cấp thiết. Tuy nhiên, nhiều người gặp khó khăn trong việc duy trì thói quen xanh do thiếu động lực và thiếu công cụ theo dõi tiến trình.

Eco Tracker giải quyết bài toán này bằng cách:
1. **Trực quan hóa tác động (Visualize Impact):** Mỗi hành động như tái chế, trồng cây, tiết kiệm điện hay đi phương tiện công cộng đều được tích lũy tiến độ rõ ràng.
2. **Trò chơi hóa trải nghiệm (Gamify Experience):** Người dùng thực hiện nhiệm vụ hàng ngày/hàng tuần, tích lũy điểm kinh nghiệm để thăng cấp (10 cấp độ từ *Tân binh* đến *Hộ vệ Trái đất*), nhận huy hiệu danh giá, và thi đua trên bảng xếp hạng toàn cầu/bạn bè.
3. **Thúc đẩy tương tác xã hội (Socialized Green Living):** Tích hợp bản tin xã hội (Eco Feed) để chia sẻ hành động sống xanh kèm hình ảnh thực tế, thả tim, bình luận và tạo nhóm thách đấu thi đua cùng bạn bè.
4. **Phần thưởng tinh thần độc đáo (Premium Rewards):** Điểm thưởng kiếm được dùng để mở khóa các khung viền Avatar phát sáng và viền động độc quyền trong Cửa hàng Khung (Avatar Frame Shop).

---

## 🤖 Đột phá Công nghệ AI & Xử lý Bất đồng bộ
*   **Trợ lý kiểm duyệt Google Gemini 2.5 Flash:** Khi người dùng tải lên hình ảnh hoạt động sống xanh kèm mô tả, hệ thống gửi ảnh trực tiếp đến mô hình ngôn ngữ lớn **Gemini** để phân tích thời gian thực. AI sẽ tự động thẩm định tính xác thực của bức ảnh, phân loại chính xác vào danh mục tương ứng (Tái chế, Trồng cây, Tiết kiệm năng lượng...) và từ chối các bài đăng không hợp lệ (không liên quan đến môi trường) kèm lý do rõ ràng.
*   **Kiến trúc Celery + Redis Task Queue:** Toàn bộ quá trình gọi API Gemini và xử lý ảnh nặng được chuyển xuống hàng đợi tác vụ ngầm chạy bất đồng bộ qua Celery, giúp trang web phản hồi tức thì mà không bị nghẽn mạng hay tải trang chậm.
*   **AI Eco Coach cá nhân hóa:** Trợ lý ảo AI phân tích dữ liệu hoạt động trong tuần của người dùng, tự động nhận diện danh mục sống xanh nào người dùng đang thiếu sót và đưa ra các lời khuyên thiết thực để cân bằng lối sống thân thiện với môi trường.

---

## 📌 Mục lục
1. [Tính Năng Cốt Lõi](#-tính-năng-cốt-lõi)
2. [Cơ Cấu Tổ Chức Thư Mục](#-cơ-cấu-tổ-chức-thư-mục)
3. [Kiến Trúc & Tối Ưu Hiệu Năng](#-kiến-trúc--tối-ưu-hiệu-năng)
4. [Hướng Dẫn Cài Đặt Cục Bộ (Local Setup)](#-hướng-dẫn-cài-đặt-cục-bộ-local-setup)
5. [Sử Dụng AWS S3 & Công Cụ Tích Hợp](#-sử-dụng-aws-s3--công-cụ-tích-hợp)
6. [Triển Khai Sản Xuất (Production)](#-triển-khai-sản-xuất-production)
7. [Định Hướng Phát Triển Tính Năng Nâng Cao](#-định-hướng-phát-triển-tính-năng-nâng-cao)

---

## 🌟 Tính Năng Cốt Lõi

*   **Tải lên hoạt động xanh & Xác minh AI:** Google Gemini 2.5 Flash chạy ngầm thông qua hàng đợi Celery tự động phân tích ảnh và mô tả để phân loại danh mục, tính điểm và phê duyệt tự động.
*   **Hệ thống Cấp độ & Điểm số (Eco Level):** 10 cấp bậc sống xanh từ *Eco Novice (Mầm xanh)* đến *Earth Guardian (Hộ vệ Trái đất)*. Mỗi cấp bậc đi kèm quyền lợi và đặc quyền riêng biệt.
*   **Nhiệm vụ Hàng ngày & Hàng tuần:** Người dùng nhận ngẫu nhiên các thử thách bảo vệ môi trường mỗi ngày/tuần. Có cơ chế thưởng "Perfect Day" khi hoàn thành toàn bộ nhiệm vụ trong ngày và cơ chế giới hạn điểm tối đa hàng ngày (Daily Points Cap) để chống gian lận.
*   **Cộng đồng & Mạng xã hội (Eco Feed):** Người dùng có thể chia sẻ hành động lên bảng tin chung, thả tim (like) và bình luận (comment) các hoạt động của nhau với 4 trạng thái phản ứng xanh (💚, ♻️, 🌳, ⚡).
*   **Nhóm & Nhiệm vụ Đồng đội (Co-op Quests):** Thành lập nhóm tối đa 10 người, gửi lời mời kết bạn và tham gia nhóm, cùng nhau làm nhiệm vụ tuần để nhận điểm thưởng co-op đồng đội.
*   **Cửa hàng Khung ảnh đại diện (Frame Shop):** Dùng điểm tích lũy được từ nhiệm vụ để mua các khung viền Avatar phát sáng, viền động mang phong cách gaming cao cấp.
*   **Trắc nghiệm Kiến thức Môi trường (Trivia Quiz):** Gồm 3 câu hỏi trắc nghiệm ngẫu nhiên mỗi ngày giúp nâng cao nhận thức bảo vệ môi trường, trả lời đúng được cộng thêm điểm.
*   **Trợ lý AI Eco Coach:** Tự động theo dõi thói quen hành vi trong tuần của người dùng, phân tích xem danh mục nào còn thiếu và đưa ra lời khuyên cá nhân hóa bằng tiếng Anh hoặc tiếng Việt.

---

## 📁 Cơ Cấu Tổ Chức Thư Mục

Dự án được cấu trúc rõ ràng theo chuẩn Django:

```text
eco_tracker/
├── config/                  # Thư mục cấu hình cốt lõi của Django (settings, urls, celery app)
├── tracker/                 # Ứng dụng nghiệp vụ chính
│   ├── ai_utils.py          # Module tích hợp Gemini 2.5 Flash
│   ├── models.py            # Khai báo cấu trúc bảng cơ sở dữ liệu (20 bảng liên kết)
│   ├── tasks.py             # Khai báo các tác vụ ngầm chạy bất đồng bộ của Celery
│   ├── utils.py             # Tầng nghiệp vụ xử lý tính điểm, cấp độ, chuỗi ngày streak
│   ├── storage_backends.py  # Cấu hình Boto3 xử lý upload lên AWS S3
│   └── views.py             # Logic xử lý HTTP Requests (Caching, select_related...)
├── static/                  # File tĩnh (CSS thuần, JavaScript cơ bản)
├── templates/               # Giao diện HTML Render
├── media/                   # Lưu trữ file tải lên cục bộ (Nếu không cấu hình S3)
└── db.sqlite3               # Cơ sở dữ liệu SQLite cục bộ phục vụ phát triển
```

---

## ⚡ Kiến Trúc & Tối Ưu Hiệu Năng

Hệ thống được thiết kế để mở rộng dễ dàng, phục vụ lượng dữ liệu lớn nhờ 3 chiến lược:

1. **Redis Caching & Invalidation (Leaderboards):** Thay vì quét toàn bộ dữ liệu, xếp hạng người dùng được lưu trong Cache 10 phút. Bất cứ khi nào người dùng ghi điểm mới, hệ thống chủ động kích hoạt thao tác "xóa cache cũ" để dữ liệu bảng xếp hạng được update lập tức (Realtime) với tốc độ phản hồi cực nhanh.
2. **Khắc Phục Vấn Đề N+1 Queries:** Tối ưu hóa triệt để ORM Query Bằng `.select_related()` và `.prefetch_related()` giúp giảm tải lượng Request thừa xuống Database tại trang Bản tin (Feed) và Bảng Xếp Hạng.
3. **Tác Vụ Nền Bất Đồng Bộ (Celery + Redis Task Queue):** Các cuộc gọi tới Gemini AI xử lý ảnh có thể làm chậm hệ thống 2-5 giây. Celery sẽ đẩy công việc này xuống Background (chạy ngầm). Người dùng ngay lập tức thấy bài đăng được đưa vào trạng thái chờ duyệt `⏱️ Đang phân tích...` mà không bị gián đoạn trải nghiệm.

---

## 🛠️ Hướng Dẫn Cài Đặt Cục Bộ (Local Setup)

### 1. Chuẩn bị thư mục & Môi trường
```bash
git clone https://github.com/minhhuy2409/ECOTRACKER.git
cd ECOTRACKER
python3 -m venv .venv
source .venv/bin/activate
pip install django pillow httpx celery redis boto3 django-storages psycopg2-binary
```

### 2. Thiết lập Redis & Biến môi trường
Khởi động Redis Server trên máy của bạn (nếu dùng macOS có thể dùng Homebrew):
```bash
brew services start redis
# Hoặc gõ lệnh: redis-server
```
Khởi tạo các biến môi trường cấu hình API:
```bash
export GEMINI_API_KEY="your-google-gemini-api-key"
export USE_MOCK_AI="False"
export REDIS_URL="redis://127.0.0.1:6379/0"
```

### 3. Tạo cấu trúc bảng & Khởi chạy hệ thống
Di chuyển dữ liệu Database và bắt đầu Server:
```bash
python eco_tracker/manage.py migrate

# Mở 1 terminal mới và kích hoạt Celery Worker
celery -A config worker --loglevel=info -D eco_tracker

# Ở terminal gốc, bật Server chạy Web
python eco_tracker/manage.py runserver
```
👉 Truy cập ứng dụng tại địa chỉ: `http://127.0.0.1:8000/`

---

## ☁️ Sử Dụng AWS S3 & Công Cụ Tích Hợp

Dự án hỗ trợ mạnh mẽ việc đồng bộ hóa dữ liệu lên Cloud bằng **AWS S3** thông qua `boto3`. 
Để kích hoạt tính năng này ở Local, bạn chỉ cần gán các Credentials như tham số vào dòng lệnh chạy server như sau:

```bash
USE_S3=True AWS_ACCESS_KEY_ID=AKIA... AWS_SECRET_ACCESS_KEY=... AWS_STORAGE_BUCKET_NAME=my-bucket AWS_S3_REGION_NAME=ap-southeast-1 python eco_tracker/manage.py runserver
```
*Lưu ý: Bạn cũng có thể thiết lập các biến này trong file cấu hình shell `.bashrc` / `.zshrc` hoặc file `.env`.*

### 📜 Công Cụ Hỗ Trợ: `upload_to_s3.py`
Trong bộ source code cung cấp sẵn công cụ Terminal tự động tải file tùy ý lên hệ thống AWS S3 của bạn. File này bắt lỗi xác thực và định dạng ảnh rất an toàn.
**Cách sử dụng:**
```bash
python upload_to_s3.py /duong/dan/den/anh.jpg ten-bucket-cua-ban
```

---

## 🚀 Triển Khai Sản Xuất (Production)

Để đưa ứng dụng lên hệ thống máy chủ thật như AWS EC2, bạn cần thay đổi một số mô hình nền tảng:
*   **Database (RDS):** Thay thế DB cục bộ SQLite sang cơ sở dữ liệu mạnh mẽ như PostgreSQL. Sửa trực tiếp thông số tại biến `DATABASES` trong `settings.py`.
*   **Web Server / Proxy:** Khuyên dùng hệ thống Gunicorn chạy app, bảo bọc phía trước bằng Nginx.
*   **Worker:** Dùng phần mềm quản trị tiến trình như **Supervisor** để đảm bảo Background Task của Celery luôn chạy 24/7 không bị sập.
*   **Storage (S3):** Giữ `USE_S3=True` để đẩy toàn bộ Static & Media file lên AWS S3 nhằm tiết kiệm băng thông và ổ cứng Server ảo.

---

## 📈 Định Hướng Phát Triển Tính Năng Nâng Cao

1. **Trình tính toán Khí thải CO2 Thực tế (Carbon Footprint Calculator):** Quy đổi điểm số thành lượng khí thải CO2 giảm thiểu được trên thực tế dựa trên danh mục hành động. (VD: Đi xe đạp 5km -> Giảm 750g CO2).
2. **Cơ chế Chống gian lận hình ảnh nâng cao (AI Anti-Fraud Verification):** Sử dụng thuật toán dHash/pHash để so sánh mã định danh ảnh, chặn đăng ảnh tải từ internet hoặc ảnh lặp lại trong hệ thống.
3. **Bản đồ Sống xanh Tương tác (Eco Interactive Map):** Tích hợp bản đồ OpenStreetMap để ghim địa điểm làm sự kiện bảo vệ môi trường, hoặc vẽ bản đồ nhiệt mức độ tích cực sống xanh tại các khu phố.

---

*Cảm ơn bạn đã quan tâm. Hãy cùng kiến tạo một tương lai xanh bền vững với **Eco Tracker**! 🌍🌱*
