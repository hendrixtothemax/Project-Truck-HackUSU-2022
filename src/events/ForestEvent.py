from src.Event import Event
import time

class ForestEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Forest Event")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("The forest seems alive around you. Birds chirp endlessly, the air abuzz with the noise of insects and the rustle of leaves in the wind.")
        time.sleep(2)
        print("All at once it stops, the dead silence consuming you. You whirl toward the sound of footfall to see a dark figure break through the trees...")