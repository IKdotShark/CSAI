import pytest
from my_lib import calculator

def test_calculator_addition():
    assert calculator(3, 5, '+') == 8
    assert calculator(-1, 5, '+') == 4

def test_calculator_subtraction():
    assert calculator(10, 4, '-') == 6
    assert calculator(0, 4, '-') == -4

def test_calculator_multiplication():
    assert calculator(3, 5, '*') == 15
    assert calculator(-1, 5, '*') == -5

def test_calculator_division():
    assert calculator(10, 2, '/') == 5
    assert calculator(9, 3, '/') == 3

def test_calculator_division_by_zero():
    with pytest.raises(ValueError):
        calculator(10, 0, '/')

def test_calculator_invalid_operator():
    with pytest.raises(ValueError):
        calculator(10, 5, '%')
