rows=int(input("Enter the number of Rows : "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
for i in range(rows-1,0,-1):
    for j in range(i,0,-1):
        print('*', end=' ')
    print()
