"""
16. Que imprima el siguiente patrón: 
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

def imprimir(numero):
    while numero > 0 :
        for i in range(numero, 0, -1):
            print(i, end=" ")
        numero -= 1
        print()

imprimir(5)