from src.Event import Event
import time

from src.UserInput import UserInput


class DeliverMessage(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Deliver Message")

    # When Creating New Events, Put Event Code In Here
    def run(self, player,floor):
        print("A frantic young girl nearly collides with you as you round a bend in the road. She tumbles to the ground, dropping a bunch of letters.")
        time.sleep(2)
        print("Panicked, she starts to gather the letters, nearly crushing the papers in her fists.")
        time.sleep(2)
        print("1- Implore her to calm down and offer your help.")
        time.sleep(2)
        print("2- Tell her to watch where she is going and continue on.")
        time.sleep(2)
        userInput = UserInput("Type 1 or 2.", 2, ["", ""])
        choice1 = userInput.getInput()
        if choice1 == 1:
            print("She stops for a moment, eyes wide. She then asks you if you can deliver one of the letters she forgot to deliver in the previous town.")
            time.sleep(2)
            print("1- Accept the request. You were going there anyway, it won't be too much trouble.")
            time.sleep(2)
            print("2- Shake your head. You are not a delivery boy.")
            time.sleep(2)
            userInput = UserInput("Type 1 or 2.", 2, ["", ""])
            choice2 = userInput.getInput()
            if choice2 == 1:
                print("Take the letter from her and slip it into your coat pocket. She thanks you profusely and sprints off in the other direction.")
                time.sleep(2)
                print("When the card is delivered, you feel a slight swelling of warmth in your chest. Gone in a flash.")
                time.sleep(2)
            elif choice2 == 2:
                print("You march away from the girl, leaving her to deliver the letters on her own.")
        elif choice1 == 2:
            print("You continue on your way, nothing but the end goal in mind.")

        print("You head back to the starter town.")