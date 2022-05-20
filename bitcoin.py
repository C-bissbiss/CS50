import requests, sys

if len(sys.argv)==2:
    try:
        total=float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    r=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data=r.json()
    btc=data['bpi']['USD']['rate_float']
    amount=btc*total
except requests.RequestException:
    print("")
    sys.exit(1)

print(f"${amount:,.4f}")