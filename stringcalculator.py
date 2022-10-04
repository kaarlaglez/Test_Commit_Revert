import re
import pytest
from calc.calculator import stringcalculator


#def Add(a):
  #Add implementation
#  return 0


def test_stringcalculator_should_return_zero_on_empty_string():
  result = stringcalculator("")
  assert result == 0
  

def test_stringcalculator_should_return_correct_numeric_value_on_one():
  result = stringcalculator("1")
  assert result == 1
  
