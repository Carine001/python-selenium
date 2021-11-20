import pytest


def addition(a, b):
    return a + b


def multiplication(a, b):
    return a * b


@pytest.mark.one
def test_addition_should_work():
    # arrange
    a = 1
    b = 2

    # act
    result = addition(a, b)

    # assert
    assert result == 3


# @pytest.mark.two
# def test_addition_should_fail():
#     # arrange
#     a = 2
#     b = 2

#     # act
#     result = multiplication(a, b)

#     # assert
#     assert result == 5


def test_letter_should_be_in_string():
    # arrange and act
    word = "Hello"

    # assert
    assert "e" in word


# def test_letter_should_not_be_in_string():
#     # arrange and act
#     word = "Hello"

#     # assert
#     assert 'f' in word
