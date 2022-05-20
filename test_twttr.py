from Week_6.twttr import shorten

def test_lower():
    assert shorten("twitter")=="twttr"
    assert shorten("what's your name?")=="wht's yr nm?"
    assert shorten("cs")=="cs"

def test_cap():
    assert shorten("TwItTEr")=="TwtTr"
    assert shorten("What's your naMe?")=="Wht's yr nM?"
    assert shorten("CS")=="CS"

def test_num():
    assert shorten("1200")=="1200"
    assert shorten("50csas")=="50css"
    assert shorten("CS50")=="CS50"