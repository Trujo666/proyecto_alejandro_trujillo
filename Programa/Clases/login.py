def cargar_usuarios():
    try:
        with open("../Usuarios/usuarios.txt", "r", encoding="utf-8") as archivo:
            return [linea.strip().split(";") for linea in archivo]
    except FileNotFoundError:
        print("Archivo de usuarios no encontrado.")
        exit()


def comparar_datos_usuario(usuario, clave, usuarios):
    return [usuario, clave] in usuarios


def login():
    intentos: int = 0
    intentos = 3

    usuarios = cargar_usuarios()

    while intentos > 0:
        print("----LOGIN----")
        usuario = input("Usuario: ").strip()
        clave = input("Contraseña: ").strip()

        if comparar_datos_usuario(usuario, clave, usuarios):
            print("\nAcceso permitido.")
            return
        else:
            intentos -= 1
            print(f"Datos incorrectos. Intentos restantes: {intentos}")

    print("Has superado el número de intentos. El programa se cerrará.")
    exit()
