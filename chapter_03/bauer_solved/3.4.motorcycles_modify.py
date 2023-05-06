# Adding to a list
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)
motorcycles.append('yamaha')
print(motorcycles)
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

# Deleting from a list
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Deleting last index and using it in variable
motorcycles.insert(1, 'yamaha')
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.append('suzuki')
print(motorcycles)

last_owned = motorcycles.pop()
print(f'Ostatnio zakupiony {last_owned.title()}')


motorcycles.append('suzuki')
print(motorcycles)
first_owned = motorcycles.pop(0)
print(f'Mój pierwszy {first_owned.title()}')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nMotocykl {too_expensive.title()} jest zbyt drogi dla mnie.')







