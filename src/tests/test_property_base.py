from src.model.property import Property, Owner, MaintenanceRequest, mr, Review, Renovation
from src.model.property_attributes import UtilityProvider, TaxRecord, House, Apartment, Shop, Land

p1 = Property('London', 'England', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49)
o1 = Owner('Mister Business', '@millionaire')

h1 = House(
    num_bedrooms=2,
    num_bathrooms=3,
    has_garden=False,
    city='Los Angeles',
    country='USA',
    size=3000,
    facilities=['bath', 'shower', 'wi-fi'],
    price=15000
)

a1 = Apartment(
    floor_number=23,
    has_elevator=True,
    has_balcony=True,
    city='Miami',
    country='USA',
    size=700,
    facilities=['bath', 'shower', 'wi-fi', 'queen-size bed', 'cleaning'],
    price=3500
)

s1 = Shop(
    business_type='Retail',
    parking_available=True,
    city='Berlin',
    country='Germany',
    size=500,
    facilities=['AC', 'Security'],
    price=8000
)
l1 = Land(
    zoning_type='Residential',
    buildable_area=2000,
    city='Paris',
    country='France',
    size=5000,
    facilities=[],
    price=25000
)

u1 = UtilityProvider('EVN', 'Electricity and Gas', 5)
tr1 = TaxRecord(p1, 2023, 150.13)


def test_owner_property_management():
    # Test initial state
    assert len(o1.properties_owned) == 0

    # Test adding properties
    o1.add_property(p1)
    assert p1.property_id in o1.properties_owned

    o1.add_property(h1)
    assert h1.property_id in o1.properties_owned
    assert len(o1.properties_owned) == 2

    # Test removing property
    o1.remove_property(p1)
    assert p1.property_id not in o1.properties_owned
    assert len(o1.properties_owned) == 1

    # Test get_properties
    properties = o1.get_properties()
    assert isinstance(properties, list)
    assert h1.property_id in properties


def test_property_methods():
    # Test get_status
    status = p1.get_status()
    assert status in ["the property is currently occupied",
                      "the property is currently free"]

    # Test calculate_cost
    months = 5
    expected_cost = p1.price * months
    assert p1.calculate_cost(months) == expected_cost

    # Test add_tax_payment
    initial_tax_len = len(p1.tax_history)
    p1.add_tax_payment(1000)
    assert len(p1.tax_history) == initial_tax_len + 1


def test_house_properties():
    assert h1.address == 'Los Angeles, USA'
    assert h1.price == 15000
    assert h1.num_bedrooms == 2
    assert h1.num_bathrooms == 3
    assert h1.has_garden is False


def test_apartment_properties():
    assert a1.address == 'Miami, USA'
    assert a1.price == 3500
    assert a1.floor_number == 23
    assert a1.has_elevator is True
    assert a1.has_balcony is True

def test_shop_properties():
    assert s1.business_type == 'Retail'
    assert s1.parking_available is True
    assert isinstance(s1, Property)

def test_land_properties():
    assert l1.zoning_type == 'Residential'
    assert l1.buildable_area == 2000
    assert isinstance(l1, Property)

def test_renovation():
    renovation = Renovation(p1, 5000, "Kitchen remodel")
    assert renovation.property == p1
    assert renovation.cost == 5000
    assert renovation.comment == "Kitchen remodel"

    # Test adding to history
    initial_history_len = len(renovation.history)
    renovation.history.append(renovation)
    assert len(renovation.history) == initial_history_len + 1

    # Test get_total_cost (needs at least one renovation in history)
    total_cost = renovation.get_total_cost(p1)
    assert total_cost == 5000


def test_maintenance_request():
    request = MaintenanceRequest(h1)
    assert request.property == h1
    assert request.status == "pending"

    # Test approve
    request.approve()
    assert request.status == "approved"

    # Test reject
    request = MaintenanceRequest(h1)
    request.reject()
    assert request.status == "rejected"

    # Test resolve with renovation
    renovation = Renovation(h1, 3000, "Fix plumbing")
    request = MaintenanceRequest(h1)
    request.resolve(renovation)
    assert request.status == "resolved"


def test_review():
    review = Review(p1, 5, "Great property!")
    assert review.property == p1
    assert review.rating == 5
    assert review.comment == "Great property!"

    # Test rating was added to property
    assert len(p1.ratings_history) > 0

    # Test get_average_rating
    avg_rating = review.get_average_rating(p1)
    assert avg_rating == 5.0

    # Add another review and test average
    Review(p1, 3, "Could be better")
    avg_rating = review.get_average_rating(p1)
    assert avg_rating == 4.0


def test_utility_provider():
    # Test initialization
    assert u1.name == 'EVN'
    assert u1.service_type == 'Electricity and Gas'
    assert u1.monthly_cost == 5

    # Test cost calculation
    cost = u1.calculate_utility_cost(p1)
    expected_cost = round(p1.size * u1.monthly_cost, 2)
    assert cost == expected_cost


def test_tax_record():
    # Test initialization
    assert tr1.property == p1
    assert tr1.year == 2023
    assert tr1.amount == 150.13

    # Test tax calculation
    tax = tr1.calculate_tax()
    expected_tax = round(p1.size * tr1.amount, 2)
    assert tax == expected_tax


