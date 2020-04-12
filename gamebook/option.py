class Option(object):
    def __init__(self, text, key, nextscene):
        self.text = text 
        self.key = key
        self.nextscene = nextscene

    def show_text(self):
        return self.text

    def show_nextscene(self):
        nextscene_list = 'next scenes:'
        for i in self.nextscene:    
            scene = i.get_scene_name()
            rate = i.get_success_rate()

            nextscene_list +=f"{scene}, {rate}\n"
        
        return nextscene_list

    def show_keys(self):
        key_list = "available keys: "
        for i in self.key:
            key_list += i
            if i+1 < len(self.key):
                key_list += ", "

        return key_list

