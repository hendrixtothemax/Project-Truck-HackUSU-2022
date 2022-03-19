import random
import time

from src.Combat import Combat
from src.FinalBoss.DemonLord import DemonLord
from src.FloorBosses.F1Boss import Aqua
from src.FloorBosses.F2Boss import Rem
from src.FloorBosses.F3Boss import Megumin
from src.FloorBosses.F4Boss import Ram
from src.SideEvents.BuryCorpses import BuryCorpses
from src.SideEvents.CatchPigs import CatchPigs
from src.SideEvents.CleanWarehouse import CleanWarehouse
from src.SideEvents.DeliverMessage import DeliverMessage
from src.SideEvents.DiscoverChest import DiscoverChest
from src.SideEvents.HelpBartender import HelpBartender
from src.SideEvents.HelpOldMan import HelpOldMan
from src.SideEvents.RecoverLostItem import RecoverLostItem
from src.UserInput import UserInput
from src.events.BeachEvent import BeachEvent
from src.events.BogEvent import BogEvent
from src.events.CastleEvent import CastleEvent
from src.events.CavesEvent import CavesEvent
from src.events.CliffsEvent import CliffsEvent
from src.events.DungeonEvent import DungeonEvent
from src.events.ForestEvent import ForestEvent
from src.events.MireEvent import MireEvent
from src.events.PlainsEvent import PlainsEvent
from src.events.RiverEvent import RiverEvent
from src.events.RuinsEvent import RuinsEvent
from src.events.VillaEvent import VillaEvent


class branch:
    def __init__(self,player,floor = 1):
        self.player = player
        self.events = []
        self.quests = []
        self.floor = floor

        event1 = BeachEvent()
        event2 = BogEvent()
        event3 = CastleEvent()
        event4 = CavesEvent()
        event5 = CliffsEvent()
        event6 = DungeonEvent()
        event7 = ForestEvent()
        event8 = MireEvent()
        event9 = PlainsEvent()
        event10 = RiverEvent()
        event11 = RuinsEvent()
        event12 = VillaEvent()

        self.validevents = [event1, event2, event3, event4, event5, event6, event7, event8, event9, event10, event11, event12]

        quest1 = BuryCorpses()
        quest2 = CatchPigs()
        quest3 = CleanWarehouse()
        quest4 = DeliverMessage()
        quest5 = DiscoverChest()
        quest6 = HelpBartender()
        quest7 = HelpOldMan()
        quest8 = RecoverLostItem()

        self.validquests = [quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8]

        if floor == 5:
            self.finalboss(floor)
        self.randomevent(floor)
        time.sleep(1)
        player.health.addHealth(10)
        print("*You have healed 10 hitpoints overnight!*")
        print("\n")
        time.sleep(1)
        self.randomsidequest(floor)
        self.randomevent(floor)
        player.health.addHealth(10)
        print("\n")
        print("*You have healed 10 hit points overnight!*")
        print("\n")
        self.floorboss(floor)
        player.health.addHealth(99)
        # print(self.events)
        # print(self.quests)


    def randomevent(self,floor):

        # Testing Code Line Directly Below
        #self.events.append(events.pop(0))

        for i in range(4):
            location = random.randint(0, len(self.validevents) - 1)
            self.events.append(self.validevents.pop(location))

        print("You look at the QUEST postings to see what is available.")


        userInput = UserInput("Type 1, 2, 3, or 4 to choose a quest.", 4, [self.events[0], self.events[1],self.events[2],self.events[3]])
        choice1 = userInput.getInput()
        if choice1 == 1:
            self.events[0].run(self.player,floor)
        elif choice1 ==2:
            self.events[1].run(self.player,floor)
        elif choice1 == 3:
            self.events[2].run(self.player,floor)
        elif choice1 == 4:
            self.events[3].run(self.player,floor)

        self.events = []

        #Testing Code Line Directly Below
        #self.events[0].run(self.player)

        # for event in self.events:
        #     event.run(self.player)

    def randomsidequest(self,floor):


        #test like above
        #self.quests.append(quests.pop(0))

        for i in range(len(self.validquests)):
            location = random.randint(0, len(self.validquests) - 1)
            self.quests.append(self.validquests.pop(location))

        self.quests[location].run(self.player,floor)

        self.quests = []

        #test like above
        #self.quests[0].run(self.player)


    def floorboss(self,floor):
        print("After finishing off more than a few of the Demon Lord's underlings, you find yourself drawn to a tower you had not noticed before.")
        time.sleep(2)
        print("You stride confidently up to the front door, fear a distant thing. Mist swirls around your ankles and the door groans loudly as you enter.")
        time.sleep(2)
        print("\n")
        print("YOU HAVE ENTERED THE DOMAIN OF THE FLOOR BOSS")
        time.sleep(2)
        print("YOU MUST DEFEAT IT TO ADVANCE TO THE NEXT FLOOR")
        if floor == 1:
            possibleEnemies = [Aqua()]
            combat = Combat(self.player, possibleEnemies, 1,floor,True)
            combat.start()
        elif floor == 2:
            possibleEnemies = [Rem()]
            combat = Combat(self.player, possibleEnemies, 1,floor,True)
            combat.start()
        elif floor == 3:
            possibleEnemies = [Megumin()]
            combat = Combat(self.player, possibleEnemies, 1,floor,True)
            combat.start()
        elif floor == 4:
            possibleEnemies = [Ram()]
            combat = Combat(self.player, possibleEnemies, 1,floor,True)
            combat.start()
        print("\n")
        print("YOU HAVE DEFEATED THE FLOOR BOSS")
        time.sleep(2)
        print("YOU ADVANCE TO THE NEXT FLOOR")
        self.floor += 1
        time.sleep(2)
        print("\n")
        print("You climb to the top of the spire and exit out onto the NEXT FLOOR.")
        time.sleep(2)
        print("\n")
        print("*The magical barrier between floors has restored you to full health!*")
        print("\n")
        time.sleep(2)
        print("The first town you come across is less busy than the first. Everyone you see here is a seasoned adventurer.")
        time.sleep(2)
        print("You walk into the town, a sense of familiarity growing around you.")


    def finalboss(self,floor):
        if floor == 5:
            possibleEnemies = [DemonLord()]
            combat = Combat(self.player, possibleEnemies, 1, floor, True)
            combat.start()
