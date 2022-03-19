from src.Event import Event
import time

from src.UserInput import UserInput


class DiscoverChest(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Discover Chest")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("You pick up a map laying on the side of the road. A large, flamboyant X marks a spot not too far from this very location.")
        time.sleep(2)
        print("You look around for who might have dropped such an obviously valuable piece of information. You see no one.")
        time.sleep(2)
        print("1- Follow the map to the x.")
        time.sleep(2)
        print("2- Drop the map and continue on your way.")
        time.sleep(2)
        userInput = UserInput("Type 1 or 2.", 2, ["", ""])
        choice1 = userInput.getInput()
        if choice1 == 1:
            print("You follow the map a couple miles to the location it specifices. Hidden between a set of boulders lies a wooden chest, worn from weather but otherwise unharmed.")
            time.sleep(2)
            print("1- Open the chest.")
            time.sleep(2)
            print("2- It's a trap. Run.")
            time.sleep(2)
            userInput = UserInput("Type 1 or 2.", 2, ["", ""])
            choice2 = userInput.getInput()
            if choice2 == 1:
                print("You open the chest slowly, entire body braced for an explosion.")
                time.sleep(2)
                print("Nothing happens. Relieved, you reach inside and pull out what's within.")
                time.sleep(2)
                # add weapon n+1 to inventory
            elif choice2 == 2:
                print("You turn on your heel and sprint away. No way are you opening something that's so obviously a trap")
        elif choice1 == 2:
            print("You continue on your way, nothing but the end goal in mind.")

        print("You head back to the starter town.")