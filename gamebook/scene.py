class Scene(object):
    """ 
        arguments:
        desc - A string containing what is hppening in this current scene

        choices - a list of options that the user can choose to continue to the next scene

    """
    def __init__(self, name, desc, choices):
        self.name = name
        self.desc = desc
        self.choices = choices
        
    def get_name(self):
        return self.name

    def show_desc(self):
        return self.desc

    def show_choices(self):
        """return a string of all availabe choices"""
        
        choice_list = "available options:\n"
        for options in range(len(self.choices)-1):
            text = self.choices[options].show_text()
            keys = self.choices[options].show_keys()
            des = str(self.choices[options].get_decision())
            
            choice_list += f'{text} , {keys} , {des} \n'
        
        return choice_list

