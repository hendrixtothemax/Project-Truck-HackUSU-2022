from src.Enemy import Enemy


class UndeadWitch(Enemy):
    def __init__(self):
        name = "UndeadWitch"
        desc = "A desecrated woman clutching a rotten staff. She smells of herbs and death."
        health = 32
        floor = 2
        minDamage = 18
        maxDamage = 19
        super().__init__(name, desc, health, floor, minDamage, maxDamage)