import pytest
from math import isinf, isnan

from gcd import gcd_iter, gcd_rec

def test_gcd_iter_integers():
    assert gcd_iter(10, 5) == 5
    assert gcd_iter(100, 25) == 25
    assert gcd_iter(54, 24) == 6
    assert gcd_iter(18, 48) == 6
    assert gcd_iter(7, 13) == 1

def test_gcd_rec_integers():
    assert gcd_rec(10, 5) == 5
    assert gcd_rec(100, 25) == 25
    assert gcd_rec(54, 24) == 6
    assert gcd_rec(18, 48) == 6
    assert gcd_rec(7, 13) == 1

def test_gcd_iter_zero():
    assert gcd_iter(0, 5) == 5
    assert gcd_iter(5, 0) == 5
    assert gcd_iter(0, 0) == 0

def test_gcd_rec_zero():
    assert gcd_rec(0, 5) == 5
    assert gcd_rec(5, 0) == 5
    assert gcd_rec(0, 0) == 0

def test_gcd_iter_invalid_int():
    with pytest.raises(TypeError):
        gcd_iter(10, "5")

def test_gcd_iter_invalid_str():
    with pytest.raises(TypeError):
        gcd_iter("10", 5)

def test_gcd_iter_invalid_float():
    with pytest.raises(TypeError):
        gcd_iter(10.5, 5)

def test_gcd_iter_invalid_list():
    with pytest.raises(TypeError):
        gcd_iter(10, [5])

def test_gcd_iter_invalid_none():
    with pytest.raises(TypeError):
        gcd_iter(10, None)

def test_gcd_rec_invalid_int():
    with pytest.raises(TypeError):
        gcd_rec(10, "5")

def test_gcd_rec_invalid_str():
    with pytest.raises(TypeError):
        gcd_rec("10", 5)

def test_gcd_rec_invalid_float():
    with pytest.raises(TypeError):
        gcd_rec(10.5, 5)

def test_gcd_rec_invalid_list():
    with pytest.raises(TypeError):
        gcd_rec(10, [5])

def test_gcd_rec_invalid_none():
    with pytest.raises(TypeError):
        gcd_rec(10, None)

def test_gcd_iter_negative_numbers():
    with pytest.raises(ValueError):
        gcd_iter(-10, 5)
    with pytest.raises(ValueError):
        gcd_iter(10, -5)
    with pytest.raises(ValueError):
        gcd_iter(-10, -5)

def test_gcd_rec_negative_numbers():
    with pytest.raises(ValueError):
        gcd_rec(-10, 5)
    with pytest.raises(ValueError):
        gcd_rec(10, -5)
    with pytest.raises(ValueError):
        gcd_rec(-10, -5)

def test_gcd_iter_large_numbers():
    assert gcd_iter(123456789, 987654321) == 9
    assert gcd_iter(9876543210, 1234567890) == 90
    assert gcd_iter(99999999, 88888888) == 11111111

def test_gcd_rec_large_numbers():
    assert gcd_rec(123456789, 987654321) == 9
    assert gcd_rec(9876543210, 1234567890) == 90
    assert gcd_rec(99999999, 88888888) == 11111111

def test_gcd_iter_edge_cases():
    assert gcd_iter(1, 1) == 1
    assert gcd_iter(1, 1000) == 1
    assert gcd_iter(1000, 1) == 1

def test_gcd_rec_edge_cases():
    assert gcd_rec(1, 1) == 1
    assert gcd_rec(1, 1000) == 1
    assert gcd_rec(1000, 1) == 1

def test_gcd_iter_opposites():
    assert gcd_iter(25, 100) == 25
    assert gcd_iter(100, 25) == 25

def test_gcd_rec_opposites():
    assert gcd_rec(25, 100) == 25
    assert gcd_rec(100, 25) == 25

def test_gcd_iter_large_inputs():
    assert gcd_iter(10000000000, 1000000000) == 1000000000
    assert gcd_iter(20000000000, 1000000000) == 1000000000

def test_gcd_rec_large_inputs():
    assert gcd_rec(10000000000, 1000000000) == 1000000000
    assert gcd_rec(20000000000, 1000000000) == 1000000000
