import pytest
from math import isinf, isnan

from fibonacci_sequence import fib_iter, fib_rec

def test_fib_iter_valid_inputs():
    assert fib_iter(0) == 0
    assert fib_iter(1) == 1
    assert fib_iter(2) == 1
    assert fib_iter(3) == 2
    assert fib_iter(4) == 3
    assert fib_iter(5) == 5
    assert fib_iter(6) == 8
    assert fib_iter(7) == 13
    assert fib_iter(8) == 21
    assert fib_iter(9) == 34
    assert fib_iter(10) == 55
    assert fib_iter(20) == 6765


def test_fib_rec_valid_inputs():
    assert fib_rec(0) == 0
    assert fib_rec(1) == 1
    assert fib_rec(2) == 1
    assert fib_rec(3) == 2
    assert fib_rec(4) == 3
    assert fib_rec(5) == 5
    assert fib_rec(6) == 8
    assert fib_rec(7) == 13
    assert fib_rec(8) == 21
    assert fib_rec(9) == 34
    assert fib_rec(10) == 55
    assert fib_rec(20) == 6765


def test_fib_iter_edge_cases():
    assert fib_iter(0) == 0
    assert fib_iter(1) == 1


def test_fib_rec_edge_cases():
    assert fib_rec(0) == 0
    assert fib_rec(1) == 1


def test_fib_iter_invalid_string():
    with pytest.raises(TypeError):
        fib_iter("string")


def test_fib_iter_invalid_float():
    with pytest.raises(TypeError):
        fib_iter(1.5)


def test_fib_iter_invalid_list():
    with pytest.raises(TypeError):
        fib_iter([1, 2, 3])


def test_fib_iter_invalid_none():
    with pytest.raises(TypeError):
        fib_iter(None)


def test_fib_rec_invalid_string():
    with pytest.raises(TypeError):
        fib_rec("string")


def test_fib_rec_invalid_float():
    with pytest.raises(TypeError):
        fib_rec(1.5)


def test_fib_rec_invalid_list():
    with pytest.raises(TypeError):
        fib_rec([1, 2, 3])


def test_fib_rec_invalid_none():
    with pytest.raises(TypeError):
        fib_rec(None)


def test_fib_iter_negative():
    with pytest.raises(ValueError):
        fib_iter(-1)
    with pytest.raises(ValueError):
        fib_iter(-10)


def test_fib_rec_negative():
    with pytest.raises(ValueError):
        fib_rec(-1)
    with pytest.raises(ValueError):
        fib_rec(-10)


def test_fib_iter_large_numbers():
    assert fib_iter(100) == 354224848179261915075
    assert fib_iter(200) == 280571172992510140037611932413038677189525
    assert fib_iter(300) == 222232244629420445529739893461909967206666939096499764990979600 

def test_fib_rec_large_numbers():
    assert fib_rec(20) == 6765
    assert fib_rec(30) == 832040
    assert fib_rec(40) == 102334155


def test_fib_iter_large_negative():
    with pytest.raises(ValueError):
        fib_iter(-100)


def test_fib_rec_large_negative():
    with pytest.raises(ValueError):
        fib_rec(-100)
