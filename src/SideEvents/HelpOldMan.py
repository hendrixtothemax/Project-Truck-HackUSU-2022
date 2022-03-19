from src.Event import Event
import time

from src.UserInput import UserInput


class HelpOldMan(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Help Old Man")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("You see an old crippled man on the side of the road holding out a tin cup. An odd place for a beggar.")
        time.sleep(2)
        print("He seems to be sick or ailed in some way.")
        time.sleep(2)
        print("1- Stop by the man and ask if he needs help.")
        time.sleep(2)
        print("2- Continue on your way, ignoring the man.")
        time.sleep(2)
        userInput = UserInput("Type 1 or 2.", 2, ["", ""])
        choice1 = userInput.getInput()
        if choice1 == 1:
            print("He looks up in your direction, eyes narrowed. He grins a toothless grin and proffers his tin cup.")
            time.sleep(2)
            print("1- Drop in a few coins and smile at the old man.")
            time.sleep(2)
            print("2- Shake your head and continue forward.")
            time.sleep(2)
            userInput = UserInput("Type 1 or 2.", 2, ["", ""])
            choice2 = userInput.getInput()
            if choice2 == 1:
                print("The old man slowly stands and beckons you forward. Confused, you follow him to a small hidden valley behind some boulders.")
                time.sleep(2)
                print("He pulls out a large chest and opens it. From within, he withdraws and item and hands it to you.")
                time.sleep(2)
                # add weapon n+1 to inventory
            elif choice2 == 2:
                print("The old man sighs softly as you leave.")
        elif choice1 == 2:
            print("You continue on your way, nothing but the end goal in mind.")

        print("You head back to the starter town.")