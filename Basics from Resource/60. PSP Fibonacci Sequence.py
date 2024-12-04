a=0
b=1
fibo=0
n=int(input("Enter the number of terms : "))
if n==1:
    print(f"0")
elif n==2:
    print(f"0\n1")
else:
    print(f"0\n1")
    for i in range(1,n-1):
        fibo=a+b
        a=b
        b=fibo
        print(fibo)