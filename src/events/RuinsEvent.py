from src.Event import Event
import time

class RuinsEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Ruins Event")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("You walk up to an ancient, collapsed building overgrown with moss. The architecture is foreign and somewhat terrifying, setting you on edge.")
        time.sleep(2)
        print("You hear a sound from behind a shattered pillar and you whirl, heart leaping...")
