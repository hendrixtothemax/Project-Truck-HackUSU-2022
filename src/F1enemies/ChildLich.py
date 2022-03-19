from src.Enemy import Enemy


class ChildLich(Enemy):
    def __init__(self):
        name = "ChildLich"
        desc = "A small, barley formed or trained lich capable of small necromantic feats."
        health = 10
        floor = 0
        minDamage = 3
        maxDamage = 5
        super().__init__(name, desc, health, floor, minDamage, maxDamage)