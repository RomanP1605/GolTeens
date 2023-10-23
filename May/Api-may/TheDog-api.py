import requests
from pprint import pprint

r=requests.get(f"https://api.thedogapi.com/v1/breeds")

data=r.json()
sled_name = data[8]['name']
sled_group = data[8]['breed_group']
sled_height = data[8]['height']['metric']
sled_age = data[8]['life_span']
sled_temp = data[8]['temperament']
sled_weight = data[8]['weight']['metric']
pprint(data)

print(f"Назва породи: {sled_name}\n"
      f"Група: {sled_group}\n"
      f"Розмір(в сантиметрах): {sled_height}\n"
      f"Вага(в кілограмах): {sled_weight}"
      f"Живе: {sled_age}\n"
      f"Опис породи: {sled_temp}"
      )
