from tkinter import NONE
import unittest
import stringcalculator 


class TestStringMethods(unittest.TestCase):
    def test_zero_args(self):
        self.assertEqual(stringcalculator.Add(""), 0)
        self.assertEqual(stringcalculator.Add(None), 0)
        
    def test_numbers_in_expression_are_converted_to_integers(self):
        self.assertEqual(stringcalculator.Add("0"), 0)
        
    def test_numbers_in_expression_are_separated_by_commas(self):
        self.assertEqual(stringcalculator.Add("1,1"), 2)
        self.assertEqual(stringcalculator.Add("2,10"), 12)
        self.assertEqual(stringcalculator.Add("1,4,1"), 6)
        self.assertEqual(stringcalculator.Add("1,2,3"), 6)
        
    def separated_instead_of_commas(self):
        self.assertEqual(stringcalculator.Add("1\n2,3"), 5)


if __name__ == '__main__':
    unittest.main()