# 1. Vào website đã chọn.
# Đối với web bất động sản
# 2. Click chọn bất kì Tỉnh/TP(Hà Nội, Đà Nẵng, Hồ Chí Minh, …). Chọn bất kì loại nhà đất(Căn hộ chung cư, nhà, đất, …).
# 3. Bấm tìm kiếm(nếu trang web tin tức không có Button tìm kiếm thì có thể bỏ qua).
# 5. Lấy tất cả dữ liệu của các trang.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import schedule

def crawl_data():
    options = Options()
    options.add_argument("--headless")  # Chạy ẩn
    driver = webdriver.Chrome(options=options)

    base_url = 'https://alonhadat.com.vn/can-ban-nha-ha-noi-t1.htm'
    all_data = []
    page = 1

    # 4. Lấy tất cả dữ liệu(Tiêu đề, Mô tả, Địa chỉ, Diện tích, Giá) hiển thị ở bài viết.
    while True:
        url = f'{base_url}?page={page}'
        print(f'Đang tải trang {page}: {url}')
        driver.get(url)
        time.sleep(2)  # chờ JS load

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        listings = soup.find_all('div', class_='content-item')

        if not listings:
            print('Không còn dữ liệu, dừng lại.')
            break
# 5. Lấy tất cả dữ liệu của các trang.
        for item in listings:
            # Tiêu đề
            title = item.find('div', class_='ct_title')
            title_text = title.get_text(strip=True) if title else ''

            # Mô tả
            description = item.find('div', class_='ct_brief')
            description_text = description.get_text(strip=True) if description else ''

            # Địa chỉ
            address = item.find('div', class_='ct_dis')
            address_text = address.get_text(strip=True) if address else ''

            # Diện tích
            area_div = item.find('div', class_='ct_dt')
            if area_div:
                for tag in area_div.find_all(['label', 'sup']):
                    tag.extract()
                area_text = area_div.get_text(strip=True)
            else:
                area_text = ''

            # Giá
            price_div = item.find('div', class_='ct_price')
            if price_div:
                for tag in price_div.find_all(['label']):
                    tag.extract()
                price_text = price_div.get_text(strip=True)
            else:
                price_text = ''

            all_data.append({
                'Tiêu đề': title_text,
                'Mô tả': description_text,
                'Địa chỉ': address_text,
                'Diện tích': area_text,
                'Giá': price_text
            })

        page += 1
        time.sleep(1)  # nghỉ 1 giây tránh bị chặn

    driver.quit()
# 6. Lưu dữ liệu đã lấy được vào file excel hoặc csv.
    df = pd.DataFrame(all_data)
    filename = f"alonhadat_da_nang_{time.strftime('%Y%m%d')}.xlsx"
    df.to_excel(filename, index=False)
    print(f'Đã lưu dữ liệu vào {filename}')

# 7. Set lịch chạy vào lúc 6h sáng hằng ngày.
# ----------------
# Đặt lịch chạy 18:01 hằng ngày
schedule.every().day.at("06:00").do(crawl_data)

print("Đang chờ đến 06:00 để chạy...")
while True:
    schedule.run_pending()
    time.sleep(1)  # kiểm tra mỗi giây
# 8. Tạo project github chế độ public.
# 9. Viết file README.md hướng dẫn cài đặt cho project github đầy đủ rõ ràng.
# 10. Push(file code, README.md, requirements.txt) lên project và nộp link project github vào classroom.

    
