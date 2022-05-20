def main():
    x=input("What time is it? ")
    time=convert(x)
    if time >=7 and time <=8:
        print("breakfast time")
    elif time >=12 and time <=13:
        print("lunch time")
    elif time >=18 and time <=19:
        print("dinner time")

def convert(time):
    h, minutes=time.split(":")
    min=float(minutes)/60
    return float(h)+min


if __name__ == "__main__":
    main()