numbers=list(range(1,25))
odd=[]
even=[]

for i in numbers:
    if i%2==0:
        even.append(i)
    if i%2!=0:
        odd.append(i)
print("Even numbers", end='\n')
print(even)
print("Odd numbers", end='\n')
print(odd)
