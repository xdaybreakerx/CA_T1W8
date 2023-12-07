import pytest

from calculator import add, subtract, division, convert_to_list

#  test, test, is pytest on?
def test_basic():
    assert "" == ""

def test_add():
    assert add(2, 3) == 5
    assert add(10, 5) == 15
    assert add(4781, 1378) == 6159
    assert add(0, -2) == -2
    
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(5, -7) == 12
    
def test_divison():
    assert division(10, 2) == 5
    
def test_divison_raise_exception():
    with pytest.raises(Exception):
        division(10, 0)
        
def test_convert():
    assert 5 in convert_to_list(3, 4, 5)