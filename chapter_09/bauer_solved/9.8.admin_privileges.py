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

class Privileges:
    def __init__(self):
        self.privileges = ["może dodać post",
                           "może usunąć post",
                           "może zbanować użytkownika"]

    def show_privileges(self):
        """Metoda wyświetla uprawnienia admina."""
        print(f"Uprawnienia: \n")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    """Tworzy obiekt administratora z uprawnieniami"""
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = Privileges()



user_01 = User('Karol', 'Krawężnik', 'kk@gmail.com')
admin_01 = Admin('Pan', 'Bóg', 'admin@gmail.com')
admin_01.privileges.show_privileges()
