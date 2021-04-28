from gamebook.creature import Creature


class Monster(Creature):
    def __init__(self, name, traits: list):
        self.name = name
        self.traits = {"attack": traits[0], "health": traits[1]}
        self.is_alive = True

    def show_monster(self):
        data_string = ""
        data_string += self.name + "\n"
        for trait in self.traits:
            data_string + f"trait name: {trait.name}, value: {trait.value}\n"

        return data_string
