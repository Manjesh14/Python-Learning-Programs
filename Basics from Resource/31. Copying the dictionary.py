x=10
y=x
print(id(x))
print(id(y))
y=20
print(id(y))
print(y)
print(x)

# mutable
car={'brand':'Audi', 'model':'q7'}
car2=car
print(id(car))
print(id(car2))
car2['model']='q8'
print(car2)
print(car)

# copy() method

car_copy=car.copy()
print(car_copy)
car_copy['model']='s50'
print(car)
print(car_copy)

# dict() method
car_copy2=dict(car)
print(car_copy2)
car_copy2['model']='s5'
print(car)
print(car_copy2)
