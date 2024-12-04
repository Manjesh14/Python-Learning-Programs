# Traditional Method
names=["John","James","Emmy","Michel","Jimmy"]
j_names=[]
for name in names:
    if "J" in name:
        j_names.append(name)
print(j_names)

# By List Comprehension
J_names=[name for name in names if "J" in name]
print(J_names)

# To get copy by list Comprehension
num=[1,2,3,4]
num2=[value for value in num ]
print(num2)

# HomeWork
animals=['lion','tiger','monkey','elephant','frog']
flittered_animals=[]
for animal in animals:
    flittered_animals.append(animal.title())
print(flittered_animals)

# By comprehension
flittered_animals2=[animal.title() for animal in animals ]
print(flittered_animals2)