from gamebook.creature import Creature


class Monster(Creature):
    def __init__(self, name, traits):
        self.name = name
        self.traits = {"attack": traits[0], "health": traits[1]}
        self.is_alive = True

    def attack(self, trait_to_use):
        return super().attack(trait_to_use)

    def defend(self, trait_to_use, damage):
        return super().defend(trait_to_use, damage)

    def show_monster(self):
        data_string = ""
        data_string += self.name + "\n"
        for trait in self.traits:
            data_string + f"trait name: {trait.name}, value: {trait.value}\n"

        return data_string
