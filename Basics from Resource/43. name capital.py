name=input("Enter your name : ")
print("Hi",end=' ')
for word in name.split():
    print(word.title(), end=' ')