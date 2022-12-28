"""
Mostrar todas las tablas de multiplicar del 1 al 10
"""
tabla = 1

for tabla in range(tabla, 11):
    print(f'Tabla del {tabla}'.center(50,'*'))
    for i in range(1, 11):
        print(f'{tabla} * {i} = {tabla * i}')
