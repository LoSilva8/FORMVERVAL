import unittest

class TestCalculaAreaRetangulo(unittest.TestCase):
    def test_area_retangulo(self):
        altura = 5
        largura = 10
        esperado = 50
        self.assertEqual(calcula_area_retangulo(altura, largura), esperado)
