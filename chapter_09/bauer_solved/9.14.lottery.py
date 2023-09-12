import string
from random import randint
from random import choice, sample

rnd_numbers = sample(range(0, 20), 10)
rnd_letters = tuple(sample(string.ascii_lowercase, 5))

numbers_letters = tuple(rnd_numbers) + tuple(rnd_letters)
print(f"Lottery base: {numbers_letters}")

result = [choice(numbers_letters) for x in range(4)]

print(f"Coupon including: {result} wins prize.")