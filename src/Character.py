
class character:
    def __init__(self,name,description,health):
        self.name = name
        self.description = description
        self.health = health

    def status(self):
        print(self.name + ": " + self.description)
        print("          Their health is: " + str(self.health))


    def __str__(self):
        return self.name




