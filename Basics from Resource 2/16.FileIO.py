f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
data2= f.read(5)
print(data2)
line1= f.readline()
print(line1)
line2= f.readline()
print(line2)

f.close()


e=open("demo.txt","w")
e.write("I am studying in Banglore")
e.close()

o=open("demo.txt","a")
o.write("\nI am in Banglore")
o.close()

e=open("demo.txt","r+")
e.write('abc')
e.close()

with open("demo.txt","r") as f:
    data=f.read()
    print(data)

with open("demo.txt","w") as f:
    data=f.write("New Data")
    print(data)
