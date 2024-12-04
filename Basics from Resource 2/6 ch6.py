#Functions in python
def sum(a,b):
    sum=a+b
    print(sum)
    return sum

sum(2,1)                #Calling of Functions
sum(5,6)                #Calling of Functions


#Similarly
def calc(x,y=3):
    return x+y

print(calc(1))

def print_hello():
    print("hello")

s=1
while s<=5:
    print_hello()
    s+=1

#Practise qs
# Qs1 
# WAF to print the length of a list. ( list is the parameter) 
cities=["Kollegal","Mysore","Banglore","Delhi"]
heroes=["Prabhas","Yash", "Allu","Ram","Ravi"]

def length(list):
    print(len(list))

length(cities)

print(cities[0] ,end=" ")
print(cities[1]) 

def printlist(list):
    for el in list:
        print(el, end=" ")

printlist(heroes)
print("\n")

# WAF to find the factorial of n. (n is the parameter)
# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

def calcfact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(fact)

calcfact(10)


# WAF to convert USD to INR.

def converter(usd):
    inr=usd*83
    print(usd, "Usd =", inr,"inr")

converter(10)

#Recursion
#Recursive functions
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))

# Qs 1
#Write a recursive function to calculate the sum of first n natural numbers
def calsum(n):
    if(n==0):
        return
    print(n)
    return calsum(n-1)+n

print(calsum(5))

# Write a recursive function to print all elements in a list.
def prilist(list,idx):
    if(idx==len(list)):
        return
    print(list[0])
    prilist(list,idx+1)

prilist(cities)
