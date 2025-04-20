import uuid
from src.model.property import Property
from src.model.residency import Resident
from src.model.rentalcompany import RentalCompany, rc

users = []


class User:
    def __init__(self, username: str, password_hash: str, role: str):
        self.user_id = int(uuid.uuid4())
        self.username = username
        self.password_hash = password_hash
        self.role = role
        self.notifications = []
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
            print(f"You has successfully been authenticated")
            return True
        else:
            print('Incorrect password')
            return False

    def check_notifications(self, psw: str):
        if self.authenticate(psw):
            if len(self.notifications) > 0:
                for notification in self.notifications:
                    print(notification)
            else:
                print("No notifications yet")

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
        rc.add_property(p)
        print(f'Property {p.property_id} has been added to the Rental Company')

    def remove_property(self, p: Property):
        rc.remove_property(p)
        print(f'Property {p.property_id} has been removed from the Rental Company')


class PropertyManager(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.properties_managed = []

    def assign_property(self, p: Property):
        self.properties_managed.append(p)
        print('Property has been successfully assigned')


class Renter(User):
    all_renters = [] # need this for automated notifications

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.resident = None
        Renter.all_renters.append(self)

    def become_resident(self, resident: Resident, psw: str):
        if self.authenticate(psw):
            self.resident = resident
            print('You have successfully became a resident')

    def view_lease_details(self, psw: str):
        if self.authenticate(psw):
            print(self.resident.get_active_lease())


class Notification:
    def __init__(self, message: str, recipient: User, system_notification: bool):
        self.notification_id = int(uuid.uuid4())
        self.message = message
        self.recipient = recipient
        self.system_notification = system_notification
        self._auto()

    def __str__(self):
        return self.message

    def __repr__(self):
        self.__str__()

    def _auto(self):
        if self.system_notification == True:
            self.recipient.notifications.append(self)


    def send(self):
        self.recipient.notifications.append(self)




# u1 = User('Sviatik', 'Turbo', 'Renter')
# u2 = User('Sviatik', 'Turbo', 'Renter')

# u1.authenticate('Turbo')
# u2.authenticate('Turbo')
# print(users)