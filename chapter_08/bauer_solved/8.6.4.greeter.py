def get_formatted_name(fist_name, last_name, middle_name=''):
    """Zwraca elegancko sformatowanie pełne imię i nazwisko."""
    if middle_name:
        full_name = f"{fist_name} {middle_name} {last_name}"
    else:
        full_name = f"{fist_name} {last_name}"
    return full_name.title()

while True:
    print("\nProszę podać imię i nazwisko:")
    f_name = input('Imię: ')
    l_name = input('Nazwisko: ')

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nWitaj, {formatted_name}")
