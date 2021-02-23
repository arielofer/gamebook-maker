from gamebook.scene import Scene
import gamebook.important_strings


class FightScene(Scene):
    """
        A scene containing a battle with a monster

        arguments:

        next_scenes - a list of two NextScene objects, 1st is the victory scene
        and 2nd is the the defeat scene

        enemy - a monster instance

    """
    def __init__(self, name, desc, next_scenes, enemy):
        self.name = name
        self.desc = desc
        self.next_scenes = {"win": next_scenes[0], "loss": next_scenes[1]}
        self.enemy = enemy

    def get_name(self):
        return super().get_name()

    def show_desc(self):
        return super().show_desc()

    def show_options(self):
        return super().show_options()

    def show_monster(self):
        data_string = ""
        data_string += self.enemy.name + "\n"
        for trait in self.enemy.traits:
            data_string + f"trait name: {trait.name}, value: {trait.value}\n"

        return data_string

    def run_fight(self, hero):
        if hero.fight(gamebook.important_strings.power_trait_name,
                      gamebook.important_strings.health_trait_name,
                      self.enemy):
            return self.next_scenes["win"]
        return self.next_scenes["loss"]
