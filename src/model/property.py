import datetime
from property_attributes import UtilityProvider

class Owner:
    def __init__(self, owner_id: int, name: str, contact_info: str):
        self.owner_id = owner_id
        self.name = name
        self.contact_info = contact_info
        self.properties_owned = []

    def get_properties(self):
        if len(self.properties_owned) > 0:
            names_get_properties = []
            for property in self.properties_owned:
                names_get_properties.append(property)

            print(f"Here is the list of owned properties by ID: {names_get_properties}")
        else:
            print(f"Owner has no properties")

    # applying a functionality to add and remove owned properties
    def add_property(self, property):
        if property.property_id not in self.properties_owned:
            self.properties_owned.append(property.property_id)
            print(f"Property with the followind ID: {property.property_id} has been added to Mr. {self.name}'s property list")

        else:
            print(f'{self.name} already owns ID: {property.property_id} property')

    def remove_property(self, property):
        if property.property_id not in self.properties_owned:
            print(f'{self.name} does not own property: {property.property_id}')
        else:
            self.properties_owned.remove(property.property_id)
            print(f"property with the following ID: {property.property_id} has been removed from Mr. {self.name}'s property list")


class Property():
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
        if self.is_occupied == True:
            print("the property is currently occupied")
        elif self.is_occupied == False:
            print("the property is currently free")

    def calculate_cost(self, months):
        print(f"your cost is {self.price * months}")
        return self.price * months

    #  setting utility provider
    def add_utility_provider(self, provider: UtilityProvider):
        self.utility_provider.append(provider)

    # altering tax and utility histories
    def add_utility_payment(self, provider: UtilityProvider, payment):
        self.utility_history.append((provider, payment))

    def add_tax_payment(self, payment):
        self.tax_history.append(payment)



class Contract():
    def __init__(self, contract_id: int, owner: Owner, property: Property, start_date: str, end_date: str, commission_rate: float):
        self.contract_id = contract_id
        self.owner = owner
        self.property = property
        self.start_date = start_date
        self.end_date = end_date
        self.commission_rate = commission_rate
        # make everything inline
        self._relations_setup()

    def _relations_setup(self):
        self.owner.add_property(self.property) # adding property to owner's property list
        self.property.history.append(self) # updating property history
        self.property.is_occupied = True # updating occupation status


    def is_active(self):
        if str(datetime.date.today()) >= self.start_date or str(datetime.date.today()) <= self.end_date:
            print("the contract is active")
            return True
        else:
            print("the contract is not active")
            return False

    def calculate_commission(self):
        if self.commission_rate == 0:
            print("Your commission rate is set to 0")
            return 0
        elif self.commission_rate > 0:
            end = self.end_date
            start = self.start_date
            from datetime import datetime

            start_date = datetime.strptime(start, "%Y-%m-%d")
            end_date = datetime.strptime(end, "%Y-%m-%d")

            all_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
            print(f"your payment is: {(self.property.price * int(all_months)) / 100 * self.commission_rate}")







# testing
p1 = Property(1, 'London', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49)
p2 = Property(2, 'New York', 46.31, ['shower', 'wi-fi', 'queen-size bed', "pc"], 1400)

p1.get_status()
p1.calculate_cost(3)

c1 = Contract(1, p1, "2025-02-19", "2025-04-19", 5)

# print(datetime.date.today())
c1.is_active()
c1.calculate_commission()

o1 = Owner(1, 'Mister Business', '@millionaire')
o1.get_properties()
o1.add_property(p1)
o1.get_properties()
o1.add_property(p2)
o1.get_properties()
o1.remove_property(p1)
o1.get_properties()