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
        
        choice_list = "available options:\n"
        for option in self.options:
            title = option.show_title()
            user_inputs = option.show_user_inputs()
            nextscene = option.show_next_scenes()
            
            choice_list += f"{title} , {user_inputs} , {nextscene}\n"
        
        return choice_list

    def next_scene_draw(self, option_to_evaluate):
        
        if len(self.options) == 0:
            raise ValueError("options is empty")
        
        for opt in self.options:
            if option_to_evaluate == opt:
                option = option_to_evaluate
        
        if not option:
            raise Exception("this option does not exist in this scene")

        if type(option.next_scenes) == list:
            weights = [i.get_success_rate() for i in option.next_scenes]
        else:
            return option.next_scenes

        draw = random.choices(option.next_scenes,weights,k=1)
        return draw[0]