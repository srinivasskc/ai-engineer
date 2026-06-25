import pytest

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

# The equivalence class values can be stored as tuple. Each test value in one pair.

multiply_data = [
    (2, 2, 4),
    (-2, -2, 4),
    (6, 1, 6),
    (6, 0, 0),
    (10, -2, -20),
    (2.0, 2.0, 4.0),
    (6, 2.0, 12.0),
    (-2.0, -2.0, 4.0),
]


# parametrize has two parameters - 1st: func parameters in quotes, 2nd: tuple name
@pytest.mark.parametrize("a,b,result", multiply_data)
def test_multiply_param(a, b, result):
    assert a * b == result
