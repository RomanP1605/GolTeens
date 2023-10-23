from bs4 import BeautifulSoup

html_file = open('main.html', encoding='UTF-8')
html_data = html_file.read()
print(html_data)
data_soup = BeautifulSoup(html_data)
html_lists = data_soup.findAll('a')
print(html_lists)
for item in html_lists:
    print(f"Тема {item.string},посилання: {item.attrs['href']}")
