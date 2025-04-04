from property import Property
from property import Contract
from property import Owner
import datetime

class UtilityProvider:
    def __init__(self, provider_id, name, service_type, monthly_cost):
        self.id = provider_id
        self.name = name
        self.service_type = service_type
        self.monthly_cost = monthly_cost

    def calculate_utility_cost(self, property):
       print(f"Your monthly utility cost for property is: {property.size * self.monthly_cost}")


class TaxRecord():
    def __init__(self, tax_id: int, property: Property, year: int, amount: float):
        self.id = tax_id
        self.property = property
        self.year = year
        self.amount = amount

    def calculate_tax(self):
        print(f"Your monthly tax cost for property is: {self.property.size * self.amount}")


class House(Property):
    def __init__(self, num_bedrooms: int, num_bathrooms: int, has_garden: bool):
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.has_garden = has_garden

class Apartment(Property):
    def __init__(self, floor_number: int, has_elevator: bool, has_balcon: bool):
        self.floor_number = floor_number
        self.has_elevator = has_elevator
        self.has_balcon = has_balcon



p1 = Property(1, 'tam 2', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49, ['Mia', 'Max', 'Andriy'], True)
u1 = UtilityProvider("up1", "EVN", "Electricity and Gas", 5)
tr1 = TaxRecord(1, p1, 2000, 150.13)

u1.calculate_utility_cost(p1)
tr1.calculate_tax()



