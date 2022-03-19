import random
import time

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
    def __init__(self,player):
        self.player = player
        self.events = []
        self.quests = []

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

        self.randomevent()
        time.sleep(3)
        self.randomsidequest()
        self.randomevent()
        # print(self.events)
        # print(self.quests)

    def randomevent(self):



        # Testing Code Line Directly Below
        #self.events.append(events.pop(0))

        for i in range(4):
            location = random.randint(0, len(self.validevents) - 1)
            self.events.append(self.validevents.pop(location))

        print("You look at the QUEST postings to see what is available.")


        userInput = UserInput("Type 1, 2, 3, or 4 to choose a quest.", 4, [self.events[0], self.events[1],self.events[2],self.events[3]])
        choice1 = userInput.getInput()
        if choice1 == 1:
            self.events[0].run(self.player)
        elif choice1 ==2:
            self.events[1].run(self.player)
        elif choice1 == 3:
            self.events[2].run(self.player)
        elif choice1 == 4:
            self.events[3].run(self.player)

        self.events = []

        #Testing Code Line Directly Below
        #self.events[0].run(self.player)

        # for event in self.events:
        #     event.run(self.player)

    def randomsidequest(self):


        #test like above
        #self.quests.append(quests.pop(0))

        for i in range(len(self.validquests)):
            location = random.randint(0, len(self.validquests) - 1)
            self.quests.append(self.validquests.pop(location))

        self.quests[location].run(self.player)

        self.quests = []

        #test like above
        #self.quests[0].run(self.player)