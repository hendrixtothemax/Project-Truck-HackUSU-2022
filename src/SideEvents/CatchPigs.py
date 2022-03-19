from src.Event import Event
import time

class CatchPigs(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Catch Pigs")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("You stride confidently up to the shore, the waves lapping gently against the sand.")
        time.sleep(2)
        print("You narrow your eyes at a dark form in the sand. It begins to move...")