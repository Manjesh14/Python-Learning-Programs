rows=int(input("Enter the number of rows : "))
for i in range(rows,0,-1):
    for space in range(1,(rows-i+1)):
        print(end=' ')
    for star in range(1,i+1):
        print("*", end=' ')
    print()
for i in range(1,rows+1):
    for space in range(1,(rows-i+1)):
        print(end=' ')
    for star in range(1,i+1):
        print("*", end=' ')
    print()



for i in range(rows,0,-1):
    diff=rows-i
    print(' '*diff,"* "*i,sep='')
for i in range(1,rows+1):
    diff=rows-i
    print(' '*diff,"* "*i,sep='')
