from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)
url = "https://www.scmp.com/news/hong-kong"
driver.get(url)
search = driver.find_element(by=By.CSS_SELECTOR, value="span[data-qa='ContentHeadline-Headline']").text
search1 = driver.find_element(by=By.CSS_SELECTOR, value="p[data-qa='Component-Component']").text
print(search, search1)
#search.send_keys("hello")
time.sleep(3)
driver.close()

