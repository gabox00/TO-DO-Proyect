import usuarios.usuario as usuarioModel

class Acciones:

    def registroUsuario(self):
        while True:
            print("--- Empezemos con el registro ---")

            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            email = input("Email: ")
            password = input("Password: ")

            usuario = usuarioModel.Usuario(nombre,apellidos,email,password)
            rs = usuario.registro()

            if(rs[0] >= 1):
                print(f"Usuario Correctamente creado, tu email es: {rs[1].email}")
                break
            else:
                print("Intentelo de nuevo")

    def loginUsuario(self):
        while True:
            print("--- Empezemos con el Login ---")

            email = input("Email: ")
            password = input("Password: ")

            usuario = usuarioModel.Usuario("",'',email,password)

            try:
                rs = usuario.login()
                if(rs[3] == email and rs[4] == password):
                    print(f"Welcome {rs[1]} {rs[2]}")
                    return [rs,True]

            except:
                print("Usuario incorrecto")  
                return False   