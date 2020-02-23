class Option(object):
    """
        a choice you can choose from a list in a scene, that leads you to a next scene.
        returns a scene

        arguments:

        key - a list of acceptable inputs that the option identifies for when the player needs to choose an option in the scene

        desicion - leads to the following scene
    """
    def __init__(self, text, key, decision):
        self.text = text
        self.key = key
        self.decision = decision

    def show_text(self):
        return self.text

    def get_decision(self):
        return self.decision.get_decision_name()

    def show_keys(self):
        """returns a string of all available keys"""

        key_list = "available keys: "
        for i in range(len(self.key)-1):
            key_list += self.key[i]
            if i + 1 <= len(self.key):
                key_list += ", "

        return key_list

