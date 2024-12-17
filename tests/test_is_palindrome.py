import pytest
from techtest02.palindrome import is_palindrome


def test_case_1():
    assert is_palindrome("kayak") == True
    assert is_palindrome("Kayak") == False
    assert is_palindrome("Python") == False
    assert is_palindrome("python") == False
