# Break Statement
numbers=list(range(0,100))
for number in numbers:
    if number > 50:
        break
    print(number, end=' ')

print("\n")

while True:
    num=input("Enter the number (q for quit ) : ")
    if num=='q':
        break
    print(num)

# Continue Statement
for i in range(0,5):
    if i == 2 or i==4:
        continue
    print(i)

print("\n")

n=0
while n<=10:
    n+=1
    if n%2!=0:
        continue
    print(n,end="\t")

