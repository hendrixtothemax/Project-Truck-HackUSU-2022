from src.Event import Event
import time

class PlainsEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Plains Event")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("The grass sways in the wind, tall and dark. Signs of a wet year. You think you see something flit through the grass a fair distance off, but you shake your head, dismissing it.")
        time.sleep(2)
        print("A heavy rustle out of time with the wind. You draw your weapon, turning...")