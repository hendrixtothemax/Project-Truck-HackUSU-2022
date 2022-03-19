from src.Event import Event


class TestEvent2(Event):

    def __init__(self):
        # (eventName, eventDescription)
        super().__init__("Test Event 2")

    # When Creating New Events, Put Event Code In Here
    def run(self):
        print("testing!" + self.name)