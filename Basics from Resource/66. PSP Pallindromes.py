s=input("Enter a string : ")
s=s.replace(" ","")
s=s.lower()
start=0
end=len(s)-1
flag=True
while start != end:
    if s[start]!=s[end]:
        flag=False
    start +=1
    end-=1
if flag:
    print("The String is a palindrome")
else:
    print("The string is not a palindrome")

