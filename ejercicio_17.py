"""
17. Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay. 
"""

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


cantidad_primos = 0

for i in range(0,101):
    if es_primo(i):
        print(i)
        cantidad_primos += 1

print(f'Hay {cantidad_primos} primos')

