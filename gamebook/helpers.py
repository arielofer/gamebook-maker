import random
import gamebook.trait
from gamebook.terminal_output import TerminalOutput


def trait_init():
    """
    stats setting function:creates traits with given conduments(name, min_value
    , amount) and emulates the creation to the player(asks it to roll the dice)
    """

    output_instance = TerminalOutput()

    trait1 = gamebook.trait.Trait("Skill", 6, 1)
    trait2 = gamebook.trait.Trait("Luck", 6, 1)
    trait3 = gamebook.trait.Trait("Stamina", 12, 2)

    # trait1
    output_instance.output(f"to set your {trait1.get_name()}, please role "
                           f"{trait1.get_amount()} die and add "
                           f"{trait1.get_min_value()}")

    input("press enter to roll...")
    output_instance.output(f"your {trait1.get_name()} is in total: "
                           f"{trait1.get_value()}")

    # trait2
    output_instance.output(f"to set your {trait2.get_name()}, please role "
                           f"{trait2.get_amount()} die and add "
                           f"{trait2.get_min_value()}")

    input("press enter to roll...")
    output_instance.output(f"your {trait2.get_name()} is in total: "
                           f"{trait2.get_value()}")

    # trait3
    output_instance.output(f"to set your {trait3.get_name()}, please role "
                           f"{trait3.get_amount()} die and add "
                           f"{trait3.get_min_value()}")

    input("press enter to roll...")
    output_instance.output(f"your {trait3.get_name()} is in total: "
                           f"{trait3.get_value()}")

    return trait1, trait2, trait3


def stats_display(trait1, trait2, trait3):
    """a function that creates a nice display of the hero's stats"""

    display = (' ------------------------------\n'
               f'|{trait1.get_name()}: {trait1.get_value()}|'
               f'{trait2.get_name()}: {trait2.get_value()}'
               f'|{trait3.get_name()}: {trait3.get_value()}|\n'
               ' ------------------------------')

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

    output = f"you rolled a {dice_roll}"

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
    output_instance = TerminalOutput()

    output_instance.output(f"your stamina:{stamina}"
                           f",monster stamina:{m_stamina}")

    temp_skill = skill + random.randint(1, 6)

    output_instance.output(f"your skill is {temp_skill}")

    temp_m_skill = m_skill + random.randint(1, 6)

    output_instance.output(f"monster skill is {temp_m_skill}")

    if temp_skill >= temp_m_skill:
        m_stamina = m_stamina - 2
    else:
        stamina = stamina - 2

    output_instance.output(f"your stamina {stamina}"
                           f",monster stamina {m_stamina}")

    while stamina > 0 and m_stamina > 0:
        temp_skill = skill + random.randint(1, 6)
        output_instance.output(f"your skill is {temp_skill}")
        temp_m_skill = m_skill + random.randint(1, 6)
        output_instance.output(f"monster skill is {temp_m_skill}")

        if temp_skill >= temp_m_skill:
            m_stamina = m_stamina - 2
        else:
            stamina = stamina - 2

        output_instance.output(f"your stamina {stamina}"
                               f",monster stamina {m_stamina}")

    return stamina
