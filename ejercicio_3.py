"""
3. Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la 
cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca 
la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""

def total_factura_con_iva(cantidad_sin_iva, porcentaje_iva = 21):
    
    total = cantidad_sin_iva + cantidad_sin_iva * (porcentaje_iva / 100)
    return total

# Pruebas:

print(f'El total de la factura es: ${total_factura_con_iva(1000, 21)}')
print(f'El total de la factura es: ${total_factura_con_iva(1000, 10.5)}')
print(f'El total de la factura es: ${total_factura_con_iva(1000)}')

# Ingresado por el usuario:

cantidad = input('Por favor ingrese el monto de la factura sin iva: ')
porcentaje = input('Por favor ingrese el porcentaje de iva: ')

if porcentaje == '':
    resultado = total_factura_con_iva(float(cantidad))
else:
    resultado = total_factura_con_iva(float(cantidad), float(porcentaje))

print(f'El total de la factura con iva es igual a: {resultado}')



