class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        print(self.real,"i+",self.img,"j")

    def __add__(self,num2):
        newr=self.real+num2.real
        newi=self.img+num2.img
        return complex(newr,newi)
    
num1=complex(1,2)
num1.show()
num2=complex(4,5)
num2.show()
num3=num1+num2
num3.show()