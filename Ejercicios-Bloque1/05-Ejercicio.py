"""
Crear programa que muestre todos los numeros entre el rango que digite el usuario
"""
min = int(input('Digita el rango minimo: '))
max = int(input('Digita el rango maximo: '))

for i in range(min, max+1):
    print(i)

print(f"Fin del Programa".center(50,'*'))