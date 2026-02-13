import pytest
from fuel import convert,gauge

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_xmorethany():
    with pytest.raises(ValueError):
        convert("2/1")

def test_normal():
    assert convert("2/3") == 67

def test_e():
    assert gauge(1) == "E"

def test_f():
    assert gauge(99) == "F"

def test_percent():
    assert gauge(67) == "67%"
