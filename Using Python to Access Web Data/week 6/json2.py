import json

data = '''
[
    {
    "name": "Manish",
    "phone": {
        "type": "intl",
        "number": "+12345677890"
    },
    "email": {
        "hide": "yes"
    }
 },
 {
    "name": "Manish",
    "phone": {
        "type": "intl",
        "number": "+12345677890"
    },
    "email": {
        "hide": "yes"
    }
}
]
'''

info = json.loads(data)
for user in info:
    print("Name:-", user["name"])
    print("Hide:-", user["email"]["hide"])
