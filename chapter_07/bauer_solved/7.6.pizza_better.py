prompt = "Podaj składniki do Twojej pizzy: "
prompt += "\nGdy skończysz napisz 'koniec'"

active = True
pizza_toppings = []
while active:
    topping = input(prompt)
    if topping == 'koniec':
        print(f'\nTwoja pizza zawiera następujące składniki:')
        for topping in pizza_toppings:
            print(topping)
        active = False
    pizza_toppings.append(topping)