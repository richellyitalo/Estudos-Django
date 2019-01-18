# If/ Else conditions are used to decide to do something based on something being true or false
x = 15
y = 15

# if x > y:
#     print(f'x={x} é maior que y={y}')
# else:
#     print(f'x={x} não é maior que y={y}')

# if x > 10:
#     print('x é maior que 10')
#     if x == 20:
#         print('x é 20')
#     elif x < 15:
#         print('x é menor que 15')
#     else:
#         print('x é menor que 15')


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values



# Logical operators (and, or, not) - Used to combine conditional statements
x = 11
y = 10
# if x == 10 and y == 10:
#     print('x e y são 10')
# if x is not 10:
#     print('x não é 10')

if not(x == 10) and y is 10:
    print('x não é igual a 10 e y é 10')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object
x = 5
lista = [1, 2, 3, 4, 5]

if x  in lista:
    print('x está na lista')
else:
    print('x não está na lista')



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
if x is y:
    print('x é y')

if x is not y:
    print('x não é y')