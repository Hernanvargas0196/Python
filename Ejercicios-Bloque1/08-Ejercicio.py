"""
Crear un programa que permita sacar el % de un numero dado por el usuario
"""
numero = int(input('Digita el numero: '))
porc = int(input('Digita el porcentaje a sacar (%): '))

resultado = (porc * numero)/100

print(f'El {porc}% de {numero} es = {resultado}')