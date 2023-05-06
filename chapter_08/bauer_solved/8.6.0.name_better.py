def get_formatted_name(fist_name, last_name, middle_name=''):
    """Zwraca elegancko sformatowanie pełne imię i nazwisko."""
    if middle_name:
        full_name = f"{fist_name} {middle_name} {last_name}"
    else:
        full_name = f"{fist_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
musician = get_formatted_name('jimmi', 'hendrix')
print(musician)
