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

class RiverEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Cleanse the River")

    # When Creating New Events, Put Event Code In Here
    def run(self, player,floor):
        print("The river gurgles as you kneel down to fill your water skin. This is the only watering hold in miles and you flinch at every sound.")
        time.sleep(2)
        print("A figure appears on the other bank of the river. You recognize it, draw your weapon.")

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