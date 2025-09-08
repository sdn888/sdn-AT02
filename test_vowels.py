import pytest
from vowels import count_vowels

def test_all_vowels():
    assert count_vowels("aeiou") == 5
    assert count_vowels("АЕЁИОУЫЭЮЯ") == 10

def test_no_vowels():
    assert count_vowels("bcdfg") == 0
    assert count_vowels("йцкнш") == 0

def test_mixed_string():
    assert count_vowels("Hello World") == 3   # e, o, o
    assert count_vowels("ПрИвЕт Мир") == 3   # и, е, и

@pytest.mark.parametrize("text, expected", [
    ("Python", 1),       # o
    ("sky", 0),          # no vowels
    ("OpenAI", 4),       # o, e, a, i
    ("мама мыла раму", 6)
])
def test_parametrized(text, expected):
    assert count_vowels(text) == expected
