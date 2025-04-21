from src.model.events import EventLog, Event, EventLogYes


def test_event_creation():
    event = Event("Test message")
    assert event.text == "Test message"
    assert event.opened is False
    assert len(EventLogYes.events) == 1


def test_event_log_recording():
    log = EventLog()
    event = Event("Test")
    log.record_event(event)
    assert len(log.events) == 1
    assert log.events[0] == event


def test_read_new_messages(capsys):
    event1 = Event("Msg1")
    event2 = Event("Msg2")
    event1.opened = True

    EventLogYes.read_new_messages()
    captured = capsys.readouterr()
    assert "Msg2" in captured.out
    assert "Msg1" not in captured.out
    assert event2.opened is True


def test_read_all_messages(capsys):
    Event("Msg1")
    Event("Msg2")

    EventLogYes.read_all_messages()
    captured = capsys.readouterr()
    assert "Msg1" in captured.out
    assert "Msg2" in captured.out
    assert all(e.opened for e in EventLogYes.events)


def test_auto_registration():
    initial_count = len(EventLogYes.events)
    Event("Auto message")
    assert len(EventLogYes.events) == initial_count + 1