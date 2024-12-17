import pytest
from techtest03.digital_root import digital_root


def test_case_1():
    assert digital_root(1) == 1
    assert digital_root(16) == 7
    assert digital_root(942) == 6
    assert digital_root(132189) == 6
    assert digital_root(493193) == 2
