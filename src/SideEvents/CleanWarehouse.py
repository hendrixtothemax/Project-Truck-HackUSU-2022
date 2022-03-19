from src.Event import Event
import time

from src.UserInput import UserInput


class CleanWarehouse(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Clean Warehouse")

    # When Creating New Events, Put Event Code In Here
    def run(self, player,floor):
        self.player = player
        print("The small port in this town is very old and hardly used. You pass by a sunken warehouse in terrible condition, dirt and grim covering every wall.")
        time.sleep(2)
        print("You spot a small woman scrubbing away at the grim. It seems like she's been there for hours.")
        time.sleep(2)
        print("1- Walk up and offer to help her.")
        time.sleep(2)
        print("2- Shake your head and continue on your way.")
        time.sleep(2)
        userInput = UserInput("Type 1 or 2.", 2, ["", ""])
        choice1 = userInput.getInput()
        if choice1 == 1:
            print("The woman looks up and smiles. She asks what you need.")
            time.sleep(2)
            print("1- Ask if you can help clean.")
            time.sleep(2)
            print("2- Change your mind and walk away.")
            time.sleep(2)
            userInput = UserInput("Type 1 or 2.", 2, ["", ""])
            choice2 = userInput.getInput()
            if choice2 == 1:
                print("Her face radiates gratitude and she swiftly sets you to work cleaning the other side of the building.")
                time.sleep(2)
                print("After a few hours of good work, everything is finished. You start to head off when she stops you, handing you something.")
                time.sleep(2)
                weapon = self.player.weapons.getRandomWeaponByLevel(str(self.floor + 1))
                self.player.addItemToInventory(weapon)
                print(f"{weapon.name} has been added to your inventory!")
            elif choice2 == 2:
                print("She stares after you, a confused look on her face.")
        elif choice1 == 2:
            print("You continue on your way, nothing but the end goal in mind.")
            time.sleep(2)

        print("You head back to the starter town.")
        time.sleep(2)