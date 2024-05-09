"""
En esta segunda parte deberán utilizar estructuras de control condicionales (y en lo posible y dado el 
caso funciones)  para escribir programas que lleven a cabo lo siguiente: 
6. Que pida al usuario una palabra y la muestre por pantalla 10 veces
"""

def imprimir_diez_veces(palabra):
    for i in range(10):
        print(palabra)


imprimir_diez_veces(input('Ingrese una palabra: '))