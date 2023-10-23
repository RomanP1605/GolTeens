from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
element_by_id = driver.find_element(By.ID, "product_description").text
element_by_css = driver.find_element(By.CSS_SELECTOR, "#product_description").text
element_by_xpath = driver.find_element(By.XPATH, "//div[@id='product_description']").text
driver.quit()
print(element_by_id)
print(element_by_css)
print(element_by_xpath)
