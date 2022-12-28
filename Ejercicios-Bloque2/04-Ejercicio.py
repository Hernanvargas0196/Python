"""
Crear una funcion que compruebe el tipo de dato y lo devuelva.
"""

def comprobarTipo(var):
    print(f'La variable {var} es de tipo {type(var)} ')

lista = []
entero = 26
cadena = 'Hola mundo'
booleano = True

comprobarTipo(entero)