n=int(input("Enter an integer : "))
if n<=1:
    print(f"{n} is neither prime nor composite")
elif n>1:
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is a composite number")
            print(f"{i} is a factor of {n}")
            break
    else:
        print(f"{n} is a prime number")
