import pytest


# with fixture - autouse=True, no need to specifically provide the  fixture: tc_set_up and it is automatically called.


# Session Scope: Created once for the entire test suite execution.
# (Set up and tear down once for each test session i.e comprising one or more test files)
# @pytest.fixture(scope="session", autouse=True)


# Function Scope:(Set up and tear down once for each test function)
# @pytest.fixture(scope="function", autouse=True)


@pytest.fixture(scope="function", autouse=True)
def tc_set_up():
    print("===Fixture Start===")
    print("Open Browser")
    print("Launch the website url:")
    print("Search for product")
    yield
    print("===TEARDOWN===")
    print("Logoff from website")
    print("Close the Browser")
    # Before the yield, it is setup and after yield is teardown


# TBD: Fixtures with other scopes
