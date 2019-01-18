# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade
    
    def saudacao(self):
        return f'Olá, eu sou o {self.nome} <{self.email}> e tenho {self.idade} anos.'

    def completou_ano(self):
        self.idade += 1

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.saldo_conta = 0
    
    def depositar(self, valor):
        self.saldo_conta += valor

# Exemplo Usuario
rij = Usuario('Rijelly', 'rijelly@gmail.com', 30)
print(rij.nome)
print(rij.saudacao())

rij.completou_ano()

print(rij.idade)

# Exemplo Cliente 
it = Cliente('Italo', 30)
print(it.saldo_conta)

it.depositar(50)
print(it.saldo_conta)

it.depositar(50)
print(it.saldo_conta)
