import random


class branch:
    def __init__(self):
        print("INIT Branch")
        self.events = []
        self.randomevent()
        print(self.events)

    def randomevent(self):
        events = ["Ruins", "Forest", "Caves", "Dungeons", "Bog", "Mire", "Castle", "Villa", "Cliffs", "Plains", "River",
                  "Beach"]
        for i in range(4):
            location = random.randint(0, len(events) - 1)
            self.events.append(events.pop(location))
