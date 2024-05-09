"""
13. Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos 
A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un 
nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el 
resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla 
el grupo que le corresponde.
"""

def grupo(nombre, sexo):
    nombre = nombre.lower()
    sexo = sexo.lower()
    if sexo == 'mujer' and nombre[0] < 'm':
        return 'Grupo A'
    elif sexo == 'hombre' and nombre[0] > 'n':
        return 'Grupo A'
    else:
        return 'Grupo B'

nombre = input('Por favor ingrese su nombre: ')
sexo = input('Ingrese su sexo: ')

print(f'Usted pertenece a el: {grupo(nombre, sexo)}')