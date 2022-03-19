
from Branch import branch
import time
from Character import character
from UserInput import UserInput
from src.Game import Game


def choosecharacter():
    player = ""
    Tohka = character("Tohka","A strong headed girl with a tendency to shoot first and ask questions later",100,"Flimsy Sword")
    Rimuru = character("Rimuru", "A down-to-earth warrior with only the best for his friends in mind",100,"Broken Greatsword")
    Kurumi = character("Kurumi", "A psychopathic murderer who really loves to kill things.",100,"Weak Longbow")

    prompt = ""

    print("\n\n")
    print("Hello player! Please choose a character from below\n")
    time.sleep(1)
    prompt += f"[1]- {Tohka.fullDesc()}\n"
    prompt += f"[2]- {Rimuru.fullDesc()}\n"
    prompt += f"[3]- {Kurumi.fullDesc()}\n"
    userInput = UserInput(prompt,3,[str(Tohka),str(Rimuru),str(Kurumi)])
    choice = userInput.getInput()
    if choice == 1:
        player = Tohka
    elif choice == 2:
        player = Rimuru
    elif choice == 3:
        player = Kurumi
    return player


def storystart():
    print("It's a nice lovely day you find yourself in. The cars are loud, the children screaming, and the air full to chocking with smoke.")
    time.sleep(1)
    print("As you stride down the crowded, dirty street, you spy an old grandma edging her way across the crosswalk.")
    time.sleep(1)
    print("You glance to the side to see a semi-truck hurtling toward the old, shuffling grandma at close to mach seven. What do you do?")
    time.sleep(1)
    print("1- Sigh and and take a step back to prevent the blood from splattering over your new suit.")
    time.sleep(1)
    print("2- Turn up your music and keep walking.")
    time.sleep(1)
    print("3- Dash heroically out into the street to throw the grandma from harms way.")
    time.sleep(1)
    userInput = UserInput("Type 1, 2, or 3." , 3, ["", "", ""])
    choice1 = userInput.getInput()
    if choice1 == 1:
        time.sleep(1)
        print("The truck barrels through the red light, hitting the poor grandma dead on.")
        time.sleep(2)
        print("You have no time to be amazed as the truck ricochets off the immovable old lady, flips over midair, and lands directly on top of you.")
        time.sleep(2)
        print("You die fifteen minutes later from blood loss. You were in excruciating pain the entire time, blood soaking every inch of your new suit.")
    elif choice1 == 2:
        time.sleep(1)
        print("You dimly hear the sound of screeching tires through your Japanese pop and you have enough time to glance over your shoulder before the truck hits you right on.")
        time.sleep(3)
        print("You die instantly")

    elif choice1 == 3:
        time.sleep(1)
        print("You dash out onto the street, bag forgotten on the sidewalk. Without thinking you shove the grandma forward with impossible strength.")
        time.sleep(5)
        print("She flies to the other side of the street. You stumble, look to the side.")
        time.sleep(4)
        print("The truck hits you, killing you instantly")
        time.sleep(3)
        print("The grandma blesses your name for the rest of her short life.")

    else:
        time.sleep(1)
        print("You hesitate as the truck flies through the red light. Your mind goes blank.")
        time.sleep(2)
        print("Which is probably why you are not fast enough to dodge when the truck swerves and slams into you, killing you instantly")


def towerstart(player):
    print("|\t|\t|\t|")
    print("|\t|\t|\t|")
    print("\t|\t|\t|")
    print("\t|\t|\t|")
    print("\t\t|\t|")
    print("\t\t|\t|")
    print("\t\t\t|")
    print("\t\t\t|\n")

    print("Good Morning " + str(player) + "! Congratulations, you have died.\n")
    time.sleep(1)
    print("Oh, don't be so confused. I'll break it all down for you!")
    time.sleep(1)
    print("First, this is no longer your world. You have been reincarnated as " + str(player) + " in a new world full of magic and evil demons\n")
    time.sleep(1)
    print("\tSpecifically, this world is a TOWER. Each floor in this tower has a series of QUESTS and SIDE QUESTS to complete. \n\tTo progress, one must complete these quests.")
    time.sleep(1)
    print("\tAt the end of each floor resides a FLOOR BOSS which you must beat to continue on to the next floor.")
    time.sleep(1)
    print("\tOnce you beat all the floor bosses, you can confront the FINAL BOSS, the Demon Lord.")
    time.sleep(1)
    print("\tFailure to beat this foul beast will result in the rapid deconstruction of the entire universe.")
    time.sleep(1)
    print("\nI'm afraid time is running short " + str(player) + ", best hurry onward.")

    print("\n----------\n")

    print("You find yourself standing in the middle of a town crowded to breaking with people. You can hardly walk two steps without knocking someone over.")
    time.sleep(1)
    print("You wade through the crowd to the side of the street where you find a large wooden board with the words 'AVAILABLE QUESTS' written at the top.")
    time.sleep(1)
    print("Beneath those words, you see FOUR pieces of paper pegged to the wood, labeled...")


def floorlayout():
    for i in range(4):
        i = 4
        branch(player, i+1)




#Chain of Events
#storystart()
game = Game()
player = choosecharacter()
game.setPlayer(player)
#time.sleep(3)
towerstart(player)
floorlayout()
