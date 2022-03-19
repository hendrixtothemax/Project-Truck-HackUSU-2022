from src.Enemy import Enemy


class CursedSpirit(Enemy):
    def __init__(self):
        name = "Cursed Spirit"
        desc = "A ghost with a knack for revenge. Not sure if it knows it's dead..."
        health = 47
        floor = 3
        minDamage = 26
        maxDamage = 29
        super().__init__(name, desc, health, floor, minDamage, maxDamage)