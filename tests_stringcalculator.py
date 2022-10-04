import unittest
import stringcalculator import a


class TestStringMethods(unittest.TestCase):

    def test_zero_args(self):
        self.assertEqual(stringcalculator.Add(""), 0)


if __name__ == '__main__':
    unittest.main()