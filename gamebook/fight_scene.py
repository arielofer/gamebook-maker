from gamebook.scene import Scene


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

    def get_monster(self):
        return self.enemy

    def run_fight(self, hero):
        if hero.fight(self.enemy):
            return self.next_scenes["win"]
        return self.next_scenes["loss"]
