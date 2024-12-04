#append
num=[1,2,3,2,4]
num2=["I",'am','Manjesh']
num.append(int(input("Enter a number : ")))
print(num)

#Extend
num.extend(num2)
print(num)

#Insert
num.insert(2,3)
print(num)

#Remove
num.remove('am')
print(num)

#Sorting
name=["Manjesh","Akshay","Ram","Manjula"]
name.sort()
print(name)

#Reverse
name.reverse()
print(name)

#POP
pop_name=name.pop(2)
print(name)
print(pop_name)

#Index
print(num.index(3))

# Count
print(name.count('Ram'))

# Copy
name2=name.copy()
print(name2)

#Clear
name.clear()
print(name)
