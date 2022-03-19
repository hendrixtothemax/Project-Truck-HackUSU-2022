from src.Event import Event
import time

from src.UserInput import UserInput


class RecoverLostItem(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Recover Lost Item")

    # When Creating New Events, Put Event Code In Here
    def run(self, player,floor):
        print("A woman sorts through the piles of trash outside her home. She appears completely panicked and desperate.")
        time.sleep(2)
        print("You scratch your head, wondering what it is she is doing.")
        time.sleep(2)
        print("1- Walk up and ask what she is doing.")
        time.sleep(2)
        print("2- Ignore her and move on. You have better things to do.")
        time.sleep(2)
        userInput = UserInput("Type 1 or 2.", 2, ["", ""])
        choice1 = userInput.getInput()
        if choice1 == 1:
            print("Through heavy breaths, she points at the pile of garbage and informs you that she has lost her wedding ring within. She implores for your help finding it.")
            time.sleep(2)
            print("1- Of course you'll help. Wedding rings are very special, after all.")
            time.sleep(2)
            print("2- Touch trash? No thank you.")
            time.sleep(2)
            userInput = UserInput("Type 1 or 2.", 2, ["", ""])
            choice2 = userInput.getInput()
            if choice2 == 1:
                print("You sort through the trash alongside her for close to twenty minutes. She grows calmer as you help.")
                time.sleep(2)
                print("You find the ring lodged in some metal piping at the bottom and she thanks you close to a thousand times before rushing back inside.")
                time.sleep(2)
                # add weapon n+1 to inventory
            elif choice2 == 2:
                print("You walk away, leaving the woman to her hysteria.")
        elif choice1 == 2:
            print("You continue on your way, nothing but the end goal in mind.")

        print("You head back to the starter town.")