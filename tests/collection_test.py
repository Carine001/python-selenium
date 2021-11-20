import pytest


# will be running before each test
@pytest.fixture
def numbers():
    abc = 10
    mno = 20
    xyz = 30
    return [abc, mno, xyz]


# def test_number_in_array(numbers):
#     x = 15
#     assert numbers[0] == x


def test_number_not_in_array(numbers):
    variable = 20
    assert numbers[1] == variable
