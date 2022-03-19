from src.Enemy import Enemy


class EscapedConvict(Enemy):
    def __init__(self):
        name = "Escaped Convict"
        desc = "A walking corpse with rotting flesh clinging to the bones."
        health = 25
        floor = 1
        minDamage = 6
        maxDamage = 9
        super().__init__(name, desc, health, floor, minDamage, maxDamage)