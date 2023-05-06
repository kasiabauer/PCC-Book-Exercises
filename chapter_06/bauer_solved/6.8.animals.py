giraffe = {'name': 'Grażyna', 'mammal': True, 'owner': 'Bauer'}
elefant = {'name': 'Józek', 'mammal': True, 'owner': 'Ewa'}
stork = {'name': 'Filip', 'mammal': False, 'owner': 'Magda'}
pets = [giraffe, elefant, stork]
for pet in pets:
    print(f"{pet['name']}")
    print(f"\tWłaściciel: {pet['owner']}")
    print(f"\tSsak: {pet['mammal']}")