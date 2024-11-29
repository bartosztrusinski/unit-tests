import pytest
from math import isinf, isnan

from arithmetic_operations import add, subtract, multiply, divide


# ====== test add ======

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
        
def test_add_lists():
    with pytest.raises(TypeError):
        add([1, 2], [3, 4])

def test_add_tuples():
    with pytest.raises(TypeError):
        add((1, 2), (3, 4))

def test_add_none():
    with pytest.raises(TypeError):
        add(None, 5)

def test_add_nan():
    assert isnan(add(float('nan'), 1))
    assert isnan(add(float('nan'), float('nan')))

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

# ====== test subtract ======

def test_subtract_integers():
    assert subtract(1, 2) == -1
    assert subtract(-1, -1) == 0
    assert subtract(-1, 1) == -2

def test_subtract_floats():
    assert subtract(1.5, 2.5) == -1.0
    assert subtract(-1.2, -1.5) == pytest.approx(0.3, rel=1e-9)
    assert subtract(0.1, 0.2) == pytest.approx(-0.1, rel=1e-9)

def test_subtract_mixed_types():
    assert subtract(1, 2.5) == -1.5
    assert subtract(1.5, 2) == -0.5
    assert subtract(-1.2, -5) == 3.8

def test_subtract_strings():
    with pytest.raises(TypeError):
        subtract("hello", "world")
        
def test_subtract_lists():
    with pytest.raises(TypeError):
        subtract([1, 2], [3, 4])

def test_subtract_tuples():
    with pytest.raises(TypeError):
        subtract((1, 2), (3, 4))

def test_subtract_none():
    with pytest.raises(TypeError):
        subtract(None, 5)

def test_subtract_nan():
    assert isnan(add(float('nan'), 1))
    assert isnan(add(float('nan'), float('nan')))

def test_subtract_large_numbers():
    large_number = 1e308
    assert subtract(large_number, large_number) == 0
    assert subtract(-large_number, -large_number) == 0
    assert subtract(large_number, -large_number) == float('inf')

def test_subtract_small_numbers():
    small_number = 1e-308
    assert subtract(small_number, small_number) == pytest.approx(0)
    assert subtract(-small_number, small_number) == pytest.approx(-2e-308)

def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(0, 5) == -5
    assert subtract(-5, 0) == -5

def test_subtract_opposites():
    assert subtract(1, -1) == 2
    assert subtract(1e10, -1e10) == 2e10

def test_subtract_extreme_values():
    assert subtract(float('inf'), float('-inf')) == float('inf')
    assert isnan(subtract(float('inf'), float('inf')))
    assert isnan(subtract(float('-inf'), float('-inf')))

def test_subtract_infinity():
    assert subtract(float('inf'), 1) == float('inf')
    assert subtract(float('-inf'), -1) == float('-inf')

def test_subtract_min_max_float():
    min_float = -1.7e308
    max_float = 1.7e308
    assert subtract(min_float, 0) == min_float
    assert subtract(max_float, 0) == max_float
    assert subtract(max_float, min_float) == float('inf')

    pos_overflow = subtract(max_float, -max_float)
    assert isinf(pos_overflow) and pos_overflow > 0

    neg_overflow = subtract(min_float, -min_float)
    assert isinf(neg_overflow) and neg_overflow < 0

def test_subtract_large_inputs():
    max_number = 1e308
    assert subtract(max_number, -max_number) == float('inf')
    assert subtract(-max_number, max_number) == float('-inf')
    assert subtract(max_number, max_number) == 0


# ====== test multiply ======

def test_multiply_integers():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(2, -3) == -6
    assert multiply(-2, -3) == 6
    assert multiply(0, 3) == 0
    assert multiply(3, 0) == 0

def test_multiply_floats():
    assert multiply(1.5, 2.5) == pytest.approx(3.75, rel=1e-9)
    assert multiply(-1.5, 2.5) == pytest.approx(-3.75, rel=1e-9)
    assert multiply(1.5, -2.5) == pytest.approx(-3.75, rel=1e-9)
    assert multiply(-1.5, -2.5) == pytest.approx(3.75, rel=1e-9)

def test_multiply_mixed_types():
    assert multiply(2, 2.5) == pytest.approx(5.0, rel=1e-9)
    assert multiply(-2, 2.5) == pytest.approx(-5.0, rel=1e-9)
    assert multiply(2.5, -2) == pytest.approx(-5.0, rel=1e-9)
    assert multiply(-2.5, -2) == pytest.approx(5.0, rel=1e-9)

def test_multiply_zero():
    assert multiply(0, 0) == 0
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0

def test_multiply_negative_and_positive():
    assert multiply(2, -3) == -6
    assert multiply(-3, 2) == -6
    assert multiply(-2, -3) == 6

def test_multiply_large_numbers():
    large_number = 1e308
    assert multiply(large_number, large_number) == float('inf')
    assert multiply(large_number, 0.5) == pytest.approx(0.5e308)
    assert multiply(-large_number, large_number) == float('-inf')
    assert multiply(large_number, -large_number) == float('-inf')


def test_multiply_small_numbers():
    small_number = 1e-154
    assert multiply(small_number, small_number) == pytest.approx(1e-308, rel=1e-9)
    assert multiply(-small_number, small_number) == pytest.approx(-1e-308, rel=1e-9)

def test_multiply_strings():
    with pytest.raises(TypeError):
        multiply("hello", "world")

def test_multiply_lists():
    with pytest.raises(TypeError):
        multiply([1, 2], [3, 4])

def test_multiply_tuples():
    with pytest.raises(TypeError):
        multiply((1, 2), (3, 4))

def test_multiply_none():
    with pytest.raises(TypeError):
        multiply(None, 5)

def test_multiply_nan():
    result = multiply(float('nan'), 1)
    assert isnan(result)
    result = multiply(float('nan'), float('nan'))
    assert isnan(result)

def test_multiply_infinity():
    assert multiply(float('inf'), 1) == float('inf')
    assert multiply(float('inf'), -1) == float('-inf')
    assert multiply(float('-inf'), 1) == float('-inf')
    assert multiply(float('-inf'), -1) == float('inf')
    assert isnan(multiply(float('inf'), 0))
    assert isnan(multiply(float('-inf'), 0))

def test_multiply_min_max_float():
    min_float = -1.7e308
    max_float = 1.7e308
    assert multiply(min_float, 0) == 0
    assert multiply(max_float, 0) == 0
    assert multiply(max_float, 1) == max_float
    assert multiply(min_float, 1) == min_float

    pos_overflow = multiply(max_float, 2)
    assert isinf(pos_overflow) and pos_overflow > 0

    neg_overflow = multiply(min_float, 2)
    assert isinf(neg_overflow) and neg_overflow < 0

def test_multiply_opposites():
    assert multiply(1, -1) == -1
    assert multiply(1e10, -1e10) == -1e20

def test_multiply_extreme_values():
    assert multiply(float('inf'), float('-inf')) == float('-inf')
    assert multiply(float('-inf'), float('inf')) == float('-inf')
    assert multiply(float('inf'), float('inf')) == float('inf')
    assert multiply(float('-inf'), float('-inf')) == float('inf')
