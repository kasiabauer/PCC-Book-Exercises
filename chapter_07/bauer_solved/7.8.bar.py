sandwich_orders = ['Kanapka BLT', 'Kanapka z Tuńczykiem', 'Kanapka z Tofu']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f'Przygotowano {current_order}')
    finished_sandwiches.append(current_order)

print('\nWszystkie zrobione kanapki: ')
for sandwich in finished_sandwiches:
    print(sandwich)