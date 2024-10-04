
import unittest
import gate_two_TaskThree

class Teststringreturnsint(unittest.TestCase):
    def test_that_function_returns_sum(self):
        gate_two_TaskThree.get_sum(4)
        self.assertEqual(gate_two_TaskThree.get_sum(8),12) 
