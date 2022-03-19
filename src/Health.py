
class Health:
    health = 100
    maxHealth = 100
    armor = 0
    maxArmor = 0

    def __init__(self, maxHealth=100, maxArmor=0, health=None, armor=None):
        self.maxHealth = maxHealth
        self.maxArmor = maxArmor
        if health is None:
            self.health = self.maxHealth
        else:
            self.health = health
        if armor is None:
            self.armor = self.maxArmor
        else:
            self.armor = armor

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

    def healthReadout(self):
        return f"[{self.health}/{self.maxHealth}]"
