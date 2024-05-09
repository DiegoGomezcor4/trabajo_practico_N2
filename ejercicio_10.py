"""
10. Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente: 
a. Todos los números impares desde 1 hasta ese número separados por comas. 
b. La cuenta atrás desde ese número hasta cero separados por comas. 
c. Que indique si es primo o no. 
d. Por último, su factorial
"""

def numeros_impares(numero):
    for i in range(1, numero):
        if (i % 2 != 0):
            print(i, end=", ")
    print()
    print()


def cuenta_atras(numero):
    i = numero
    while i >= 0:
        print(i, end=", ")
        i -= 1
    print()
    print()

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero - 1)


numero = int(input('por favor ingrese un numero entero positivo: '))

print('a. Todos los números impares desde 1 hasta ese número separados por comas: ')
numeros_impares(numero)

print('b. La cuenta atrás desde ese número hasta cero separados por comas: ')
cuenta_atras(numero)

print('c. indique si es primo o no: ')
print('es primo') if es_primo(numero) else print('no es primo') #operador ternario
print()

print('su factorial:')
print(factorial(numero))

