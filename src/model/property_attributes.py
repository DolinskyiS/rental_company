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
    def __init__(self, property_id: int, address: str, size: float, facilities: list, price: float, history: list, is_occupied: bool, num_bedrooms: int, num_bathrooms: int, has_garden: bool):
        super().__init__(property_id, address, size, facilities, price, history, is_occupied)
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.has_garden = has_garden

class Apartment(Property):
    def __init__(self, property_id: int, address: str, size: float, facilities: list, price: float, history: list, is_occupied: bool, floor_number: int, has_elevator: bool, has_balcony: bool):
        super().__init__(property_id, address, size, facilities, price, history, is_occupied)
        self.floor_number = floor_number
        self.has_elevator = has_elevator
        self.has_balcony = has_balcony



p1 = Property(1, 'tam 2', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49, ['Mia', 'Max', 'Andriy'], True)
u1 = UtilityProvider("up1", "EVN", "Electricity and Gas", 5)
tr1 = TaxRecord(1, p1, 2000, 150.13)

h1 = House(3, 'doroshenka', 100, ['bath', 'shower', 'wi-fi', 'cleaning-service'], 15000, ['Maxon'], True, 2, 3, False)

u1.calculate_utility_cost(p1)
tr1.calculate_tax()



