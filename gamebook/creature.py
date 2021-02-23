import random
from gamebook.exceptions import TraitNotFoundError


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
        attack_trait = None
        for trait in self.traits:
            if trait_to_use == trait.name:
                attack_trait = trait

        if attack_trait is None:
            raise TraitNotFoundError(trait_to_use)

        return attack_trait.get_value() + random.randint(1, 6)

    def defend(self, trait_to_use, damage):
        """apllies damage if the creature lost the current fight sequence"""
        defence_trait = None
        for trait in self.traits:
            if trait_to_use == trait.name:
                defence_trait = trait

        if defence_trait is None:
            raise TraitNotFoundError(trait_to_use)

        defence_trait.set_value(defence_trait.get_value()-damage)

        if defence_trait.get_value() <= 0:
            self.is_alive = False  # the creature died
