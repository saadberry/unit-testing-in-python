import unittest
import calc

class TestCalc(unittest.TestCase):

    #test method for func 'add'
    def test_add(self):
       
       self.assertEqual(calc.add(10,5), 15) 
       self.assertEqual(calc.add(-1,1), 0)
       self.assertEqual(calc.add(-1,-1), -2)

    #test method for func 'subtract'
    def test_subtract(self):
        self.assertEqual(calc.subtract(1,1), 0)
        self.assertEqual(calc.subtract(-1,1), -2)

    #test method for func 'product'
    def test_product(self):
        self.assertEqual(calc.product(2,0), 0)
        self.assertEqual(calc.product(2,-1), -2)
        self.assertEqual(calc.product(-2,-2), 4)


    #test method for func 'divide'
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-10, -10), 1)

if __name__ == '__main__':
    unittest.main()