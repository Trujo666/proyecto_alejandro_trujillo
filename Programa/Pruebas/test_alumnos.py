import unittest
import sys
import os
sys.path.insert(0, os.path.abspath("../Clases"))

from alumnos import Alumno


class TestAlumno(unittest.TestCase):

    def test_crear_objeto(self):
        alumno = Alumno("03220367E", "Alejandro", "Trujillo", False, "II")
        self.assertEqual(alumno.nie, "03220367E")
        self.assertEqual(alumno.nombre, "Alejandro")
        self.assertEqual(alumno.apellidos, "Trujillo")
        self.assertFalse(alumno.bilingue)
        self.assertEqual(alumno.tramo, "II")

    def test_cambiar_objeto_a_linea(self):
        alumno = Alumno("03220367E", "Alejandro", "Trujillo", False, "II")
        resultado = alumno.cambiar_objeto_a_linea()
        esperado = "03220367E|Alejandro|Trujillo|0|II"
        self.assertEqual(resultado, esperado)

    def test_crear_desde_linea(self):
        linea = "03220367E|Alejandro|Trujillo|0|II"
        alumno = Alumno.crear_desde_linea(linea)
        self.assertEqual(alumno.nie, "03220367E")
        self.assertEqual(alumno.nombre, "Alejandro")
        self.assertEqual(alumno.apellidos, "Trujillo")
        self.assertFalse(alumno.bilingue)
        self.assertEqual(alumno.tramo, "II")


if __name__ == "__main__":
    unittest.main()
