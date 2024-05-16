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
            print(i, end=", ")  # end=", " le dice a Python que imprima una coma seguida de un espacio en lugar de ir a la siguiente línea
    print()
    print()


def cuenta_atras(numero):
    while numero >= 0:
        print(numero, end=", ")
        numero -= 1
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


num = input('por favor ingrese un numero entero positivo: ')

if num.isdigit():
    num = int(num)
    if num >= 0:
        print('a. Todos los números impares desde 1 hasta ese número separados por comas: ')
        numeros_impares(num)

        print('b. La cuenta atrás desde ese número hasta cero separados por comas: ')
        cuenta_atras(num)

        print('c. indique si es primo o no: ')
        print('Si es primo') if es_primo(num) else print('No es primo') #operador ternario
        print()

        print('d. su factorial:')
        print(factorial(num))
        print()

else:
    print('El numero tiene que ser entero y positivo')

