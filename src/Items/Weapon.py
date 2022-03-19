import random

from src.Items.Item import Item


class Weapon(Item):

    def __init__(self, name, desc, itype, level, minDamage, maxDamage):
        super().__init__(name, desc, itype, level)
        self.minDamage = minDamage
        self.maxDamage = maxDamage

    def determineDamage(self):
        damage = random.randint(self.minDamage, self.maxDamage)
        return damage

    def __repr__(self):
        return self.name

    # def __add__(self, other):
    #     return self.determineDamage()
    #
    # def __sub__(self, other):
    #     return self.determineDamage()

