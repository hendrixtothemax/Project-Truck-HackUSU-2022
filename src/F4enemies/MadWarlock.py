from src.Enemy import Enemy


class MadWarlock(Enemy):
    def __init__(self):
        name = "Mad Warlock"
        desc = "A wizard driven mad. He looks old and kind until he bares fangs and tries to bite your throat out."
        health = 49
        floor = 3
        minDamage = 24
        maxDamage =29
        super().__init__(name, desc, health, floor, minDamage, maxDamage)