import random
from gamebook.option import Option


class Scene(object):
    """
        arguments:

        desc - A string containing what is hppening in this current scene

        options - a list of options that the user can choose

    """
    def __init__(self, name, desc, options):
        self.name = name
        self.desc = desc
        self.options = options

    def get_name(self):
        return self.name

    def show_desc(self):
        return self.desc

    def show_options(self):
        """return a string of all availabe options"""

        choice_string = "available options:\n"

        if not isinstance(self.options, list):
            option = self.options
            title = option.show_title()
            user_inputs = option.show_user_inputs()
            nextscene = option.show_next_scenes()

            choice_string += (f"{title} , {user_inputs} , {nextscene}")

            return choice_string

        for option in self.options:
            title = option.show_title()
            user_inputs = option.show_user_inputs()
            nextscene = option.show_next_scenes()

            choice_string += f"{title} , {user_inputs} , {nextscene}\n"

        return choice_string

    def get_option_by_user_input(self, user_input_recieved):
        for option in self.options:
            if user_input_recieved in option.user_inputs:
                return option

        raise ValueError("no option with this user_input found")

    def next_scene_draw(self, option_user_key):
        """
            picks the next scene randomly based on its success_rate

            option_user_key: the user_input of the option the user chose
        """

        if len(self.options) == 0:
            raise ValueError("options is empty")

        option = self.get_option_by_user_input(option_user_key)

        if not option:
            raise Exception("the user input_recieved",
                            " does not match any option")

        if option.next_scenes:
            if not isinstance(option.next_scenes, list) or\
                 len(option.next_scenes) == 1:
                return option.next_scenes
            weights = [i.get_success_rate() for i in option.next_scenes]
        else:
            raise ValueError("this option has no next_scene")

        draw = random.choices(option.next_scenes, weights, k=1)
        return draw[0]
