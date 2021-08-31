import datetime
import usuarios.conexion as conexion

connect = conexion.conectar()
db = connect[0]
cursor = connect[1]

class Usuario:
    
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registro(self):
        fecha = datetime.datetime.now()

        sql = "INSERT INTO usuarios VALUES (null,%s,%s,%s,%s,%s)"
        usuario = (self.nombre,self.apellidos,self.email,self.password,fecha)

        try:
            cursor.execute(sql,usuario)
            db.commit()
            rs = [cursor.rowcount, self]
        except:
            rs = [0, self]

        return rs

    def login(self):
        sql = "SELECT * FROM usuarios where email = %s and password = %s;"
        usuario = (self.email,self.password)

        try:
            cursor.execute(sql,usuario)
            db.commit()
            rs = cursor.fetchone()
        except:
            rs = 0
        
        return rs
    
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setEmail(self, email):
        self.email = email

    def setPassword(self, password):
        self.password = password