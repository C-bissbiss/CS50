import inflect
p=inflect.engine()

strg=["Adieu", "adieu"]

while True:
    try:
        x=input("Name: ")
    except EOFError:
        print()
        break
    strg.append(x)

strg[2]="to "+strg[2]

if len(strg)==3:
    salutations=p.join(strg, conj='')
elif len(strg)==4:
    salutations=p.join(strg, final_sep='')
else:
    salutations=p.join(strg)

print(salutations)