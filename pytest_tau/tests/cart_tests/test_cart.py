import pytest


@pytest.fixture
def set_up():
    print("Open Browser")
    print("Launch the website url:")
    print("Search for product")
    yield
    print("Logoff from website")
    print("Close the Browser")
    # Before the yield, it is setup and after yield is teardown


def test_add_item_to_cart(set_up):
    print("Added Item to Cart Successfully")


def test_remove_item_from_cart(set_up):
    print("Removed Item from Cart Successfully")
