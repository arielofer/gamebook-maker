from gamebook.creature import Creature


class Hero(Creature):
    def __init__(self, traits):
        self.traits = {"attack": traits[0],
                       "luck": traits[1],
                       "health": traits[2]}
        self.is_alive = True

    def fight(self, monster):
        while self.is_alive and monster.is_alive:
            if self.attack(self.traits["attack"]) >=\
               monster.attack(monster.traits["attack"]):
                monster.defend(monster.traits["health"], 2)
            else:
                self.defend(self.traits["health"], 2)

        if self.is_alive:
            return True  # the hero won
        return False  # the hero lost
