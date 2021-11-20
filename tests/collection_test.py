import pytest


# will be running before each test
@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 30
    return [a, b, c]


# def test_number_in_array(numbers):
#     x = 15
#     assert numbers[0] == x


def test_number_not_in_array(numbers):
    x = 20
    assert numbers[1] == x
