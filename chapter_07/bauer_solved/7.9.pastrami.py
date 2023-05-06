sandwich_orders = ['Kanapka z Pastrami', 'Kanapka BLT', 'Kanapka z Pastrami',
                   'Kanapka z Tuńczykiem', 'Kanapka z Tofu',
                   'Kanapka z Pastrami']

print('Skończyło się pastrami')

while 'Kanapka z Pastrami' in sandwich_orders:
    sandwich_orders.remove('Kanapka z Pastrami')

print(sandwich_orders)