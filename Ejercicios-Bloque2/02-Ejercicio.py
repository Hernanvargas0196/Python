"""
Programa que añada valores a una lista mientras que la longitud sea menor a 120, luego mostrar la lista.
Usar While y For
"""
lista = []
for i in range(1,121):
    lista.append(i)

for i in lista:
    print(f'Mostrando el elemento: {i}')

print('Usando ciclo While')
contador = 0
lista = []
while contador < 120:
    contador += 1
    lista.append(contador)
    print(f'Mostrando el elemento: {contador}')