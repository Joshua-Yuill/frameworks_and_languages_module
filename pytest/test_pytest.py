from calc import *
import pytest

def test_add():
    assert add(1, 2) == 3
    assert add(1, -2) == -1
    assert add(1000000000000000000, 2) == 1000000000000000002

def test_multiply():
    assert multiply(1,2) == 2
    assert multiply(69,69) == 4761
    assert multiply(0.0001 , 27) == 0.0027

def test_div():
    assert div(1,2) == 0.5
    assert div(69,69) == 1
    with pytest.raises(ZeroDivisionError):
        div(1,0)