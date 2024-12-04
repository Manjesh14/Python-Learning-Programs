# Accessing Characters of a String
name="Manjesh"
for c in name:
    print(c , end=' ')
print("\n")

# Iterating a string in Reverse order
for a in name[::-1]:
    print( a, end=' ')

# Accessing Words of a String
sentence="My name is Manjesh"
count=0
for word in sentence.split():
    count += 1
    print(word, end='\t')
print(f"\nThere are {count} words in sentence.")