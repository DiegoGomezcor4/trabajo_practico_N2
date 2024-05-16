"""
2. Que  reciba un número entero positivo y una potencia a elevar  y que nos devuelva el 
resultado. 
"""

def calculo_potencia(numero, potencia):
    resultado = numero ** potencia
    return resultado



# prueba de funcionamiento:

print(f'3 elevado a la potencia 2 es igual a: {calculo_potencia(3, 2)}')

print(f'3 elevado a la potencia 3 es igual a: {calculo_potencia(3, 3)}')

print(f'5 elevado a la potencia 5 es igual a: {calculo_potencia(5, 5)}')

# Ingresado por el usuario:
num = int(input('Por favor, ingrese un número entero positivo: '))
pot = int(input('Por favor ingrese una potencia: '))

result = calculo_potencia(num, pot)
print(f'El numro {num}, elevado a la potencia {pot} es igual a: {result}')

