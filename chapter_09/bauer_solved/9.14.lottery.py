from random import randint
from random import choice

rnd_numbers = {randint(10, 20) for x in range(10)}
rnd_numbers = tuple(rnd_numbers)
numbers_letters = ('a', 'z', 'x', 't', 'k') + rnd_numbers
print(f"Lottery: {numbers_letters}")

result = [choice(numbers_letters) for x in range(4)]

print(f"Coupon including: {result} wins prize.")
