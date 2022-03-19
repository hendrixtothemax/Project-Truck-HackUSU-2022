from src.Enemy import Enemy


class ArmedBeggar(Enemy):
    def __init__(self):
        name = "Armed Beggar"
        desc = "A dirty, malformed man with a dagger."
        health = 20
        floor = 1
        minDamage = 6
        maxDamage = 8
        super().__init__(name, desc, health, floor, minDamage, maxDamage)