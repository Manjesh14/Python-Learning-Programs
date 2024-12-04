# Key names
car={'brand':'Audi', 'model':'q7'}
print(car['brand'])

# get() method
print(car.get('brand'))

# keys() method
car_keys=car.keys()
print(car_keys)
car['fuel type']='diesel'
print(car_keys)

# values() method
car_values=car.values()
print(car_values)

# items() method
car_items=car.items()
print(car_items)