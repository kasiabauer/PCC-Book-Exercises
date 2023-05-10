
class Restaurant:
    """Modelowanie obiektu restauracja."""
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

class IceCreamStand(Restaurant):
    """Modelowanie obiektu stoiska z lodami."""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """
        Inicjacja atrybutów klasy nadrzędnej .
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print(f"Dostępne smaki to:")
        for flavor in self.flavors:
            print(flavor)

my_stand = IceCreamStand('Środa', 'lodziarnia', ['śmietankowe', 'czekoladowe'])
my_stand.describe_restaurant()
my_stand.show_flavors()
