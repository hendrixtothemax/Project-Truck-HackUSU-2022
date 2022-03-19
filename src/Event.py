class Event:
    def __init__(self, name, desc=""):
        self.name = name
        self.desc = desc

    def run(self, player):
        print("Event Class")

    def __repr__(self):
        return self.name


