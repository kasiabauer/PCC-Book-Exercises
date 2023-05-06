pizza = {
    'crust': 'grubym',
    'toppings': ['pieczarki', 'podwójny ser']
}
print(f"Zamówiłeś pizzę na {pizza['crust']} cieście wraz z następującymi"
      f"dodatkami:")
for toppings in pizza['toppings']:
    print(f"\t{toppings}")
