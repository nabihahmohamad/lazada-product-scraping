import requests
import time
import csv
import os
from bs4 import BeautifulSoup 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime 

# setup the webdriver (using Chrome) 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL of the product page 
url = 'https://www.lazada.com.my/products/karcher-spray-extraction-cleaner-puzzi-81-c-1100-2400-i2589727440-s11596437060.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253A%253Bnid%253A2589727440%253Bsrc%253AlazadaInShopSrp%253Brn%253A172da75f3586ec5f264d852ff965e4ff%253Bregion%253Amy%253Bsku%253A2589727440_MY%253Bprice%253A2599%253Bclient%253Adesktop%253Bsupplier_id%253A100013352%253Bbiz_source%253Ah5_internal%253Bslot%253A29%253Butlog_bucket_id%253A470687%253Basc_category_id%253A10100313%253Bitem_id%253A2589727440%253Bsku_id%253A11596437060%253Bshop_id%253A1232%253BtemplateInfo%253A107880_D_E%2523-1_A3_C%2523&freeshipping=1&fs_ab=2&fuse_fs=&lang=en&location=Selangor&price=2599&priceCompare=skuId%3A11596437060%3Bsource%3Alazada-search-voucher-in-shop%3Bsn%3A172da75f3586ec5f264d852ff965e4ff%3BoriginPrice%3A259900%3BdisplayPrice%3A259900%3BsinglePromotionId%3A900000034244038%3BsingleToolCode%3AshopPromPrice_lzdAscDiscount%3BvoucherPricePlugin%3A0%3Btimestamp%3A1736398366644&ratingscore=&request_id=172da75f3586ec5f264d852ff965e4ff&review=&sale=6&search=1&spm=a2o4k.store_product.list.29&stock=1'

# Set up CSV file path
csv_file = r'C:\Users\User\Documents\Data Analysis Docs\Python\lazada_product_data.csv'

# Define CSV headers 
csv_headers = ['Product Name','Price','Timestamp']

# create a csv file and write headers if not exists 
with open(csv_file, mode = 'w', newline='', encoding='utf-8') as file: 
    writer = csv.writer(file)
    writer.writerow(csv_headers)

# Function to get Product details 
def get_product_details(): 
    driver.get(url)

    try:
        # get Product Name 
        product_name = driver.find_element(By.CLASS_NAME, "pdp-mod-product-badge-title").text.strip()
        # get product Price
        product_price = driver.find_element(By.CLASS_NAME, "pdp-price").text.strip()
        # get current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return product_name, product_price, timestamp
    except Exception as e:
        print(f'Error: {e}')
        return None, None, None 

# scrape and save data every 60 second 
while True:
    product_name, product_price, timestamp = get_product_details()
    if product_name and product_price and timestamp:
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([product_name, product_price, timestamp])

    print(f"Data saved for {timestamp}. Waiting for 60 second")
    # wait for 60 second
    time.sleep(60)

#close the driver
driver.quit()