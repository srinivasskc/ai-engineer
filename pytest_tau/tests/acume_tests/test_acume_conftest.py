import pytest
from my_package.acume import Accumulator


"""
We can add the fixture in the same test program or can be added in specific file "conftest.py" - name of file is specific.
"""
# @pytest.fixture
# def accum():
#     return Accumulator()


def test_accumulator_init(accum, accum1):  # Dependency Injection
    assert accum.count == 0


def test_accumulator_add_one(accum, accum2):
    accum.add()  # Act - Execute the target behavior
    assert accum.count == 1  # Assert - Verify the outcome.


def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2


def test_accumulator_cannot_set_value_to_count(accum):
    with pytest.raises(
        AttributeError, match=r"property 'count' of 'Accumulator' object has no setter"
    ):
        accum.count = 10


# Running the tests:
# (my_env) F:\Career\ai_engineer\pytest_tau>python -m pytest tests/test_acume.py
# 5 passed in 0.03s
