import usuarios.conexion as conn
import datetime
import hashlib

connect = conn.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(NULL, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            resultado = [cursor.rowcount, self]
        except:
            resultado = [0, self]

        return resultado

    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

         #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql,usuario)
        result = cursor.fetchone()

        return result