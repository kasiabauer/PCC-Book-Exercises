class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name}, typ kuchni: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} operuje w godzinach 11:00 - 21:00")

my_restaurant = Restaurant('My Thai', 'tajska')
print(f"Nazwa restauracji: {my_restaurant.restaurant_name}")
print(f"Typ kuchni: {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
