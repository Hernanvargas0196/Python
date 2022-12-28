"""
Crear programa que pide la nota de 15 alumnos y muestra la cantidad de alumnos reprobados y aprobados
"""

cont = 0

for i in range(1,16):
    nota = float(input(f'Digite la nota del alumno {i}: '))
    if nota < 3:
        cont += 1

aprobados = 15 - cont
print(f'El total de alumnos aprobados fue de: {aprobados} y reprobados: {cont}')
    
