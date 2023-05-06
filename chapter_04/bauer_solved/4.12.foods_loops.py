my_foods = ['pizza', 'falafel', 'ciasto z marchwi']
friend_foods = my_foods[:]

my_foods.append('cannolo')
friend_foods.append('lody')

print('\nMoje:')
for food in my_foods:
    print(food)

print('\nPrzyjaciela:')
for food in friend_foods:
    print(food)

