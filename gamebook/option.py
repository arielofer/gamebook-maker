class Option(object):
    def __init__(self, text, key, decision):
        self.text = text
        self.key = key
        self.decision = decision

    def show_text(self):
        return self.text

    def show_decision(self):
        decision_list = 'decisions:'
        for i in range(len(self.decision)):    
            scene = self.decision[i].get_scene_name()
            rate = self.decision[i].get_success_rate()

            decision_list +=f"{scene}, {rate}\n"
        
        return decision_list

    def show_keys(self):
        key_list = "available keys: "
        for i in range(len(self.key)):
            key_list += self.key[i]
            if i+1 < len(self.key):
                key_list += ", "

        return key_list

