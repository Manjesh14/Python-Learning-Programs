import math

a=int(input("Enter the Value of a : "))
b=int(input("Enter the Value of b : "))
c=int(input("Enter the Value of c : "))
d=b*b-(4*a*c)
if d<0:
    sol1=-b/(2*a)
    sol2=math.sqrt(-d)/(2*a)
    print("Solutions are : \n",complex(sol1,sol2))
    print(complex(sol1,-sol2))

else:
    sol1=-(b-math.sqrt(d))/(2*a)
    sol2=-(b+math.sqrt(d))/(2 * a)
    print("Solutions are = \n",sol1)
    print(sol2)