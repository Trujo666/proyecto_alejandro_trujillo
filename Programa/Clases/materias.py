class Materia:
    def __init__(self, id_materia: str, nombre_materia: str, departamento: str):
        self.id_materia = id_materia
        self.nombre_materia = nombre_materia
        self.departamento = departamento

    def __str__(self):
        return (f"ID: {self.id_materia}"
                f"Nombre: {self.nombre_materia} "
                f"Departamento: {self.departamento}")

    @staticmethod
    def crear_desde_linea(linea):
        id_materia, nombre_materia, departamento = linea.strip().split("|")
        return Materia(id_materia.strip(), nombre_materia.strip(), departamento.strip())

    @staticmethod
    def cargar_materias(ruta="../Datos/materias.txt"):
        materias: list = []
        try:
            with open(ruta, "r") as fichero:
                for linea in fichero:
                    materias.append(Materia.crear_desde_linea(linea))
        except FileNotFoundError:
            pass
        return materias
