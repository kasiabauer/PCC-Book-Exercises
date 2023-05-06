places = {}
active = True
while active:
      name = input('Podaj swoje imię do ankiety: ')
      place = input('Jeżeli mógłbyś odwiedzić jedno dowolne miejsce na świecie, gdzie byś '
            'pojechał? ')
      places[name] = place
      repeat = input('Czy jest kolejna osoba do wypełnienia ankiety? (tak/nie) ')
      if repeat == 'nie':
            break
print(f'\nWyniki ankiety to: ')
for name, place in places.items():
      print(f'{name} chciałaby pojechać do {place}')
