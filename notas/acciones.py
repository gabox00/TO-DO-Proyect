import notas.nota as notaModel

class Acciones:

    def crearNota(self,usuario):
        print("\n--------------     Crear Nota     --------------\n")
        titulo = input("Ingrese un titulo para la nota: ")
        descripcion = input("Ingrese una descripcion para la nota: ")
        nota = notaModel.Nota(usuario[0],titulo,descripcion)
        flagCrear = nota.crearNota()

        if(flagCrear[0] >= 1):
            print("\n--------------     Nota correctamente creada     --------------")
        elif(flagCrear[1] == 0):
            print("!!!!!!!!!!!!!     Ocurrio un error al crear la nota     !!!!!!!!!!!!!")

        self.menuNotas(usuario)

    def verNotas(self,usuario,arg=None):
        print("\n--------------     Todas mis notas     --------------\n")
        nota = notaModel.Nota(usuario[0],None,None)
        rs = nota.getNotas()

        if(rs):
            for el in rs:
                print(f"({el[0]}) {el[2]}")

        if(arg == None):
            notaID = input("Escoga una nota a desplegar o caracter para continuar: ")

            if(not notaID.isnumeric()):
                self.menuNotas(usuario)

            rs2 = nota.getNota(notaID,usuario[0])

            if(rs2[0] != 0):
                print(f"Fecha: {rs2[1][4]}\nTitulo: {rs2[1][2]}\nDescripcion: {rs2[1][3]}")

            self.menuNotas(usuario)
            

    def eliminarNota(self,usuario):
        self.verNotas(usuario,'delete')
        notaID = int(input("Escoga una nota a eliminar: "))
        
        nota = notaModel.Nota.deleteNota(notaID)
        
        if(nota >= 1):
            print('\n--------------     La nota se ha eliminado con exito    --------------')
        elif(notaID == 0):
            print('\n--------------     Error al eliminar la nota    --------------')

        self.menuNotas(usuario)

    def modificarNota(self,usuario):
        self.verNotas(usuario,'update')  
        notaID = int(input("\nEscoga una nota para modificar: "))
        notaTitulo = input("Tiulo: ")
        notaDescripcion = input("Descripcion: ")
        
        notaModel.Nota.updateNota(notaID,notaTitulo,notaDescripcion)
        
        self.menuNotas(usuario)

    def menuNotas(self,usuario):
        print(""" 
        Crear nota (1)
        Mostrar mis notas (2)
        Eliminar nota (3)
        Modificar nota (4)
        Logout (5)
        """)
        arg = int(input("Eliga una opcion: "))

        if(arg == 1):
            self.crearNota(usuario)
        elif(arg == 2):
            self.verNotas(usuario)
        elif(arg == 3):
            self.eliminarNota(usuario)
        elif(arg == 4):
            self.modificarNota(usuario)
        elif(arg == 5):
            exit()

