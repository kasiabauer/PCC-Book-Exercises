import string
from random import randint
from random import choice, sample

my_coupon = (3, 'l', 0, 2)

i = 0
hit = 0

while True:
    rnd_numbers = sample(range(0, 20), 10)
    rnd_letters = tuple(sample(string.ascii_lowercase, 5))
    numbers_letters = tuple(rnd_numbers) + tuple(rnd_letters)
    winning_result = tuple([choice(numbers_letters) for x in range(4)])
    i += 1
    print(i, f'coupon: {my_coupon}, winning result: {winning_result}')
    if set(my_coupon) == set(winning_result):
        print(
            f"After {i} tries, your coupon {my_coupon} matches the winning result {winning_result}!")
        break
