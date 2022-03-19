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

    def approach(self):
        return f"The floor boss {self.name} approaches you. {self.desc} Their health is: {self.health.healthReadout()}"