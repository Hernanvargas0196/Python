"""
Crear un programa que nos pida un numero indefinidamente hasta que nos pida el 111
"""
numero = int(input('Digite el numero: '))

while numero != 111:
    print(f'Numero digitado: {numero}')
    numero = int(input('Digite el numero: '))

print('Fin del programa'.center(50,'*'))