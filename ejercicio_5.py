"""
5. Que dado tres números ingresados por el usuario nos devuelva el promedio.
"""

def promedio(numero1, numero2, numero3):
    return (numero1 + numero2 + numero3)/3


num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

print(f'El promedio es: {promedio(num1, num2, num3)}')

