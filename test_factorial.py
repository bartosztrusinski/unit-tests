import pytest
from math import isinf, isnan

from factorial import factorial_iter, factorial_rec

def test_factorial_iter_valid_inputs():
    assert factorial_iter(0) == 1
    assert factorial_iter(1) == 1
    assert factorial_iter(2) == 2
    assert factorial_iter(3) == 6
    assert factorial_iter(4) == 24
    assert factorial_iter(5) == 120
    assert factorial_iter(10) == 3628800
    assert factorial_iter(20) == 2432902008176640000

def test_factorial_rec_valid_inputs():
    assert factorial_rec(0) == 1
    assert factorial_rec(1) == 1
    assert factorial_rec(2) == 2
    assert factorial_rec(3) == 6
    assert factorial_rec(4) == 24
    assert factorial_rec(5) == 120
    assert factorial_rec(10) == 3628800
    assert factorial_rec(20) == 2432902008176640000


def test_factorial_iter_edge_cases():
    assert factorial_iter(0) == 1
    assert factorial_iter(1) == 1

def test_factorial_rec_edge_cases():
    assert factorial_rec(0) == 1
    assert factorial_rec(1) == 1


def test_factorial_iter_negative():
    with pytest.raises(ValueError):
        factorial_iter(-1)
    with pytest.raises(ValueError):
        factorial_iter(-10)

def test_factorial_rec_negative():
    with pytest.raises(ValueError):
        factorial_rec(-1)
    with pytest.raises(ValueError):
        factorial_rec(-10)


def test_factorial_iter_invalid_string():
    with pytest.raises(TypeError):
        factorial_iter("string")

def test_factorial_iter_invalid_float():
    with pytest.raises(TypeError):
        factorial_iter(1.5)

def test_factorial_iter_invalid_list():
    with pytest.raises(TypeError):
        factorial_iter([1, 2, 3])

def test_factorial_iter_invalid_none():
    with pytest.raises(TypeError):
        factorial_iter(None)


def test_factorial_rec_invalid_string():
    with pytest.raises(TypeError):
        factorial_rec("string")

def test_factorial_rec_invalid_float():
    with pytest.raises(TypeError):
        factorial_rec(1.5)

def test_factorial_rec_invalid_list():
    with pytest.raises(TypeError):
        factorial_rec([1, 2, 3])

def test_factorial_rec_invalid_none():
    with pytest.raises(TypeError):
        factorial_rec(None)


def test_factorial_iter_large_numbers():
    assert factorial_iter(100)
    assert factorial_iter(200)
    assert factorial_iter(500)

def test_factorial_rec_large_numbers():
    assert factorial_rec(100)
    assert factorial_rec(200)
    assert factorial_rec(500)


def test_factorial_iter_boundary():
    assert factorial_iter(170)

def test_factorial_rec_boundary():
    assert factorial_rec(170)


def test_factorial_iter_invalid_dict():
    with pytest.raises(TypeError):
        factorial_iter({"key": "value"})

def test_factorial_rec_invalid_dict():
    with pytest.raises(TypeError):
        factorial_rec({"key": "value"})

def test_factorial_iter_invalid_set():
    with pytest.raises(TypeError):
        factorial_iter({1, 2, 3})

def test_factorial_rec_invalid_set():
    with pytest.raises(TypeError):
        factorial_rec({1, 2, 3})

def test_factorial_iter_invalid_tuple():
    with pytest.raises(TypeError):
        factorial_iter((1, 2, 3))

def test_factorial_rec_invalid_tuple():
    with pytest.raises(TypeError):
        factorial_rec((1, 2, 3))
