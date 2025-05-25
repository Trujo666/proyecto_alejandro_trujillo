from alumnos import Alumno
from libros import Libro
from cursos import Curso


class Prestamo:
    def __init__(self, nie: str, isbn: int, id_curso: int,
                 fecha_prestamo: str, fecha_devolucion: str, estado: str):
        self.nie = nie
        self.isbn = isbn
        self.id_curso = id_curso
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado

    def __str__(self):
        return (f"NIE: {self.nie} | "
                f"ISBN: {self.isbn} | "
                f"Id Curso: {self.id_curso} | "
                f"Fecha de prestamo: {self.fecha_prestamo} | "
                f"Fecha de devolucion: {self.fecha_devolucion} | "
                f"Estado de prestamo: {self.estado}")

    def cambiar_objeto_a_linea(self):
        return (f"{self.nie} | "
                f"{self.isbn} | "
                f"{self.id_curso} | "
                f"{self.fecha_prestamo} | "
                f"{self.fecha_devolucion} | "
                f"{self.estado}")

    @staticmethod
    def crear_desde_linea(linea):
        nie, isbn, id_curso, fecha_prestamo, fecha_devolucion, estado = linea.strip().split("|")
        return Prestamo(nie.strip(), isbn.strip(), id_curso.strip(), fecha_prestamo.strip(), fecha_devolucion.strip(),
                        estado.strip())

    @staticmethod
    def cargar_prestamos(ruta="../Datos/prestamos.txt"):
        prestamos: list = []
        prestamos = []
        try:
            with open(ruta, "r") as fichero:
                for linea in fichero:
                    prestamos.append(Prestamo.crear_desde_linea(linea))
        except FileNotFoundError:
            pass
        return prestamos

    @staticmethod
    def guardar_prestamo(prestamo, ruta="../Datos/prestamos.txt"):
        with open(ruta, "a", encoding="utf-8") as fichero:
            fichero.write(prestamo.cambiar_objeto_a_linea() + "\n")

    @staticmethod
    def actualizar_estado_prestamo(nie, isbn, fecha_devolucion):
        actualizado: bool = False
        prestamos = Prestamo.cargar_prestamos()

        with open("../Datos/prestamos.txt", "w", encoding="utf-8") as fichero:
            for prestamo in prestamos:
                if prestamo.nie == nie and prestamo.isbn == isbn and prestamo.estado.lower() == "prestado":
                    prestamo.estado = "Devuelto"
                    prestamo.fecha_devolucion = fecha_devolucion
                    actualizado = True
                fichero.write(prestamo.cambiar_objeto_a_linea() + "\n")
        return actualizado

    @staticmethod
    def libro_esta_prestado(isbn):
        prestamos = Prestamo.cargar_prestamos()
        for prestamo in prestamos:
            if prestamo.isbn == isbn and prestamo.estado.lower() == "prestado":
                return True
        return False

    @staticmethod
    def pedir_fecha_correcta():
        while True:
            fecha: str = ""
            fecha = input("Ingrese la fecha actual (Formato DD/MM/AAAA): ").strip()
            partes = fecha.split("/")

            if len(partes) != 3:
                print("El formato debe ser: DD/MM/AAAA")
                continue

            dia, mes, anno = partes
            if not (dia.isdigit() and mes.isdigit() and anno.isdigit()):
                print("La fecha debe contener solo números.")
                continue

            if len(dia) != 2 or len(mes) != 2 or len(anno) != 4:
                print("El formato debe ser: DD/MM/AAAA")
                continue

            return fecha

    @staticmethod
    def calcular_fecha_devolucion(fecha_prestamo):
        try:
            dia, mes, anno = fecha_prestamo.split("/")
            anno_devolucion = str(int(anno) + 1)
            return f"{dia}/{mes}/{anno_devolucion}"
        except ValueError:
            print("Formato de fecha incorrecto. Se pondrá '_' en fecha de devolución.")
            return "-"

    @staticmethod
    def realizar_prestamo():
        nie = input("Ingrese el NIE del alumno: ").strip().upper()
        curso = input("Ingrese el ID del curso: ").strip()

        print("\nIntroduce los ISBN de los libros (ENTER para finalizar):")
        libros: list = []
        libros = []
        while True:
            entrada = input("ISBN: ").strip()
            if entrada == "":
                break
            libros.append(entrada)

        fecha_prestamo = Prestamo.pedir_fecha_correcta()
        fecha_devolucion = Prestamo.calcular_fecha_devolucion(fecha_prestamo)

        for isbn in libros:
            if Prestamo.libro_esta_prestado(isbn):
                print(f"El libro con ISBN {isbn} ya está prestado.")
                return

        for isbn_str in libros:
            isbn = int(isbn_str)
            curso_int = int(curso)
            nuevo_prestamo = Prestamo(nie, isbn, curso_int, fecha_prestamo, "", "Prestado")
            Prestamo.guardar_prestamo(nuevo_prestamo)

        Prestamo.generar_contrato_texto(nie, curso, libros, fecha_prestamo, fecha_devolucion)
        print("Préstamo registrado.")
        print(f"Fecha devolución estimada: {fecha_devolucion}")

    @staticmethod
    def pedir_datos_devolucion():
        nie = input("Ingrese el NIE del alumno: ").strip().upper()
        isbn = input("Ingrese el ISBN del libro a devolver: ").strip()
        fecha = Prestamo.pedir_fecha_correcta()
        return nie, isbn, fecha

    @staticmethod
    def devolver_prestamo():
        nie, isbn, fecha_devolucion = Prestamo.pedir_datos_devolucion()
        actualizado = Prestamo.actualizar_estado_prestamo(nie, isbn, fecha_devolucion)

        if actualizado:
            print("Libro devuelto correctamente.")
        else:
            print("No se encontró un préstamo activo con ese NIE e ISBN.")

    @staticmethod
    def generar_contrato_texto(nie, curso, lista_isbns, fecha_prestamo, fecha_devolucion):
        nombre_archivo = f"../Contratos/Contrato_{nie}.txt"
        todos_los_libros = Libro.cargar_libros()

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("===== CONTRATO DE PRÉSTAMO DE LIBROS =====\n\n")
            archivo.write(f"DNI del alumno: {nie}\n")
            archivo.write(f"Curso ID: {curso}\n")
            archivo.write(f"Fecha de préstamo: {fecha_prestamo}\n")
            archivo.write(f"Fecha de devolución estimada: {fecha_devolucion}\n\n")
            archivo.write("Libros prestados:\n")

            for libro in todos_los_libros:
                marca = " X" if libro.isbn in lista_isbns else "  "
                archivo.write(f"{marca} {libro.isbn} - {libro.titulo}\n")

            archivo.write("\n\nFirma del alumno: _________________________\n")
            archivo.write("Firma del centro: _________________________\n\n")
            archivo.write("Fecha de la firma: ________________________\n")

        print(f"Contrato generado: {nombre_archivo}")
