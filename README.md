# How to deploy your project at your local and AWS
- pull code to Nginx folder web
- cd folder code
- python -m venv venv
- source venv/bin/activate
- pip install django
- pip install Pillow
- pip install celery
- python manage.py migrate
- python manage.py runserver

Enjoy the code

# Eco Tracker - Nền tảng Mạng xã hội Gamification vì Môi trường

**Eco Tracker** là một ứng dụng web mạng xã hội đột phá kết hợp giữa bảo vệ môi trường và **Gamification (Trò chơi hóa)**, hướng tới mục tiêu thúc đẩy cộng đồng xây dựng và duy trì thói quen sống xanh một cách tự nhiên và thú vị. Thay vì những lời kêu gọi khô khan, Eco Tracker biến hành trình bảo vệ môi trường thành một trò chơi nhập vai thực tế đầy lôi cuốn, nơi mỗi hành động nhỏ của bạn đều được ghi nhận, tôn vinh và xếp hạng.

Ứng dụng được xây dựng trên nền tảng **Python 3.13+** và **Django 5+** (sử dụng cấu trúc Django 6.0.6 hiện đại), kết hợp cùng hệ thống giao diện UI/UX cao cấp hỗ trợ chế độ Light/Dark Mode mượt mà bằng CSS thuần (Vanilla CSS) và JavaScript tối ưu.

### 🌟 Ý tưởng sản phẩm (Product Concept)
Trong thời đại biến đổi khí hậu và ô nhiễm môi trường đang trở thành vấn đề toàn cầu, việc chuyển đổi sang lối sống bền vững là vô cùng cấp thiết. Tuy nhiên, nhiều người gặp khó khăn trong việc duy trì thói quen xanh do thiếu động lực và thiếu công cụ theo dõi tiến trình.

Eco Tracker giải quyết bài toán này bằng cách:
1. **Trực quan hóa tác động (Visualize Impact):** Mỗi hành động như tái chế, trồng cây, tiết kiệm điện hay đi phương tiện công cộng đều được tích lũy tiến độ rõ ràng.
2. **Trò chơi hóa trải nghiệm (Gamify Experience):** Người dùng thực hiện nhiệm vụ hàng ngày/hàng tuần, tích lũy điểm kinh nghiệm để thăng cấp (10 cấp độ từ *Tân binh* đến *Hộ vệ Trái đất*), nhận huy hiệu danh giá, và thi đua trên bảng xếp hạng toàn cầu/bạn bè.
3. **Thúc đẩy tương tác xã hội (Socialized Green Living):** Tích hợp bản tin xã hội (Eco Feed) để chia sẻ hành động sống xanh kèm hình ảnh thực tế, thả tim, bình luận và tạo nhóm thách đấu thi đua cùng bạn bè.
4. **Phần thưởng tinh thần độc đáo (Premium Rewards):** Điểm thưởng kiếm được dùng để mở khóa các khung viền Avatar phát sáng và viền động độc quyền trong Cửa hàng Khung (Avatar Frame Shop).

### 🤖 Đột phá Công nghệ AI & Xử lý Bất đồng bộ
*   **Trợ lý kiểm duyệt Google Gemini 2.5 Flash:** Khi người dùng tải lên hình ảnh hoạt động sống xanh kèm mô tả, hệ thống gửi ảnh trực tiếp đến mô hình ngôn ngữ lớn **Gemini** để phân tích thời gian thực. AI sẽ tự động thẩm định tính xác thực của bức ảnh, phân loại chính xác vào danh mục tương ứng (Tái chế, Trồng cây, Tiết kiệm năng lượng...) và từ chối các bài đăng không hợp lệ (không liên quan đến môi trường) kèm lý do rõ ràng.
*   **Kiến trúc Celery + Redis Task Queue:** Toàn bộ quá trình gọi API Gemini và xử lý ảnh nặng được chuyển xuống hàng đợi tác vụ ngầm chạy bất đồng bộ qua Celery, giúp trang web phản hồi tức thì mà không bị nghẽn mạng hay tải trang chậm.
*   **AI Eco Coach cá nhân hóa:** Trợ lý ảo AI phân tích dữ liệu hoạt động trong tuần của người dùng, tự động nhận diện danh mục sống xanh nào người dùng đang thiếu sót và đưa ra các lời khuyên thiết thực để cân bằng lối sống thân thiện với môi trường.


---

