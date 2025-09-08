import pytest
from main import check
from main import isPalindrome

def test_check():
    assert check(6) == True

def test_check2():
   assert check(3) == False

@pytest.mark.parametrize("number, expected", [
   (2, True),
   (5, False),
   (0, True),
   (56, True),
   (0, True)
])

def test_check_with_param(number, expected):
   assert check(number) == expected

def test_isPalindrome():
    assert isPalindrome('madam') == True
    assert isPalindrome('hello') == False

@pytest.mark.parametrize("test_input,expected", [
    ('level', True),
    ('python', False),
    ('racecar', True),
    ('', True),
])

def test_isPalindrome(test_input, expected):
    assert isPalindrome(test_input) == expected
