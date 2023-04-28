import unittest
from calculadora.hipotenusa import hipotenusa

class TestHipotenusa(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            hipotenusa(3, 4),
            5
        )