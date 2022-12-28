"""
Escribir un programa que muestre los cuadrados de los 60 primeros numeros naturales
usar while y for
"""
cont = 1
print('Usando ciclo While'.center(50,'*'))
while cont <= 60:
    print (f'{cont}^2 = {cont * cont}')
    cont += 1
print('Usando ciclo For'.center(50,'*'))
for cont in range(1,60):
    print (f'{cont}^2 = {cont * cont}')
    cont += 1