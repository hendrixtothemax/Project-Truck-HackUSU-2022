from src.events.TestEvent import TestEvent
from src.events.TestEvent2 import TestEvent2

event1 = TestEvent()
event2 = TestEvent2()

events = [event1, event2]

event1.run()

for event in events:
    event.run()