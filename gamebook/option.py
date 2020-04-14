class Option(object):
    def __init__(self, text, key, next_scene):
        self.text = text # TODO: rename to title
        self.key = key # TODO: rename to user_input
        self.next_scene = next_scene

    def show_text(self): 
        return self.text

    def show_next_scene(self):
        next_scene_list = 'next_scenes:'
        for i in range(len(self.next_scene)):    
            scene = self.next_scene[i].get_scene_name()
            rate = self.next_scene[i].get_success_rate()

            next_scene_list +=f"{scene}, {rate}\n"
        
        return next_scene_list

    def show_keys(self):
        """returns a string of all available keys"""

        key_list = "available keys: "
        for i in range(len(self.key)):
            key_list += self.key[i]
            if i+1 < len(self.key):
                key_list += ", "

        return key_list
