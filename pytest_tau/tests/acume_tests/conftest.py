import pytest
from my_package.acume import Accumulator


@pytest.fixture
def accum():
    return Accumulator()


# Fixture with Yield and post-print()
@pytest.fixture
def accum1():
    yield Accumulator()
    print("Done with testing accum1")


# Fixture with Scope = Function
@pytest.fixture
def accum2(scope="Function"):
    yield Accumulator()
    print("Done with testing accum1")
