import unittest
from examenempaquetar import examenempaquetar


class pruebaempaquetar(unittest.TestCase):


    def setUp(self):


        self.prueb = examenempaquetar()


    def test_probar_tuplas(self):

        lista = [1, 1, 1, 3, 5, 1, 1, 3, 3]
        lista_resultado = [(1, 3), (3, 1), (5, 1), (1, 2), (3, 2)]

        resultado = self.prueb.empaquetar(lista)

        self.assertEqual(lista_resultado, resultado)

if __name__ == "__main__":
    unittest.main()
