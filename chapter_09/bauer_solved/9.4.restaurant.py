class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"{self.restaurant_name}, typ kuchni: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} operuje w godzinach 11:00 - 21:00")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, served_today):
        self.number_served += served_today

julia_restaurant = Restaurant('Indie Jules', 'indyjsko-polska')

julia_restaurant.describe_restaurant()
print(f"Liczba obsłużonych klientów: {julia_restaurant.number_served}")

julia_restaurant.number_served = 14
print(f"Liczba obsłużonych klientów: {julia_restaurant.number_served}")

julia_restaurant.set_number_served(120)
print(f"Liczba obsłużonych klientów: {julia_restaurant.number_served}")

julia_restaurant.set_number_served(-1)
print(f"Liczba obsłużonych klientów: {julia_restaurant.number_served}")

# julia_restaurant.set_number_served("dupa")
# print(f"Liczba obsłużonych klientów: {julia_restaurant.number_served}")

julia_restaurant.increment_number_served(50)
print(f"Liczba obsłużonych klientów: {julia_restaurant.number_served}")
