class Libro:
    def __init__(self, isbn: int, titulo: str, autor: str, n_ejemplares: int, id_materia: str, curso: str) -> None:
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.n_ejemplares = n_ejemplares
        self.id_materia = id_materia
        self.curso = curso

    def __str__(self):
        return (f"ISBN: {self.isbn} | "
                f"Título: {self.titulo} | "
                f"Autor: {self.autor} | "
                f"Nº de ejemplares: {self.n_ejemplares} | "
                f"ID: {self.id_materia} | "
                f"Curso: {self.curso}")

    @staticmethod
    def crear_desde_linea_libros(linea):
        isbn, titulo, autor, n_ejemplares, id_materia, curso = linea.strip().split("|")
        return Libro(
            isbn.strip(),
            titulo.strip(),
            autor.strip(),
            int(n_ejemplares.strip()),
            id_materia.strip(),
            curso.strip())

    @staticmethod
    def cargar_libros(ruta="../Datos/libros.txt"):
        libros: list = []
        libros = []
        try:
            with open(ruta, "r", encoding="utf-8") as fichero:
                for linea in fichero:
                    libros.append(Libro.crear_desde_linea_libros(linea))
        except FileNotFoundError:
            pass
        return libros
