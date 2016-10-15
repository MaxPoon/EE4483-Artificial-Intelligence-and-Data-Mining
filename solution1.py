x=float(input("Please enter the value of x: "))
if x==0:
    print("x^(3/5) is 0")
if x>0:
    if x<1:
        left = x
        right = 1
    else:
        left = 1
        right = x
else:
    if x>-1:
        left = -1
        right = x
    else:
        left = x
        right = -1
x3=x**3
error = 0.000001
while(True):
    mid = (left+right)/2
    mid5=mid**5
    if abs(mid5-x3)<error:
        print("x^(3/5) is "+str(mid))
        break
    if mid5<x3:
        left = mid
    else:
        right = mid