x=float(input("Please enter the value of x: "))
x3=x**3
error = 0.000001
y=x/2
while True:
    y5=y**5
    if abs(y5-x3)<error:
        print("x^(3/5) is " + str(y))
        break
    y=y-(y5-x3)/(5*(y**4))