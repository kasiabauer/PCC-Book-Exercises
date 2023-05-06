# tickets version 1
age = 17
if age >= 18:
    print('Możesz wziąć udział w głosowaniu')
    print('Czy zarejestrowałeś się już, aby móc głosować?')
else:
    print('Przykro nam, jesteś zbyt młody aby głosować.')
    print('Możesz się zarejestrować po ukończeniu 18 lat!')

# tickets version 2
age = 13
if age < 4:
    print('Cena biletu wstępu wynosi: 0 zł.')
elif age < 18:
    print('Cena biletu wstępu wynosi: 25 zł.')
else:
    print('Cena biletu wstępu wynosi: 40 zł.')

# tickets version 3
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f'Cena biletu wstępu wynosi {price} zł.')

# tickets version 4
age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f'Cena biletu wstępu wynosi {price} zł.')

# tickets version 5

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    prince = 20

print(f'Cena biletu wstępu wynosi {price} zł.')


# pizza version 1
requested_toppings = ['pieczarki', 'podwójny ser']

if 'pieczarki' in requested_toppings:
    print('Dodaję pieczarki')
if 'pepperoni' in requested_toppings:
    print('Dodaję pepperoni')
if 'podwójny ser' in requested_toppings:
    print('Dodaję podwójny ser')

print(f'\nTwoja pizza jest już gotowa')