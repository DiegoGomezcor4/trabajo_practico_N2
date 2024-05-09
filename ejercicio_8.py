"""
Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""

def es_mayor_de_edad(edad):
    if edad >= 18:
        print("Es mayor de edad!!")
    else:
        print("No es mayor de edad")
    

es_mayor_de_edad(int(input("Ingrese su edad: ")))


    