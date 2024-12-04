# "%" Formatting
name='Manjesh'
print("My name is %s." %name)
city="Banglore"
print("My name is %s , I live in %s." %(name,city))
print("My name is {} , I live in {}." .format(name,city))
print("My name is {0} , I live in {1}." .format(name,city))
n="Manjesh"
c="Banglore"
print("My name is {nam} , I live in {cit}." .format(nam=n,cit=c))
print("I got {0:f}% marks in Maths.".format(98.00))
print("I got {0:d}% marks in Maths.".format(98))
print("I got {0:.2f}% marks in Maths.".format(98.00))

# F strings
print(f"My name is {name} , I live in {city}.")
print(f"My name is {name.upper()} , I live in {city.upper()}.")

age=18
gender="male"
introduction=f"My name is {name} , "\
    f"My age is {age}, "\
    f"I am a {gender}."
print(introduction)

introduction=f'''"My name is {name} , "
    f"My age is {age}, "
    f"I am a {gender}."'''
print(introduction)

print(f"{'Manjesh'}")
print(f'{"Manjesh"}')

x=10
y=20
print(f'The x+y is {x+y}')
print(f"the result of {{x+y}} is {{{x+y}}}")