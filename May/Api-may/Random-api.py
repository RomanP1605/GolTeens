import requests
from pprint import pprint

r=requests.get(f"https://randomuser.me/api/")
data=r.json()
pprint(data)
phone=data['results'][0]['phone']
email=data['results'][0]['email']
print(f"phone:{phone}")
print(f"email:{email}")