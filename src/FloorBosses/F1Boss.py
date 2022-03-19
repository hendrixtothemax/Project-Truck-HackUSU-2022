from src.Enemy import Enemy


class Aqua(Enemy):
    def __init__(self):
        name = "Aqua"
        desc = "A childish, immature goddess that never quite learns what it means to be serious."
        health = 16
        floor = 0
        minDamage = 4
        maxDamage = 6
        super().__init__(name, desc, health, floor, minDamage, maxDamage)