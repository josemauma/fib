import pytest
from fibonacci import fibonaccci_iterative as fib

def test_fib_9_is_34():
    assert fib(9) == 34

def test_fib_negative_raise_error():
    with pytest.raises(ValueError):
        fib(-1)