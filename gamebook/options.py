import random

class Options():
    """a set of options which the player won't necessarily be succesful
    in preforming (depends on the next scene's success rate)"""

    def __init__(self, options):
        self.options = options

    
    def next_scene_draw(self, option_to_evaluate):
        
        if len(self.options) == 0:
            raise Exception("options is empty")
        
        for opt in self.options:
            if option_to_evaluate == opt:
                option = option_to_evaluate
        
        if not option:
            raise Exception("this option does not exist in this scene")

        if type(option.next_scene) == list:
            weights = [i.get_success_rate() for i in option.next_scene]
        else:
            return option.next_scene

        draw = random.choices(option.next_scene,weights,k=1)
        return draw[0]