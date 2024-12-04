x=10
y=20
z=30

#Logical AND
print(x>y and y>z)
print(y>x and z>y)
print(y>x and z<y)

#Logical OR
print(x>y or y>z)
print(y>x or z>y)
print(y>x or z<y)

#Logical NOT
print(not(x>y or y>z))
print(not(y>x or z>y))
print(not(y>x or z<y))