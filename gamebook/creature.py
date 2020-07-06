import random


class Creature(object):
    def __init__(self, traits):
        self.traits = traits
        self.is_alive = True

    def attack(self, trait_to_use):
        """
        returns the attack power for the current fight sequence
        which is the sum of the given trait's value plus a random generated
        number between 1-6 (simulating the roll of a regular game die)
        """
        for trait in self.traits:
            if trait_to_use == trait:
                attack_trait = trait

        return attack_trait.get_value() + random.randint(1, 6)

    def defend(self, trait_to_use, damage):
        """apllies damage if the creature lost the current fight sequence"""
        for trait in self.traits:
            if trait_to_use == trait:
                defence_trait = trait

        defence_trait.set_value(defence_trait.get_value()-damage)

        if defence_trait.get_value() <= 0:
            self.is_alive = False  # the creature died
