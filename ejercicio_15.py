"""
15. Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe 
validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, 
informarle que no se puede procesar el dato
"""

def es_vocal(letra):
    vocales = 'aeiouáéíóú'
    letra = letra.lower()
    if letra in vocales:
        return True
    else:
        return False


while True:
        letra_ingresada = input('Ingrese una letra: ')
        if len(letra_ingresada) != 1:
            print('Por favor, ingrese solo un carácter.')
            continue
        if es_vocal(letra_ingresada):
            print('Es vocal.')
        else:
            print('No es vocal.')

        break    

