
import unittest
from conjunto import calcular_promedio

class TestCalcularPromedio(unittest.TestCase):
    def test_arreglo_vacio(self):
        self.assertEqual(calcular_promedio([]), 0)

    def test_un_solo_elemento(self):
        self.assertEqual(calcular_promedio([5]), 5.0)

    def test_varios_elementos_positivos(self):
        self.assertEqual(calcular_promedio([1, 2, 3, 4, 5]), 3.0)

    def test_varios_elementos_negativos(self):
        self.assertEqual(calcular_promedio([-1, -2, -3, -4, -5]), -3.0)

    def test_mezcla_elementos_positivos_negativos(self):
        self.assertEqual(calcular_promedio([-1, 2, -3, 4, -5]), -0.6)

    def test_elementos_con_cero(self):
        self.assertEqual(calcular_promedio([0, 0, 0, 0, 0]), 0.0)

    def test_elementos_positivos_negativos_cero(self):
        self.assertEqual(calcular_promedio([1, -1, 0, 1, -1]), 0.0)

if __name__ == '__main__':
    unittest.main()
