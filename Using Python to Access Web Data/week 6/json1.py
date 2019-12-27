import json

data = '''
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
'''

info = json.loads(data)
print("Name:-", info["name"])
print("Hide:-", info["email"]["hide"])
