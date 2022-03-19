from src.Combat import Combat
from src.Event import Event
import time

from src.F1enemies.Zombie import Zombie


class BeachEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Beach Event")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("You stride confidently up to the shore, the waves lapping gently against the sand.")
        time.sleep(2)
        print("You narrow your eyes at a dark form in the sand. It begins to move...")
        #initiate combat
        possibleEnemies = [Zombie()]
        combat = Combat(player, possibleEnemies, 2)
        combat.start()


