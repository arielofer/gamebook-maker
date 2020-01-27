"""skeleton for TextAdventure package"""
import random


class Trait(object):
    def __init__(self, name, const, dice_num):
        """rolled based trait
            name: trait's name
            const: constant numeric value that adds to the randomized value to create the finale value of the trait
            dice_num: number of dices to be rolled

            :rtype = Trait
        """
        self.name = name
        self.dice_num = dice_num
        self.const = const

        dice_sum = 0
        for i in range(dice_num):
            dice_sum += random.randint(1, 6)

        self.value = dice_sum + const

    def getName(self):
        return self.name

    def getDice(self):
        return self.dice_sum

    def getValue(self):
        return self.value

    def setValue(self, num):
        self.value = num

    def getDiceNum(self):
        return self.dice_num

    def getConst(self):
        return self.const

    '''
        def __init__(self, name, value):
            """pre determined trait"""
            self.name = name
            self.value = value '''
