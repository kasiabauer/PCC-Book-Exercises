from random import randint


class Die:
    """Class imitates a gie used in games"""
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        """Method imitates a die roll"""
        return randint(1, self.sides)


# 6-faced die rolls
my_die = Die(6)
print('\nDie Roll:')
for x in range(10):
    print(my_die.roll_die())

# 10-faced die rolls
my_die = Die(10)
print('\nDie Roll:')
for x in range(10):
    print(my_die.roll_die())

# 20-faced die rolls
my_die = Die(20)
print('\nDie Roll:')
for x in range(10):
    print(my_die.roll_die())
