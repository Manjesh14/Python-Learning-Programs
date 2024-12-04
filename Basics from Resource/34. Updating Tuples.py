# Adding items to tuple
cars=('audi','Mercedes','BMW')
temp=list(cars)
temp.append('Toyota')
print(temp)
cars=tuple(temp)
print(cars)

# Updating the Tuple
temp[1]='Ferrari'
print(temp)
cars=tuple(temp)
print(cars)

# Removing the items in a Tuple
temp.remove('BMW')
cars=tuple(temp)
print(cars)

del cars
print(cars)