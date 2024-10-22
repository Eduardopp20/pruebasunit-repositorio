import unittest
from calculadora import sumar

class TestCalculadora(unittest.TestCase):

    def test_sumar_igualdad(self):
        self.assertEqual(sumar(1, 2), 3)

    def test_sumar_desigualdad(self):
        self.assertNotEqual(sumar(1, 2), 4)

    def test_sumar_mayor_que(self):
        self.assertTrue(sumar(2, 3) > 4)

    def test_sumar_menor_que(self):
        self.assertFalse(sumar(-1, 1) > 0)

    def test_sumar_letra_numero(self):
        # Prueba que devuelve el mensaje de error adecuado
        self.assertEqual(sumar('a', 1), "Error: no se puede sumar una letra con un número")

if __name__ == "__main__":
    unittest.main()
