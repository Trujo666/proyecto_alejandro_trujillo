class Curso:
    def __init__(self, id_curso: str, curso: str, nivel: str):
        self.id_curso = id_curso
        self.curso = curso
        self.nivel = nivel

    def __str__(self):
        return f"ID Curso: {self.id_curso} | Curso: {self.curso} | Nivel: {self.nivel}"

    @staticmethod
    def crear_desde_linea(linea):
        id_curso, curso, nivel = linea.strip().split("|")
        return Curso(id_curso.strip(), curso.strip(), nivel.strip())

    @staticmethod
    def cargar_cursos(ruta="../Datos/cursos.txt"):
        cursos: list = []
        cursos = []
        try:
            with open(ruta, "r") as fichero:
                for linea in fichero:
                    cursos.append(Curso.crear_desde_linea(linea))
        except FileNotFoundError:
            pass
        return cursos
