import pytest
from cc_test_module.cc_test_module import rot13_encode

"""
Unit test cc_test_module.py
  python -m pytest -v test_cc_test_module.py
"""

@pytest.mark.parametrize("test_input, expected", [
    ("foo", "sbb"),
	("sbb", "foo"),
    ("bar", "one"),
    ("one", "bar"),
])
def test_rot13_encode(test_input, expected):
    assert rot13_encode(test_input) == expected
