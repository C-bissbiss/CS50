from Week_6.plates import is_valid

def test_1():
    assert is_valid("hello, world")==False
    assert is_valid("23")==False
    assert is_valid("c")==False

def test_2():
    assert is_valid("cs50")==True
    assert is_valid("CS50")==True

def test_3():
    assert is_valid("cs.!50")==False
    assert is_valid("cs.50")==False

def test_4():
    assert is_valid("CS 05")==False
    assert is_valid("CS05")==False
    assert is_valid("cs50p")==False
    assert is_valid("CS50p")==False