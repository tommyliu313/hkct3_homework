from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)
url = "https://tvb.com"
driver.get(url)
print(url.title)

search = driver.find_element(By.NAME, 'tvb-search')
search.send_keys("jade")
search.send_keys(Keys.RETURN)



time.sleep(3)
driver.close()