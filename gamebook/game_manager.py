from gamebook.scene import Scene
from gamebook.exceptions import *
from gamebook.important_strings import *


class GameManager(object):
    def __init__(self, scenes_import, output_instance, input_instance):
        """
            takes care of presenting the scenes to the user and moving
            from one scene to next fluently

            scenes_import: a list of all the sceness
        """
        self.scenes_import = scenes_import
        self.output_instance = output_instance
        self.input_instance = input_instance

    def start(self, current_scene):
        """
            current_scene: the current scene the player is in at the moment.
            insert the first scene for your game.
        """
        self.current_scene = current_scene
        while True:
            try:
                next_scene_name = self.run_scene()
                self.current_scene = self.get_next_scene(next_scene_name)

            except ReachedTheEndError:
                self.output_instance.exit(end_message)
                break

            except ExitRequested:
                self.output_instance.exit(exit_message)

    def get_next_scene(self, scene_name):
        for scene in self.scenes_import:
            if scene.get_name() == scene_name:
                return scene

    def run_scene(self):
        """evaluates the current scene and returns
           the following one by it's name"""

        self.output_instance.output(self.current_scene.show_desc())

        if len(self.current_scene.options) == 0:
            # if the current scene has no options, the game ends
            raise ReachedTheEndError

        user_input = self.input_instance.\
            ask_for_user_inputs(self.current_scene.options)

        if user_input == exit_user_input:
            # the user wants to quit the game
            raise ExitRequested

        while True:
            try:
                next_scene = self.current_scene.next_scene_draw(user_input)
                if isinstance(next_scene, str):
                    return next_scene
                return next_scene.get_scene_name()

            except OptionNotFoundError:
                self.output_instance.output(invalid_user_input_message)
                user_input = self.input_instance.input("your choice: ")
