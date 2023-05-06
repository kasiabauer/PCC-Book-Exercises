users = ['admin', 'Brajan', 'Beata', 'Grażyna', 'Józef']

for user in users:
    if user == 'admin':
        print(f'Witaj, {user}, czy chcesz przejrzeć dzisiejszy raport?')
    else:
        print(f'Witaj, {user}! Dziękujemy, że ponownie się zalogowałeś')