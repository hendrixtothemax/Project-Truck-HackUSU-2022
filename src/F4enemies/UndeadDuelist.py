from src.Enemy import Enemy


class UndeadDuelist(Enemy):
    def __init__(self):
        name = "Undead Duelist"
        desc = "A fine gentlemen still in his finery. He seems quite intent on killing you. Respectfully, of course."
        health = 45
        floor = 0
        minDamage = 28
        maxDamage = 31
        super().__init__(name, desc, health, floor, minDamage, maxDamage)