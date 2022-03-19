
class Health:
    health = 100
    maxHealth = 100
    armor = 0
    maxArmor = 0

    def __init__(self, maxHealth, maxArmor, health, armor):
        self.maxHealth = maxHealth
        self.maxArmor = maxArmor
        self.armor = armor
        self.health = health

    def __init__(self, maxHealth, maxArmor, health):
        self.__init__(maxHealth, maxArmor, health, maxArmor)

    def __init__(self, maxHealth, maxArmor):
        self.__int__(maxHealth, maxArmor, maxHealth)

    def __int__(self, maxHealth):
        self.__init__(maxHealth, 0)

    def __init__(self):
        self.__int__(100)

    def addHealth(self, addHealth):
        proposedNewHealth = self.health + addHealth
        if proposedNewHealth > self.maxHealth:
            self.health = self.maxHealth
        else:
            self.health = proposedNewHealth

    def subHealth(self, subHealth):
        proposedNewHealth = self.health - subHealth
        self.health = proposedNewHealth

    def addArmor(self, addArmor):
        proposedNewArmor = self.armor + addArmor
        if proposedNewArmor > self.maxArmor:
            self.armor = self.maxArmor
        else:
            self.armor = proposedNewArmor

    def subArmor(self, subArmor):
        proposedNewArmor = self.armor - subArmor
        self.health = proposedNewArmor
        