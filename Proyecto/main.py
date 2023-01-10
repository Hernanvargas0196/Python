"""
Proyecto Python Mysql:
    -Abrir asistente
    -Login o registro
    -Si elegimos registro, creara usuario en la bbdd
    -Si elegimos login, identifica al usuario y nos preguntara
    -Crear, mostrar, eliminar notas o salir
"""
from usuarios import acciones

print("""
Acciones Disponibles: 
    1 - Registro
    2 - Login
""")
realizar = acciones.Acciones()
accion = int(input("¿Que quieres hacer?: "))

if accion == 1:
    realizar.registro()
elif accion == 2:
    realizar.login()