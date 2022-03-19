import sys

from src.Health import Health
from src.Items.Weapons import Weapons
from src.UserInput import UserInput


class character:
    def __init__(self,name,description,health,weaponName="Flimsy Sword"):
        self.weapons = Weapons()
        self.name = name
        self.description = description
        self.health = Health(health)
        self.equippedItem = self.weapons.getWeaponByName(weaponName)
        self.inventory = []

    def fullDesc(self):
        return f"{self.name}: {self.description}\n\t\tTheir starting weapon is: {self.equippedItem} [{self.equippedItem.minDamage}|{self.equippedItem.maxDamage}]"

    def __str__(self):
        return self.name

    def getCharacterDamage(self):
        return self.equippedItem.determineDamage()

    def setWeapon(self, weapon):
        self.equippedItem = weapon

    def addItemToInventory(self, item):
        self.inventory.append(item)

    def printInventory(self):
        print(f"\n{self.name}'s Inventory")
        i = 1
        for item in self.inventory:
            i = i + 1
            print(f"\t[{i}] {item.name} | min dmg: {item.minDamage} | max dmg: {item.maxDamage}")

    def inventoryTUI(self):
        self.printInventory()
        emptyStrings = ["Cancel"]
        for i in range(len(self.inventory)):
            emptyStrings.append("")
        inputObj = UserInput("",len(emptyStrings),emptyStrings)
        userInput = inputObj.getInput()
        if userInput == 1:
            return
        chosenItem = self.inventory[userInput-2]
        self.setWeapon(chosenItem)
        print(f"\nYou have equipped: {chosenItem.name}")

    def die(self):
        print(f"\nYou, {self.name} are dead...")
        print(f"\nIt is a shame, the world soon after your downfall fell under the control of the CHAOS.")
        sys.exit()


