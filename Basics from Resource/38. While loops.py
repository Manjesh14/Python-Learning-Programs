from math import sumprod

n=1
while n<=3:
    print(n)
    n+=1

# Sum of n Natural Numbers
n=int(input("Enter the number : "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i+=1
print(sum)

# Infinate loop
# n=200
# while True:
#     print(n)
#     n-=1

# Breaking Infinate loop

while True:
    line=input("Enter the line (enter 'q' to quit) : ")
    if line=='q':
        break
    print(line)

# While loop with else
fruits=['apple','banana','mango','strawberry']
index=0
fruit_found=False
while index<len(fruits):
    if fruits[index]=='orange':
        fruit_found=True
        print('orange is available')
        break
    index+=1
if not fruit_found:
    print("Orange not found")

# or
fruits=['apple','banana','mango','strawberry']
index=0
while index<len(fruits):
    if fruits[index]=='orange':
        print('orange is available')
        break
    index+=1
else:
    print("Orange not found")