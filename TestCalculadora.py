import unittest;
from Calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
	def setUp(self):
		self.calc = Calculadora()

	def test_sumar_de_3_mas_2(self):
		resultado = self.calc.suma(3,2)
		self.assertEqual(5, resultado)

	def test_sumar_de_3_mas_3(self):
		resultado = self.calc.suma(3,3)
		self.assertEqual(6, resultado)

	def test_sumar_de_10_mas_10(self):
		resultado = self.calc.suma(10,10)
		self.assertEqual(20, resultado) 

	def test_resta_de_5_menos_2(self):
		resultado = self.calc.resta(5,2)
		self.assertEqual(3,resultado)

	def test_resta_de_2_menos_5(self):
		resultado = self.calc.resta(2,5)
		self.assertEqual(-3,resultado)



if __name__=="__main__":
	unittest.main()