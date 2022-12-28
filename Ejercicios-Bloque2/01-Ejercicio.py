"""
PRograma que tenga una lista con 8 numeros enteros:
    -Recorrer la lista y mostrarla
    -Ordenarla y mostrarla
    -Mostrar su longitud
    -Buscar un elemento (que el usuario pida por teclado)
"""
#Crear la lista
lista = [1,3,5,4,3,2,6,7]

#Recorrer la lista y mostrarla
print('Recorriendo y mostrando la lista de numeros'.center(50,'*'))
for i in lista:
    print(i)

#Funcion que recorra la lista y devuelva un string
print('Recorriendo y mostrando la lista de numeros por medio de función'.center(50,'*'))

def recorrerLista(lista):
    for i in lista:
        print(str(i))

recorrerLista(lista)

#Ordenarla y mostrarla
print('Ordenando y mostrando la lista de numeros'.center(50,'*'))
lista.sort()
print(lista)

#Mostrar longitud
print('Mostrando longitud de la lista'.center(50,'*'))
print(f'La lista contiene: {len(lista)} caracteres.')

#Buscar elemento
elemento = int(input('Digite el elemento a buscar en la lista: '))
cont = 0
for i in lista:
    if i==elemento:
        cont +=1 

print(f'El elemento {elemento} se encuentra {cont} veces en la lista')

