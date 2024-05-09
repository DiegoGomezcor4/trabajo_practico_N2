"""
5. Que dado tres números ingresados por el usuario nos devuelva el promedio.
"""

def promedio(numero1, numero2, numero3):
    return (numero1 + numero2 + numero3)/3


numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

print(f'El promedio es: {promedio(numero1, numero2, numero3)}')

