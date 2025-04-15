from property import Property, Owner
from datetime import *

class Resident:
    def __init_(self, resident_id: int, name: str, contact_info: str):
        self.resident_id = resident_id
        self.name = name
        self.contact_info = contact_info
        self.lease_agreements = list["LeaseAgreement"] = []

    def get_active_lease(self) -> "LeaseAgreement | None":
        for lease in self.lease_agreements:
            if lease.is_active:
                return lease


class LeaseAgreement:
    def __init__(self, lease_id: int, property: Property, resident: Resident, start_date: date, end_date: date, rent_amount: float, security_deposit: float):
        self.lease_id = lease_id
        self.property = property
        self.resident = resident
        self.start_date = start_date
        self.end_date = end_date
        self.rent_amount = rent_amount
        self.security_deposit = security_deposit
        self._relations_setup()

    def _relations_setup(self):
        self.resident.lease_agreements.append(self) #appending lease agreement auto



    def is_active(self) -> bool:
        today = date.today()
        return self.start_date <= today <= self.end_date

    def renew_lease(self, preferred_end_date):





