import car_functions
from car_functions import make_car
from car_functions import make_car as fn
import car_functions as mn
from car_functions import *

car = car_functions.make_car('subaru',  'outback', color='blue', tow_package=True)
print(car)

car = make_car('subaru',  'outback', color='blue', tow_package=True)
print(car)

car = fn('subaru',  'outback', color='blue', tow_package=True)
print(car)

car = mn.make_car('subaru',  'outback', color='blue', tow_package=True)
print(car)

car = make_car('subaru',  'outback', color='blue', tow_package=True)
print(car)
