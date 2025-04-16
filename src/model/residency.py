from src.model.property import Property, p1
from src.model.events import Event, EventLogYes
import uuid
from datetime import date

class Resident:
    def __init__(self, name: str, contact_info: str):
        self.resident_id = int(uuid.uuid4())
        self.name = name
        self.contact_info = contact_info
        self.lease_agreements: list["LeaseAgreement"] = []

    def get_active_lease(self) -> "LeaseAgreement | None":
        for lease in self.lease_agreements:
            if lease.is_active:
                print(f"Here is your active lease: {lease.lease_id}")
                return lease
        print("No active lease")
        return None


    def pay_rent(self, amount: float):
        required_payment_lease = self.get_active_lease()




class RentalApplication:
    def __init__(self, applicant: Resident, property: Property):
        self.application_id = int(uuid.uuid4())
        self.applicant = applicant
        self.property = property
        self.status = str

    def approve(self):
       pass

class Complaint:
    def __init__(self, resident: Resident, property: Property, description: str):
        self.complaint_id = int(uuid.uuid4())
        self.resident = resident
        self.property = property
        self.description = description
        self.status = "Not Resolved"
        self._auto()

    def _auto(self):
        Event(f'New complaint has been filed with the following ID: {self.complaint_id}')
    #     # print('complainiiing')

    def resolve(self):
        self.status = "Resolved"
        print('Complaint has been successfully resolved')
        return True


class LeaseAgreement:
    def __init__(self, property: Property, resident: Resident, start_date: date, end_date: date):
        self.lease_id = int(uuid.uuid4())
        self.property = property
        self.resident = resident
        self.start_date = start_date
        self.end_date = end_date
        self.rent_amount = property.price
        self.security_deposit = property.price * 3
        self._relations_setup()

    def __str__(self):
        return (f"Lease ID: {self.lease_id}, "
                f"Property: {self.property.property_id}, "
                f"Resident: {self.resident.resident_id}, "
                f"Start: {self.start_date}, End: {self.end_date}, "
                f"Rent Amount: {self.rent_amount}, "
                f"Security Deposit: {self.security_deposit:.2f}"
                )


    def _relations_setup(self):
        self.resident.lease_agreements.append(self) #appending lease agreement auto



    def is_active(self) -> bool:
        today = date.today()
        return self.start_date <= today <= self.end_date

    def renew_lease(self, preferred_end_date):
        pass


class TransactionHistory:
    def __init__(self):
        self.transactions: list["Payment"] = []


    def get_total_payments(self):
        pass


class Payment:
    def __init__(self, lease: LeaseAgreement):
        self.payment_id = int(uuid.uuid4())
        self.lease = lease
        self.amount = lease.rent_amount
        self.date = date.today()
        self.status = str

        self._auto()

    def _auto(self):
        Event(f'New payment has been made with the following ID : {self.payment_id}')

    # def is_late(self):
    #     if self.date


class LatePayment(Payment):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.penalty_fee = round(self.amount * 0.2, 2)

    def calculate_penalty(self):
        print(f"If you will be late on your payment, your fee would sum up to: {self.penalty_fee}")
        return self.penalty_fee




# r1 = Resident("Andriy", "phone_number: +431231231232")
# #
# la1 = LeaseAgreement(p1, r1, date(2025,4,1), date(2026,4,1) )
#
# payment1 = Payment(la1)
#
# complaint1 = Complaint(r1, p1, 'Faulty Fridge')
#
# EventLogYes.read_all_messages()


# print(r1.get_active_lease())
