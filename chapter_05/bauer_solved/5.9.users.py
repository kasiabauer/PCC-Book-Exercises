users = ['admin', 'Brajan', 'Beata', 'Grażyna', 'Józef']
# users = []

if users:
    for user in users:
        if user == 'admin':
            print(f'Witaj, {user}, czy chcesz przejrzeć dzisiejszy raport?')
        else:
            print(f'Witaj, {user}! Dziękujemy, że ponownie się zalogowałeś')
else:
    print(f'Musimy znaleźć jakichś użytkowników!')