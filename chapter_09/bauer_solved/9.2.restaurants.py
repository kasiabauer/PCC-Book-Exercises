class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name}, typ kuchni: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} operuje w godzinach 11:00 - 21:00")

my_restaurant = Restaurant('My Thai', 'tajska')
kasia_restaurant = Restaurant('Szybka Kasia', 'polska')
julia_restaurant = Restaurant('Indie Jules', 'indyjsko-polska')

my_restaurant.describe_restaurant()
kasia_restaurant.describe_restaurant()
julia_restaurant.describe_restaurant()