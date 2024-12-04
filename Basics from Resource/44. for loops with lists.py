# Iterating over a loop
cars=['Audi','BMV','Toyota']
for car in cars:
    print(car)

# Iterating over a loop using for loop and range()
for i in range(0,len(cars)):
    print(cars[i])

# List Comprehension
[print(car) for car in cars]