
from src.Health import Health

class character:
    def __init__(self,name,description,health):
        self.name = name
        self.description = description
        self.health = Health(health)

    def fullDesc(self):
        return f"{self.name}: {self.description}\n\t\tTheir health is: {self.health.health}"

    def __str__(self):
        return self.name




