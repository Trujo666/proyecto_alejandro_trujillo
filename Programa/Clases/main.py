from login import login
from alumnos import Alumno
from libros import Libro
from prestamos import Prestamo
from cursos import Curso
from materias import Materia

class Main:
    def menu_principal(self):
        return (f"\n === Menú Principal ==="
                "\n------------------------"
                "\n1. Gestionar alumnos."
                "\n2. Gestionar préstamos."
                "\n3. Mostrar datos."
                "\n4. Copia de seguridad."
                "\n5. Salir."
                "\n------------------------\n")

    def opciones_menu_principal(self):
        while True:
            print(self.menu_principal())
            opcion = self.pedir_opcion("Escoja una opción del menú principal: ")
            match opcion:
                case 1:
                    self.gestionar_alumnos()
                case 2:
                    self.gestionar_prestamos()
                case 3:
                    self.mostrar_datos()
                case 4:
                    self.copia_seguridad()
                case 5:
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opción inválida, escoja una de las opciones indicadas en el menú.")

    def pedir_opcion(self, mensaje: str) -> int:
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Debe introducir un número válido.")

    def submenu_gestionar_alumnos(self):
        return ("\n === Menú Principal ===                          "
                "\n------------------------                         "
                "\n1. Gestionar alumnos.                            "
                "\n           └- - - - - - - - - - - - - - - - - - -"
                "\n            1. Crear alumno.                     "
                "\n            2. Modificar alumno.                 "
                "\n            3. Mostrar información de alumno.    "
                "\n            4. Mostrar todos los alumnos.        "
                "\n            5. Volver al menú principal.         "
                "\n            - - - - - - - - - - - - - - - - - - -")

    def gestionar_alumnos(self):
        while True:
            print(self.submenu_gestionar_alumnos())

            opcion = self.pedir_opcion("Escoja una opción: ")

            match opcion:
                case 1:
                    self.crear_alumno()
                case 2:
                    nie = input("Ingrese NIE del alumno a modificar: ").strip().upper()
                    alumno = Alumno.buscar_por_nie(nie)
                    if alumno:
                        self.modificar_alumno(alumno)
                    else:
                        print("Alumno no encontrado.")
                case 3:
                    nie = input("Ingrese NIE: ")
                    alumno = Alumno.buscar_por_nie(nie)
                    if alumno:
                        print(alumno)
                    else:
                        print("Alumno no encontrado.")
                case 4:
                    alumnos = Alumno.cargar_alumnos()
                    if not alumnos:
                        print("No hay alumnos registrados.")
                    else:
                        for alumno in alumnos:
                            print(alumno)
                case 5:
                    break
                case _:
                    print("Opción inválida.")

    def menu_crear_alumno(self):
        return ("\n === Menú Principal ==="
                "\n------------------------                "
                "\n1. Gestionar alumnos.                   "
                "\n           └- - - - - - - - - - - - - - "
                "\n            1. Crear alumno.            "
                "\n            - - - - - - - - - - - - - - "
                "\n                                      \n")

    def crear_alumno(self):
        print(self.menu_crear_alumno())

        print("------------------------")
        nie = self.pedir_nie()
        nombre = self.pedir_nombre()
        apellidos = self.pedir_apellidos()
        bilingue = self.pedir_bilingue()
        tramo = self.pedir_tramo()
        print("------------------------\n")

        nuevo = Alumno(nie, nombre, apellidos, bilingue, tramo)
        nuevo.guardar_en_archivo()
        print("Alumno creado con éxito.")

    def pedir_nie(self) -> str:
        while True:
            nie: str = ""
            nie = input("\nIntroduzca el NIE del alumno: ").strip().upper()
            if self.validar_nie(nie):
                return nie
            print("Por favor, introduzca un NIE válido.")

    def validar_nie(self, nie) -> bool:
        if len(nie) != 9:
            print("El NIE debe tener exactamente 9 caracteres.")
            return False
        elif Alumno.buscar_por_nie(nie):
            print("Ya existe un alumno con ese NIE.")
            return False
        else:
            return True

    def pedir_nombre(self) -> str:
        while True:
            nombre: str = ""
            nombre = input("Introduzca el nombre del alumno: ").strip()
            if self.validar_nombre(nombre):
                return nombre
            print("El nombre no puede estar vacío.")

    def validar_nombre(self, nombre: str) -> bool:
        return bool(nombre)

    def pedir_apellidos(self) -> str:
        while True:
            apellidos: str = ""
            apellidos = input("Introduzca los apellidos del alumno: ").strip()
            if self.validar_apellidos(apellidos):
                return apellidos
            print("Los apellidos no pueden estar vacíos.")

    def validar_apellidos(self, apellidos: str) -> bool:
        return bool(apellidos)

    def pedir_bilingue(self) -> bool:
        while True:
            bilingue_aux: str = ""
            bilingue_aux = input("¿Es bilingüe? (S/N): ").strip().upper()
            if self.validar_bilingue(bilingue_aux):
                return bilingue_aux == "S"
            print("Por favor, introduzca 'S' o 'N'.")

    def validar_bilingue(self, valor: str) -> bool:
        return valor in ["S", "N"]

    def pedir_tramo(self) -> str:
        while True:
            tramo: str = ""
            tramo = input("Indique el tramo becado del alumno (0, I o II): ").strip().upper()
            if self.validar_tramo(tramo):
                return tramo
            print("El tramo debe ser '0', 'I' o 'II'.")

    def validar_tramo(self, tramo: str) -> bool:
        return tramo in ["0", "I", "II"]

    def menu_modificar_alumno(self) -> str:
        return (f"\n === Menú Principal ===                           "
                "\n------------------------                           "
                "\n1. Gestionar alumnos.                              "
                "\n           └- - - - - - - - - - - - - - - - - - - -"
                "\n            1. Crear alumno.                       "
                "\n            2. Modificar alumno.                   "
                "\n                       └- - - - - - - - - - - - - -"
                "\n                        1. Modificar NIE.          "
                "\n                        2. Modificar nombre.       "
                "\n                        3. Modificar apellidos.    "
                "\n                        4. Modificar bilingüe.     "
                "\n                        5. Modificar tramo.        "
                "\n                        6. Volver al menú anterior."
                "\n                        - - - - - - - - - - - - - -")

    def modificar_alumno(self, alumno) -> None:
        nie_original = alumno.nie
        while True:
            print(self.menu_modificar_alumno())
            opcion = self.pedir_opcion("Escoja una opción de modificación: ")
            match opcion:
                case 1:
                    nuevo_nie = self.pedir_nuevo_nie(alumno.nie)
                    alumno.modificar_datos("nie", nuevo_nie)
                    print("¡El NIE ha sido modificado!")
                case 2:
                    nuevo_nombre = self.pedir_nombre()
                    alumno.modificar_datos("nombre", nuevo_nombre)
                    print("Nombre modificado con éxito.")
                case 3:
                    nuevos_apellidos = self.pedir_apellidos()
                    alumno.modificar_datos("apellidos", nuevos_apellidos)
                    print("Apellidos modificados con éxito.")
                case 4:
                    bilingue = self.pedir_bilingue()
                    alumno.modificar_datos("bilingue", bilingue)
                    print("Valor de bilingüe actualizado.")
                case 5:
                    tramo = self.pedir_tramo()
                    alumno.modificar_datos("tramo", tramo)
                    print("Tramo modificado con éxito.")
                case 6:
                    break
                case _:
                    print("Opción inválida.")

        self.actualizar_alumno_en_archivo(alumno, nie_original)

    def actualizar_alumno_en_archivo(self, alumno_modificado, nie_original):
        alumnos = Alumno.cargar_alumnos()
        with open("../Datos/alumnos.txt", "w", encoding="utf-8") as archivo:
            for alumno in alumnos:
                if alumno.nie == nie_original:
                    archivo.write(alumno_modificado.cambiar_objeto_a_linea() + "\n")
                else:
                    archivo.write(alumno.cambiar_objeto_a_linea() + "\n")
        print("Cambios guardados.")

    def pedir_nuevo_nie(self, nie_actual: str) -> str:
        while True:
            nie: str = ""
            nie = input("Nuevo NIE: ").strip().upper()
            if len(nie) != 9:
                print("El NIE debe tener exactamente 9 caracteres.")
                continue
            if nie != nie_actual and Alumno.buscar_por_nie(nie):
                print("Ya existe un alumno con ese NIE.")
                continue
            return nie

    def submenu_gestionar_prestamos(self):
        return (f"\n === Menú Principal ===                         "
                "\n------------------------                         "
                "\n1. Gestionar alumnos.                            "
                "\n2. Gestionar préstamos.                          "
                "\n           └- - - - - - - - - - - - - - - - - - -"
                "\n             1. Realizar préstamo.               "
                "\n             2. Devolución préstamo.             "
                "\n             3. Salir al menú principal.         "
                "\n            - - - - - - - - - - - - - - - - - - -")

    def gestionar_prestamos(self):
        while True:
            print(self.submenu_gestionar_prestamos())
            opcion = self.pedir_opcion("Escoja una opción: ")
            match opcion:
                case 1:
                    Prestamo.realizar_prestamo()
                case 2:
                    Prestamo.devolver_prestamo()
                case 3:
                    break

    def submenu_mostrar_datos(self):
        return (f"\n === Menú Principal ===                "
                "\n------------------------                "
                "\n1. Gestionar alumnos.                   "
                "\n2. Gestionar préstamos.                 "
                "\n3. Mostrar datos.                       "
                "\n           └- - - - - - - - - - - - - - "
                "\n            1. Busquedas avanzadas.     "
                "\n            2. Mostrar libros.          "
                "\n            3. Mostrar cursos.          "
                "\n            4. Mostrar materias.        "
                "\n            5. Salir al menú principal. "
                "\n            - - - - - - - - - - - - - - ")

    def mostrar_datos(self):
        while True:
            print(self.submenu_mostrar_datos())
            opcion = self.pedir_opcion("Escoja una opción: ")
            match opcion:
                case 1:
                    self.busquedas_avanzadas()
                case 2:
                    libros = Libro.cargar_libros()
                    if not libros:
                        print("No hay libros registrados.")
                    else:
                        print(f"Se han cargado {len(libros)} libros.")
                        for libro in libros:
                            print(libro)
                case 3:
                    cursos = Curso.cargar_cursos()
                    if not cursos:
                        print("No hay cursos registrados.")
                    else:
                        for curso in cursos:
                            print(curso)
                case 4:
                    materias = Materia.cargar_materias()
                    if not materias:
                        print("No hay materias registradas.")
                    else:
                        for materia in materias:
                            print(materia)
                case 5:
                    break

    def submenu_busquedas_avanzadas(self):
        return (f"\n --- Busquedas avanzadas --- "
                "\n 1. Buscar libro.           "
                "\n 2. Buscar curso.           "
                "\n 3. Buscar materia.         "
                "\n 4. Salir al menú principal.  "
                "\n- - - - - - - - - - - - - - - ")

    def busquedas_avanzadas(self):
        while True:
            print(self.submenu_busquedas_avanzadas())
            opcion = self.pedir_opcion("Escoja una opción: ")
            match opcion:
                case 1:
                    isbn: str = ""
                    isbn = input("Ingrese el ISBN del libro: ").strip()
                    libros = Libro.cargar_libros()
                    encontrados = [libro for libro in libros if libro.isbn == isbn]
                    if encontrados:
                        for libro in encontrados:
                            print(libro)
                    else:
                        print("Libro no encontrado.")
                case 2:
                    id_curso: str = ""
                    id_curso = input("Ingrese el ID del curso: ").strip()
                    cursos = Curso.cargar_cursos()
                    encontrados = [curso for curso in cursos if curso.id_curso == id_curso]
                    if encontrados:
                        for curso in encontrados:
                            print(curso)
                    else:
                        print("Curso no encontrado.")
                case 3:
                    id_materia: str = ""
                    id_materia = input("Ingrese el ID de la materia: ").strip()
                    materias = Materia.cargar_materias()
                    encontrados = [materia for materia in materias if m.id_materia == id_materia]
                    if encontrados:
                        for materia in encontrados:
                            print(materia)
                    else:
                        print("Materia no encontrada.")
                case 4:
                    break
                case _:
                    print("Opción inválida.")

    def copia_seguridad(self):
        archivos_txt: list = []
        archivos_txt = [
            ("../Datos/alumnos.txt", "../Copia Seguridad/alumnos.txt"),
            ("../Datos/libros.txt", "../Copia Seguridad/libros.txt"),
            ("../Datos/cursos.txt", "../Copia Seguridad/cursos.txt"),
            ("../Datos/materias.txt", "../Copia Seguridad/materias.txt"),
            ("../Datos/prestamos.txt", "../Copia Seguridad/prestamos.txt"),
            ("../Usuarios/usuarios.txt", "../Copia Seguridad/usuarios.txt")
        ]

        for origen, destino in archivos_txt:
            try:
                with open(origen, "r", encoding="utf-8") as original:
                    contenido = original.read()
                with open(destino, "w", encoding="utf-8") as copia:
                    copia.write(contenido)
                print(f"Copia realizada desde ruta '{origen}' de origen a ruta '{destino}' destino.")
            except FileNotFoundError:
                print(f"No se encontró el archivo {origen}")

        print("Copia de seguridad finalizada.\n")


if __name__ == "__main__":
    login()
    programa = Main()
    programa.opciones_menu_principal()
