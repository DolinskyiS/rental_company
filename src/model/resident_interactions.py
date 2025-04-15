from asyncio import events

from src.model.residency import Resident, r1
from property import Property, p1
import uuid

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
        print('complainiiing')

    def resolve(self):
        self.status = "Resolved"
        print('Complaint has been successfully resolved')
        return True

class Event:
    def __init__(self, text: str):
        self.opened = False
        self.text = text


class EventLog:
    def __init__(self):
        self.events = []

    def record_event(self, event: Event):
        self.events.append(event)
        print(f"The Event has been successfully recorded")

    def read_new_messages(self):
        for event in self.events:
            if not event.opened:
                event.opened = True
                print('readiiing')
                print(event.text)




    def read_all_messages(self):
        pass

complaint1 = Complaint(r1, p1, 'Faulty Fridge')

EventLog = EventLog()
EventLog.read_new_messages()