from src.Event import Event
import time

class CastleEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Castle Event")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("The ominous castle seems abandoned as you stride through the main gates. Corpses still cover the courtyard.")
        time.sleep(2)
        print("You hear the scuff of boots from behind. You whirl around, drawing your weapon.")