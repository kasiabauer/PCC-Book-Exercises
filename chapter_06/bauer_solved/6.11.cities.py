cities = {
    'warszawa': {
        'country': 'polska',
        'population': '3.1 mln',
        'fact': 'During II World War two uprisings against nazits happend here.'
    },
    'new delhi': {
        'country': 'indie',
        'population': '32.9 mln',
        'fact': 'New Delhi consist of Old Delhi'
    },
    'san francisco': {
        'country': 'USA',
        'population': '715 thousand',
        'fact': 'Home of famous Golden Gate bridge'
    },
}
for city, city_info in cities.items():
    print(f"{city.title()}")
    print(f"\tpopulacja: {city_info['population']}")
    print(f"\tfakt: {city_info['fact']}")