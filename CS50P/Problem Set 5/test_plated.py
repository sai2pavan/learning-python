import pytest
from plated import is_valid

def test_starttwoletters():
    assert is_valid("CS50") == True
    assert is_valid("c50") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False

def test_othercharacters():
    assert is_valid("AA!@50)") == False

def test_numbersend():
    assert is_valid("ZB20XB") == False