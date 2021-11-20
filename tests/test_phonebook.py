import pytest

from scripts.phonebook import Phonebook


@pytest.fixture
def phonebook():
    return Phonebook()


# @pytest.fixture
# def phonebook():
#     phonebook = Phonebook()
#     yield phonebook
#     phonebook.clear()


# @pytest.fixture
# def phonebook(temp_directory):
#     return Phonebook(temp_directory)
#     # after the test is run, the temp_directory will be deleted by Pytest


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert phonebook.lookup("Bob") == "1234"


def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()


def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
