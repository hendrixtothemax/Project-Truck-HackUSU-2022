from src.Enemy import Enemy


class Assassin(Enemy):
    def __init__(self):
        name = "Assassin"
        desc = "Quick witted and quicker with a blade."
        health = 35
        floor = 2
        minDamage = 14
        maxDamage = 15
        super().__init__(name, desc, health, floor, minDamage, maxDamage)