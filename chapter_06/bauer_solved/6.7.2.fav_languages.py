print(f'\nExample #1:')
favorite_languages = {
    'janek': ['python', 'ruby'],
    'sara': ['c'],
    'edward': ['ruby', 'go'],
    'paweł': ['python', 'haskell']
}
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\nUlubione języki programowania użytkownika {name.title()} to:")
    else:
        print(f"\nUlubiony język programowania użytkownika {name.title()} to:")
    for language in languages:
        print(f"\t{language.title()}")

