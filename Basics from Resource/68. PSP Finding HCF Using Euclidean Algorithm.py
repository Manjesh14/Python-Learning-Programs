num1=int(input("Enter the first number  : "))
num2=int(input("Enter the second number : "))
if num1<num2:
    num1,num2=num2,num1

# Using Euclidean Algorithm
while num2!=0:
    num1,num2=num2,num1%num2

print(f"HCF is = {num1}")
