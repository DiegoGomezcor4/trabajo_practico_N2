"""
9. Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso 
en que ambos números son iguales.
"""

def es_menor(numer1, numer2):
    if numero1 < numero2:
        print(f"El número {numero1} es menor: ")
    elif numero2 < numero1:
        print(f"El número {numero2} es menor: ")
    else:
        print("Son iguales")


numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

es_menor(numero1, numero2)