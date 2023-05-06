current_users = ['admin', 'Brajan', 'Beata', 'Grażyna', 'Józef']
current_users2 = ['admin', 'brajan', 'beata', 'grażyna', 'józef']
new_users = ['Brajan', 'Dżesika']
for new_user in new_users:
    if new_user in current_users or new_user.lower() in current_users2:
        print(f'Użytkownik z taką nazwą już się znajduje w bazie.')
    else:
        print(f'Witaj nowy użytkowniku! Nazwa {new_user} jest dostępna.')
