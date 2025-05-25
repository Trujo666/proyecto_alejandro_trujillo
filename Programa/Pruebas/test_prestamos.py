import unittest
import sys
import os
sys.path.insert(0, os.path.abspath("../Clases"))

from prestamos import Prestamo


class TestPrestamo(unittest.TestCase):

    def test_crear_prestamo(self):
        p = Prestamo("03220367E", "1234567890", "1A", "2024-05-01", "2024-05-15", "Pendiente")
        self.assertEqual(p.nie, "03220367E")
        self.assertEqual(p.isbn, "1234567890")
        self.assertEqual(p.id_curso, "1A")
        self.assertEqual(p.fecha_prestamo, "2024-05-01")
        self.assertEqual(p.fecha_devolucion, "2024-05-15")
        self.assertEqual(p.estado, "Pendiente")

    def test_str(self):
        p = Prestamo("03220367E", "1234567890", "1A", "2024-05-01", "2024-05-15", "Pendiente")
        esperado = ("NIE: 03220367E | ISBN: 1234567890 | Id Curso: 1A | "
                    "Fecha de prestamo: 2024-05-01 | Fecha de devolucion: 2024-05-15 | Estado de prestamo: Pendiente")
        self.assertEqual(str(p), esperado)

    def test_cambiar_objeto_a_linea(self):
        p = Prestamo("03220367E", "1234567890", "1A", "2024-05-01", "2024-05-15", "Pendiente")
        esperado = "03220367E | 1234567890 | 1A | 2024-05-01 | 2024-05-15 | Pendiente"
        self.assertEqual(p.cambiar_objeto_a_linea(), esperado)

    def test_crear_desde_linea(self):
        linea = "03220367E | 1234567890 | 1A | 2024-05-01 | 2024-05-15 | Pendiente"
        p = Prestamo.crear_desde_linea(linea)
        self.assertEqual(p.nie, "03220367E")
        self.assertEqual(p.isbn, "1234567890")
        self.assertEqual(p.id_curso, "1A")
        self.assertEqual(p.fecha_prestamo, "2024-05-01")
        self.assertEqual(p.fecha_devolucion, "2024-05-15")
        self.assertEqual(p.estado, "Pendiente")

if __name__ == "__main__":
    unittest.main()
