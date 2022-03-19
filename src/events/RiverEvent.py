from src.Event import Event
import time

class RiverEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("River Event")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("The river gurgles as you kneel down to fill your water skin. This is the only watering hold in miles and you flinch at every sound.")
        time.sleep(2)
        print("A figure appears on the other bank of the river. You recognize it, draw your weapon.")