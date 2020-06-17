from gamebook.creature import Creature
import random


class Hero(Creature):
    def __init__(self, traits):
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
            self.is_alive = False  # the hero died

    def fight(self, attack_t_name, defence_t_name, monster):
        """
            attack_t_name: the name of the trait that is used as the creature's
            power

            defence_t_name: the name of the trait that is used as the
            creature's health
        """

        while self.is_alive and monster.is_alive:
            if self.attack(attack_t_name) >= monster.attack(attack_t_name):
                monster.defend(defence_t_name, 2)
            else:
                self.defend(defence_t_name, 2)

        if self.is_alive:
            return True  # the hero won
        return False  # the hero lost
