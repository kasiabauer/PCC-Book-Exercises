class User:
    """Tworzy obiekt użytkownika z imieniem i nazwiskiem i dostępną metodą."""
    def __init__(self,first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        """Metoda wyświetla dane użytkownika"""
        print(f"Użytkownik:  {self.first_name} {self.last_name}\n"
              f"Email: {self.email}")
    def greet_user(self):
        """Metoda wita użytkownika jego imieniem i nazwiskiem"""
        print(f"Witaj, {self.first_name} {self.last_name}")

user_01 = User('Karol', 'Krawężnik', 'kk@gmail.com')
user_02 = User('Małgorzata', 'Rybacka', 'malrybacka01@wp.pl')
user_03 = User('Julia', 'Tyagi', 'juliatyagi@gmail.com')

user_01.greet_user()
user_01.describe_user()
user_02.greet_user()
user_02.describe_user()
user_03.greet_user()
user_03.describe_user()
