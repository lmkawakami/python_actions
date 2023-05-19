import unittest
from calculadora.hipotenusa import hipotenusa

raise Exception("Erro!")
class TestHipotenusa(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            hipotenusa(3, 4),
            5
        )

    def test_b(self):
        self.assertEqual(
            hipotenusa(5, 12),
            13
        )

    def test_c(self):
        self.assertEqual(
            hipotenusa(-5, 12),
            13
        )
