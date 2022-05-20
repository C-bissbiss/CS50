from Week_6.hello import hello

def test_default():
    assert hello()=="hello, world"
def test_argument():
    assert hello("Charles")=="hello, Charles"