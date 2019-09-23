import unittest
import sut 
from unittest.mock import MagicMock,mock_open
from unittest.mock import patch
#from math import math.sum
#from unittest.mock.patch(math.exp, math.sqrt)

class Test_sut(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sut.sumar(2,4),6)

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
        valorabs=sut.valorabsoluto(-4)
        self.assertTrue(valorabs == 4)
		
    @patch('sut.sumar')
    def test_costototal(self,sumar):
        sumar.return_value= 2
        a=sut.costototal(5,4)
        esperado= 'el costo total es $2'
        self.assertEqual(a,esperado)

    @patch('math.exp')
    @patch('math.sqrt')
    def supercalc(self, exp, sqrt):
        exp.return_value=2
        sqrt.return_value=2
        a= sut.supercalc(3)
        self.assertTrue(a == 2)	
	
    def test_CalcuClass_sum(self):
        calc = sut.CalcuClass().suma(a=7, b=4)
        self.assertTrue(calc == 11)
        
    def test_CalcuClass_pro(self):
        calcu = sut.CalcuClass().producto(a=5, b=5)
        self.assertTrue(calcu == 25)
        
    def test_CalcuClass_list(self):
        calcu = sut.CalcuClass().sumar_varios(lista = [4,9,3])
        self.assertTrue(calcu == 16)

if __name__ == '__main__':
    unittest.main()
