visited_places = {
    'Ewa': {
        'Kenia': False,
        'Island': True,
        'Japonia': True
    },
    'Lola': {
        'USA': False,
        'Holandia': True,
        'Chine': True
    },
    'Lan': {
        'Wietnam': True,
        'UK': True,
        'Argentyna': False,
    },
}
for person, places in visited_places.items():
    print(f"Miejsca {person.title()} to:")
    for place, visited in places.items():
        print(f"\t{place}: {'Odwiedziła' if visited else 'Nie odwiedziła'}")
