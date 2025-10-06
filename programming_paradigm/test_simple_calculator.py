import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(2.5, 1.2), 1.3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertIsNone(self.calc.divide(5, 0))  
        self.assertIsNone(self.calc.divide(0, 0)) 

    def test_large_numbers(self):
        large_num = 10**10
        self.assertEqual(self.calc.add(large_num, 1), large_num + 1)
        self.assertEqual(self.calc.multiply(large_num, 2), large_num * 2)
        self.assertEqual(self.calc.divide(large_num, 2), large_num / 2)

if __name__ == "__main__":
    unittest.main()