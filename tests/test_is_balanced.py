import pytest
from techtest04.is_balanced import is_balanced


def test_case_1():
    assert is_balanced("{}") == True
    assert is_balanced("{}{") == False
