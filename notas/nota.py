import datetime
import notas.conexion as conexion

connect = conexion.conectar()
db = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self, usuarioID=None, titulo=None, descripcion=None):
        self.usuarioID = usuarioID
        self.titulo = titulo
        self.descripcion = descripcion

    def crearNota(self):
        date = datetime.datetime.now()
        sql = "INSERT INTO notas values (null,%s,%s,%s,%s)"
        nota = (self.usuarioID, self.titulo, self.descripcion, date)
        try:
            cursor.execute(sql,nota)
            db.commit()
            rs = [cursor.rowcount, self]
        except:
            rs = [0, self]

        return rs

    def getNotas(self):
        sql = "SELECT * FROM notas where usuario_id = {} order by id;".format(self.usuarioID)
 
        cursor.execute(sql)
        db.commit()
        rs = cursor.fetchall()

        return rs

    @staticmethod
    def getNota(id,idUsuario):
        sql = "SELECT * FROM notas where id = {} and usuario_id = {};".format(id,idUsuario)

        try:
            cursor.execute(sql)
            db.commit()
            rs = cursor.fetchone()
            return [cursor.rowcount, rs]
        except:
            rs = 0

        return rs


    @staticmethod
    def deleteNota(id):
        sql = "DELETE FROM notas where id = {};".format(id)

        try:
            cursor.execute(sql)
            db.commit()
            rs = cursor.rowcount
        except:
            rs = 0

        return rs

    @staticmethod
    def updateNota(id,titulo,descripcion):
        sql = "UPDATE notas set titulo = '{}', descripcion = '{}' where id = {};".format(titulo,descripcion,id)
        try:
            cursor.execute(sql)
            db.commit()
            rs = cursor.rowcount
        except:
            rs = 0

        return rs

    def getUsuarioID(self):
        return self.usuarioID

    def getTitulo(self):
        return self.titulo

    def getDescripcion(self):
        return self.descripcion
    