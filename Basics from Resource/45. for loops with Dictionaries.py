# Iterate over a Dictionary
course={'name':'Python','instructor':'Jaspreet'}
for x in course:
    print(x)

# Accessing values of a Dictionary
for x in course:
    print(course[x])
# values() method
for y in course.values():
    print(y)

# Accessing keys of a Dictionary
for z in course.keys():
    print(z)

# Accessing keys and values of a Dictionary
for a,b in course.items():
    print(a,b)