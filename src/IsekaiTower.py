
from Branch import branch
import time

branch()
def storystart():
    print("It's a nice lovely day you find yourself in. The cars are loud, the children screaming, and the air full to chocking with smoke.")
    time.sleep(5)
    print("As you stride down the crowded, dirty street, you spy an old grandma edging her way across the crosswalk.")
    time.sleep(5)
    print("You glance to the side to see a semi-truck hurtling toward the old, shuffling grandma at close to mach seven. What do you do?")
    time.sleep(5)
    print("1- Sigh and and take a step back to prevent the blood from splattering over your new suit.")
    time.sleep(5)
    print("2- Turn up your music and keep walking.")
    time.sleep(5)
    print("3- Dash heroically out into the street to throw the grandma from harms way.")
    time.sleep(5)
    print("Type 1, 2, or 3. ")
    choice1 = input()
    if choice1 == "1":
        time.sleep(1)
        print("The truck barrels through the red light, hitting the poor grandma dead on.")
        time.sleep(2)
        print("You have no time to be amazed as the truck ricochets off the immovable old lady, flips over midair, and lands directly on top of you.")
        time.sleep(2)
        print("You die fifteen minutes later from blood loss. You were in excruciating pain the entire time, blood soaking every inch of your new suit.")
        towerstart()
    elif choice1 == "2":
        time.sleep(1)
        print("You dimly hear the sound of screeching tires through your Japanese pop and you have enough time to glance over your shoulder before the truck hits you right on.")
        time.sleep(3)
        print("You die instantly")
        towerstart()
    elif choice1 == "3":
        time.sleep(1)
        print("You dash out onto the street, bag forgotten on the sidewalk. Without thinking you shove the grandma forward with impossible strength.")
        time.sleep(2)
        print("She flies to the other side of the street. You stumble, look to the side.")
        time.sleep(2)
        print("The truck hits you, killing you instantly")
        time.sleep(1)
        print("The grandma blesses your name for the rest of her short life.")
        towerstart()
    else:
        time.sleep(1)
        print("You hesitate as the truck flies through the red light. Your mind goes blank.")
        print("Which is probably why you are not fast enough to dodge when the truck swerves and slams into you, killing you instantly")
        towerstart()

def towerstart():
    print("oh you wake up. Congrats")







