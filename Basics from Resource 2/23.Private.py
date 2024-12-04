class Account:
    def __init__(self,accno,accpass):
        self.accno=accno
        self.__accpass=accpass
    def passw(self):
        print(self.__accpass)

A1=Account(12345,"Manje")
print(A1.accno)
# print(A1.__accpass)

print(A1.passw())