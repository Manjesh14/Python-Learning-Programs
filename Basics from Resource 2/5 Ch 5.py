# Loops in python
print("Hello")  #without loops
print("Hello")  #without loops
print("Hello")  #without loops
print("Hello")  #without loops
print("Hello")  #without loops

#Using loops(Iteration)
count=1                 #iterator
while count<=5:         #while condition
    print("Hello")      #Work
    count+=1            # updation

#print the numbers from 1 to 5
i=1
while i<=5:
    print(i)
    i+=1

#Practise
#Print the multiplication table of a number n
ir=1
while ir<=10:
    print(ir*3)
    ir+=1

# qs 4
#Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
#traverse
list=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
idx=0
while idx<=len(list)-1:
    print(list[idx])
    idx+=1

# Qs 5
#Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
Tup=(1, 4, 9, 16, 25, 36, 49, 64, 81,100,36)
x=36
idx2=0
while idx2<=len(Tup)-1:
    if(Tup[idx2]==x):
        print("Found at index",idx2)
        break                           #Terminates
    else:
        print("finding.....")
    idx2+=1

#Using Continue
iret=0
while iret<=10:
    if(iret==3):
        iret+=1
        continue
    print(iret)
    iret+=1    

# For Looops
list2=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for el in list2:
    print(el)

str="Manjesh"
for char in str:
    print(char)
else:
    print("END")

for char in str:
    if(char=="a"):
        print("a is found")
        break
    print(char)

#Qs1
# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

tup2=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
idx3=0
for a in tup2:
    if(a==(a%2==0)):
        print("Number found at index", idx3)
        continue
    idx3+=1    

#Range function
seq=range(5)
for nu in seq:
    print(nu)

for el in range(1,10,2):
    print(el)

#pass Statement
for i in range(50):
    pass

# Practise
# WAP to find the sum of first n numbers. (using while)
n=5
sum=0
for i in range(1,n+1):
    sum+=i

print(sum)

# WAP to find the factorial of first n numbers. (using for)
n=5
fact=1
z=1
while z<=n:
    fact*=z
    z+=1

print(fact)