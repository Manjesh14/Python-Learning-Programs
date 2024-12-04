# pop() method
from time import perf_counter

car= {'brand': 'Audi', 'model': 's50', 'color': 'Black', 'fuel type': 'diesel'}
a=car.pop('fuel type')
print(a)
print(car)

# popitem() method
b=car.popitem()
print(b)
print(car)

# del keyword
del car['model']
print(car)

# delete entire dictionary
# del car ###Name Error

# clear() method
car.clear()
print(car)