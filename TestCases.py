import unittest
import math
from ScientificCalculator import ScientificCalculator

class TestScientificCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertAlmostEqual(ScientificCalculator.square_root(4), 2.0)
        self.assertAlmostEqual(ScientificCalculator.square_root(9), 3.0)
        self.assertAlmostEqual(ScientificCalculator.square_root(25), 5.0)
        with self.assertRaises(ValueError):
            ScientificCalculator.square_root(-1)

    def test_factorial(self):
        self.assertEqual(ScientificCalculator.factorial(5), 120)
        self.assertEqual(ScientificCalculator.factorial(0), 1)
        self.assertEqual(ScientificCalculator.factorial(1), 1)
        self.assertEqual(ScientificCalculator.factorial(7), 5040)
        with self.assertRaises(ValueError):
            ScientificCalculator.factorial(-3)

    def test_natural_log(self):
        self.assertAlmostEqual(ScientificCalculator.natural_log(1), 0.0)
        self.assertAlmostEqual(ScientificCalculator.natural_log(math.e), 1.0)
        with self.assertRaises(ValueError):
            ScientificCalculator.natural_log(0)
        with self.assertRaises(ValueError):
            ScientificCalculator.natural_log(-10)

    def test_power_function(self):
        self.assertEqual(ScientificCalculator.power(2, 3), 8)
        self.assertEqual(ScientificCalculator.power(5, 0), 1)
        self.assertEqual(ScientificCalculator.power(7, 2), 49)
        self.assertEqual(ScientificCalculator.power(10, -1), 0.1)

if __name__ == '__main__':
    unittest.main()