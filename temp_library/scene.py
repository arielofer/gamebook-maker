class Scene(object):
    def __init__(self, name, desc, choices):
        self.name = name
        self.desc = desc
        self.choices = choices
        
    def get_name(self):
        return self.name

    def show_desc(self):
        return self.desc

    def show_choices(self):
        choice_list = "available options:\n"
        for options in range(len(self.choices)-1):
            choice_list += self.choices[options].show_text()+" "+self.choices[options].show_keys()+" "+\
                          str(self.choices[options].get_decision())+"\n"

        return choice_list

