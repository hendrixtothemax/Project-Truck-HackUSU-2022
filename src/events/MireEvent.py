from src.Event import Event
import time

class MireEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Mire Event")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("Fog sweeps the land to the point you can't tell which direction is which despite it being high noon.")
        time.sleep(2)
        print("The ominous sound of approaching figures filters through the mist. You draw your weapons.")