from platform import architecture

from src.model.property import Property, Owner
from src.model.residency import transaction_history
import uuid
from datetime import date
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

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

    def __init__(self, owner: Owner, prop: Property, start_date: date, end_date: date, commission_rate: float):
        self.contract_id = int(uuid.uuid4())
        self.owner = owner
        self.property = prop
        self.start_date = start_date
        self.end_date = end_date
        self.commission_rate = commission_rate
        # make everything inline
        self._relations_setup()

    # def __str__(self):
    #     return (f"Contract ID: {self.contract_id}, "
    #             f"Owner: {self.owner.name}, "
    #             f"Property ID: {self.property.property_id}, "
    #             f"Start: {self.start_date}, End: {self.end_date}, "
    #             f"Commission Rate: {self.commission_rate}%")
    #
    def __str__(self):
        return (f"{self.contract_id}")

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
        rc.properties_managed.append(self.property)


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

class MonthlyReport:
    def __init__(self):
        self.report_id = int(uuid.uuid4())
        self.month = date.today().month
        self.year = date.today().year
        self.vacancy_percentage = self.func_for_vp()
        self.income = self.calculate_income()
        self.loss_due_to_vacancy = self.calc_ldtv()

    def free_occup_props(self):
        occup = []
        free = []
        for prop in rc.get_properties():
            if prop.is_occupied:
                occup += prop
            else:
                free += prop
            return free

    def func_for_vp(self):
        free = self.free_occup_props()
        if len(rc.get_properties()) > 0:
            print(f'The vacancy percentage is ')
            return round(len(free) * 100 / len(rc.get_properties()), 2)
        else:
            print("Rental company manages 0 properties")
            return 100

    def calculate_income(self):
        total_revenue_of_month = 0
        for payment in transaction_history:
            if payment.date.month == self.month:
                total_revenue_of_month += payment.income
        return total_revenue_of_month

    def calc_ldtv(self):
        loss = 0
        for p in self.free_occup_props():
            loss += p.price
        return loss

    def generate_report(self):
        report = {
            "report_id": self.report_id,
            "month": self.month,
            "year": self.year,
            "vacancy_percentage": self.vacancy_percentage,
            "income": self.income,
            "loss_due_to_vacancy": self.loss_due_to_vacancy,
        }

        return report

class PropertySearch:
    def search_by_location(self, city: str, country: str):
        properties = []
        location = f"{city}, {country}"
        for prop in rc.get_properties():
            if prop.address.lower() == location.lower():
                properties.append(prop)
        if len(properties) > 0:
            print(f'Here are all the locations in {location}: {properties}')
        else:
            print(f"No properties by location {location} found")
        return properties

    def search_by_price(self, price_from: float, price_to: float):
        properties = []
        for prop in rc.get_properties():
            if price_from <= prop.price <= price_to:
                properties.append(prop)
        if len(properties) > 0:
            print(f'Here are all the properties in the price range from ${price_from} to ${price_to}: {properties}')
        else:
            print(f'No properties range from ${price_from} to ${price_to} were found')
        return properties

    def search_by_availability(self):
        properties = []
        for prop in rc.get_properties():
            if not prop.is_occupied:
                properties.append(prop)
        if len(properties) > 0:
            print(f"Here is the list of all currently available properties: {properties}")
        else:
            print(f"There are no currently available properties")
        return properties

Property_Search = PropertySearch()

class Navigation:
    def get_nearest_available_property(self, city: str, country: str):
        available_properties = Property_Search.search_by_availability()
        location = f"{city}, {country}"
        locator = Nominatim(user_agent="rental_company_assignment")

        location_geo = locator.geocode(location)
        if location_geo is None:
            print(f"No location found for {location}")

        starting_point = (location_geo.latitude, location_geo.longitude)

        def getting_prop_lat_and_long(prompt: Property):
            address = locator.geocode(prompt.address)
            prop_address = (address.latitude, address.longitude)
            return prop_address

        if len(available_properties) > 0:
            print('here')
            nearest_available_property  = min(available_properties,
                                              key=lambda p: geodesic(starting_point, getting_prop_lat_and_long(p))) # lambda function for comparing to locations
            print(f"Here is the nearest available property: {nearest_available_property.address}")
            return nearest_available_property.address
        else:
            # print('yo')
            return None








