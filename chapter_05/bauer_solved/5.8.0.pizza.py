requested_toppings = ['pieczarki', 'boczek', 'podwójny ser']

for requested_topping in requested_toppings:
    if requested_topping == "boczek":
        print(f'Przepraszamy, nie mamy już boczku.')
    else:
        print(f'Dodaję {requested_topping}.')
print(f'\nTwoja pizza jest już gotowa.')

print(f'\n# version 2')
requested_toppings2 = []
if requested_toppings2:
    for requested_topping in requested_toppings2:
        print(f"Dodaję {requested_topping}.")
    print("\nTwoja pizza jest już gotowa!")
else:
    print("Czy jesteś pewien, że chcesz pizzę bez dodatków?")

print(f'\n# version 3')
available_toppings = ['pieczarki','oliwki','boczek',
                      'pepperoni', 'ananas', 'podwójny ser']
requested_toppings3 = ['pieczarki', 'frytki', 'podwójny ser']

for requested_topping in requested_toppings3:
    if requested_topping in available_toppings:
        print(f'Dodaję {requested_topping}')
    else:
        print(f'Przepraszamy, ale obecnie nie mamy dodatku '
              f'{requested_topping}.')
print('\nTwoja pizza jest już gotowa.')

