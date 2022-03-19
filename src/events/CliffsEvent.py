from src.Event import Event
import time

class CliffsEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Cliffs Event")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("The wind howls as you edge up to the cliff. You peer over to see an endless drop into mist and clouds.")
        time.sleep(2)
        print("You turn at the sound of rocks sliding, hand going to your weapon.")