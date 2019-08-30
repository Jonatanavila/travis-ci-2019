import unittest
import sut 
from unittest.mock import MagicMock
from unittest.mock import patch
#from math import math.sum
#from unittest.mock.patch(math.exp, math.sqrt)

class Test_sut(unittest.TestCase):

	def test_sumar(self):
		self.assertEqual(sut.sumar(2,4),2)

	def test_saludar(self):
		self.assertTrue(sut.saludar('hola'+'nombre'),'hola joni')

	def test_sumatoria(self):
		a=[1,2,3]
		sumatoria= sut.sumatoria(a,2)
		self.assertTrue(sumatoria==3)

	def test_productoria(self):
		a=[1,2,3]
		productoria=sut.productoria(a,3)
		self.assertTrue(productoria==6)

	def test_multiplicar(self):
		a=3
		b=4
		multiplicar= sut.multiplicar(a,b)
		self.assertTrue(multiplicar==12)

	def comparar_menor_que_otro(self):
		self.assertNotEqual(sut.comparar(2,6),"A menor que B")

	def comparar_mayot_que_el_otro(self):
		self.assertNotEqual(sut.comparar(7,3),"A mayor que B")

	def comparar_igualdad(self):
		self.asserEqual(sut.comparar(7,3),"A y B son iguales")

	def test_valorabsoluto(self):
		self.assertEqual(sut.valorabsoluto(-7),7)

	def test_costototal(self):
		sut.sumar = MagicMock(return_value=2)
		valor = sut.costototal(4,7)
		string= 'El costo total es $2' 
		self.assertEqual(valor, string)

	@patch('math.exp')
	@patch('math.sqrt')
	def supercalc(self,exp,sqrt):
		exp.return_value=2
		sqrt.return_value=2
		a=sut.supercalc(3)
		self.assertTrue(a == 2)
		return sqrt

		
		

if __name__ == '__main__':
    unittest.main()
