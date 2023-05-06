def make_pizza(size, *toppings):
    """Podsumowanie informacji o przygotowanej pizzy."""
    print(f'\nPrzygotowuję pizzę o wielkości {size}:')
    for topping in toppings:
        print(f'- {topping}')

make_pizza(40, 'pieczarki')
make_pizza(30, 'pieczarki', 'tofu', 'szpinak')
