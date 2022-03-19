from src.Event import Event
import time

class VillaEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Villa Event")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("The Villa seems empty for some reason. You enter to investigate only to find the place smashed to near ruin.")
        time.sleep(2)
        print("On the third floor, you find fresh blood. You draw your weapon and slowly enter the next room...")