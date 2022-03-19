from src.Enemy import Enemy


class Zombie(Enemy):
    def __init__(self):
        name = "Zombie"
        desc = "A walking corpse with rotting flesh clinging to the bones."
        health = 13
        floor = 0
        minDamage = 1
        maxDamage = 2
        super().__init__(name, desc, health, floor, minDamage, maxDamage)
