from src.Enemy import Enemy


class Vampire(Enemy):
    def __init__(self):
        name = "Vampire"
        desc = "A pale demon with twisted lusts."
        health = 40
        floor = 2
        minDamage = 16
        maxDamage = 18
        super().__init__(name, desc, health, floor, minDamage, maxDamage)