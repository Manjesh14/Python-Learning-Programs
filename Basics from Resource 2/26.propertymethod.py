class Student:
    def __init__(self,p,c,m):
        self.p=p;
        self.c=c;
        self.m=m;

    @property
    def per(self):
        return str(int((self.p + self.c + self.m)/3)) + "%"
    
s1=Student(95,87,95)
print(s1.per())
s1.c=99
print(s1.per())