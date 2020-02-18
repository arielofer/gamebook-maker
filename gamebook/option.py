class Option(object):
    def __init__(self, text, key, decision):
        self.text = text
        self.key = key
        self.decision = decision

    def show_text(self):
        return self.text

    def get_decision(self):
        return self.decision.get_decision_name()

    def show_keys(self):
        key_list = "available keys: "
        for i in range(len(self.key)-1):
            key_list += self.key[i]
            if i + 1 <= len(self.key):
                key_list += ", "

        return key_list

