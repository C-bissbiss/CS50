from Week_6.bank import value

def test_lower():
    assert value("hello")==0
    assert value("hello, newman?")==0
    assert value("how are you doing")==20
    assert value("what's happening?")==100

def test_caps():
    assert value("Hello")==0
    assert value("Hello, Newman?")==0
    assert value("How are you doing")==20
    assert value("What's HappeninG?")==100