import pytest
from bank import value

def test_uppercase():
    assert value("HELLO") == "$0"
def test_lowercase():
    assert value("hello") == "$0"

def test_startswithh():
    assert value("hola") == "$20"
    assert value("Hi") == "$20"

def test_othercharacters():
    assert value("!hello") == "$100"
    assert value("_crazy") == "$100"

def test_invalid():
    with pytest.raises(AttributeError):
        value(123)

def test_empty():
    assert value("") == "$100"