## 📌 Mục lục
1. [Tính Năng Cốt Lõi](#-tính-năng-cốt-lõi)
2. [Cơ Cấu Tổ Chức Thư Mục](#-cơ-cấu-tổ-chức-thư-mục)
3. [Kiến Trúc Hệ Thống & Cơ Sở Dữ Liệu](#-kiến-trúc-hệ-thống--cơ-sở-dữ-liệu)
4. [Tối Ưu Hóa Hiệu Năng & Quy Mô (Đã Triển Khai)](#-tối-ưu-hóa-hiệu-năng--quy-mô-đã-triển-khai)
5. [Hướng Dẫn Cài Đặt Cục Bộ (Local Setup)](#-hướng-dẫn-cài-đặt-cục-bộ-local-setup)
6. [Hướng Dẫn Triển Khai Sản Xuất (AWS EC2 + S3 + RDS PostgreSQL)](#-hướng-dẫn-triển-khai-sản-xuất-aws-ec2--s3--rds-postgresql)
7. [Định Hướng Phát Triển Tính Năng Nâng Cao](#-định-hướng-phát-triển-tính-năng-nâng-cao)

---

## 🌟 Tính Năng Cốt Lõi

*   **Tải lên hoạt động xanh & Xác minh AI:** Người dùng tải lên các hoạt động thân thiện với môi trường (như tái chế, đi xe đạp, trồng cây). Google Gemini 2.5 Flash chạy ngầm thông qua hàng đợi Celery tự động phân tích ảnh và mô tả để phân loại danh mục, tính điểm và phê duyệt tự động.
*   **Hệ thống Cấp độ & Điểm số (Eco Level):** 10 cấp bậc sống xanh từ *Eco Novice (Mầm xanh)* đến *Earth Guardian (Hộ vệ Trái đất)*. Mỗi cấp bậc đi kèm quyền lợi và đặc quyền riêng biệt.
*   **Nhiệm vụ Hàng ngày & Hàng tuần:** Người dùng nhận ngẫu nhiên các thử thách bảo vệ môi trường mỗi ngày/tuần. Có cơ chế thưởng "Perfect Day" khi hoàn thành toàn bộ nhiệm vụ trong ngày và cơ chế giới hạn điểm tối đa hàng ngày (Daily Points Cap) để chống gian lận.
*   **Cộng đồng & Mạng xã hội (Eco Feed):** Người dùng có thể chia sẻ hành động lên bảng tin chung, thả tim (like) và bình luận (comment) các hoạt động của nhau với 4 trạng thái phản ứng xanh (💚, ♻️, 🌳, ⚡).
*   **Nhóm & Nhiệm vụ Đồng đội (Co-op Quests):** Thành lập nhóm tối đa 10 người, gửi lời mời kết bạn và tham gia nhóm, cùng nhau làm nhiệm vụ tuần để nhận điểm thưởng co-op đồng đội.
*   **Cửa hàng Khung ảnh đại diện (Frame Shop):** Dùng điểm tích lũy được từ nhiệm vụ để mua các khung viền Avatar phát sáng, viền động mang phong cách gaming cao cấp.
*   **Trắc nghiệm Kiến thức Môi trường (Trivia Quiz):** Gồm 3 câu hỏi trắc nghiệm ngẫu nhiên mỗi ngày giúp nâng cao nhận thức bảo vệ môi trường, trả lời đúng được cộng thêm điểm.
*   **Trợ lý AI Eco Coach:** Tự động theo dõi thói quen hành vi trong tuần của người dùng, phân tích xem danh mục nào còn thiếu và đưa ra lời khuyên cá nhân hóa bằng tiếng Anh hoặc tiếng Việt.
*   **Ngôn ngữ mặc định:** Toàn bộ ứng dụng sử dụng Tiếng Anh làm ngôn ngữ chuẩn hóa và thống nhất cho cả giao diện người dùng lẫn trợ lý AI Coach.

---

## 📁 Cơ Cấu Tổ Chức Thư Mục

Dự án được cấu trúc rõ ràng theo chuẩn Django sản xuất:

```
eco_tracker/
│
├── config/                  # Thư mục cấu hình cốt lõi của Django
│   ├── celery.py            # Cấu hình khởi tạo Celery App
│   ├── settings.py          # Cấu hình Database, Middleware, Caches, Celery, Gemini API
│   └── urls.py              # Định tuyến URLs cấp hệ thống
│
├── tracker/                 # Ứng dụng nghiệp vụ chính
│   ├── admin.py             # Trang quản trị admin tùy biến bộ lọc, hành động
│   ├── ai_utils.py          # Module tích hợp Gemini 2.5 Flash và bộ kiểm duyệt từ khóa dự phòng
│   ├── context_processors.py# Bộ cung cấp biến ngữ cảnh toàn cục (Từ điển hiển thị, trạng thái)
│   ├── forms.py             # Các biểu mẫu Django Forms (Đăng ký, upload ảnh, vv.)
│   ├── models.py            # Khai báo cấu trúc bảng cơ sở dữ liệu (20 bảng liên kết)
│   ├── signals.py           # Bộ bắt tín hiệu tự động (ví dụ: tạo Profile mặc định)
│   ├── tasks.py             # Khai báo các tác vụ ngầm chạy bất đồng bộ của Celery
│   ├── tests.py             # Bộ kiểm thử tự động (Unit test views, auth, set-language)
│   ├── urls.py              # Định tuyến URLs cấp ứng dụng
│   ├── utils.py             # Tầng nghiệp vụ xử lý tính điểm, cấp độ, chuỗi ngày streak, nhiệm vụ nhóm
│   └── views.py             # Logic xử lý HTTP Requests (Leaderboard cache, Feed select_related, vv.)
│
├── static/                  # File tĩnh phục vụ phía client
│   └── css/
│       └── style.css        # Hệ thống thiết kế CSS thuần hỗ trợ Light/Dark Mode
│
├── templates/               # Giao diện HTML Render
│   ├── base.html            # Khung xương layout chung (Sidebar, Topbar, Alerts)
│   ├── components/          # Các phần giao diện tái sử dụng (Sidebar, Topbar, Thẻ tiến trình)
│   └── pages/               # Các trang giao diện chức năng chính (Dashboard, Feed, Shop, vv.)
│
├── media/                   # Lưu trữ file tải lên cục bộ (Ảnh đại diện, Ảnh hoạt động)
└── db.sqlite3               # Cơ sở dữ liệu SQLite cục bộ phục vụ phát triển
```

---

## 📊 Kiến Trúc Hệ Thống & Cơ Sở Dữ Liệu

Hệ thống quản lý 20 bảng cơ sở dữ liệu quan hệ chặt chẽ, tối ưu hóa hiệu năng truy vấn bằng cách đánh chỉ mục (`db_index=True`) trên các cột thường xuyên lọc và sắp xếp (như `created_at`, `is_completed`, `start_date`, `ai_status`).

```mermaid
erDiagram
    User ||--o| UserProfile : "có hồ sơ"
    User ||--o{ EcoAction : "tải lên hành động"
    User ||--o{ Friendship : "gửi/nhận kết bạn"
    User ||--o{ GroupMember : "là thành viên nhóm"
    User ||--o{ UserDailyMission : "nhận nhiệm vụ ngày"
    User ||--o{ UserWeeklyMission : "nhận nhiệm vụ tuần"
    User ||--o{ UserBadge : "đạt huy hiệu"
    User ||--o{ EcoActionLike : "thích bài viết"
    User ||--o{ UserAvatarFrame : "sở hữu khung avatar"
    User ||--o{ UserTriviaSubmission : "làm trắc nghiệm"
    User ||--o{ AICoachSuggestion : "nhận lời khuyên AI"
 
    EcoGroup ||--o{ GroupMember : "chứa"
    EcoGroup ||--o| GroupWeeklyQuest : "có nhiệm vụ tuần nhóm"
    EcoGroup ||--o{ GroupInvite : "gửi lời mời"
    
    EcoAction ||--o{ UserDailyMission : "hoàn thành nhiệm vụ"
    EcoAction ||--o{ EcoActionLike : "có lượt thích"
 
    DailyMission ||--o{ UserDailyMission : "chỉ định"
    WeeklyMission ||--o{ UserWeeklyMission : "chỉ định"
    Badge ||--o{ UserBadge : "đại diện"
    AvatarFrame ||--o{ UserAvatarFrame : "đại diện"
    GroupWeeklyQuest ||--o{ UserGroupQuestReward : "chia thưởng co-op"
```

---

## ⚡ Tối Ưu Hóa Hiệu Năng & Quy Mô (Đã Triển Khai)

Nhằm đảm bảo khả năng mở rộng quy mô hệ thống phục vụ hàng triệu người dùng, dự án đã triển khai 3 chiến lược tối ưu hóa hiệu năng thực tế sau:

### 1. Redis Caching & Invalidation (Leaderboards)
*   **Vấn đề:** Trang Bảng xếp hạng (Leaderboard) thực hiện nhiều phép tính gom nhóm (`Sum`, `Count`) trên lượng dữ liệu rất lớn mỗi lần tải trang.
*   **Giải pháp:** Tích hợp bộ đệm cache. Kết quả sắp xếp xếp hạng được lưu trữ vào cache mặc định (`leaderboard_data`) trong thời gian 10 phút.
*   **Cơ chế Invalidation (Xóa cache thông minh):** Thay vì đợi hết hạn 10 phút, bất cứ khi nào người dùng có thay đổi về điểm số (hoàn thành nhiệm vụ ngày/tuần, nộp đáp án trắc nghiệm Trivia chính xác, hoặc nhóm đạt mục tiêu Co-op Quest), hệ thống sẽ chủ động xóa khóa cache `leaderboard_data`. Điều này đảm bảo tốc độ phản hồi tức thì ($O(1)$) và cập nhật dữ liệu bảng xếp hạng chính xác theo thời gian thực.

### 2. Giải Quyết Vấn Đề N+1 Queries Trong Django ORM
*   **Bảng xếp hạng (Leaderboard View):** 
    *   Sử dụng `.select_related("profile__active_frame")` trên câu lệnh truy vấn chính.
Nhằm đảm bảo khả năng mở rộng quy mô, dự án đã triển khai:

### 1. Redis Caching & Invalidation
*   **Giải pháp:** Tích hợp bộ đệm cache cho bảng xếp hạng (Leaderboard) giúp tốc độ phản hồi tức thì và cập nhật dữ liệu chính xác theo thời gian thực nhờ cơ chế xóa cache thông minh.

### 2. Giải Quyết Vấn Đề N+1 Queries
*   **Bảng xếp hạng (Leaderboard View):** Sử dụng `.select_related("profile__active_frame")`.

### 3. Tác Vụ Nền Bất Đồng Bộ (Celery + Redis Task Queue)
*   **Vấn đề:** Cuộc gọi API Google Gemini AI để phân tích hình ảnh và tính toán cộng điểm mất từ 2-5 giây, khiến người dùng phải chờ đợi lâu ở trang tải lên.
*   **Giải pháp:** Đưa tác vụ AI phân tích ảnh vào hàng đợi bất đồng bộ ngầm của Celery. Luồng hoạt động:
    1.  Khi người dùng tải ảnh lên, bài viết được lưu ngay lập tức với trạng thái `ai_status="pending"` (Đang chờ duyệt). Trình duyệt của người dùng lập tức được chuyển hướng về trang chủ.
    2.  Hệ thống kích hoạt Celery Task chạy ngầm `classify_eco_action_task.delay(eco_action.id)`. Task này tự động gọi API Gemini AI, phân loại danh mục, tính điểm, cập nhật chuỗi ngày hoạt động (streak) và tự động ghi nhận tiến độ nhiệm vụ.
    3.  Tại giao diện Bảng tin (Feed) và Hồ sơ cá nhân (My Progress), hệ thống hiển thị nhãn trạng thái động: `⏱️ Đang phân tích...` (nếu đang chờ), `❌ Bị từ chối` kèm lý do chi tiết từ AI (nếu ảnh không hợp lệ), hoặc hiển thị danh mục xanh đã được duyệt thành công.
*   **Chế độ dự phòng cục bộ (Eager Mode):** Trong môi trường cục bộ nếu không có Redis/Worker chạy sẵn, cấu hình `CELERY_TASK_ALWAYS_EAGER = True` tự động kích hoạt giúp tác vụ chạy đồng bộ bình thường mà không gây lỗi ứng dụng.

---

## 🛠️ Hướng Dẫn Cài Đặt Cục Bộ (Local Setup)

Thực hiện các bước sau để thiết lập môi trường phát triển trên máy tính của bạn:

### 1. Chuẩn bị thư mục dự án
Truy cập vào thư mục chứa mã nguồn:
```bash
cd "/Users/minhhuy/Downloads/EcoTracker-main 3"
```

### 2. Thiết lập Môi trường ảo (Virtual Environment)
Khởi tạo và kích hoạt môi trường ảo Python:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Cài đặt các thư viện phụ thuộc (Dependencies)
Cài đặt Django cùng các thư viện phục vụ Caching, AI và Celery:
```bash
pip install django pillow httpx celery redis
```

### 4. Khởi động Redis Server (Làm bộ đệm Cache và Broker cho Celery)
Đảm bảo bạn đã cài đặt Redis trên máy (ví dụ: thông qua Homebrew trên macOS):
```bash
brew services start redis
# Hoặc khởi chạy trực tiếp:
redis-server
```

### 5. Cấu hình biến môi trường
Thiết lập API Key của Google Gemini và chế độ chạy ngầm.
```bash
export GEMINI_API_KEY="your-google-gemini-api-key"
export USE_MOCK_AI="False"
export REDIS_URL="redis://127.0.0.1:6379/0"
```

### 6. Tạo cấu trúc bảng & Khởi tạo dữ liệu
Chạy di chuyển dữ liệu (Migrations):
```bash
python eco_tracker/manage.py migrate
```

### 7. Chạy thử nghiệm tự động (Unit Tests)
Chạy bộ test suite để kiểm tra tính đúng đắn của toàn bộ nghiệp vụ:
```bash
python eco_tracker/manage.py test tracker
```

### 8. Khởi chạy Celery Worker (để xử lý tác vụ AI bất đồng bộ)
Mở một Terminal mới, kích hoạt môi trường ảo và chạy lệnh:
```bash
celery -A config worker --loglevel=info
```

### 9. Khởi chạy Django Server
Mở Terminal chính và khởi động máy chủ phát triển:
```bash
python eco_tracker/manage.py runserver
```
Truy cập vào ứng dụng tại địa chỉ: `http://127.0.0.1:8000/`



---

## 🚀 Hướng Dẫn Triển Khai Sản Xuất (AWS EC2 + S3 + RDS PostgreSQL)

Để đưa ứng dụng Eco Tracker lên môi trường sản xuất thực tế trên AWS:

### 1. Cấu hình Cơ sở dữ liệu PostgreSQL (AWS RDS)
Cài đặt thư viện kết nối PostgreSQL:
```bash
pip install psycopg2-binary
```
Cập nhật cấu hình database trong [config/settings.py](file:///Users/minhhuy/Downloads/EcoTracker-main%203/eco_tracker/config/settings.py):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecotracker_db',
        'USER': 'postgres_admin',
        'PASSWORD': 'secure_rds_password',
        'HOST': 'ecotracker-rds.xxxxx.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
```

### 2. Lưu trữ tệp tĩnh & hình ảnh tải lên (AWS S3)
Cài đặt thư viện lưu trữ đám mây:
```bash
pip install django-storages boto3
```
Kích hoạt AWS S3 trong settings.py:
```python
INSTALLED_APPS += ['storages']

AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACCESS_KEY'
AWS_SECRET_ACCESS_KEY = 'YOUR_AWS_SECRET_ACCESS_KEY'
AWS_STORAGE_BUCKET_NAME = 'ecotracker-production-bucket'
AWS_S3_REGION_NAME = 'us-east-1'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'
```

### 3. Khởi chạy hàng đợi Celery trên AWS
Cài đặt và cấu hình Supervisor để duy trì tiến trình chạy ngầm Celery Worker ổn định trên Ubuntu:
Tạo file `/etc/supervisor/conf.d/ecotracker-celery.conf`:
```ini
[program:ecotracker-celery]
command=/home/ubuntu/EcoTracker/.venv/bin/celery -A config worker -l info
directory=/home/ubuntu/EcoTracker/eco_tracker
user=ubuntu
numprocs=1
stdout_logfile=/home/ubuntu/EcoTracker/logs/celery.log
stderr_logfile=/home/ubuntu/EcoTracker/logs/celery_err.log
autostart=true
autorestart=true
startsecs=10
```

---

## 📈 Định Hướng Phát Triển Tính Năng Nâng Cao

Dưới đây là các đề xuất mở rộng tính năng sản phẩm nâng cao trong tương lai:

#### A. Trình tính toán Khí thải CO2 Thực tế (Carbon Footprint Calculator)
*   **Mô tả:** Quy đổi điểm số thành lượng khí thải CO2 giảm thiểu được trên thực tế dựa trên danh mục hành động.
*   **Ví dụ:** Đi xe đạp 5km thay vì đi xe máy -> Giảm thiểu **750g CO2**; gom 1kg nhựa tái chế -> Giảm thiểu **1.5kg CO2** phát thải vào môi trường.

#### B. Cơ chế Chống gian lận hình ảnh nâng cao (AI Anti-Fraud Verification)
*   **Mô tả:** Ngăn chặn người dùng tải lên ảnh tải từ internet hoặc lặp lại ảnh cũ để cày điểm.
*   **Giải pháp:** Sử dụng thuật toán dHash/pHash để so sánh mã định danh ảnh, chặn đăng ảnh trùng lặp trong hệ thống cơ sở dữ liệu.

#### C. Bản đồ Sống xanh Tương tác (Eco Interactive Map)
*   **Mô tả:** Tích hợp bản đồ OpenStreetMap để ghim địa điểm sự kiện bảo vệ môi trường, dọn rác khu phố hoặc vẽ bản đồ nhiệt mức độ tích cực sống xanh của các nhóm bạn bè gần vị trí địa lý của bạn.

---

Chúc bạn có những trải nghiệm phát triển tuyệt vời cùng **Eco Tracker** để chung tay kiến tạo một tương lai xanh bền vững! 🌍🌱
