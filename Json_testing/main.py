import json

with open('users.json') as f:
    users = json.load(f)
    for user in users:
        print(user['name'])
    users.append({'name':'Roman','email':'roman@gmail.com'})

with open('users.json', 'w') as f:
    json.dump(users,f, indent=4, ensure_ascii=False)
