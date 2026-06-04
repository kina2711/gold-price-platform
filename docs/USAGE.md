# 🚀 Cẩm nang Triển khai (End-to-End Setup Guide)

Dự án này sử dụng kiến trúc **Data Engineering (ELT / Medallion Architecture)**. Dưới đây là hướng dẫn chi tiết từ A-Z để bạn thiết lập tự động hóa hoàn toàn trên GitHub.

---

## Bước 1: Khởi tạo và Đẩy lên GitHub (Push to GitHub)

Nếu bạn chưa tạo kho lưu trữ (repository) trên GitHub, hãy tạo một Repository mới (ví dụ: `gold-price-pipeline`).
Mở Terminal tại thư mục dự án trên máy của bạn và chạy lần lượt các lệnh sau:

```bash
git init
git add .
git commit -m "update code"
git branch -M main
git remote add origin https://github.com/kina2711/gold-price-pipeline.git
git push -u origin main
```

## Bước 2: Cấp quyền cho GitHub Actions ghi dữ liệu

Để GitHub Actions có thể tự động commit cập nhật file giá vàng (`data/`) và `README.md`, bạn cần cấp quyền cho nó:

1. Vào repository trên GitHub của bạn.
2. Chuyển đến tab **Settings** > **Actions** > **General**.
3. Cuộn xuống phần **Workflow permissions**.
4. Chọn **Read and write permissions**.
5. Nhấn **Save**.

---

## Bước 3: Thiết lập Discord Webhook (Tuỳ chọn)

1. Mở ứng dụng Discord, vào Server của bạn.
2. Nhấn vào biểu tượng ⚙️ (Edit Channel) của kênh bạn muốn nhận thông báo.
3. Chọn **Integrations** > **Webhooks** > **New Webhook**.
4. Đặt tên (ví dụ: `Gold Price Bot`) và nhấn **Copy Webhook URL**.
5. Quay lại repository trên GitHub, vào **Settings** > **Secrets and variables** > **Actions**.
6. Nhấn **New repository secret**.
7. Name: `DISCORD_WEBHOOK_URL`
8. Secret: Dán URL bạn vừa copy ở bước 4 vào đây.
9. Nhấn **Add secret**.

---

## Bước 4: Test thử luồng chạy tự động (End-to-End Test)

Ngay khi bạn push code lên nhánh `main`, luồng GitHub Actions sẽ tự động được kích hoạt. Tuy nhiên, bạn hoàn toàn có thể chạy test thủ công:

1. Trên GitHub, chuyển sang tab **Actions**.
2. Ở cột bên trái, chọn workflow có tên **daily-update**.
3. Nhấn vào nút **Run workflow** (ở bên phải) > Chọn nhánh `main` > Nhấn nút màu xanh **Run workflow**.
4. Đợi khoảng 30s-1 phút để pipeline chạy (Extract -> Transform/Load -> Notify).
5. **Kết quả:** 
   - Kiểm tra kênh Discord của bạn, sẽ có một tin nhắn báo cáo giá vàng mới nhất.
   - Trở lại trang chủ repository, bạn sẽ thấy `README.md` đã được update.

---

## Phụ lục: Chạy Pipeline ở máy Local

Nếu bạn muốn test ở máy tính cá nhân hoặc phát triển tính năng mới, cài đặt [uv](https://docs.astral.sh/uv/) và chạy:

```bash
# Cài đặt môi trường
uv sync

# 1. Chạy Extract data (Scrape)
uv run pipeline update

# 2. Render UI Dashboard ra file README.md
uv run pipeline render-readme

# 3. Test gửi Discord
uv run pipeline notify-discord
```
