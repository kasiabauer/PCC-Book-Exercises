from user import User
""" Klasy naśladujące zachowanie uprawnień oraz administratora na postawie User"""

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

