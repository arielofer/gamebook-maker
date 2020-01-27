import random
import temp_library.trait


def openscrn():  # for my personal game-change to your liking
    """
    opening screen
    """
    print("          /\\\n         /**\\\n        /****\   /\\\n       /      \ /**\\\n      /  /\    /    \ \n     /  /  \  /      \\\n    /  /    \/ /\     \\\n   /  /  _   \/  \/\   \\\n__/__/__( )__/___/__\___\_")
    print('welcome to the text adventure: "the warlock of firetop mountain"')
    input("press enter to start your quest...")


def statbuild():  # inserts initial values to attributes-change the strings and values according to your specific traits
    """stats setting function

    :rtype: Trait
    """

    trait1 = temp_library.trait.Trait("Skill", 6, 1)
    trait2 = temp_library.trait.Trait("Luck", 6, 1)
    trait3 = temp_library.trait.Trait("Stamina", 12, 2)

    # trait1
    print("to set your "+trait1.getName()+", please role "+str(trait1.getDiceNum())+" die and add "+str(trait1.getConst()))
    input("press enter to roll...")
    print("your " + trait1.getName() + " is in total: " + str(trait1.getValue()))

    # trait2
    print("to set your "+trait2.getName()+", please role "+str(trait2.getDiceNum())+" die and add "+str(trait2.getConst()))
    input("press enter to roll...")
    print("your " + trait2.getName() + " is in total: " + str(trait2.getValue()))

    # trait3
    print("to set your "+trait3.getName()+", please role "+str(trait3.getDiceNum())+" die and add "+str(trait3.getConst()))
    input("press enter to roll...")
    print("your " + trait3.getName() + " is in total: " + str(trait3.getValue()))

    return trait1, trait2, trait3


def statsdsply(trait1, trait2, trait3):
    # displaying the stats function
    print(' ------------------------------')
    print('|'+trait1.getName()+': ' + str(trait1.getValue()) + '|'+trait2.getName()+': '+str(trait2.getValue())+'|'+trait3.getName()+': '+str(trait3.getValue())+'|')
    print(' ------------------------------')
    print()


def roll(num, arg):
    # dice rolling function
    input("press enter to roll the dice...")
    dice = 0
    for i in range(1):
        dice += random.randint(1, 6)

    if arg == 'less':
        if dice <= num:
            print("")
            print("you rolled a " + str(dice))
            print("")
            input('success - press enter to continue...')
            return True
        else:
            print("")
            print("you rolled a " + str(dice))
            print("")
            input('you were unlucky this time. press enter to continue...')
            return False
    else:
        if dice >= num:
            print("")
            print("you rolled a " + str(dice))
            print("")
            input('success - press enter to continue...')
            return True
        else:
            print("")
            print("you rolled a " + str(dice))
            print("")
            input('you were unlucky this time. press enter to continue...')
            return False


def fight(skill, stamina, m_skill, m_stamina):
    # fighting function
    print("your stamina "+str(stamina)+"monster stamina "+str(m_stamina))
    Tskill = skill + random.randint(1, 6)
    print("your skill is "+str(Tskill))
    Tm_skill = m_skill + random.randint(1, 6)
    print("monster skill is " + str(Tm_skill))

    if Tskill >= Tm_skill:
        m_stamina = m_stamina - 2
    else:
        stamina = stamina - 2
    print("your stamina" + str(stamina) + "monster stamina" + str(m_stamina))
    while stamina > 0 and m_stamina > 0:
        Tskill = skill + random.randint(1, 6)
        print("your skill is " + str(Tskill))
        Tm_skill = m_skill + random.randint(1, 6)
        print("monster skill is " + str(Tm_skill))

        if Tskill >= Tm_skill:
            m_stamina = m_stamina - 2
        else:
            stamina = stamina - 2
        print("your stamina" + str(stamina) + "monster stamina" + str(m_stamina))
    return stamina


def choice(text,c1,c2):

    print(text)
    return input("your choice: ").lower().strip()


def dice_roll(num):
    return random.randint(num * 1, num * 6)