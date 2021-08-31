import mysql.connector

#conexion
def conectar():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="proyecto_notas",
        port="3306"
    )

    cursor = db.cursor(buffered=True)

    return [db,cursor]