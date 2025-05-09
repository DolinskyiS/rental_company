from src.model.property import Property
import uuid

class UtilityProvider:
    def __init__(self, name: str, service_type: str, monthly_cost: float):
        self.provider_id = int(uuid.uuid4())
        self.name = name
        self.service_type = service_type
        self.monthly_cost = monthly_cost

    def calculate_utility_cost(self, prop):
        print(f"Your monthly utility cost for property is: {(prop.size * self.monthly_cost):.2f}")
        return round(prop.size * self.monthly_cost, 2)


class TaxRecord:
    def __init__(self, prop: Property, year: int, amount: float):
        self.tax_id = int(uuid.uuid4())
        self.property = prop
        self.year = year
        self.amount = amount

    def calculate_tax(self):
        print(f"Your monthly tax cost for property is: {(self.property.size * self.amount):.2f}")
        return round(self.property.size * self.amount, 2)


class House(Property):
    def __init__(self, num_bedrooms: int, num_bathrooms: int, has_garden: bool, **kwargs):
        super().__init__(**kwargs)
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.has_garden = has_garden

class Apartment(Property):
    def __init__(self, floor_number: int, has_elevator: bool, has_balcony: bool, **kwargs):
        super().__init__(**kwargs)
        self.floor_number = floor_number
        self.has_elevator = has_elevator
        self.has_balcony = has_balcony

class Shop(Property):
    def __init__(self, business_type: str, parking_available: bool, **kwargs):
        super().__init__(**kwargs)
        self.business_type = business_type
        self.parking_available = parking_available

class Land(Property):
    def __init__(self, zoning_type: str, buildable_area: float, **kwargs):
        super().__init__(**kwargs)
        self.zoning_type = zoning_type
        self.buildable_area = buildable_area


# p1 = Property(1, 'tam 2', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49,)
# u1 = UtilityProvider(1, "EVN", "Electricity and Gas", 5)
# tr1 = TaxRecord(1, p1, 2000, 150.13)
#
# h1 = House(
#     num_bedrooms=2,
#     num_bathrooms=3,
#     has_garden=False,
#     property_id=3,
#     address='Los Angeles',
#     size=100,
#     facilities=['bath', 'shower', 'wi-fi'],
#     price=1500
# )
#
# print(u1.calculate_utility_cost(p1))
# print(tr1.calculate_tax())



