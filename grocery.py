grocerylist={}

while True:
    try:
        item = input().lower()
        if item in grocerylist:
            grocerylist[item]+=1
        else:
            grocerylist[item]=1
    except EOFError:
        for x in sorted(grocerylist.keys()):
            print(grocerylist[x], x.upper())
        break