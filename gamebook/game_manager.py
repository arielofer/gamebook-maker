import gamebook.exceptions
import gamebook.constants
from gamebook.hero import Hero
from gamebook.helpers import trait_init
from gamebook.fight_scene import FightScene
from gamebook.nextscene import NextScene
from gamebook.game_input import Input
from gamebook.terminal_input import TerminalInput
from gamebook.output import Output
from gamebook.terminal_output import TerminalOutput


class GameManager(object):
    def __init__(self, scenes_import: list, format: str):
        """
            takes care of presenting the scenes to the user and moving
            from one scene to next fluently

            scenes_import: a list of all the sceness

            format: the type of IN/OUT format: terminal, web or socket
        """
        self.scenes_import = scenes_import
        output_formats = {"terminal": TerminalOutput()}
        input_formats = {"terminal": TerminalInput()}
        self.output_instance = Output(output_formats[format])
        self.input_instance = Input(input_formats[format])

        power_trait, luck_trait, health_trait = trait_init()
        self.hero = Hero(traits=[power_trait, luck_trait, health_trait])

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

            except gamebook.exceptions.ReachedTheEndException:
                self.output_instance.exit(gamebook.constants.
                                          end_message)
                break

            except gamebook.exceptions.ExitRequested:
                self.output_instance.exit(gamebook.constants.
                                          exit_message)
                break

            except gamebook.exceptions.TraitNotFoundError as T:
                self.output_instance.output(gamebook.constants.
                                            invalid_trait_name.format(
                                                trait_name=T.trait_name
                                            ))
                break

            except gamebook.exceptions.NextSceneTypeError:
                self.output_instance.output(gamebook.constants.
                                            invalid_next_scene_value)
                break

    def get_next_scene(self, scene_name):
        for scene in self.scenes_import:
            if scene.get_name() == scene_name:
                return scene

    def run_scene(self):
        """evaluates the current scene and returns
           the following one by it's name"""

        self.output_instance.output(self.current_scene.show_desc())

        if isinstance(self.current_scene, FightScene):
            next_scene = self.current_scene.run_fight(self.hero)
            if not isinstance(next_scene, NextScene):
                raise gamebook.exceptions.NextSceneTypeError
            if isinstance(next_scene, str):
                return next_scene
            return next_scene.get_scene_name()

        if len(self.current_scene.options) == 0:
            # if the current scene has no options, the game ends
            raise gamebook.exceptions.ReachedTheEndException

        user_input = self.input_instance.\
            ask_for_user_inputs(self.current_scene.options)

        if user_input == gamebook.constants.exit_user_input:
            # the user wants to quit the game
            raise gamebook.exceptions.ExitRequested

        while True:
            try:
                next_scene = self.current_scene.next_scene_draw(user_input)
                if isinstance(next_scene, str):
                    return next_scene
                if not isinstance(next_scene, NextScene):
                    raise gamebook.exceptions.NextSceneTypeError
                return next_scene.get_scene_name()

            except gamebook.exceptions.OptionNotFoundError:
                self.output_instance.output(gamebook.constants.
                                            invalid_user_input_message)

                user_input = self.input_instance.input(gamebook.
                                                       constants.
                                                       input_prompt)
