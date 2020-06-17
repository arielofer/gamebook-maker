class Creature(object):
    def __init__(self, traits):
        self.traits = traits
        self.is_alive = True

    def fight(self):
        raise NotImplementedError

    def attack(self, trait_name):
        raise NotImplementedError

    def defend(self, trait_name):
        raise NotImplementedError
