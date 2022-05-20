def main():
    fraction=input("Fraction: ")
    convertion=convert(fraction)
    output=gauge(convertion)
    print(output)

def convert(fraction):
    while True:
        try:
            x,y=fraction.split("/")
            z=int(x)
            w=int(y)
            d=z/w
            if d<=1:
                per=int(d*100)
                return per
            else:
                fraction=input("Fraction: ")
                pass
        except(ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <=1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()