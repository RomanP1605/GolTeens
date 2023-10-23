import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()

browser.get('https://jobs.dou.ua/companies/')
element = browser.find_element(By.TAG_NAME, 'body')
elements= element.find_elements(By.TAG_NAME, 'a')
for e in elements:
    print(e.text)
time.sleep(3)
browser.close()