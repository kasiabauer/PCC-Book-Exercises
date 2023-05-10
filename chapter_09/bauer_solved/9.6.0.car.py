class Car:
    """Prosta próba zaprezentowania samochodu"""
    def __init__(self, make, model, year):
        """Inicjacja atrybutów opisujących samochód."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Wyświetla informacje wartość przebiegu."""
        print(f"Ten samochód ma przejechane {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        """Przypisanie podanej wartości licznikowi przebiegu samochodu.
        Zmiana zostanie odrzucona w przypadku próby cofnięcia licznika."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Nie można cofnąć licznika przebiegu samochodu!')

    def increment_odometer(self, kilometers):
        """Inkrementacja wartości licznika przebiegu samochodu o podaną
        wartość."""
        self.odometer_reading += kilometers

class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego."""

    def __init__(self, make, model, year):
        """Inicjacja atrybutów klasy nadrzędnej."""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_batter(self):
        """Wyświetlenie informacji o wielkości akumulatora."""
        print(f"Ten samochóod ma akumulator o pojemności "
              f"{self.battery_size} kWh.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_batter()
