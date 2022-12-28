"""
Mostrar numeros impares entre el rango que da el usuario
"""
min = int(input('Digita el rango minimo: '))
max = int(input('Digita el rango maximo: '))

print(f'Numeros impares entre {min} y {max}'.center(50,'*'))
for i in range(min, max+1):
    if i%2 != 0:
        print(i)