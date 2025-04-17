from src.model.rentalcompany import Contract, RentalAnalytics, RentalCompany, rc
from src.model.property import Property, Owner, MaintenanceRequest, mr, Review
from src.model.property_attributes import UtilityProvider, TaxRecord, House, Apartment
from src.model.residency import Resident, RentalApplication, LeaseAgreement, TransactionHistory, transaction_history, Payment, LatePayment, Complaint
from src.model.events import Event, EventLogYes
from datetime import date




p1 = Property('London', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49)
p2 = Property('New York', 46.31, ['shower', 'wi-fi', 'queen-size bed', "pc"], 1400)
o1 = Owner('Mister Business', '@millionaire')

# p1.get_status()
# p1.calculate_cost(3)

    ## property attributes
u1 = UtilityProvider("EVN", "Electricity and Gas", 5)
tr1 = TaxRecord(p1, 2000, 150.13)

h1 = House(
    num_bedrooms=2,
    num_bathrooms=3,
    has_garden=False,
    address='Los Angeles',
    size=3000,
    facilities=['bath', 'shower', 'wi-fi'],
    price=15000
)

a1 = Apartment(
    floor_number=23,
    has_elevator=True,
    has_balcony=True,
    address='Miami',
    size=700,
    facilities=['bath', 'shower', 'wi-fi', 'queen-size bed', 'cleaning'],
    price=3500
)

# u1.calculate_utility_cost(p1)
# tr1.calculate_tax()

    ##rc stuff
c1 = Contract(o1, p1, date(2025, 4, 1), date(2025, 4, 19), 5)

# print(datetime.date.today())
# c1.is_active()
# c1.calculate_commission()
# c1.get_owner()
#
# # rc testing
# rc.add_property(p1)
# rc.add_property(h1)
#
# # rc.remove_property(p1)

ra = RentalAnalytics()
# rc.get_properties()
# ra.vacancy_rate()
# ra.average_rent()


# residency
r1 = Resident("Andriy", "phone_number: +431231231232")
r2 = Resident("Stoffer", 'Email: stofferiscool@gmail.com')

la1 = LeaseAgreement(p1, r1, date(2025, 4, 1), date(2026, 4, 1))
la2 = LeaseAgreement(h1, r2, date(2025, 3, 20), date(2026, 3, 20))
# print(r1.get_active_lease())

payment1 = Payment(la1)
payment2 = LatePayment(la1)
payment3 = LatePayment(la2)
transaction_history.get_total_payments()

# complaint1 = Complaint(r1, p1, 'Faulty Fridge')
#
# EventLogYes.read_new_messages()
#
#
# print(mr.request_date)
# print(rc.contracts)
# print(rc.properties_managed)
#
# rev1_h1 = Review(h1, 4, "didn't like the weather")
# rev2_h1 = Review(h1, 1, "horrible")
# rev3_h1 = Review(h1, 5, "great house")
#
# print(rev1_h1.get_average_rating(h1))
# print(rev1_h1.get_average_rating(a1))

# tuplee = (123, 'hello')
# print(type(tuplee[0]))