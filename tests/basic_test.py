import pytest


def addition(first, second):
    return first + second


def multiplication(first, second):
    return first * second


@pytest.mark.one
def test_addition_should_work():
    # arrange
    first = 1
    second = 2

    # act
    result = addition(first, second)

    # assert
    assert result == 3


# @pytest.mark.two
# def test_addition_should_fail():
#     # arrange
#     first = 2
#     second = 2

#     # act
#     result = multiplication(first, second)

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
#     assert "f" in word
