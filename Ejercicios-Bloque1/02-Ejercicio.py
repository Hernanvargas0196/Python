"""
Mostrar todos los numeros pares del 1 al 100
"""
print('Numeros Pares del 1 al 100'.center(50,'*'))
for i in range(1, 100+1):
    if i%2 == 0:
        print(i)