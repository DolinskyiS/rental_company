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
        needed_lease = self.get_active_lease()
        print("Payment has been successfully made")
        LatePayment(needed_lease, amount)





class RentalApplication:
    def __init__(self, applicant: Resident, property: Property):
        self.application_id = int(uuid.uuid4())
        self.applicant = applicant
        self.property = property
        self.status = "Not Decided"

    def approve(self):
        self.status = "Approved"

    def reject(self):
        self.status = "Rejected"

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
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        print('trans appended')

    def get_total_payments(self):
        sum = 0
        print('here')
        for payment in self.transactions:
            sum += payment.amount
        print(f"Total payments: {sum}")
        return sum

transaction_history = TransactionHistory()

class Payment:
    def __init__(self, lease: LeaseAgreement, amount: float):
        self.payment_id = int(uuid.uuid4())
        self.lease = lease
        self.amount = amount # lease.rent_amount
        self.date = date.today()
        self.status = 'Pending'



    def is_late(self) -> bool:
        rent_day = self.lease.start_date.replace(year=self.date.year, month=self.date.month) # replacing year and month in order to calculate the payment deadline
        return self.date > rent_day



class LatePayment(Payment):
    def __init__(self, lease: LeaseAgreement, amount: float):
        super().__init__(lease, amount)

        if self.is_late():
            self.penalty_fee = round(self.amount * 0.2, 2)
            self.lease.rent_amount = round(self.amount + self.penalty_fee, 2)
            self.status = 'Late Payment'
            Event(f'Late payment has been made with the following ID : {self.payment_id}. Lease ID: {self.lease.lease_id}. A penalty fee of {self.penalty_fee} has been applied')


        else:
            self.penalty_fee = 0.0
            self.status = 'Paid on time'
            Event(f'Payment has been made with the following ID : {self.payment_id}. Lease ID: {self.lease.lease_id}. No additional fees')

        # Event(f'New payment has been made with the following ID : {self.payment_id}')
        global transaction_history
        transaction_history.add_transaction(self)
        if self.amount < self.lease.rent_amount:
            self.status = "Unfinished Payment"
            owed = self.lease.rent_amount - self.amount
            Event(f'Insufficient payment has been made with the following ID : {self.payment_id}. Lease ID: {self.lease.lease_id}. Still ${owed} needed')
            print(f"Insufficient payment. You still owe: {owed}")


    def calculate_penalty(self):
        print(f"Your penalty fee is ${self.penalty_fee}")
        return self.penalty_fee
