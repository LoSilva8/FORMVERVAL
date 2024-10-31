import unittest

def calcula_area_retangulo(altura, largura):
    return altura * largura

class TestCalculaAreaRetangulo(unittest.TestCase):
    def test_area_retangulo(self):
        altura = 5
        largura = 10
        esperado = 50
        self.assertEqual(calcula_area_retangulo(altura, largura), esperado)

if __name__ == "__main__":
    unittest.main()
