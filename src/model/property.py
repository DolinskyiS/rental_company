# from property_attributes import UtilityProvider
import uuid
from datetime import date
from src.model.events import Event

class Owner:
    def __init__(self, name: str, contact_info: str):
        self.owner_id = int(uuid.uuid4())
        self.name = name
        self.contact_info = contact_info
        self.properties_owned = []


    def get_properties(self):
        if len(self.properties_owned) > 0:
            names_get_properties = []
            for prop in self.properties_owned:
                names_get_properties.append(prop)
            print(f"Here is the list of owned properties by ID: {names_get_properties}")
            return names_get_properties
        else:
            print(f"Owner has no properties")

    # applying a functionality to add and remove owned properties
    def add_property(self, prop):
        if prop.property_id not in self.properties_owned:
            self.properties_owned.append(prop.property_id)
            print(f"Property with the following ID: {prop.property_id} has been added to Mr. {self.name}'s property list")

        else:
            print(f'{self.name} already owns ID: {prop.property_id} property')

    def remove_property(self, prop):
        if prop.property_id not in self.properties_owned:
            print(f'{self.name} does not own property: {prop.property_id}')
        else:
            self.properties_owned.remove(prop.property_id)
            print(f"property with the following ID: {prop.property_id} has been removed from Mr. {self.name}'s property list")


class Property:
    def __init__(self, city: str, country: str, size: float, facilities: list, price: float):
        id_prop = int(uuid.uuid4())
        self.property_id = id_prop
        self.address = f"{city}, {country}"
        self.size = size
        self.facilities = facilities
        self.price = price
        self.history = []
        self.is_occupied = False
        self.ratings_history = []


    def __str__(self):
        return (f"{self.property_id}")

    def __repr__(self):
        return self.__str__()


    def get_status(self):
        if self.is_occupied:
            return "the property is currently occupied"
        elif not self.is_occupied:
            return "the property is currently free"

    def calculate_cost(self, months):
        print(f"Your cost for property {self.property_id} for {months} month/s is ${(self.price * months):.2f}")
        return self.price * months

    # def add_tax_payment(self, payment):
    #     self.tax_history.append(payment)
    #     print('the payment has been successfully appended')

renovation_history = []

class Renovation:
    def __init__(self, prop: Property, cost: int, comment: str):
        self.renovation_id = int(uuid.uuid4())
        self.property = prop
        self.date = date.today()
        self.cost = cost
        self.comment = comment
        self.history = renovation_history

    def get_total_cost(self, p: Property):
        total_cost = 0
        for ren in self.history:
            if ren.property == p:
                total_cost += ren.cost
                print(f"The cost of all renovations sums up to ${total_cost:.2f}. Property ID: {ren.property}")
                return round(total_cost, 2)

    def get_desc_of_renovations(self, p: Property): # as a renovation history
        for ren in self.history:
            if ren.property == p:
                print(ren.comment)


class MaintenanceRequest:
    def __init__(self, prop: Property):
        self.request_id = int(uuid.uuid4())
        self.property = prop
        self.request_date = date.today()
        self.status = "pending"
        self._auto()

    def __str__(self):
        return (f"ID: {self.request_id},"
                f"Property: {self.property},"
                f"Date: {self.request_date},"
                f"Status: {self.status}")

    def __repr__(self):
        return self.__str__()

    def _auto(self):
        Event(f"Maintenance request has been made with the following ID: {self.request_id}")

    def approve(self):
        self.status = "approved"
        print("The property maintenance request has been approved")

    def reject(self):
        self.status = "rejected"
        print("The property maintenance request has been rejected")

    def resolve(self, renovation: Renovation):
        self.status = "resolved"
        renovation_history.append(renovation)
        print("The property maintenance request has been resolved")


class Review:
    def __init__(self, prop: Property, rating: int, comment: str):
        self.review_id = int(uuid.uuid4())
        self.property = prop
        self.rating = rating
        self.comment = comment
        self._auto()

    def _auto(self):
        Event(f"Review has been made with the following ID: {self.review_id}")
        self.property.ratings_history.append((self.property, self.rating))

    def get_average_rating(self, prop: Property):
        needed_rating = []
        for rating in self.property.ratings_history:
            if int(rating[0].property_id) == int(prop.property_id):
                needed_rating.append(rating[1])
        # return round(sum(needed_rating) / len(needed_rating), 2)
        if len(needed_rating) > 0:
            print(f'Average rating for this property is {sum(needed_rating) / len(needed_rating):.2f}')
            return round(sum(needed_rating) / len(needed_rating), 2)
        else:
            print("No rating for this property")
            return 0




# testing
p1 = Property('London', "England", 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49)
mr = MaintenanceRequest(p1)

# p2 = Property('New York', 46.31, ['shower', 'wi-fi', 'queen-size bed', "pc"], 1400)
# o1 = Owner('Mister Business', '@millionaire')

# p1.get_status()
# p1.calculate_cost(3)

# c1 = Contract(1, o1, p1, "2025-02-19", "2025-04-19", 5)

# print(datetime.date.today())
# print(c1.is_active())
# c1.calculate_commission()
# c1.get_owner()


# o1.get_properties()
# o1.add_property(p1)
# o1.get_properties()
# o1.add_property(p2)
# o1.get_properties()
# o1.remove_property(p1)
# o1.get_properties()

# print(o1.owner_id)
# print(p1.property_id)
# print(p2.property_id)
