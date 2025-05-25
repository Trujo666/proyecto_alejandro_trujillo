class Alumno:
    def __init__(self, nie: str, nombre: str, apellidos: str, bilingue, tramo):
        self.nie = nie
        self.nombre = nombre
        self.apellidos = apellidos
        self.bilingue = bilingue
        self.tramo = tramo

    def set_nie(self, nie):
        self.nie = nie

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

    def set_bilingue(self, bilingue):
        self.bilingue = bilingue

    def set_tramo(self, tramo):
        self.tramo = tramo

    def cambiar_objeto_a_linea(self):
        return f"{self.nie}|{self.nombre}|{self.apellidos}|{int(self.bilingue)}|{self.tramo}"

    @staticmethod
    def crear_desde_linea(linea):
        nie, nombre, apellidos, bilingue_str, tramo = linea.strip().split("|")
        bilingue = bool(int(bilingue_str))
        return Alumno(nie, nombre, apellidos, bilingue, tramo)

    @staticmethod
    def cargar_alumnos(ruta="../Datos/alumnos.txt"):
        alumnos: list = []
        alumnos = []
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    alumnos.append(Alumno.crear_desde_linea(linea))
        except FileNotFoundError:
            print("Archivo de alumnos no encontrado. Se creará un nuevo archivo.")
        return alumnos

    @staticmethod
    def buscar_por_nie(nie_buscado, ruta="../Datos/alumnos.txt"):
        alumnos = Alumno.cargar_alumnos(ruta)
        for alumno in alumnos:
            if alumno.nie == nie_buscado:
                return alumno
        return None

    def guardar_en_archivo(self, ruta="../Datos/alumnos.txt"):
        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(self.cambiar_objeto_a_linea() + "\n")

    def modificar_datos(self, campo, valor):
        match campo:
            case "nie":
                self.nie = valor
            case "nombre":
                self.nombre = valor
            case "apellidos":
                self.apellidos = valor
            case "bilingue":
                self.bilingue = valor
            case "tramo":
                self.tramo = valor

    def __str__(self):
        return (f"NIE: {self.nie} | "
                f"Nombre: {self.nombre} {self.apellidos} | "
                f"Bilingüe: {'Sí' if self.bilingue else 'No'} | "
                f"Tramo: {self.tramo}")
