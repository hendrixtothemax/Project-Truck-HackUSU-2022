from src.Event import Event
import time

from src.UserInput import UserInput


class CatchPigs(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Catch Pigs")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("You pass by a farmhouse, the wail of children and the general din of animals filling the air.")
        time.sleep(2)
        print("A farmer spots you and waves his arms desperately, a horror filled look on his face.")
        time.sleep(2)
        print("1- Walk over to see what is the matter.")
        time.sleep(2)
        print("2- Ignore him and continue on your way.")
        time.sleep(2)
        userInput = UserInput("Type 1 or 2.", 2, ["", ""])
        choice1 = userInput.getInput()
        if choice1 == 1:
            print("You walk up to the farmer and ask what has happen. He informs you that his prized pig has escaped the pen and needs your help recovering it.")
            time.sleep(2)
            print("1- Accept the proposal. You have a bit of spare time, after all.")
            time.sleep(2)
            print("2- Laugh in the farmers face and turn away. You have better things to do.")
            time.sleep(2)
            userInput = UserInput("Type 1 or 2.", 2, ["", ""])
            choice2 = userInput.getInput()
            if choice2 == 1:
                print("You scour the farmland for the pig. You find tracks and follow it to the bank of a nearby creak.")
                time.sleep(2)
                print("You capture the pig with ease. The thing was no match for you anyway. Upon returning the prized animal, the farmer nods and gives you a loaf of bread. Very kind of him.")
                time.sleep(2)
            elif choice2 == 2:
                print("You scoff and turn from the old man. He can catch his own pig.")
        elif choice1 == 2:
            print("You continue on your way, nothing but the end goal in mind.")

        print("You head back to the starter town.")