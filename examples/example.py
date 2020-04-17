import os
import sys
from gamebook import helpers
from gamebook.terminal_output import TerminalOutput

def main():
    # opening screen
    opening_screen = ""
    opening_screen += r"          /\\\n         /**\\\n        /****\   /\\\n       /      \ /**\\\n      /  /\    /    \ \n     /  /  \  /      \\\n    /  /    \/ /\     \\\n   /  /  _   \/  \/\   \\\n__/__/__( )__/___/__\___\_"
    opening_screen += '\nwelcome to the text adventure: "the warlock of firetop mountain"'
    output_instance = TerminalOutput()

    # print(helpers.openscrn(opening_screen))
    output_instance.output(opening_screen)

    input("press enter to start your quest...")
    os.system("cls")
    # stats
    SKILL, LUCK, STAMINA = helpers.statbuild()
    os.system("cls")

    choice = " "
    tester = False
    # scene no. 1
    while not tester:
        print(helpers.statsdsply(SKILL, LUCK, STAMINA))
        
        print("At last your two-day hike is over.\nYou unsheathe your sword, lay it on the ground and sigh with relief as you lower yourself down on to the mossy rocks to sit for a moment's rest.\nYou stretch, rub your eyes and finally look up at Firetop Mountain.")
        print("The very mountain itself looks menacing.\nThe steep face in front of you looks to have been savaged by the claws of some gargantuan beast.\nSharp rocky crags jut out at unnatural angles.\nAt the top of the mountain you can see the eerie red colouring - probably some strange vegetation-which has given the mountain its name.\nPerhaps no one will ever know exactly what grows up there, as climbing the peak must surely be impossible.")
        print("Your quest lies ahead of you.\nAcross the clearing is a dark cave entrance.\nYou pick up your sword, get to your feet and consider what dangers may lie ahead of you.\nBut with determination, you thrust the sword home into its scabbard and approach the cave.")
        Bstart = '\033[1m'
        Bstop = '\033[0m'
        print("You peer into the gloom to see dark, slimy walls with pools of water on the stone floor in front of you.\nThe air is cold and dank.\nYou light your lantern and step warily into the blackness.\nCobwebs brush your face and you hear the scurrying of tiny feet: rats, most likely.\nYou set off into the cave.\nAfter a few yards you arrive at a junction.")
        print("Will you turn " + Bstart + "west" + Bstop + " or" + Bstart + " east?" + Bstop)
        choice = input("your choice: ")

        if choice == 'east' or choice == 'west':
            tester = True
        else:
            print()
            input("this is an invalid choice. please press enter to try again...")
            os.system("cls")

    if choice == 'east':
        # scene no. 278

        tester = False

        while not tester:
            os.system("cls")
            print(print(helpers.statsdsply(SKILL, LUCK, STAMINA)))

            print("The passageway soon comes to an end at a locked wooden door.\nYou listen at the door but hear nothing.")
            print("Will you try to" + Bstart + " charge" + Bstop + " the door down or would you rather" + Bstart +" turn around" + Bstop + " and go back to the junction?")
            choice = input("your choice: ")

            if choice == "charge" or choice == "turn around":
                tester = True
            else:
                print()
                input("this is an invalid choice. please press enter to try again...")
                os.system("cls")

        if choice == 'charge':

            # scene no. 156

            os.system("cls")
            print(print(helpers.statsdsply(SKILL, LUCK, STAMINA)))

            print("You charge the door with your shoulder.\n" + Bstart + "Roll two dice." + Bstop + "\nIf the number rolled is less than or equal to 7, you succeed.\nIf the number rolled is greater than your skill, you fail at opening the door.")
            ok = helpers.roll(LUCK, 'less')
            LUCK.set_value(LUCK.get_value()-1)
            if ok:
                print()
                # scene no. 343

                os.system("cls")
                print(print(helpers.statsdsply(SKILL, LUCK, STAMINA)))

                print("The door bursts open and you fall headlong into a room.\nBut your heart jumps as you realize you are not landing on the floor, but plunging down a pit of some kind!\nLuckily the pit is not particularly deep and you land in a heap less than two metres down.\nLose 1 stamina point for your bruises, climb out of the pit into the room and leave through the door, heading westwards.")
                input("press enter to continue...")
                STAMINA.set_value(STAMINA.get_value()-1)
            else:

                # scene no. 156 - unlucky

                os.system("cls")
                print(print(helpers.statsdsply(SKILL, LUCK, STAMINA)))

                print("you rub your bruised shoulder and decide against trying again and go back to the junction.")
                input("press enter to continue...")

        # scene no. 92

        os.system("cls")
        print(print(helpers.statsdsply(SKILL, LUCK, STAMINA)))

        print("You arrive back at the junction in the passage.\nYou look left to see the cave entrance in the dim distance but walk straight on.")
        input("press enter to continue...")

    # scene no. 71

    os.system("cls")
    print(print(helpers.statsdsply(SKILL, LUCK, STAMINA)))

    print("There is a right-hand turn to the north in the passage.\nCautiously you approach a sentry post on the corner and, as you look in, you can see a strange Goblin-like creature in leather armour asleep at his post.\nYou try to tiptoe past him.\nTest your Luck. If you are Lucky, he does not wake up and remains snoring loudly. If you are Unlucky, you step with a crunch on some loose ground and his eyes flick open.")
    input("press enter to continue...")
    ok = helpers.roll(LUCK, 'less')
    LUCK.set_value(LUCK.get_value()-1)

    # unlucky
    if not ok:
        # scene no 248
        os.system("cls")
        print(print(helpers.statsdsply(SKILL, LUCK, STAMINA)))
        print("The creature that has just awakened is an ORC! He scrambles to his feet and turns to grasp at a rope which is probably the alarm bell. You must attack him quickly.\nORC SKILL 6 STAMINA 5")
        input("press enter to start the fight sequence...")
        # fight
        STAMINA.set_value(helpers.fight(SKILL.get_value(), STAMINA.get_value(), 6, 5))
        if STAMINA.get_value() <= 0:
            print("you died")
            sys.exit()
        input("you are victorious. press enter to continue...")

    #lucky
    else:
        os.system("cls")
        print(helpers.statsdsply(SKILL, LUCK, STAMINA))
        print("the creature does not wake up and remains snoring loudly. you walk past him.")
        input("press enter to continue...")

    # scene no. 301

    tester = False
    while not tester:
        os.system("cls")
        print(helpers.statsdsply(SKILL, LUCK, STAMINA))
        print("To your left, on the west face of the passage, there is a rough-cut wooden door.\nYou listen at the door and can hear a rasping sound which may be some sort of creature snoring.\nDo you want to "+Bstart+"open"+Bstop+" the door or do you wish to "+Bstart+"press on"+Bstop+" northwards?")
        choice = input("your choice: ")

        if choice == "open" or choice == "press on":
            tester = True
        else:
            print()
            input("this is an invalid choice. please press enter to try again...")
            os.system("cls")

    if choice == "open":
        # scene no. 82
        tester = False
        while not tester:
            os.system("cls")
            print(helpers.statsdsply(SKILL, LUCK, STAMINA))
            print("The door opens to reveal a small, smelly room.\nIn the centre of the room is a rickety wooden table on which stands a lit candle.\nUnderneath the table is a small wooden box.\nAsleep on a straw mattress in the far corner of the room is a short, stocky creature with an ugly, warty face; the same sort of creature that you found asleep at the sentry post.")
            print("He must be the guard for the night watch.\nYou may either "+Bstart+"return"+Bstop+" to the corridor and press on northwards or creep into the room and try to "+Bstart+"steal"+Bstop+" the box without waking the creature.\nIf you want to try to steal the box, Test your Luck. If you are Lucky, he does not wake up.")
            choice = input("your choice: ")

            if choice == "return" or choice == "steal":
                tester = True
            else:
                print()
                input("this is an invalid choice. please press enter to try again...")
                os.system("cls")

        if choice == "steal":
            ok = helpers.roll(LUCK, 'less')

            if not ok:
                # scene no. 33
                tester = False
                while not tester:
                    os.system("cls")
                    print(helpers.statsdsply(SKILL, LUCK, STAMINA))
                    print("The sleeping creature awakens startled.\nHe jumps up and rushes at you, unarmed.\nWith your sword you should be able to defeat him, but his sharp teeth look rather vicious.\nYou may "+Bstart+"Escape"+Bstop+" through the door or stand and "+Bstart+"fight"+Bstop+" the ORC who is attacking you.")
                    print("If you defeat the creature, you may take the box.")
                    print("ORC SKILL 6 STAMINA 4")
                    choice = input("your choice: ")
                if choice == "fight":
                    STAMINA.set_value(helpers.fight(SKILL.get_value(), STAMINA.get_value(), 6, 4))
                    # defeat
                    if STAMINA.get_value() <= 0:
                        print("you died")
                        sys.exit()
                    # victory
                    print("you are victorious, you may take the box")
                    input("press enter to continue...")

                # scene no. 147

    # scene no. 208


if __name__ == '__main__':
    main()
