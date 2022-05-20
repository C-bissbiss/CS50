import random

while True:
    try:
        x=int(input("Level: "))
        if x>0:
            break
    except:
        pass

natural=int(x)
answer=random.randint(1,natural)

while True:
    try:
        guess=int(input("Guess: "))
        if guess>0:
            if guess<answer:
                print("Too small!")
            elif guess>answer:
                print("Too large!")
            elif guess==answer:
                print("Just right!")
                break
    except:
        pass