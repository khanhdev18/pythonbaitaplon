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

    df = pd.DataFrame(all_data)
    filename = f"alonhadat_da_nang_{time.strftime('%Y%m%d')}.xlsx"
    df.to_excel(filename, index=False)
    print(f'Đã lưu dữ liệu vào {filename}')

# ----------------
# Đặt lịch chạy 18:01 hằng ngày
schedule.every().day.at("06:00").do(crawl_data)

print("Đang chờ đến 06:00 để chạy...")
while True:
    schedule.run_pending()
    time.sleep(1)  # kiểm tra mỗi giây
