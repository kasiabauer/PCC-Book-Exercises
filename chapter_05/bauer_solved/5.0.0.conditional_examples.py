car = 'bmw'
print(car == 'bmw')
print(car == 'audi')
print(car == 'BMW')
print(car.upper() == 'BMW')

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_toppings = 'pieczarki'

if requested_toppings != 'anchois':
    print('Proszę o anchois!')

age = 18
print(age == 18)

answer = 17
if answer != 42:
    print('To nie jest prawidłowa odpowiedź. Proszę spróbuj ponownie!')

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

requested_toppings = ['pieczarki', 'cebula', 'ananas']
print('pieczarki' in requested_toppings)
print('pepperoni' in requested_toppings)

banned_users = ['andrzej', 'karolina', 'dawid']
user = 'maria'

if user not in banned_users:
    print(f'{user.title()}, możesz opublikować odpowied, jeśli chcesz.')

game_active = True
can_edit = False
