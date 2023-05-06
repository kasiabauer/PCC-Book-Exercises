def get_sandwich(*ingredients):
    print(f'\nZamówiono kanapkę ze składnikami:')
    for ingredient in ingredients:
        print(f"- {ingredient}")

get_sandwich('tofu')
get_sandwich('tempeh', 'sałata', 'pomidor')
get_sandwich('tofu', 'ser wegański')