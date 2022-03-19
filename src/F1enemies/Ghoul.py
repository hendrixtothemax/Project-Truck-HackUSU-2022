from src.Enemy import Enemy


class Ghoul(Enemy):
    def __init__(self):
        name = "Ghoul"
        desc = "They like to eat flesh and are quite fond of their Zombie brethren."
        health = 9
        floor = 0
        minDamage = 1
        maxDamage = 2
        super().__init__(name, desc, health, floor, minDamage, maxDamage)