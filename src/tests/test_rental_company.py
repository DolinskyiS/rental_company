from src.model.rentalcompany import Contract, RentalAnalytics, RentalCompany, rc
from src.model.property import Property, Owner
from src.model.property_attributes import UtilityProvider, TaxRecord, House, Apartment
from src.model.residency import Resident, RentalApplication, LeaseAgreement, TransactionHistory, Payment, LatePayment
from datetime import date

def test_rental_company():
    company = RentalCompany("Test Company")
    assert company.company_name == "Test Company"
    # assert isinstance(company, RentalCompany)

    # assert False, "This was just an example. Add more tests here"




    p1 = Property('London', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49)
    p2 = Property('New York', 46.31, ['shower', 'wi-fi', 'queen-size bed', "pc"], 1400)
    o1 = Owner('Mister Business', '@millionaire')

    p1.get_status()
    p1.calculate_cost(3)

    ## property attributes
    p1 = Property('tam 2', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49, )
    u1 = UtilityProvider("EVN", "Electricity and Gas", 5)
    tr1 = TaxRecord(p1, 2000, 150.13)

    h1 = House(
        num_bedrooms=2,
        num_bathrooms=3,
        has_garden=False,
        property_id=3,
        address='Los Angeles',
        size=3000,
        facilities=['bath', 'shower', 'wi-fi'],
        price=15000
    )

    a1 = Apartment(
        floor_number=23,
        has_elevator=True,
        has_balcony=True,
        property_id=4,
        address='Miami',
        size=700,
        facilities=['bath', 'shower', 'wi-fi', 'queen-size bed', 'cleaning'],
        price=3500
    )

    print(u1.calculate_utility_cost(p1))
    print(tr1.calculate_tax())

    ##rc stuff
    c1 = Contract(o1, p1, date(2025, 4, 1), date(2025, 4, 19), 5)

    # print(datetime.date.today())
    print(c1.is_active())
    c1.calculate_commission()
    c1.get_owner()

    # rc testing
    rc.add_property(p1)
    rc.add_property(h1)

    # rc.remove_property(p1)

    ra = RentalAnalytics()
    rc.get_properties()
    ra.vacancy_rate()
    print(ra.average_rent())

    print(rc.contracts)

    # residency
    r1 = Resident("Andriy", "phone_number: +431231231232")

    la1 = LeaseAgreement(p1, r1, date(2025, 4, 1), date(2026, 4, 1))
    print(r1.get_active_lease())
