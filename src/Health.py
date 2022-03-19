
class Health:
    health = 100
    armor = 0

    def __init__(self, health, armor):
        self.health = health
        self.armor = armor

    def __int__(self, health):
        self.__init__(health, 0)

    def __init__(self):
        self.__int__(100)
