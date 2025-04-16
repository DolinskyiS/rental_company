# from asyncio import events

# from src.model.residency import Resident, r1
# from src.model.property import Property, p1



class EventLog:
    def __init__(self):
        self.events: list["Event"] = []

    def record_event(self, event: "Event"):
        self.events.append(event)
        print(f"The Event has been successfully recorded")

    def read_new_messages(self):
        for event in self.events:
            if not event.opened:
                # print('readiiing')
                print(event.text)
                event.opened = True


    def read_all_messages(self):
        for event in self.events:
            # print('readdddd')
            print(event.text)
            event.opened = True

EventLogYes = EventLog()

class Event:
    def __init__(self, text: str):
        self.opened: bool = False
        self.text = text
        self._auto()

    def _auto(self):
        EventLogYes.record_event(self)
        # print('event has been recorded')

# print(EventLogYes.events)




