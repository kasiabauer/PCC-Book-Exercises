person_1 = {
    'first_name': 'Katherine',
    'last_name': 'Hepburn',
    'city': 'Hollywood',
    'age': 96,
}
person_2 = {
    'first_name': 'Katherine',
    'last_name': 'Janeway',
    'city': 'Voyager',
    'age': 58,
}
person_3 = {
    'first_name': 'Rebecca',
    'last_name': 'Solnit',
    'city': 'San Francisco',
    'age': 61,
}
people = [person_1, person_2, person_3]
for person in people:
    print(f"{person['first_name']} {person['last_name']}")
    print(f"\tage: {person['age']} \n\tcity: {person['city']}")