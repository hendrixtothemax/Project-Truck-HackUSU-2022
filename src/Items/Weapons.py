import os.path
import random

from src.Items.Weapon import Weapon

from copy import deepcopy


class Weapons:

    def __init__(self):
        self.weaponsDataByName = {}
        self.weaponsDataByType = {}
        self.weaponsDataByLevel = {}
        self.__readTSV()

    def __readTSV(self):
        weaponsData = {}
        # open the Weapon's List
        cwd = os.getcwd()
        file = open(cwd + '/data/WeaponsList.tsv')
        # throw out the first line, not needed
        file.readline()
        while True:
            line = file.readline()
            if line == "":
                break
            else:
                weaponData = line.replace("\n", "")
                weaponData = weaponData.split("\t")
                weapon = Weapon(weaponData[0], weaponData[1], weaponData[2], weaponData[5], weaponData[3],
                                weaponData[4])

                self.weaponsDataByName[weaponData[0]] = weapon

                if self.weaponsDataByType.__contains__(weaponData[2]):
                    self.weaponsDataByType[weaponData[2]].append(weapon)
                else:
                    self.weaponsDataByType[weaponData[2]] = [weapon]

                if self.weaponsDataByLevel.__contains__(weaponData[5]):
                    self.weaponsDataByLevel[weaponData[5]].append(weapon)
                else:
                    self.weaponsDataByLevel[weaponData[5]] = [weapon]

        file.close()

    def getWeaponByName(self, name):
        if self.weaponsDataByName.__contains__(name):
            return deepcopy(self.weaponsDataByName.get(name))
        else:
            return None

    def getWeaponByType(self, itype):
        if self.weaponsDataByType.__contains__(itype):
            return deepcopy(self.weaponsDataByType.get(itype))
        else:
            return None

    def getWeaponByLevel(self, level):
        if self.weaponsDataByLevel.__contains__(level):
            return deepcopy(self.weaponsDataByLevel.get(level))
        else:
            return None

    def getRandomWeaponByType(self, itype):
        index = random.randint(0, len(self.getWeaponByType(itype))-1)
        return self.getWeaponByType(itype)[index]

    def getRandomWeaponByLevel(self, level):
        index = random.randint(0, len(self.getWeaponByLevel(level))-1)
        return self.getWeaponByLevel(level)[index]
        