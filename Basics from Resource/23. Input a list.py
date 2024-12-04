# problem with input() method
numbers=input("Enter the list of numbers")
print(numbers)

# Taking input using loops
n=int(input("Enter the number of elements : "))
num=[]
for i in range(n):
    x=int(input())
    num.append(x)
print(num)

# Taking input using split() Method
num2=input("Enter the elements of the list : ")
num2=num2.split()
print(num2)

# Taking input using split() and for loop Method
n2=int(input("Enter the number of elements : "))
num3=input("Enter the elements of the list : ")
num3=num3.split()
for i in range(0,n2):
    num3[i]=int(num3[i])
print(num3)