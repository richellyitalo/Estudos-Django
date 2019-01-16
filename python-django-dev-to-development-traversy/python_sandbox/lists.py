# A List is a collection which is ordered and changeable. Allows duplicate members.

# Criação de listas
# numbers = [1, 2, 3, 4]
# com constructor
numbers = list((1, 2, 3, 4))

# print(type(numbers))
# print(numbers)

frutas = ['Maçã', 'Mamão', 'Banana', 'Laranja']

print(frutas[1])

# tamanho
print(len(frutas))

# adicionando
frutas.append('Uva')
print(frutas)

# adicionando em uma posição
frutas.insert(1, 'Jaca')
print(frutas)

# removendo
frutas.pop(0)
print(frutas)

# reverte a lista
frutas.reverse()
print(frutas)

# associação direta pelo index
frutas[0] = 'Pêra'

# ordena
frutas.sort(reverse=True)
print(frutas)