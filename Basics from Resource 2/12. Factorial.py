#WAF to find the factorial of n. (n is the parameter)

n=int(input("Enter the number for which you want factorial : "))

def factorial():
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)

factorial()