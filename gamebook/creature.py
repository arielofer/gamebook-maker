import random
from gamebook.exceptions import TraitNotFoundError


class Creature(object):
    def __init__(self, traits: dict):
        self.traits = traits
        self.is_alive = True

    def attack(self, trait_to_use: str = "attack") -> int:
        """
        returns the attack power for the current fight sequence
        which is the sum of the given trait's value plus a random generated
        number between 1-6 (simulating the roll of a regular game die)

        trait_to_use: kind of trait to use (default is "attack")
        """
        try:
            return self.traits.get(trait_to_use, "attack").get_value() +\
                random.randint(1, 6)
        except KeyError:
            raise TraitNotFoundError(trait_to_use)

    def defend(self, damage: int, trait_to_use: str = "health") -> int:
        """
        apllies damage if the creature lost the current fight sequence

        trait_to_use: kind of trait to use (default is "health")
        """
        self.traits.get(trait_to_use, "health").\
            set_value(self.traits.get(trait_to_use, "health").
                      get_value()-damage)

        if self.traits.get(trait_to_use, "health").get_value() <= 0:
            self.is_alive = False  # the creature died
