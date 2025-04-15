from property import Property, Owner
from datetime import date
from property_attributes import h1

class RentalCompany:
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.properties_managed = []
        self.contracts = []

    def get_properties(self):
        prop_list = []
        for prop in self.properties_managed:
            prop_list.append(prop.property_id)
        print(f"Here is the list of properties by ID: {prop_list}")
        return list(self.properties_managed)

    def add_property(self, p: Property):
        if p not in self.properties_managed:
            self.properties_managed.append(p)
            print(f'The property with ID: {p.property_id} has been added to RentalCompany {self.company_name}')
        else:
            print(f'The property with ID: {p.property_id} already exists in RentalCompany {self.company_name}')

    def remove_property(self, p: Property):
        if p in self.properties_managed:
            self.properties_managed.remove(p)
            print(f'The property with ID: {p.property_id} has been removed from RentalCompany {self.company_name}')
        else:
            print(f"There is no property with the following ID: {p.property_id} in RentalCompany {self.company_name}")


    # def get_income(self): # at first i want to establish payment system

    # def analyze_occupancy(self): # same



## The Rental Company
rc = RentalCompany('SoldYaHome')

import datetime
class Contract:

    def __init__(self, contract_id: int, owner: Owner, prop: Property, start_date: date, end_date: date, commission_rate: float):
        self.contract_id = contract_id
        self.owner = owner
        self.property = prop
        self.start_date = start_date
        self.end_date = end_date
        self.commission_rate = commission_rate
        # make everything inline
        self._relations_setup()

    def __str__(self):
        return (f"Contract ID: {self.contract_id}, "
                f"Owner: {self.owner.name}, "
                f"Property ID: {self.property.property_id}, "
                f"Start: {self.start_date}, End: {self.end_date}, "
                f"Commission Rate: {self.commission_rate}%")

    def __repr__(self):
        return self.__str__()

    def _relations_setup(self):
        self.owner.add_property(self.property) # adding property to owner's property list
        self.property.history.append(self) # updating property history
        # self.property.is_occupied = True # updating occupation status
        if self.start_date <= datetime.date.today() <= self.end_date:
            self.property.is_occupied = True
        else:
            self.property.is_occupied = False
        rc.contracts.append(self)


    def is_active(self):
        if self.start_date <= datetime.date.today() <= self.end_date:
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


            all_months = (end.year - start.year) * 12 + (end.month - start.month)
            final_price = round((self.property.price * int(all_months)) / 100 * self.commission_rate, 2)
            print(f"Your payment is: {final_price}")
            return final_price

    def get_owner(self):
        return self.owner.name




class RentalAnalytics:
    def vacancy_rate(self):
        if len(rc.get_properties()) > 0:
            free_pl = []
            occupied_pl = []
            for prop in rc.get_properties():
                if prop.is_occupied:
                    occupied_pl.append(prop)
                else:
                    free_pl.append(prop)
            print(f'The vacancy rate is {len(occupied_pl) / (len(occupied_pl) + len(free_pl))}')
            return len(occupied_pl) / (len(occupied_pl) + len(free_pl))

        else:
            print("Rental company manages 0 properties")
            return 0

    def average_rent(self):
        sum = 0
        for prop in rc.get_properties():
            sum += prop.price
        print(f'The average rent is {(sum / len(rc.get_properties())):.2f}')
        return round(sum / len(rc.get_properties()), 2)

    # def revenue_analytics(self):
    #     sum = 0
    #     for cont in rc.contracts:



# testing
# property.py testing
p1 = Property(1, 'London', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49)
p2 = Property(2, 'New York', 46.31, ['shower', 'wi-fi', 'queen-size bed', "pc"], 1400)
o1 = Owner(1, 'Mister Business', '@millionaire')

p1.get_status()
p1.calculate_cost(3)

c1 = Contract(1, o1, p1, date(2025, 4, 1), date(2025, 4, 19), 5)

# print(datetime.date.today())
print(c1.is_active())
c1.calculate_commission()
c1.get_owner()

# rc testing

rc.add_property(p1)
rc.add_property(h1)


# rc.remove_property(p1)

ra = RentalAnalytics()
rc.get_properties()
ra.vacancy_rate()
print(ra.average_rent())

print(rc.contracts)

