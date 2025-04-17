import uuid
from src.model.property import Property

users = []


class User:
    def __init__(self, username: str, password_hash: str, role: str):
        self.user_id = int(uuid.uuid4())
        self.username = username
        self.password_hash = password_hash
        self.role = role
        self.not_unique = self._auto()

    def _auto(self):
        # print('hello')
        for user in users:
            if user == self.username:
                print(f"User {self.username} already exists, choose another username or log in into your account")
                return 0
        users.append(self.username)
        print("user has been created")
        return 1

    def authenticate(self, psw: str):
        if self.not_unique == 0:
            print("Create account with a new username. You are not able to continue with current.")
            return False

        if psw == self.password_hash:
            print(f"Welcome back, {self.username}!")
            return True
        else:
            print('Incorrect password')
            return False

        # for user in users:
        #     if user[2] == self.user_id:
        #         if user[1] == password:
        #             print('You are logged in')
        #             return True
        #         else:
        #             print('Incorrect password')
        #             return False
        # print("No user found")
        # return False


class Admin(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_property(self, p: Property):
        pass

    def remove_property(self, p: Property):
        pass


class PropertyManager(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.properties_managed = []

    def assign_property(self, p: Property):
        self.properties_managed.append(p)
        print('Property has been successfully assigned')


class Renter(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def view_lease_details(self):
        pass


class Notification:
    def __init__(self):
        self.notification_id = int(uuid.uuid4())




u1 = User('Sviatik', 'Turbo', 'Renter')
# u2 = User('Sviatik', 'Turbo', 'Renter')

u1.authenticate('Turbo')
# u2.authenticate('Turbo')
# print(users)