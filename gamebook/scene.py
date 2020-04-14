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
            text = option.show_text()
            keys = option.show_keys()
            des = option.show_decision()
            
            choice_list += f"{text} , {keys} , {des}\n"
        
        return choice_list

