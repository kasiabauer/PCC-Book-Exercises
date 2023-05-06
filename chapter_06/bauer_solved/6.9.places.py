favorite_places = {
    'Ewa': ['Kenia', 'RPA', 'Japonia'],
    'Lola': ['USA', 'Holandia', 'Tajlandia'],
    'Lan': ['Wietnam', 'UK', 'Argentyna'],
}
for person, places in favorite_places.items():
    print(f"Ulubione miejsca {person} to:")
    for place in places:
        print(f"\t{place}")
