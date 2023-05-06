def describe_pet(animal_type, pet_name):
    """Wyświetla informacje o zwierzęciu."""
    print(f"\nMoje zwierzę to {animal_type}.")
    print(f"Mój {animal_type} ma na imię {pet_name.title()}.")

describe_pet('chomik', 'harry')
describe_pet('pies', 'reksio')

# Niepoprawne wywołanie funkcji z zamienionymi argumentami
describe_pet('harry', 'chomik')

# Wywołanie funkcji z argumentami ze słowami kluczowymi
describe_pet(pet_name='harry', animal_type='chomik')

