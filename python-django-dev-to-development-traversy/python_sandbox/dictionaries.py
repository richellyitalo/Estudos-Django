# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# pessoa = {
#     'primeiro_nome': 'Rije',
#     'ultimo_nome': 'Talo'
# }
pessoa = dict(primeiro_nome='Rije', ultimo_nome='Italo')
print(pessoa)

# retornando key
print(pessoa['primeiro_nome'])
print(pessoa.get('ultimo_nome'))

pessoa['telefone'] = '84999-9999'
print(pessoa)

# Clonando dict
pessoa2 = pessoa.copy()

print(pessoa.keys())
print(pessoa.items())

# Removendo atributos
pessoa.pop('ultimo_nome')
del(pessoa['primeiro_nome'])

# Limpando
pessoa.clear()

print(pessoa)

print(pessoa2)

# Lista de dict
pessoas = [
    dict(nome='Jão'),
    {'nome':'Jão'}
]

print(pessoas)

# Acessando chave de um item da lista
print(pessoas[0]['nome'])