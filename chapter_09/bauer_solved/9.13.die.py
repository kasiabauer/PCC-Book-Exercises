from random import randint


class Dice:
    """Class imitates a die used in games"""
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        """Method imitates a die roll"""
        return randint(1, self.sides)


# 6-faced die rolls
my_dice = Dice(6)
print('\nDie Roll:')
for x in range(10):
    print(my_dice.roll_dice())

# 10-faced die rolls
my_dice = Dice(10)
print('\nDie Roll:')
for x in range(10):
    print(my_dice.roll_dice())

# 20-faced die rolls
my_dice = Dice(20)
print('\nDie Roll:')
for x in range(10):
    print(my_dice.roll_dice())
