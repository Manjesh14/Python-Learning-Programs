from math import factorial
rows=int(input("Enter the number of rows : "))
for i in range(rows):
    for spaces in range(1,rows-i):
        print(end=' ')
    for n in range(i+1):
        ncr=factorial(i)//(factorial(n)*factorial(i-n))
        print(ncr, end=' ')
    print()
