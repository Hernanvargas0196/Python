import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nOK! Vamos a registrarnos en el sistema...")
        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cual son tus apellidos?: ")
        email = input("¿Cual es tu email?: ")
        password = input("¿Cual es tu contraseña?: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("Ups, no te has registrado correctamente")

    def login(self):
        print("\nVale! Identificate en el sistema...")
        
        try:
            email = input("Introduce tu email: ")
            password = input("Contraseña: ")

            usuario = modelo.Usuario("","",email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Login incorrecto, intentalo mas tarde")    

    def proximasAcciones(self, usuario):
        print("""
        Acciones Disponibles:
        -Crear Nota (1)
        -Mostrar Notas (2)
        -Eliminar Nota (3)
        -Salir (4)
        """)

        accion = int(input("¿Que quieres hacer?: "))
        realizar = notas.acciones.Acciones()



        if accion == 1:
            realizar.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == 2:
            realizar.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == 3:
            realizar.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == 4:
            print(f"Ok!, {usuario[1]} hasta pronto.")
            exit()
