from src.Event import Event


class TestEvent(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Test Event 1")

    # When Creating New Events, Put Event Code In Here
    def run(self, player):
        print("testing!" + self.name)
        print(str(player))