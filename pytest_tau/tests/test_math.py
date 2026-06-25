import pytest


def test_one_plus_one():
    assert 1 + 1 == 2


def test_one_plus_two():
    a = 1
    b = 1
    c = 0
    assert a + b == c


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    # print(f"\nCaptured message: {e.value}")
    # command to run: python -m pytest -s
    assert "division by zero" in str(e.value)
