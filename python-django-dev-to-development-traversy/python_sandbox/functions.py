# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
def olaAlguem(nome='Jao'):
    """ 
    Imprime olá alguém.
    """
    print('Olá ' + nome)
# olaAlguem('Rijelly')

def somaNumeros(num1, num2):
    novoValor = num1 + num2
    return novoValor
soma = somaNumeros(2, 3)
print(soma)

def adicionaUmAoNumero(num):
    num += 1
    return num
numero = 5
somado = adicionaUmAoNumero(numero)
print(somado)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functionss
getSoma = lambda num1, num2 : num1 + num2
getSomaValorPadrao = lambda num1, num2=7 : num1 + num2

print(getSomaValorPadrao(5))