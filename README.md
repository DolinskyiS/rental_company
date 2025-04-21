import:
datetime for the dates
from unittest imported patch for easier testing
uuid for unqiue IDs
geopy for locations


non-UML:
Property:
for class Property I added additional inits separately for city and country
becaues it was needed for Navigation get_nearest_available_property



Late Payments:

i was having some trouble with determining how late_payment should work,
and considering date that a typical rent day is 1st of the month, i wrote 
code the way that in any circumstance a payment is considered late if it wasn't
paid in the interval between 11st and 5th of the month, so if the payment was made
in advance(like 30th or 31th) it will be considered late.

As a way to implement late fee, i made a status of the payment be "Unfinished" if  
the payment isn't complete(not full amount payed, or fees aren't considered)

user_interface.py:

for most of the User actions i made an obligatory authentication

For dates in Contracts, Leases etc you need to write date(year, month, day)

