from src.Enemy import Enemy


class BlightedDemon(Enemy):
    def __init__(self):
        name = "Blighted Demon"
        desc = "A walking calamity. Run if sighted."
        health = 55
        floor = 3
        minDamage = 24
        maxDamage = 27
        super().__init__(name, desc, health, floor, minDamage, maxDamage)