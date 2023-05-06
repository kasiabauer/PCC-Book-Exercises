age = ''
prompt = 'Podaj swój wiek: '
while age == '':
    age = int(input(prompt))
    if age < 3:
        print('Bilet jest bezpłatny')
    elif 3 <= age <= 12:
        print('Bilet kosztuje: 10zł')
    elif age > 12:
        print('Bilet kosztuje: 15zł')
