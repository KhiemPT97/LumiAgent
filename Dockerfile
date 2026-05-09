# Sử dụng Python image chính thức
FROM python:3.11-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép file requirements trước để tận dụng Docker cache
COPY requirements.txt .

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Lệnh để chạy Bot
CMD ["python", "-m", "bot.main"]
