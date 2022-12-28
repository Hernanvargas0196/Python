"""
Representar una tabla con informacion dentro de un diccionario.

"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "call of duty","PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSASINS", "CRASH", "PRINCE OF PERSIA"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA","PES 21", "MOTOS"]
    }
]

for categoria in tabla:
    print(f"{categoria['categoria']}".center(50,'-'))
    for juego in categoria['juegos']:
        print(juego)