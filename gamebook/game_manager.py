from gamebook.terminal_output import TerminalOutput
from gamebook.terminal_input import TerminalInput
import sys


class GameManager(object):
    def __init__(self, scene):
        self.scene = scene
        self.output_instance = TerminalOutput()
        self.input_instance = TerminalInput()

    def start(self, scene_import):
        while True:
            next_scene_name = self.run_scene()
            self.scene = self.get_next_scene(next_scene_name, scene_import)

    def get_next_scene(self, scene_name, scene_import):
        for scene in scene_import:
            if scene.get_name() == scene_name:
                return scene

    def run_scene(self):

        self.output_instance.output(self.scene.show_desc())

        if len(self.scene.options) == 0:
            sys.exit()

        user_input = self.input_instance.\
            ask_for_user_inputs(self.scene.options)

        while True:
            try:
                next_scene = self.scene.next_scene_draw(user_input)
                if isinstance(next_scene, str):
                    return next_scene
                return next_scene.get_scene_name()

            except ValueError:
                error_string = "this is an invalid choice. please try again"
                self.output_instance.output(error_string)
                user_input = self.input_instance.input("your choice: ")
