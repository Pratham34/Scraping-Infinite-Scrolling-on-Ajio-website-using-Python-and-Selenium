# with help of webdriver , we'll run selenium in the driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:\selenium\chromedriver.exe")
driver = webdriver.Chrome(service = s)

url = "https://www.ajio.com/c/830307006"
driver.get(url)
time.sleep(4)

height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break
    height = new_height