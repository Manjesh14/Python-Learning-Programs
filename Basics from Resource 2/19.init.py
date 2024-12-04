class Student:
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("Adding new student to Database....")

s1=Student("Manjesh", 98)
print(s1.name)
print(s1.marks)

s2=Student("Ram",88)
print(s2.name)
print(s2.marks)