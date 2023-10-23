import json

json_file = open("1.json", 'r')
json_data = json.load(json_file)
for item in json_data:
    print(item['name'])
    print(item['phone'])
    print(item['email'])