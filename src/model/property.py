import datetime

class Property():
    def __init__(self, property_id: int, address: str, size: float, facilities: list, price: float, history: list, is_occupied: bool):
        self.property_id = property_id
        self.address = address
        self.size = size
        self.facilities = facilities
        self.price = price
        self.history = history
        self.is_occupied = is_occupied

    def get_status(self):
        if self.is_occupied == True:
            print("the property is currently occupied")
        elif self.is_occupied == False:
            print("the property is currently free")

    def calculate_cost(self, months):
        print(f"your cost is {self.price * months}")
        return self.price * months


class Contract():
    def __init__(self, contract_id: int, owner: Owner, property: Property, start_date: date, end_date: date, commission_rate: float):
        self.contract_id = contract_id
        self.owner = owner
        self.property = property
        self.start_date = start_date
        self.end_date = end_date
        self.commission_rate = commission_rate

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


class Owner:
    def __init__(self, owner_id, name, contact_info, properties_owned):
        self.owner_id = owner_id
        self.name = name
        self.contact_info = contact_info
        self.properties_owned = properties_owned

    def get_properties(self):
        if len(self.properties_owned) > 0:
            names_get_properties = []
            for property in self.properties_owned:
                names_get_properties.append(property.property_id)

            print(f"Here is the list of owned properties by ID: {names_get_properties}")
        else:
            print(f"Owner has no properties")





# testing
p1 = Property(1, 'tam 2', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49, ['Mia', 'Max', 'Andriy'], True)
p2 = Property(2, 'tyt 52', 46.31, ['shower', 'wi-fi', 'queen-size bed', "pc"], 1400, ['Alex', 'Curious'], False)

p1.get_status()
p1.calculate_cost(3)

c1 = Contract(1, 'Mike', p1, "2025-02-19", "2025-04-19", 5)

# print(datetime.date.today())
c1.is_active()
c1.calculate_commission()

o1 = Owner('1', 'Mister Business', '@millionaire', [p1, p2])
o1.get_properties()