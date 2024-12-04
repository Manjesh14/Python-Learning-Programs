#Basic Strings
str1="This ia a string.\nWe are creating in Python"
print(str1)
str2="This ia a string.\tWe are creating in Python"
print(str2)

#Concatination
Str1="Hello"
Str2=" World"
Final_Str= (Str1+Str2)
print(Final_Str)

#Length of string
print(len(Final_Str))

#Indexing
a = "Manjesh T S"
X=(a[5])
print(X)

#Slicing 
A="Apna College"
print(A[ :4])  #[0:4]
print(A[5: ])  #[5:len(A)]
print(A[ :-1])

#String Functions
str= "i am Studying Coding from Apna College"
print(str.endswith("ege"))
str=str.capitalize()
print(str)
print(str.replace("Coding" , "Python"))
print(str.find("Co"))
print(str.count("a"))

# Practise Questions
#Question 1
name=input("Enter your name")
print("You name has",len(name),"Characters")
print("Thank You")
