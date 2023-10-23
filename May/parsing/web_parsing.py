import requests
from bs4 import BeautifulSoup

wikipedia_response=requests.get("https://uk.wikipedia.org/wiki/Python")
print(wikipedia_response.status_code)
wikipedia_page_content = wikipedia_response.content
wikipedia_soup = BeautifulSoup(wikipedia_page_content)
wikipedia_titles = wikipedia_soup.findAll('span', attrs={"class": "mw-headline"})
for title in wikipedia_titles:
    print(title.string)
