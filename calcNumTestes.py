import unittest
from interpolacao import *

class TestStringMethods(unittest.TestCase):
    def test_minimosQuadrados(self):
        x = [0,30,70,100]
        y= [0.94,1.05,1.17,1.28]
        resultado = list(minimosQuadrados(x,y,4))
        esperado = list((0.9428, 0.0033, '0.0033*x + (0.9428)'))
        self.assertEqual(esperado, resultado)

    def testSplines(self):
        x = [8,11,15,18]
        y= [5,9,10,8]
        esperado = 9.425
        resultado = splinesLineares(x,y,4,12.7)[2]
        self.assertEqual(esperado, resultado)
        
    def testLagrange(self):
        cx = [1,2,4,5,7]
        cy= [52,5,-5,-40,10]
        resultado = lagrange(cx,cy,4,3)[0]
        esperado = 6
        self.assertEqual(esperado, resultado)
        
    def testNewton(self):
        cx = [1,2,4,5,7]
        cy= [52,5,-5,-40,10]
        resultado = newton(cx,cy,4,3)[0]
        esperado = 6
        self.assertEqual(esperado, resultado)
        
if __name__ == '__main__':
    unittest.main()