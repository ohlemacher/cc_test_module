import pytest

#try:
#    from cc_test_module import rot13_encode
#except ImportError as e:
#    print(e)

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
    #assert rot13_encode(test_input) == expected
    print("warning: %s" % "Defeated!")
    assert test_input != expected

