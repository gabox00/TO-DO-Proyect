from usuarios import acciones as accionesUsuario
from usuarios import usuario
from notas import acciones as accionesNota
from notas import nota

accionUsuario = accionesUsuario.Acciones()
accionNota = accionesNota.Acciones()

def main():
    print(""" 
    - Registro (1)
    - Login    (2) 
    - Exit     (3)
    """)

    arg = int(input("Que quieres hacer? "))

    if(arg == 1):
        accionUsuario.registroUsuario()
    elif(arg == 2):
        usuario = accionUsuario.loginUsuario()
        if(usuario[1]):
            accionNota.menuNotas(usuario[0])
    elif(arg == 3):
        exit()
    else:
        main()

main()
