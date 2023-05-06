fav_numbers = {
    'józek': [3, 4],
    'kasia': [6, 8],
    'ewa': [4, 12],
    'filip': [7, 11]
}
for person, numbers_list in fav_numbers.items():
    print(f"Ulubione liczby {person.title()} to:")
    for number in numbers_list:
        print(f"\t {number}")
