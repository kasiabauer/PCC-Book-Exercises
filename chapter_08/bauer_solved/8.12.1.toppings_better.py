def make_pizza(*toppings):
    """Podsumowanie informacji o przygotowanej pizzy."""
    print('\nPrzygotowuję pizzę z następującymi dodatkami:')
    for topping in toppings:
        print(f'- {topping}')

make_pizza('pepperoni')
make_pizza('pepperoni', 'ser', 'szynka')
