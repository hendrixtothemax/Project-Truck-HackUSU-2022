from src.Event import Event
import time

from src.Combat import Combat

from src.F1enemies.ChildLich import ChildLich
from src.F1enemies.Ghoul import Ghoul
from src.F1enemies.Skeleton import Skeleton
from src.F1enemies.Zombie import Zombie
from src.F2enemies.ArmedBeggar import ArmedBeggar
from src.F2enemies.Bandit import Bandit
from src.F2enemies.EscapedConvict import EscapedConvict
from src.F2enemies.Ninja import Ninja
from src.F3enemies.Assassin import Assassin
from src.F3enemies.RougeSoldier import RougeSoldier
from src.F3enemies.UndeadWitch import UndeadWitch
from src.F3enemies.Vampire import Vampire
from src.F4enemies.BlightedDemon import BlightedDemon
from src.F4enemies.CursedSpirit import CursedSpirit
from src.F4enemies.MadWarlock import MadWarlock
from src.F4enemies.UndeadDuelist import UndeadDuelist



class BeachEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Secure the Beach")

    # When Creating New Events, Put Event Code In Here
    def run(self, player,floor):
        print("You stride confidently up to the shore, the waves lapping gently against the sand.")
        time.sleep(2)
        print("You narrow your eyes at a dark form in the sand. It begins to move...")
        #initiate combat
        if floor == 1:
            possibleEnemies = [ChildLich(), Ghoul(), Skeleton(), Zombie()]
            combat = Combat(player, possibleEnemies, 2,floor)
            combat.start()
        elif floor == 2:
            possibleEnemies = [ArmedBeggar(), Bandit(), EscapedConvict(), Ninja()]
            combat = Combat(player, possibleEnemies, 2,floor)
            combat.start()
        elif floor == 3:
            possibleEnemies = [Assassin(), RougeSoldier(), UndeadWitch(), Vampire()]
            combat = Combat(player, possibleEnemies, 2,floor)
            combat.start()
        elif floor == 4:
            possibleEnemies = [BlightedDemon(), CursedSpirit(), MadWarlock(), UndeadDuelist()]
            combat = Combat(player, possibleEnemies, 2,floor)
            combat.start()


