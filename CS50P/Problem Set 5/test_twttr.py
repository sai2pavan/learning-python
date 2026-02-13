import pytest
from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_mixedcase():
    assert shorten("tWITTer") == "tWTTr"

def test_Novowels():
    assert shorten("twttr") == "twttr"

def test_Allvowels():
    assert shorten("aeiou") == ""

def test_Emptyinput():
    assert shorten("") == ""

def test_Noncharacters():
    assert shorten("hello!") == "hll!"

def test_numbers():
    assert shorten("CS50P") == "CS50P"

def test_invalid():
    with pytest.raises(TypeError):
        shorten(123)