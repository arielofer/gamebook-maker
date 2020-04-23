import random
import gamebook.trait


def openscrn(screen):
    """ presents the opening screen for your game """

    opening_screen = screen
    return opening_screen


def statbuild():
    """
    stats setting function:creates traits with given conduments(name, min_value
    , amount) and emulates the creation to the player(asks it to roll the dice)
    """
    trait1 = gamebook.trait.Trait("Skill", 6, 1)
    trait2 = gamebook.trait.Trait("Luck", 6, 1)
    trait3 = gamebook.trait.Trait("Stamina", 12, 2)

    # trait1
    print("to set your "+trait1.get_name()+", please role " +
          str(trait1.get_amount())+" die and add "+str(trait1.get_min_value()))
    input("press enter to roll...")
    print("your " + trait1.get_name() + " is in total: "
          + str(trait1.get_value()))

    # trait2
    print("to set your "+trait2.get_name()+", please role " +
          str(trait2.get_amount())+" die and add "+str(trait2.get_min_value()))
    input("press enter to roll...")
    print("your " + trait2.get_name() + " is in total: " +
          str(trait2.get_value()))

    # trait3
    print("to set your "+trait3.get_name()+", please role " +
          str(trait3.get_amount())+" die and add "+str(trait3.get_min_value()))
    input("press enter to roll...")
    print("your " + trait3.get_name() + " is in total: "
          + str(trait3.get_value()))

    return trait1, trait2, trait3


def stats_display(trait1, trait2, trait3):
    """a function that creates a nice display of the hero's stats"""

    display = ' ------------------------------\n'
    display += '|'+trait1.get_name()+': ' + str(trait1.get_value()) + '|' + \
        trait2.get_name()+': '+str(trait2.get_value()) + \
        '|'+trait3.get_name()+': '+str(trait3.get_value())+'|\n'
    display += ' ------------------------------'

    return display


def roll(trait, cond):
    """
    a dice rolling function, which determens if the player was lucky or not

    arguments:

    trait - the trait which the dice roll is compared to

    cond - the condition that determines wheter the player is lucky or not.

    cond can get only 2 inputs:

    less - the player is lucky if he rolled less then the trait's value

    more - the player is lucky if he rolled more then the trait's value
    """

    input("press enter to roll the dice...")
    dice_roll = 0
    amount = trait.get_amount()
    trait_value = trait.get_value()

    lucky_message = "success - press enter to continue..."
    unlucky_message = "you were unlucky this time. press enter to continue..."

    for _ in range(amount):
        dice_roll += random.randint(1, 6)

    output = "you rolled a " + str(dice_roll)

    if cond == 'less':
        # lucky
        if dice_roll <= trait_value:
            return True, output, lucky_message
        else:
            # unlucky
            return False, output, unlucky_message
    if cond == 'more':
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
        print("your stamina" + str(stamina) +
              "monster stamina" + str(m_stamina))
    return stamina
