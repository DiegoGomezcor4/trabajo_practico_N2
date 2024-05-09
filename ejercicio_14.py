"""
14.  Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son 
múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos 
ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 
no es bisiesto.
"""

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False 

anio = int(input("Por favor ingrese un año para comprobar si es bisiesto: "))
es_bisiesto(anio)

if es_bisiesto(anio):
    print(anio, 'es año bisiesto')
else:
    print(anio, 'no es un año bisiesto')