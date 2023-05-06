def build_profile(first, last , **user_info):
    """Budowa słownika zawierającego wszelkie informacje o użytkowniku"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


def get_sandwich(*ingredients):
    """Podsumowuje zamówienie kanapki wraz z jej składnikami"""
    print(f'\nZamówiono kanapkę ze składnikami:')
    for ingredient in ingredients:
        print(f"- {ingredient}")


def send_messages(messages, sent_messages):
    """Wysyła komunikaty z listy"""
    while messages:
        print_message = messages.pop()
        print(print_message)
        sent_messages.append(print_message)