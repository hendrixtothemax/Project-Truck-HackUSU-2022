import random
import time
from src.UserInput import UserInput

from copy import deepcopy

class Combat:

    __COMBAT_GUI = [
        "List Enemies",
        "Attack Enemies",
        "View Inventory",
        "Pass"
    ]

    def __init__(self, player, possibleEnemies, numbOfEnemies,floor):
        self.numbEnemies = numbOfEnemies
        self.enemies = self.pickEnemies(possibleEnemies)
        self.player = player
        self.floor = floor

    def pickEnemies(self, possibleEnemyList):
        enemies = []
        for i in range(self.numbEnemies):
            maxIndex = len(possibleEnemyList) - 1
            index = 0
            if not (maxIndex < 1):
                index = random.randint(0, maxIndex)
            enemies.append(deepcopy(possibleEnemyList[index]))
        return enemies

    def start(self):
        combatActive = True;

        print("")
        for enemy in self.enemies:
            time.sleep(1)
            print(f"{enemy.approach()}")
            time.sleep(2)

        print("\n!COMBAT HAS STARTED!")
        while combatActive:
            self.playerTurn()
            self.enemyTurn()
            if len(self.enemies) < 1:
                break
        print("\n!COMBAT HAS ENDED!")

        weapon = self.player.weapons.getRandomWeaponByLevel(self.floor)
        self.player.addItemToInventory(weapon)
        print(f"{weapon.name} has been added to your inventory!")

        print("\n")
        print("You flee the scene with your new weapon in hand.")
        time.sleep(2)
        print("The next day...")
        print("\n\n")
        time.sleep(2)

    def playerTurn(self):
        turnActive = True
        while turnActive:
            # Have TUI for User to Interact with
            inputObj = UserInput("\nWhat will you do?", len(self.__COMBAT_GUI), self.__COMBAT_GUI)
            userInput = inputObj.getInput()
            if userInput == 1:
                # List Enemies
                print("\nEnemies:")
                for enemy in self.enemies:
                    print(f"\t{enemy.name} {enemy.health.healthReadout()}")
            elif userInput == 2:
                # Attack TUI
                self.playerAttackTUI()
                turnActive = False
            elif userInput == 3:
                # View Inventory
                print("Inventory Is Not Implemented!")
                pass
            elif userInput == 4:
                # End Turn
                print("")
                turnActive = False

    def enemyTurn(self):
        for enemy in self.enemies:
            enemy.attack(self.player)
            if self.player.health.health < 0:
                print("YOU (THE PLAYER) SHOULD BE DEAD")
        print(f"\nYour health: {self.player.health.healthReadout()}")

    def playerAttackTUI(self):
        TUIOptions = ["Cancel"]
        for enemy in self.enemies:
            enemyReadout = f"{enemy.name} {enemy.health.healthReadout()}"
            TUIOptions.append(enemyReadout)
        inputObj = UserInput("\nWho do you attack?",len(TUIOptions),TUIOptions)
        userInput = inputObj.getInput()
        if userInput == 1:
            return
        playerDamage = 99
        chosenEnemy = self.enemies[userInput-2]
        chosenEnemy.health.subHealth(playerDamage)
        print(f"\n{chosenEnemy.name} has taken {playerDamage} points of damage! {chosenEnemy.health.healthReadout()}")
        if chosenEnemy.health.health < 0:
            print(f"The {chosenEnemy.name} has died!")
            self.enemies.pop(userInput-2)
        print("")
