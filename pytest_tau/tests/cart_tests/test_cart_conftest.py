import pytest

# Using Conftest.py


@pytest.mark.item
def test_add_item_to_cart(tc_set_up):
    print("Added Item to Cart Successfully")


@pytest.mark.item
def test_remove_item_from_cart(tc_set_up):
    print("Removed Item from Cart Successfully")
