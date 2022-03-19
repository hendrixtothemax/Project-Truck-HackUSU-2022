from src.Character import character
from src.events.TestEvent import TestEvent
from src.events.TestEvent2 import TestEvent2

testCharacter = character("Tohka","A strong headed girl with a tendency to shoot first and ask questions later",100)

event1 = TestEvent()
#event2 = TestEvent2()

events = [event1, event1]

event1.run(testCharacter)

for event in events:
    event.run(testCharacter)