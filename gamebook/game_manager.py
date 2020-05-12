from gamebook.terminal_output import TerminalOutput
from gamebook.terminal_input import TerminalInput
import sys
from gamebook.scene import Scene


class GameManager(object):
    def __init__(self, current_scene, scene_import):
        """
            takes care of presenting the scenes to the user and moving
            from one scene to next fluently

            current_scene: the current scene the player is in at the moment
            when initializing a GameManager, insert the first scene.

            scene_import: a list of all the sceness
        """
        self.current_scene = current_scene  # insert the first scene here
        self.scene_import = scene_import
        self.output_instance = TerminalOutput()
        self.input_instance = TerminalInput()

    def start(self):
        while True:
            next_scene_name = self.run_scene()
            self.current_scene = self.get_next_scene(next_scene_name)

    def get_next_scene(self, scene_name):
        for scene in self.scene_import:
            if scene.get_name() == scene_name:
                return scene

    def run_scene(self):
        """evaluates the current scene and returns
           the following one by it's name"""

        self.output_instance.output(self.current_scene.show_desc())

        if len(self.current_scene.options) == 0:
            # if the current scene has no options, the game ends
            sys.exit()

        user_input = self.input_instance.\
            ask_for_user_inputs(self.current_scene.options)

        while True:
            try:
                next_scene = self.current_scene.next_scene_draw(user_input)
                if isinstance(next_scene, str):
                    return next_scene
                return next_scene.get_scene_name()

            except ValueError:
                error_string = "this is an invalid choice. please try again"
                self.output_instance.output(error_string)
                user_input = self.input_instance.input("your choice: ")
