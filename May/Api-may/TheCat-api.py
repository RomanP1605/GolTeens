import requests
from pprint import pprint

r=requests.get(f"https://api.thecatapi.com/v1/breeds")

data=r.json()
pprint(data)
for i in range(5):
    cats=data[i]['alt_names']
    print(f"Породи собак: {cats}")