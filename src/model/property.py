# from property_attributes import UtilityProvider

class Owner:
    def __init__(self, owner_id: int, name: str, contact_info: str):
        self.owner_id = owner_id
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
    def __init__(self, property_id: int, address: str, size: float, facilities: list, price: float):
        self.property_id = property_id
        self.address = address
        self.size = size
        self.facilities = facilities
        self.price = price
        self.history = []
        self.is_occupied = False
        self.utility_provider = []
        self.utility_history = []
        self.tax_history = []

    def get_status(self):
        if self.is_occupied:
            return "the property is currently occupied"
        elif not self.is_occupied:
            return "the property is currently free"

    def calculate_cost(self, months):
        print(f"Your cost for property {self.property_id} for {months} month/s is ${(self.price * months):.2f}")
        return self.price * months

    # #  setting utility provider
    # def add_utility_provider(self, provider: UtilityProvider):
    #     self.utility_provider.append(provider)
    #
    # # altering tax and utility histories
    # def add_utility_payment(self, provider: UtilityProvider, payment):
    #     self.utility_history.append((provider, payment))

    def add_tax_payment(self, payment):
        self.tax_history.append(payment)
        print('the payment has been successfully appended')





# testing
p1 = Property(1, 'London', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49)
p2 = Property(2, 'New York', 46.31, ['shower', 'wi-fi', 'queen-size bed', "pc"], 1400)
o1 = Owner(1, 'Mister Business', '@millionaire')

p1.get_status()
p1.calculate_cost(3)

# c1 = Contract(1, o1, p1, "2025-02-19", "2025-04-19", 5)

# print(datetime.date.today())
# print(c1.is_active())
# c1.calculate_commission()
# c1.get_owner()


o1.get_properties()
o1.add_property(p1)
o1.get_properties()
o1.add_property(p2)
o1.get_properties()
o1.remove_property(p1)
o1.get_properties()