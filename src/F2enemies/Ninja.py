from src.Enemy import Enemy


class Ninja(Enemy):
    def __init__(self):
        name = "Ninja"
        desc = "A quiet fellow who thinks he's stronger than he really is.."
        health = 23
        floor = 1
        minDamage = 8
        maxDamage = 9
        super().__init__(name, desc, health, floor, minDamage, maxDamage)