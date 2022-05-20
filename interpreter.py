expression=input("Expression: ")
x, y, z= expression.split(" ")
floatx=float(x)
floatz=float(z)
if y=="+":
    answer=floatx+floatz
if y=="-":
    answer=floatx-floatz
if y=="*":
    answer=floatx*floatz
if y=="/":
    answer=floatx/floatz

print(round(answer,1))