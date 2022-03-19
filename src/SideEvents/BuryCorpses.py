from src.Event import Event
import time

from src.UserInput import UserInput


class BuryCorpses(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("BuryCorpses")

    # When Creating New Events, Put Event Code In Here
    def run(self,player,floor):
        self.player = player
        print("As you shufle down the road, a weary soldier hails you from a ways off. He holds a shovle and wears a white bandana tied around his face.")
        time.sleep(2)
        print("There are corpses littered all around him, cut down not too long ago. What do you do?")
        time.sleep(2)
        print("1- Walk to the soldier and see what he wants.")
        time.sleep(2)
        print("2- Ignore the soldier and continue on your way.")
        time.sleep(2)
        userInput = UserInput("Type 1 or 2.", 2, ["", ""])
        choice1 = userInput.getInput()
        if choice1 == 1:
            print("You stride over to the soldier. He gestures to the bodies with sad eyes and asks for your help to bury them. ")
            time.sleep(2)
            print("1- Nod and grab one of the spare shovels nearby.")
            time.sleep(2)
            print("2- Shake your head in disgust and continue on your way.")
            time.sleep(2)
            userInput = UserInput("Type 1 or 2.", 2, ["", ""])
            choice2 = userInput.getInput()
            if choice2 == 1:
                print("You get to work, helping him load the twenty odd corpses into a shallow mass grave.")
                time.sleep(2)
                print("You set the shovel down and make to leave, but he stops you and hands you something.")
                time.sleep(2)
                weapon = self.player.weapons.getRandomWeaponByLevel(str(self.floor+1))
                self.player.addItemToInventory(weapon)
                print(f"{weapon.name} has been added to your inventory!")
                time.sleep(2)
            elif choice2 == 2:
                    print("The soldier looks at you knowingly and lets you walk away. You continue on your way.")
        elif choice1 == 2:
            print("You continue on your way, nothing but the end goal in mind.")
            time.sleep(2)

        print("You head back to the starter town.")
        time.sleep(2)