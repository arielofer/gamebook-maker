import random


class Trait(object):
    """
        a quaity given to the hero at the start of the game, which he needs to interact with the game's features

        arguments:
        
        const: constant numeric value that adds to the randomized value to create the finale value of the trait

        dice_num: number of dice to be rolled

    """
    def __init__(self, name, const, dice_num=0):
        self.name = name
        self.dice_num = dice_num # TODO: rename to amount 
        self.const = const

        dice_sum = 0
        for _ in range(dice_num):
            dice_sum += random.randint(1, 6)

        self.value = dice_sum + const

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def set_value(self, num):
        self.value = num

    def get_dice_num(self):
        return self.dice_num

    def get_const(self):
        return self.const

