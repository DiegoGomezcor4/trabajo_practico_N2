"""
Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro 
mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día 
ingresado no es ninguno de esos, imprimir otro mensaje.
"""

def comprobar_dia(dia):
    dia = dia.lower()
    match dia:
        case 'lunes':
            print('Hay que ir a trabajar!!')
        case 'viernes':
            print('falta poco para el finde')
        case ('sabado'):
            print('Que bien, es fin de semana!')
        case ('domingo'):
            print('Que bien, es fin de semana!')
        case _ :
            print('El dia ingresado no tiene comentarios')


dia = input('Por favor, ingrese un dia de la semana: ')
comprobar_dia(dia)


