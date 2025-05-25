import unittest
import sys
import os
sys.path.insert(0, os.path.abspath("../Clases"))

from libros import Libro


class TestLibro(unittest.TestCase):

    def test_crear_libro(self):
        libro = Libro("1234567890", "1984", "George Orwell", 5, "MAT01", "1º ESO")
        self.assertEqual(libro.isbn, "1234567890")
        self.assertEqual(libro.titulo, "1984")
        self.assertEqual(libro.autor, "George Orwell")
        self.assertEqual(libro.n_ejemplares, 5)
        self.assertEqual(libro.id_materia, "MAT01")
        self.assertEqual(libro.curso, "1º ESO")

    def test_str(self):
        libro = Libro("1234567890", "1984", "George Orwell", 5, "MAT01", "1º ESO")
        esperado = "ISBN: 1234567890 | Título: 1984 | Autor: George Orwell | Nº de ejemplares: 5 | ID: MAT01 | Curso: 1º ESO"
        self.assertEqual(str(libro), esperado)

    def test_crear_desde_linea_libros(self):
        linea = "1234567890|1984|George Orwell|5|MAT01|1º ESO"
        libro = Libro.crear_desde_linea_libros(linea)
        self.assertEqual(libro.isbn, "1234567890")
        self.assertEqual(libro.titulo, "1984")
        self.assertEqual(libro.autor, "George Orwell")
        self.assertEqual(libro.n_ejemplares, 5)
        self.assertEqual(libro.id_materia, "MAT01")
        self.assertEqual(libro.curso, "1º ESO")


if __name__ == "__main__":
    unittest.main()
