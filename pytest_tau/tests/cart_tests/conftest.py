import pytest


@pytest.fixture
def tc_set_up():
    print("Open Browser")
    print("Launch the website url:")
    print("Search for product")
    yield
    print("Logoff from website")
    print("Close the Browser")
    # Before the yield, it is setup and after yield is teardown
