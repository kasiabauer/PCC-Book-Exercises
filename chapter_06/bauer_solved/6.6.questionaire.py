favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python'
}
people = ['kasia', 'paweł', 'edward', 'sara', 'janek', 'ewa']

for person in people:
    if person in favorite_languages.keys():
        print(f"{person.title()}, Dziękujemy za wzięcie udziału w ankiecie")
    else:
        print(f"{person.title()}, prosimy o wzięcie udziału w ankiecie.")
