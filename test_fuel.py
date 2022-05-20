from Week_6.fuel import convert, gauge
import pytest

def test_random():
    assert convert("1/4")==25 and gauge(25)=="25%"
    assert convert("1/100")==1 and gauge(1)=="E"
    assert convert("99/100")==99 and gauge(99)=="F"

def test_ZD():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("100/0")

def test_VE():
    with pytest.raises(ValueError):
        convert("hello/world")
        convert("car/crash")