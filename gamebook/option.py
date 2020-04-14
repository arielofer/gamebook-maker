class Option(object):
    def __init__(self, title, user_input, next_scene):
        self.title = title
        self.user_input = user_input
        self.next_scene = next_scene

    def show_title(self): 
        return self.title

    def show_next_scene(self):
        next_scene_string = 'next scenes:'
        for i in self.next_scene:    
            scene = i.get_scene_name()
            rate = i.get_success_rate()
            next_scene_string +=f"{scene}, {rate}\n"
        
        return next_scene_string

    def show_user_inputs(self):
        """returns a string of all available user_inputs"""

        user_input_string = "available user_inputs: "
        user_input_string += ", ".join(self.user_input)

        return user_input_string

    def get_success_rate(self):
        return self.next_scene.success_rate
