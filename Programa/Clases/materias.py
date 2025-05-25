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
        if not linea.strip():
            return None

        partes = linea.strip().split("|")
        if len(partes) == 3:
            id_materia = partes[0].strip()
            nombre_materia = partes[1].strip()
            departamento = partes[2].strip()
            return Materia(id_materia, nombre_materia, departamento)
        else:
            print(f"[ERROR] Línea mal formateada en materias.txt: {linea.strip()}")
            return None

    @staticmethod
    def cargar_materias(ruta="../Datos/materias.txt"):
        materias: list = []
        materias = []
        try:
            with open(ruta, "r") as fichero:
                for linea in fichero:
                    materias.append(Materia.crear_desde_linea(linea))
        except FileNotFoundError:
            pass
        return materias
