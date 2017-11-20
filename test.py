from os import path

import json

notebook = dict(brand='Lenovo', size=13, ram='8gb')

with open('les6_1.json', 'a') as file:
    json.dump(notebook, file)

dumped = json.dumps(notebook)
print(dumped)