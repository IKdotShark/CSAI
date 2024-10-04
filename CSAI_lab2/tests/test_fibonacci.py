import pytest
from my_lib import fibonacci

def test_fibonacci_positive():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(0)
    with pytest.raises(ValueError):
        fibonacci(-5)
