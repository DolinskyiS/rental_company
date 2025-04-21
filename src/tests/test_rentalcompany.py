import pytest
from datetime import date, timedelta
from src.model.property import Property, Owner
from src.model.rentalcompany import (
    RentalCompany,
    Contract,
    RentalAnalytics,
    MonthlyReport,
    Property_Search,
    Navigation,
    rc
)


o1 = Owner('Mister Business', '@millionaire')
p1 = Property('London', 'England', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49)
p10 = Property('Helsinki', 'Finland', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49)
c1 = Contract(o1, p10, date(2025, 4, 1), date(2026, 4, 1), 5)


def test_rental_company_property_management():
    p1 = Property('London', 'England', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49)
    base = len(rc.properties_managed)
    rc.add_property(p1)
    assert len(rc.properties_managed) == base + 1
    rc.remove_property(p1)
    assert len(rc.properties_managed) == base


def test_contract_management():
    assert c1.is_active() is True
    assert p10 in rc.properties_managed

    commission = c1.calculate_commission()
    assert commission > 0


def test_rental_analytics():
    analytics = RentalAnalytics()
    p10.is_occupied = True
    assert 0 <= analytics.vacancy_rate() <= 1
    assert analytics.average_rent() == p10.price


from unittest.mock import patch
from datetime import date


def test_monthly_report():
    p10.is_occupied = False
    test_date = date(2025, 4, 15)

    class MockPayment:
        def __init__(self):
            self.date = test_date
            self.amount = 1000.49
            self.property = p10

    with patch('src.model.rentalcompany.transaction_history.transactions', [MockPayment()]):
        with patch('src.model.rentalcompany.date') as mock_date:
            mock_date.today.return_value = test_date
            mock_date.side_effect = date

            report = MonthlyReport()
            report_data = report.generate_report()

            assert report_data['month'] == 4
            assert report_data['year'] == 2025
            assert report_data['vacancy_percentage'] == 100
            assert report_data['income'] == 1000.49
            assert report_data['loss_due_to_vacancy'] == p10.price

def test_property_search():
    results = Property_Search.search_by_location('Helsinki', 'Finland')
    assert p10 in results

    price_results = Property_Search.search_by_price(900, 1100)
    assert p10 in price_results


# Mock test for search by nearest
@pytest.fixture
def mock_geopy(mocker):
    mock_geo = mocker.patch('geopy.geocoders.Nominatim')
    mock_geo.return_value.geocode.return_value.latitude = 40.7128
    mock_geo.return_value.geocode.return_value.longitude = -74.0060
    return mock_geo


def test_navigation(mock_geopy):
    nav = Navigation()
    p10.is_occupied = False
    result = nav.get_nearest_available_property('New York', 'USA')
    assert result is not None