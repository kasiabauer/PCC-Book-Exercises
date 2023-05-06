rivers = {
    'egipt': 'nil',
    'polska': 'wisła',
    'indie': 'ganges'
}
for country, river in rivers.items():
    print(f"{river.title()} przepływa przez {country.title()}.")

print('\nW słowniku rivers znajdują się następujące rzeki:')
for river in rivers.values():
    print(f"{river.title()}")

print('\nW słowniku rivers znajdują się następujące państwa:')
for country in rivers.keys():
    print(f"{country.title()}")
