from car2 import Car

"""Klasa, do zaprezentowania samochodu elektrycznego oraz akumulatora."""

class Battery:
    """Prosta próba modelowania akumulatora samochodu elektrycznego."""

    def __init__(self, battery_size=75):
        """Inicjalizacja atrybutów akulmulatora."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Wyświetlenie informacji o wielkości akumulatora."""
        print(f"Ten samochód ma akumulatora o pojemności "
              f"{self.battery_size} kWh.")

    def get_range(self):
        """
        Wyświetla informacje o zasięgu samochodu na podstawie pojemności akumulatora.
        """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"Zasięg tego samochodu wynosi około {range} km po pełnym "
              f"naładowaniu akumulatora.")


class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego."""

    def __init__(self, make, model, year):
        """
        Inicjacja atrybutów klasy nadrzędnej.
        Następnia inicjacja atrybutów charakterystycznych dla samochodu
        elektrycznego.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
