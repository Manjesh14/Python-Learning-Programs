n=input("Enter the number : ")
n=int(n)
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        print("%d is not a prime number"%n)
        break

if flag==0:
    print("%d is a prime number"%n)