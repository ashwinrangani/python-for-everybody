import json

data = '''{
"name" : "Ashwin",
"phone": {
    "type": "intl",
    "number": "646464664"
},
"email": {
    "hide": "yes"
}
}
'''
info = json.loads(data)
print(info)
print('Name', info['name'])
print("Hide", info['email']['hide'])