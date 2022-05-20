from datetime import datetime, date


today = datetime.now()
one_year_ago = today.replace(year=today.year-1)

def questions():
    global dividend, ticker, optiontype, K, expiry
    i = 0
    while i < 2:
        dividend = input("Does the security yields cash dividends? ").lower().strip()
        if any(dividend == f for f in ['yes', 'no']):
            break
        else:
            i += 1
            if i < 2:
                print("Please enter YES or NO")
            else:
                print("Too many errors, please restart")
                quit()
    ticker = input('What is the ticker of the security? ').lower().strip()
    while i < 2:
        optiontype = input('Is it a Call or a Put? ').lower().strip()
        if any(optiontype == f for f in ['call', 'put']):
            break
        else:
            i += 1
            if i < 2:
                print("Please enter CALL or PUT")
            else:
                print("Too many errors, please restart")
                quit()
    while i < 2:
        try:
            K = float(input("What is the strike price? $ "))
            break
        except ValueError:
                i += 1
                if i < 2:
                    print("The entered value is not a float")
                else:
                    print("Nothing done")
                    quit()
    expiry = input('What is the date of expiration(yyyy-mm-dd)? ').strip()
questions()