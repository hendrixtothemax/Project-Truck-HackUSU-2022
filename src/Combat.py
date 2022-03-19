from random import Random

from src.UserInput import UserInput


class Combat:

    __COMBAT_GUI = [
        "List Enemies",
        "Attack Enemies",
        "View Inventory",
        "Pass"
    ]

    def __init__(self, player, possibleEnemies, numbOfEnemies):
        self.numbEnemies = numbOfEnemies
        self.enemies = self.pickEnemies(possibleEnemies)
        self.player = player

    def pickEnemies(self, possibleEnemyList):
        enemies = []
        for i in range(self.numbEnemies):
            index = Random.randint(0, len(possibleEnemyList) - 1)
            enemies.append(possibleEnemyList[index])
        return enemies

    def start(self):
        combatActive = True;
        print("\n!COMBAT HAS STARTED!\n")
        while combatActive:
            self.playerTurn()
            self.enemyTurn()

    def playerTurn(self):
        turnActive = True
        while turnActive:
            # Have TUI for User to Interact with
            userInput = UserInput("What will you do?", len(self.__COMBAT_GUI), self.__COMBAT_GUI)
            if userInput == 1:
                # List Enemies
                pass
            elif userInput == 2:
                # Attack TUI
                self.playerAttackTUI()
            elif userInput == 3:
                # View Inventory
                print("Inventory Is Not Implemented!")
                pass
            elif userInput == 4:
                # End Turn
                turnActive = False

    def enemyTurn(self):
        for enemy in self.enemies:
            enemy.attack(self)
            if self.player.health.health < 0:
                print("YOU SHOULD BE DEAD")
        print(f"\nYour health: {self.player.health.healthReadout()}")

    def playerAttackTUI(self):
        pass