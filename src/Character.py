
class character:
    def __init__(self,name,description):
        self.name = name
        self.description = description

    def status(self):
        print(self.name + ": " + self.description)

    def __str__(self):
        return self.name




