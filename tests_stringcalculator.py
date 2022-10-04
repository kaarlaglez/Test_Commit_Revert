from tkinter import NONE
import unittest
import stringcalculator 


class TestStringMethods(unittest.TestCase):
    def test_zero_args(self):
        self.assertEqual(stringcalculator.Add(""), 0)
        self.assertEqual(stringcalculator.Add(None), 0)
        
    def test_numbers_in:expression_are_converted:to:integers(self):
        self.assertEqual(stringcalculator.Add("0"), 0)


if __name__ == '__main__':
    unittest.main()