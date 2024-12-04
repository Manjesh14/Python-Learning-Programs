class Student:
    college_name="P E S University Banglore"
    name="anonymus"
    def __init__(self,name,maths,ECE,English):
        self.name=name
        self.maths=maths
        self.ECE=ECE
        self.English=English
    def welcome(self):
        print("Hello ",self.name)
    def avg(self):
        print(f"{self.name}'s average marks is {(self.maths+self.ECE+self.English)/3}")

n=input("Enter Student's name : ")
m=int(input("Enter Maths marks : "))
Ec=int(input("Enter ECE marks : "))
e=int(input("Enter English marks : "))
s1=Student(n,m,Ec,e)
s1.welcome()
s1.avg()