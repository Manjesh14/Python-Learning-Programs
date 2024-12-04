# Creating class
class Student:
    Name="Manjesh"
    def __init__(self,fullname):
        self.name=fullname
        print("adding new student ")

s1=Student()
print(s1.Name)

class Cars:
    color="Blue"
    brand="Mercedes"

car1=Cars()
print(car1.color)
print(car1.brand)
