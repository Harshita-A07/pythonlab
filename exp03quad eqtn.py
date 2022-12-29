import math
a=int(input("enter a:")) 
b=int(input("enter b:"))
c=int(input("enter c:")) 
d= (b**2)-(4*a*c)
sq=math.sqrt(abs(d))
if a==0:
    print("enter the coefficients correctly")
elif d>0:
    print("real and different roots")
    print((-b-sq)/(2*a))
    print((-b+sq)/(2*a))
else:
    print("complex roots")
    print((-b+sq)/(2*a))
    print((-b-sq)/(2*a))
