from datetime import date, timedelta
from src.model.property import Property
from src.model.events import EventLogYes
from src.model.residency import Resident, RentalApplication, Complaint, LeaseAgreement, Payment, LatePayment, TransactionHistory, transaction_history

p1 = Property('London', 'England', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49)

r2 = Resident("Stoffer", 'Email: stofferiscool@gmail.com')


la1 = LeaseAgreement(p1, r2, date(2025, 4, 1), date(2026, 4, 1))


def test_resident_active_lease():
    assert r2.get_active_lease() == la1
    la1.end_date = date.today() - timedelta(days=2)
    assert r2.get_active_lease() is None

def test_rental_application():
    app = RentalApplication(r2, p1)
    app.approve()
    assert app.status == "Approved"
    app.reject()
    assert app.status == "Rejected"

def test_complaint():
    complaint = Complaint(r2, p1, "Faulty Fridge")
    assert complaint.status == "Not Resolved"
    assert complaint.resolve() is True
    assert complaint.status == "Resolved"
    assert len(EventLogYes.events) > 0

def test_lease_agreement():
    assert la1.is_active() is True
    new_end = date.today() + timedelta(days=60)
    la1.renew_lease(new_end)
    assert la1.end_date == new_end

def test_payment():
    payment = Payment(la1, 1000)
    assert payment.status == 'Pending'
    assert payment.is_late() is True

def test_late_payment():
    late_pay = LatePayment(la1, 1000)
    if late_pay.is_late():
        assert late_pay.penalty_fee > 0
        assert late_pay.status == 'Unfinished Payment'
    else:
        assert late_pay.penalty_fee == 0
        assert late_pay.status == 'Paid on time'
    assert len(transaction_history.transactions) > 0

def test_transaction_history():
    history = TransactionHistory()
    lease = LeaseAgreement(Property('A', 'B', 100, [], 1000),
              Resident('Test', 'test@test.com'),
              date.today(),
              date.today() + timedelta(days=30))
    payment = Payment(lease, 1000)
    history.add_transaction(payment)
    assert history.get_total_payments() == 1000