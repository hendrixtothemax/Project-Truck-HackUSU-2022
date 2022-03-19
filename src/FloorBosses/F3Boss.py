from src.Enemy import Enemy


class Megumin(Enemy):
    def __init__(self):
        name = "Megumin"
        desc = "EXPLOSION."
        health = 40
        floor = 2
        minDamage = 25
        maxDamage = 26
        super().__init__(name, desc, health, floor, minDamage, maxDamage)