
from Health import Health

class enemy:
    def __init__(self,name,description,health,floor):
        self.name = name
        self.description = description
        self.health = Health(health)
        self.floor = floor

    def approach(self):
        return f"A {self.name} approaches you. {self.description} Their health is: {self.health.health}"

    def __str__(self):
        return self.name

Skeleton = enemy("Skeleton","A walking corpse devoid of flesh.", 10,0)
Zombie = enemy("Zombie","A walking corpse with rotting flesh clinging to the bones.",13,0)
Bandit = enemy("Bandit","Once a farmer, this poor soul has turned to banditry.",20,1)
Ghoul = enemy("Ghoul","They like to eat flesh and are quite fond of their Zombie brethren.",10,0)
Vampire = enemy("Vampire","Blood-less fools who ironically love blood.", 25,2)
Assassin = enemy("Assassin","Quick witted and quicker with a blade.",30,2)
RougeSoldier = enemy("Rouge Soldier","Well trained and desperate for a few coins",35,2)
Dragon = enemy("Dragon","A majestic beast that seems inclined to bite your head off.",80,4)
DarkPixie = enemy("Dark Pixie","A small little bastard that declines to be hit",40,3)
Ninja = enemy("Ninja","A quiet fellow who thinks he's stronger than he really is.",20,1)