from src.Enemy import Enemy


class Rem(Enemy):
    def __init__(self):
        name = "Rem"
        desc = "A blue-haired demon in the form of a sweet girl. Don't be fooled."
        health = 27
        floor = 1
        minDamage = 11
        maxDamage = 14
        super().__init__(name, desc, health, floor, minDamage, maxDamage)