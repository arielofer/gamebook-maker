class Option(object):
    def __init__(self, title, user_input, next_scenes):
        self.title = title
        self.user_input = user_input
        self.next_scenes = next_scenes


    def show_title(self): 
        return self.title


    def show_next_scenes(self):
        next_scenes_string = 'next scenes:'
        for nextscene in self.next_scenes:    
            scene = nextscene.get_scene_name()
            rate = nextscene.get_success_rate()
            next_scenes_string +=f"{scene}, {rate}\n"
        
        return next_scenes_string


    def show_user_inputs(self):
        """returns a string of all available user_inputs"""

        user_input_string = "available user_inputs: "
        user_input_string += ", ".join(self.user_input)

        return user_input_string


    def get_success_rate(self):
        return self.next_scenes.success_rate

