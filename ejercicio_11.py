"""
11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se 
encuentran en dicha frase.
"""

def contar_vocales(texto):
    texto = texto.lower()
    vocales = 'aeiouáéíóú'
    cantidad_vocales = 0
    for letra in texto:
        if letra in vocales:
            cantidad_vocales += 1
    return cantidad_vocales

frase = input('Por favor ingrese una frase: ')
print(f'La cantidad de vocales en la frase es: {contar_vocales(frase)}')

