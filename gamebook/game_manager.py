from gamebook.terminal_output import TerminalOutput
from gamebook.terminal_input import TerminalInput
import sys


class GameManager(object):
    def __init__(self, scene):
        self.scene = scene

    def start(self, scene_import):
        current_scene = self.scene
        while True:
            next_scene_name = current_scene.run_scene()
            current_scene = self.next_scene(next_scene_name, scene_import)

    def next_scene(self, scene_name, scene_import):
        for scene in scene_import:
            if scene.get_name() == scene_name:
                return scene

    def run_scene(self):
        output_instance = TerminalOutput()
        input_instance = TerminalInput()

        output_instance.output(self.scene.show_desc())

        if len(self.scene.options) == 0:
            sys.exit()

        user_input = input_instance.input("your choice: ")

        while True:
            try:
                next_scene = self.scene.next_scene_draw(user_input)

            except Exception:
                error_string = "this is an invalid choice. please try again"
                output_instance.output(error_string)
                user_input = input_instance.input("your choice: ")

        if isinstance(next_scene, str):
            return next_scene
        return next_scene.get_scene_name()
