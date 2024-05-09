"""
4. Que dada la base y altura de un triángulo nos calcule su área.
"""

def calculo_area(base, altura):
    area = (base * altura) / 2
    return area

# Prueba:

print(f'El area de un triangulo de base 2 y altura 2 es igual a: {calculo_area(2, 2)}')
print(f'El area de un triangulo de base 4 y altura 4 es igual a: {calculo_area(4, 4)}')
print(f'El area de un triangulo de base 6 y altura 9 es igual a: {calculo_area(6, 9)}')