s=input("Enter a string : ")
d,l,o=0,0,0
for c in s:
    if c.isdigit():
        d+=1
    elif c.isalpha():
        l+=1
    else:
        o+=1

print(f"Digits             : {d}")
print(f"Letters            : {l}")
print(f"other Characters   : {o}")