from src.Event import Event
import time

from src.UserInput import UserInput


class HelpBartender(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Help Bartender")

    # When Creating New Events, Put Event Code In Here
    def run(self, player,floor):
        print("You enter one of your favorite taverns and sit down at the bar. The bartender, a burly woman with massive, cord-like arms smiles grimly.")
        time.sleep(2)
        print("She informs you that her daughter was sick and could not serve drinks like she usually does. She offers three weeks of free drinks if you wait tables for the night.")
        time.sleep(2)
        print("1- Accept the offer. Anything for free drinks.")
        time.sleep(2)
        print("2- Shake your head. You have better things to do.")
        time.sleep(2)
        userInput = UserInput("Type 1 or 2.", 2, ["", ""])
        choice1 = userInput.getInput()
        if choice1 == 1:
            print("She dips her head in gratitude and fills you in on all the required details. She asks if you are also willing to help with cooking and dishes.")
            time.sleep(2)
            print("1- Four weeks of free drinks.")
            time.sleep(2)
            print("2- No. Anything but dishes.")
            time.sleep(2)
            userInput = UserInput("Type 1 or 2.", 2, ["", ""])
            choice2 = userInput.getInput()
            if choice2 == 1:
                print("You gleefully wait tables and do the dishes for the next several hours.")
                time.sleep(2)
                print("You get free drinks the entire time as well as for four weeks.")
                time.sleep(2)
            elif choice2 == 2:
                print("You wait tables, but nothing more. The innkeeper keeps her word for three weeks of free drinks. You'll be sure to come by often.")
        elif choice1 == 2:
            print("You continue on your way, nothing but the end goal in mind.")

        print("You head back to the starter town.")