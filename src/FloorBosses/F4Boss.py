from src.Enemy import Enemy


class Ram(Enemy):
    def __init__(self):
        name = "Ram"
        desc = "Rem's sister, she is far more cruel and bloody than her counterpart. Best not to fight at all."
        health = 50
        floor = 3
        minDamage = 30
        maxDamage = 35
        super().__init__(name, desc, health, floor, minDamage, maxDamage)

    def approach(self):
        return f"The floor boss {self.name} approaches you. {self.desc} Their health is: {self.health.healthReadout()}"