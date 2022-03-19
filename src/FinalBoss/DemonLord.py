from src.Enemy import Enemy


class DemonLord(Enemy):
    def __init__(self):
        name = "Demon Lord"
        desc = "The pinnacle of evil. The incarnation of blasphemy and despair. He is hell-bent on destroying the universe."
        health = 75
        floor = 4
        minDamage = 40
        maxDamage = 50
        super().__init__(name, desc, health, floor, minDamage, maxDamage)