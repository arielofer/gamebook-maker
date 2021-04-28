from gamebook.monster import Monster
from gamebook.creature import Creature


class Hero(Creature):
    def __init__(self, traits: list):
        self.traits = {"attack": traits[0],
                       "luck": traits[1],
                       "health": traits[2]}
        self.is_alive = True

    def fight(self, monster: Monster):
        while self.is_alive and monster.is_alive:
            if self.attack("attack") >=\
               monster.attack("attack"):
                monster.defend(2, "health")
            else:
                self.defend(2, "health")

        if self.is_alive:
            return True  # the hero won
        return False  # the hero lost
