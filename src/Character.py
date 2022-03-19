
from src.Health import Health
from src.Items.Weapons import Weapons
from src.UserInput import UserInput


class character:
    def __init__(self,name,description,health):
        self.weapons = Weapons()
        self.name = name
        self.description = description
        self.health = Health(health)
        self.equippedItem = self.weapons.getWeaponByName("Flimsy Sword")
        self.inventory = []

    def fullDesc(self):
        return f"{self.name}: {self.description}\n\t\tTheir health is: {self.health.health}"

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


