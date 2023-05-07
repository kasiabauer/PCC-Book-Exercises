class User:
    """Tworzy obiekt użytkownika z imieniem i nazwiskiem i dostępną metodą."""
    def __init__(self,first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Metoda wyświetla dane użytkownika"""
        print(f"Użytkownik:  {self.first_name} {self.last_name}\n"
              f"Email: {self.email}")
    def greet_user(self):
        """Metoda wita użytkownika jego imieniem i nazwiskiem"""
        print(f"Witaj, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        """Metoda zwiększająca statystykę prób zalogowania."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Metoda resetująca ilość prób zalogowania."""
        self.login_attempts = 0

user_01 = User('Karol', 'Krawężnik', 'kk@gmail.com')
print(f"Ilość logowań: {user_01.login_attempts}")
user_01.increment_login_attempts()
user_01.increment_login_attempts()
print(f"Ilość logowań: {user_01.login_attempts}")

