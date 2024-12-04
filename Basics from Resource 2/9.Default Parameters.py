def cal_prod(a,b):
    print(a*b)
    return a*b

# cal_prod()            # Error

def calc_prod(x=1,y=2):
    print(x*y)
    return x*y

calc_prod()

def calprod(p,q=2):
    print(p*q)
    return p*q

calprod(2)

# def calcprod(s=0,t):      #Error
#     print(s*t)
#     return s*t