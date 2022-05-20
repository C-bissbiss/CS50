amountdue=50
while amountdue>0 and amountdue<=50:
    print("Amount Due: ", amountdue)
    amountinserted=int(input("Insert Coin: "))
    if amountinserted in [25, 10 , 5]:
        amountdue-=amountinserted

changeowed=abs(amountdue)

print("Change Owed:",changeowed)