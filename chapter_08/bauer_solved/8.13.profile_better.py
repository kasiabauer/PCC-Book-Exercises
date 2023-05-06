def build_profile(first, last , **user_info):
    """Budowa słownika zawierającego wszelkie informacje o użytkowniku"""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

user_profile = build_profile('kasia', 'bauer', year_born=1984,
                             heigh=176, programming_language='Python')
print(user_profile)
