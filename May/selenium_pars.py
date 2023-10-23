import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()

driver.get('http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
elements = driver.find_elements(By.TAG_NAME, 'span')
for e in elements:
    print(e.text)
time.sleep(15)
driver.close()