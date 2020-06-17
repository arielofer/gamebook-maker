from gamebook.creature import Creature
import random


class Monster(Creature):
    def __init__(self, name, traits):
        self.name = name
        self.traits = traits
        self.is_alive = True

    def attack(self, trait_name):
        for trait in self.traits:
            if trait_name == trait.get_name():
                attack_trait = trait

        return attack_trait.get_value() + random.randint(1, 6)

    def defend(self, trait_name, damage):
        for trait in self.traits:
            if trait_name == trait.get_name():
                defence_trait = trait

        defence_trait.set_value(defence_trait.get_value()-damage)

        if defence_trait.get_value() <= 0:
            self.is_alive = False  # the monster died
