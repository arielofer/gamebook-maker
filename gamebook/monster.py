from gamebook.creature import Creature


class Monster(Creature):
    def __init__(self, name, traits):
        self.name = name
        self.traits = traits
        self.is_alive = True
