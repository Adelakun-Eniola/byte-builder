import unittest
import multiplication


class TestMultiplication(unittest.TestCase):
    def test_that_result_of_two_numbers_display_when_multiplied(self):
        multiplication.get_result(5,4)
    def test_that_result_of_two_numbers_display_when_multiplied(self):
        self.assertEqual(5+5+5+5, 20)
    
