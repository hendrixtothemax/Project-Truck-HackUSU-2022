class Event:
    def __init__(self, name, desc="",floor=1):
        self.name = name
        self.desc = desc
        self.floor = floor

    def run(self, player,floor):
        print("Event Class")

    def __repr__(self):
        return self.name


