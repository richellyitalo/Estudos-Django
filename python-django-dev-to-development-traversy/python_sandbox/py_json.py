# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Amostra de JSON
fooJSON = '{"nome":"Jão", "idade":30, "email":"jao@gmail.com"}'

# Conversão de JSON --> Dict
usuario = json.loads(fooJSON)

print(usuario)
print(usuario['nome'])
print(type(usuario))

carro = {'marca': 'Ford', 'modelo': 'Mustang', 'ano': 1970}

# Conversão de Dict --> JSON
carroJSON = json.dumps(carro)

print(carro)
print(carroJSON)
print(type(carroJSON))
