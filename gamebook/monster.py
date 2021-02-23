from gamebook.creature import Creature


class Monster(Creature):
    def __init__(self, name, traits):
        self.name = name
        super().__init__(traits)
        self.is_alive = True

    def attack(self, trait_to_use):
        return super().attack(trait_to_use)

    def defend(self, trait_to_use, damage):
        return super().defend(trait_to_use, damage)
