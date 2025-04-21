from src.model.user_interface import User, Admin, PropertyManager, Renter, Notification
from src.model.rentalcompany import rc
from src.model.property import Property, MaintenanceRequest, Review, Renovation
from src.model.residency import Resident


p1 = Property('London', 'England', 12.54, ['bath', 'shower', 'wi-fi', 'king-size bed'], 1000.49)
r2 = Resident("Stoffer", 'Email: stofferiscool@gmail.com')
u1 = User('Sviatik', 'Turbo', 'Renter')
admin1 = Admin(username='admin', password_hash='cooladminpassword', role='Admin')
pm1 = PropertyManager(username='pm', password_hash='bestpm', role='Manager')
renter1 = Renter(
    username="Max",
    password_hash="secret",
    role="Renter"
)


def test_user_creation():
    user = User('newuser', '123', 'user')
    assert user.username == 'newuser'
    assert user.role == 'user'
    assert user.not_unique == 1


def test_existing_username():
    User('copycat', 'pass123', 'guest')
    user2 = User('copycat', 'pass123', 'guest')
    assert user2.not_unique == 0


def test_admin_property_management():
    admin1.add_property(p1)
    assert p1 in rc.get_properties()
    admin1.remove_property(p1)
    assert p1 not in rc.get_properties()


def test_property_manager_actions():
    mr = MaintenanceRequest(p1)
    pm1.manage_maintenence_request(mr, 'approve')
    assert mr.status == 'approved'
    ren1 = Renovation(p1, 1000, "the issue has been resolved")
    pm1.resolve_maintenence_request(mr, ren1)
    assert mr.status == 'resolved'

    pm1.assign_property(p1)
    assert p1 in pm1.properties_managed


def test_renter_actions():
    renter1.become_resident(r2, 'secret')
    assert renter1.resident == r2

    review = Review(Property('A', 'B', 1, [], 1), 5, "Good")
    renter1.leave_a_review('secret', review)
    assert len(renter1.reviews) == 1
    renter1.leave_a_review('secret', review)  # Should reject
    assert len(renter1.reviews) == 1


def test_notification_system():
    user = User('notif', 'notificatorpass', 'guest')
    note = Notification("Just texting bro", user, True)
    assert len(user.notifications) == 1
    assert str(user.notifications[0]) == "Just texting bro"