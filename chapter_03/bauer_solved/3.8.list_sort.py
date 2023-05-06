# Sorting list alphabetically 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Sorting list reverse alphabetically 
cars.sort(reverse=True)
print(cars)

# Sorting with function sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'\nOto lista początkowa: \n {cars}')

print(f'\nOto lista posortowana: \n {sorted(cars)}')

print(f'\nLista początkowa nie uległa zmianie: \n {cars}')

print('=====')
print(cars)
cars.reverse()
print(cars)

print(len(cars))