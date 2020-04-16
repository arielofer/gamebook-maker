import random


class Trait(object):
    """
        a quaity given to the hero at the start of the game, which he needs to 
        interact with the game's features

        arguments:
        
        min_value: constant numeric value that adds to the randomized value to 
        create the finale value of the trait

        amount: number of dice to be rolled

    """
    def __init__(self, name, min_value, amount=0):
        self.name = name
        self.amount = amount 
        self.min_value = min_value

        dice_sum = 0
        
        for _ in range(amount):
            dice_sum += random.randint(1, 6)

        self.value = dice_sum + min_value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def set_value(self, num):
        self.value = num

    def get_amount(self):
        return self.amount

    def get_min_value(self):
        return self.min_value

