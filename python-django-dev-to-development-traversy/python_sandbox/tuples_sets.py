# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# frutas_tuplas = ('Maçã', 'Banana', 'Mamão', 'Maçã')
#frutas_tuplas = tuple(('Maçã', 'Jaca', 'Melão'))

# Criação de tupla com apenas um valor, deve ser informado o vírgula
frutas_tuplas = ('Maçã',)

print(frutas_tuplas[0])

del frutas_tuplas
# print(frutas_tuplas)


# A Set is a collection which is unordered and unindexed. No duplicate members.
frutas_set = {'Maçã', 'Maçã', 'Uva', 'Banana'}

carros_set = {'Ferrari', 'McLaren'}

frutas_set.add('Pedro')

novo_set = frutas_set.union(carros_set)
frutas_set.pop()

print('Uva' in frutas_set)

print(len(novo_set))

print(frutas_set)

del frutas_set
del carros_set