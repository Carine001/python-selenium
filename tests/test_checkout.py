import pytest

from scripts.checkout import Checkout


@pytest.fixture()
def checkout_init():
    checkout = Checkout()
    checkout.add_item_price("a", 1)
    checkout.add_item_price("b", 2)
    return checkout


def test_can_calculate_total(checkout_init):
    checkout_init.add_item("a")
    assert checkout_init.calculate_total() == 1


def test_get_correct_total_with_multiple_items(checkout_init):
    checkout_init.add_item("a")
    checkout_init.add_item("b")
    assert checkout_init.calculate_total() == 3


def test_can_add_discount_rule(checkout_init):
    checkout_init.add_discount("a", 3, 2)


def test_can_apply_discount_rule(checkout_init):
    checkout_init.add_discount("a", 3, 2)
    checkout_init.add_item("a")
    checkout_init.add_item("a")
    checkout_init.add_item("a")
    assert checkout_init.calculate_total() == 2


def test_exception_with_bad_item(checkout_init):
    with pytest.raises(Exception):
        checkout_init.add_item("c")
