from src.Items.Weapons import Weapons

weapons = Weapons()

weapon1 = weapons.getWeaponByName("Flimsy Sword")
print(weapon1)

weapon2 = weapons.getWeaponsByLevel("1")
print(weapon2)

weapon3 = weapons.getWeaponsByType("2")
print(weapon3)
