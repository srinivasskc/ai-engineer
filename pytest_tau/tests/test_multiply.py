"""
Multiplication Equivalence Classes - Tests
1. Positive by Positive: 2*2=4
2. Negative by Negative: -2*-2=4
3. Any Number by 1: 6x1=6
4. Any Number by zero: 6x0=0
5. Positive by Negative: 10*-2=-20
6. Float by Float: 2.0*2.0=4.0
7. Integer by Float: 6*2.0=12.0
8. Negative Float by Negative Float: -2.0*-2.0=4.0
"""

# To Run: Specific File - python -m pytest test_multiply.py


def test_multiply_positive_by_positive_ints():
    assert 2 * 2 == 4


def test_multiply_negative_by_negative_ints():
    assert -2 * -2 == 4


def test_multiply_any_number_positive_by_one_ints():
    assert 6 * 1 == 6


def test_multiply_any_number_positive_by_zero_ints():
    assert 6 * 0 == 0


def test_multiply_positive_by_negative_ints():
    assert 10 * -2 == -20


def test_multiply_positive_by_positive_float():
    assert 2.0 * 2.0 == 4.0


def test_multiply_positive_int_by_float_positive():
    assert 6 * 2.0 == 12.0


def test_multiply_negative_by_negative_floats():
    assert -2.0 * -2.0 == 4.0
