rows=int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    diff=rows-i
    print(' '*diff,'*'*i,sep='')
for j in range(rows-1,0,-1):
    diff=rows-j
    print(' '*diff,'*'*j,sep='')

for j in range(1,rows):
    for i in range(1,j+1):
        print("*", end=" ")
    print()
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print("*", end=' ')
    print()