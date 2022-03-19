from src.Enemy import Enemy


class Skeleton(Enemy):
    def __init__(self):
        name = "Zombie"
        desc = "A walking corpse devoid of flesh."
        health = 10
        floor = 0
        minDamage = 2
        maxDamage = 3
        super().__init__(name, desc, health, floor, minDamage, maxDamage)