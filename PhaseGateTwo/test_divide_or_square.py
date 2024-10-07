import math
import unittest
import divideorsquare

class TestDivideOrSquare(unittest.TestCase):
    def test_that_number_divisible_by_five_returns_square_root(self):
        self.assertEqual(divideorsquare.get_squareroot(10), 5)
        self.assertTrue(divideorsquare.get_squareroot(10), 3.16)
        
    #def test_that_number_divisible_by_five_returns_root(self):
       # self.assertTrue(divideorsquare.get_squareroot(10), 3.16)
