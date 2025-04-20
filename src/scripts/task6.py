from src.model.user_interface import Renter, Notification
from datetime import date

def notificator():
    for renter in Renter.all_renters:
        if renter.resident:
            lease = renter.resident.get_active_lease()
            today = date.today()
            lease_dd = lease.start_date.replace(year=today.year, month=today.month)
            if lease_dd < today:
                Notification("You are late on your payment. You will be charged 20% more", renter, True)

            if lease.end_date <= today:
                Notification("Your lease has expired", renter, True)



if __name__ == "__main__":
    notificator()
