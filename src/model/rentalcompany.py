from .property import Property


class RentalCompany():
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.properties_managed = []
        self.contracts = []

    def add_property(self, property: Property):
        if property.property_id not in self.properties_managed:
            self.properties_managed.append(property.id)

            print(f'A property by ID: {property.id} has been added to RentalCompany {self.company_name}')
        else:
            print(f'A property by ID: {property.id} already exists in RentalCompany {self.company_name}')


    # Your code goes here.