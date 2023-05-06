def describe_city(city, country):
    """Funkcja zwraca nazwę miasta i państwa"""

    res = f"{city}, {country}."
    return res

city_country = describe_city('Poznań', 'Polska')
print(city_country)
city_country = describe_city('Paryż', 'Francja')
print(city_country)
