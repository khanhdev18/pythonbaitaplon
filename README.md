#  Crawl Dữ Liệu Bất Động Sản từ alonhadat.com.vn

Đây là một script **Python** tự động thu thập dữ liệu bất động sản từ website [alonhadat.com.vn](https://alonhadat.com.vn).  
Script được xây dựng nhằm **thu thập thông tin nhà đất** một cách **nhanh chóng, tự động, chính xác** để phục vụ cho các mục đích như nghiên cứu thị trường, phân tích giá bất động sản, thống kê, hoặc lưu trữ dữ liệu cá nhân.

---

##  Chức năng chính

✅ Truy cập website bất động sản alonhadat.com.vn.  
✅ Chọn **tỉnh/thành phố**  
✅ Chọn **loại nhà đất** 
✅ Tự động phân trang, thu thập dữ liệu từ **tất cả các trang**.  
✅ Lấy các thông tin chi tiết: **Tiêu đề, Mô tả, Địa chỉ, Diện tích, Giá** của từng bài đăng.  
✅ Lưu dữ liệu thành file **Excel (.xlsx)** dễ dàng xử lý sau này.  
✅ Tự động chạy vào **06:00 sáng** mỗi ngày mà không cần thao tác thủ công.

---

## 🚀 Hướng dẫn sử dụng chi tiết

### 1️⃣ Yêu cầu hệ thống

Để chạy được script này, máy tính của bạn cần đảm bảo các yêu cầu sau:

- Python phiên bản **3.7 hoặc cao hơn**.
- Trình duyệt **Google Chrome** đã cài sẵn trên máy.
- **ChromeDriver** tương thích với phiên bản Chrome (nếu Chrome đang ở phiên bản 122 thì ChromeDriver cũng cần bản 122).

👉 Kiểm tra phiên bản Chrome bằng cách truy cập `chrome://version/` trên trình duyệt.

---

### 2️⃣ Cài đặt các thư viện Python cần thiết

Chạy lệnh dưới đây trong **Terminal (Linux/Mac)** hoặc **CMD (Windows)**:

```bash
pip install selenium beautifulsoup4 pandas schedule openpyxl
