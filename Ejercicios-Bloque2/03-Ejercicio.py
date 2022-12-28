"""
Programa que compruebe si una variable esta vacia y si lo esta, rellenarla con texto en minusculas y mostrarlo en mayuscula.
"""
var = "   "
if len(var.strip()) <= 0:
    var = 'hola mundo!'

print(var.upper())