import pytest

from scripts.phonebook import Phonebook


@pytest.fixture
def phonebook():
    return Phonebook()


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert phonebook.lookup("Bob") == "1234"


def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()


def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
