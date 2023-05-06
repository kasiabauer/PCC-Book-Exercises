print(f'\nExample #1:')
favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python'
}
language = favorite_languages['sara'].title()
print(f"Ulubiony język programowania Sary to {language}")

print(f'\nExample #2:')
alien_0 = {'color': 'zielony', 'speed': 'wolno'}
# print(alien_0['points'])
point_value = alien_0.get('points', 'Brak przypisanych punktów')
print(point_value)

