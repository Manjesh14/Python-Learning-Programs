for i in range(1,500):
    s=0
    c=i
    while c!=0:
        a=c%10
        s=s+(a**3)
        c=c//10
    if s==i:
        print(i)