from src.Event import Event
import time

class BogEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Bog Event")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("The mud sucks at your boots as you struggle along what you thought had been a path.")
        time.sleep(2)
        print("From up ahead, you hear a terrible squelching noise. A form rises from the mud... you bear your weapons.")