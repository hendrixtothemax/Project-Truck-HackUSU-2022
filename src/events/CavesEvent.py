from src.Event import Event
import time

class CavesEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Caves Event")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("The cave is dark as you peer inside. The darkness stares back. You lose focus, mind going blank.")
        time.sleep(2)
        print("You manage to recover just in time to see a figure lurch from the shadows...")