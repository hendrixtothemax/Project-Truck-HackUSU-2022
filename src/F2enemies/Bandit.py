from src.Enemy import Enemy


class Bandit(Enemy):
    def __init__(self):
        name = "Bandit"
        desc = "Once a farmer, this poor soul has turned to banditry."
        health = 23
        floor = 1
        minDamage = 7
        maxDamage = 9
        super().__init__(name, desc, health, floor, minDamage, maxDamage)