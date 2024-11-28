import pytest
from math import isinf, isnan

from arithmetic_operations import add, subtract, multiply, divide


# ====== test add ======

# types

def test_add_integers():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(-1, 1) == 0

def test_add_floats():
    assert add(1.5, 2.5) == 4.0
    assert add(-1.2, -1.5) == -2.7
    assert add(0.1, 0.2) == pytest.approx(0.3, rel=1e-9)

def test_add_mixed_types():
    assert add(1, 2.5) == 3.5
    assert add(1.5, 2) == 3.5
    assert add(-1.2, -5) == -6.2

def test_add_strings():
    with pytest.raises(TypeError):
        add("hello", "world")
        
def test_add_with_lists():
    with pytest.raises(TypeError):
        add([1, 2], [3, 4])

def test_add_with_tuples():
    with pytest.raises(TypeError):
        add((1, 2), (3, 4))

def test_add_with_none():
    with pytest.raises(TypeError):
        add(None, 5)

def test_add_nan():
    assert isnan(add(float('nan'), 1))
    assert isnan(add(float('nan'), float('nan')))

# edge cases

def test_add_large_numbers():
    large_number = 1e308
    assert add(large_number, large_number) == float('inf')
    assert add(-large_number, -large_number) == float('-inf')
    assert add(large_number, -large_number) == 0

def test_add_small_numbers():
    small_number = 1e-308
    assert add(small_number, small_number) == pytest.approx(2e-308)
    assert add(-small_number, small_number) == pytest.approx(0)

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(-5, 0) == -5

def test_add_opposites():
    assert add(1, -1) == 0
    assert add(1e10, -1e10) == 0

def test_add_extreme_values():
    assert isnan(add(float('inf'), float('-inf')))
    assert add(float('inf'), float('inf')) == float('inf')
    assert add(float('-inf'), float('-inf')) == float('-inf')

def test_add_infinity():
    assert add(float('inf'), 1) == float('inf')
    assert add(float('-inf'), -1) == float('-inf')
    
def test_add_min_max_float():
    min_float = -1.7e308
    max_float = 1.7e308
    
    assert add(min_float, 0) == min_float
    assert add(max_float, 0) == max_float
    assert add(max_float, min_float) == 0

    pos_overflow = add(max_float, max_float)
    assert isinf(pos_overflow) and pos_overflow > 0
    
    neg_overflow = add(min_float, min_float)
    assert isinf(neg_overflow) and neg_overflow < 0

def test_add_large_inputs():
    max_number = 1e308
    assert add(max_number, max_number) == float('inf')
    assert add(-max_number, -max_number) == float('-inf')
    assert add(max_number, -max_number) == 0
