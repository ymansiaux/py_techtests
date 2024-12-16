import pytest
from techtest01.first_non_repeating_letter import first_non_repeating_letter


def test_case_1():
    assert first_non_repeating_letter("aabbcdd") == "c"
    assert first_non_repeating_letter("abcabc") is None
    assert first_non_repeating_letter("swiss") == "w"
    assert first_non_repeating_letter("") is None
    assert first_non_repeating_letter("abracadabra") == "c"
