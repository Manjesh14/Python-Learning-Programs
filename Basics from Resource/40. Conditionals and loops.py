# Sum of n natural numbers
n=int(input("Enter the number till which you want sum : "))
sum=0
for i in range(n+1):
    sum=sum+i
print("Sum of ",n," natural numbers is = ",sum)
