print(f'\nExample #1:')
favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python'
}
for name, language in favorite_languages.items():
    print(f"Ulubiony język programowania {name.title()} to {language.title()}.")

print(f'\nExample #2:')
for name in favorite_languages.keys():
    print(name.title())

print(f'\nExample #3:')
for name in favorite_languages:
    print(name.title())


print(f'\nExample #4:')
friends = ['paweł', 'sara']
for name in favorite_languages.keys():
    print(f"Witaj, {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\tWitaj, {name.title()}! Widzę, że Twoim ulubionym językiem"
              f" programowania jest {language}.")

print(f'\nExample #5:')
favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python'
}
if 'elżbieta' not in favorite_languages.keys():
    print("Elżbieta, proszę, weź udział w naszej ankiecie!")

print(f'\nExample #6:')
favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python'
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, dziękujemy za udział w ankiecie.")

print(f'\nExample #7:')
favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python'
}
print(f"W ankiecie zosatły wymienione następujące języki programowania:")
for language in favorite_languages.values():
    print(language.title())

print(f'\nExample #8:')
favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python'
}
print(f"W ankiecie zosatły wymienione następujące języki programowania:")
for language in set(favorite_languages.values()):
    print(language.title())

languages = {'python', 'ruby', 'python', 'c'}
print(languages)