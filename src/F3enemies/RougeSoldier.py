from src.Enemy import Enemy


class RougeSoldier(Enemy):
    def __init__(self):
        name = "Rouge Soldier"
        desc = "Well trained and desperate for a few coins."
        health = 36
        floor = 2
        minDamage = 17
        maxDamage = 18
        super().__init__(name, desc, health, floor, minDamage, maxDamage)