import random, pyfiglet, sys
from pyfiglet import Figlet
figlet=Figlet()
fonts=figlet.getFonts()
rand=random.choice(fonts)

if len(sys.argv)<2:
    y=Figlet(font=rand)
    x=input("Input: ").strip()
    print(y.renderText(x))
elif len(sys.argv)>2 and ((sys.argv[1])==("-f") or (sys.argv[1])==("--font")):
    if sys.argv[2] in fonts:
        y=Figlet(font=sys.argv[2])
        x=input("Input: ").strip()
        print(y.renderText(x))
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")