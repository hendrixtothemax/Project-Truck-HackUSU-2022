from src.Event import Event
import time

class DungeonEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Dungeon Event")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("Your boots slip on the slick dungeon steps. You must be at least a mile underground at this point. The darkness bites to the bone, and you wish to go home.")
        time.sleep(2)
        print("You turn to head back up the steps, only to find a figure slowly descending toward you")