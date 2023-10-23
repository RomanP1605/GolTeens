import requests
from bs4 import BeautifulSoup
course_response = requests.get("https://rozetka.com.ua/ua/notebooks/c80004/sort=expensive")
course_page_content = course_response.text
course_soup = BeautifulSoup(course_page_content)

res = course_soup.findAll('span', class_='goods-tile__title')
res_prices = course_soup.findAll('span', class_='goods-tile__price-value')
# release_date = course_soup.find()
for re in res:
    for res_price in res_prices:
        print(re.text, res_price.text)