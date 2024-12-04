# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    s=0
    if n==0:
        return 0
    return n+sum(n-1)
x = int(input("Enter the value of n : "))
print(sum(x))