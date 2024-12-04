num=int(input("Enter a 3 digit number : "))
sum1=0
temp=num
while temp>0:
    digit=temp%10
    sum1=sum1+(digit**3)
    temp//=10
if num==sum1:
    print(f"The number {num} you have entered is Armstrong number")
else:
    print(f"The number {num} you have entered is not Armstrong number")
