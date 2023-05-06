# Rozpoczynamy od pewnych projektów, które mają być wydrukowane.
unprinted_designs = ['etui telefonu', 'robot pendant', 'dwunastościan']
completed_models = []

#Symulujemy wydruk poszczególnych projektów, dopóki pozostał jakikolwiek projekt
# na liście. Każdy wydrukowany model zostaje przeniesiony na listę completed_models.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Wydruk modelu: {current_design}")
    completed_models.append(current_design)

#Wyświetlenie wszystkich wydrukowanych modeli.
print('\nWydrukowane zostały następujące modele:')
for completed_model in completed_models:
    print(completed_model)