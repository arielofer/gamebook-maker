import random
import temp_library.trait


def openscrn():  # for my personal game-change to your liking
    opening_screen = ""

    opening_screen += "          /\\\n         /**\\\n        /****\   /\\\n       /      \ /**\\\n      /  /\    /    \ \n     /  /  \  /      \\\n    /  /    \/ /\     \\\n   /  /  _   \/  \/\   \\\n__/__/__( )__/___/__\___\_"
    opening_screen += '\nwelcome to the text adventure: "the warlock of firetop mountain"'

    return opening_screen



def statbuild():  # inserts initial values to attributes-change the strings and values according to your specific traits
    """stats setting function

    :rtype: Trait
    """
    trait1 = temp_library.trait.Trait("Skill", 6, 1)
    trait2 = temp_library.trait.Trait("Luck", 6, 1)
    trait3 = temp_library.trait.Trait("Stamina", 12, 2)

    # trait1
    print("to set your "+trait1.get_name()+", please role "+str(trait1.get_dice_num())+" die and add "+str(trait1.get_const()))
    input("press enter to roll...")
    print("your " + trait1.get_name() + " is in total: " + str(trait1.get_value()))

    # trait2
    print("to set your "+trait2.get_name()+", please role "+str(trait2.get_dice_num())+" die and add "+str(trait2.get_const()))
    input("press enter to roll...")
    print("your " + trait2.get_name() + " is in total: " + str(trait2.get_value()))

    # trait3
    print("to set your "+trait3.get_name()+", please role "+str(trait3.get_dice_num())+" die and add "+str(trait3.get_const()))
    input("press enter to roll...")
    print("your " + trait3.get_name() + " is in total: " + str(trait3.get_value()))

    return trait1, trait2, trait3


def statsdsply(trait1, trait2, trait3):
    # displaying the stats function
    print(' ------------------------------')
    print('|'+trait1.get_name()+': ' + str(trait1.get_value()) + '|'+trait2.get_name()+': '+str(trait2.get_value())+'|'+trait3.get_name()+': '+str(trait3.get_value())+'|')
    print(' ------------------------------')
    print()


def roll(trait, arg):
    # dice rolling function
    input("press enter to roll the dice...")
    dice_roll = 0
    dice_num = trait.get_dice_num()
    trait_value = trait.get_value()

    lucky_message = "success - press enter to continue..."
    unlucky_message = "you were unlucky this time. press enter to continue..."

    for _ in range(dice_num):
        dice_roll += random.randint(1, 6)

    output = "you rolled a " + str(dice_roll)

    if arg == 'less':
        # lucky
        if dice_roll <= trait_value:
            return True, output, lucky_message
        else:
            # unlucky
            return False, output, unlucky_message
    else:
        if dice_roll >= trait_value:
            # lucky
            return True, output, lucky_message
        else:
            # unlucky
            return False, output, unlucky_message


def fight(skill, stamina, m_skill, m_stamina):
    # fighting function
    print("your stamina "+str(stamina)+"monster stamina "+str(m_stamina))
    temp_skill = skill + random.randint(1, 6)
    print("your skill is "+str(temp_skill))
    temp_m_skill = m_skill + random.randint(1, 6)
    print("monster skill is " + str(temp_m_skill))

    if temp_skill >= temp_m_skill:
        m_stamina = m_stamina - 2
    else:
        stamina = stamina - 2
    print("your stamina" + str(stamina) + "monster stamina" + str(m_stamina))
    while stamina > 0 and m_stamina > 0:
        temp_skill = skill + random.randint(1, 6)
        print("your skill is " + str(temp_skill))
        temp_m_skill = m_skill + random.randint(1, 6)
        print("monster skill is " + str(temp_m_skill))

        if temp_skill >= temp_m_skill:
            m_stamina = m_stamina - 2
        else:
            stamina = stamina - 2
        print("your stamina" + str(stamina) + "monster stamina" + str(m_stamina))
    return stamina
