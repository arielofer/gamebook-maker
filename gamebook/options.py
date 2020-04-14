import random

class Options():
    """a set of options which the player won't necessarily be succesful
    in preforming (depends on the decision's success rate)"""

    def __init__(self, options):
        self.options = options

    
    def decision_draw(self):
        weights = []
        for option in self.options:
            weights.append(option.get_success_rate())
        draw = random.choices(self.options,weights,k=1)
        return draw[0] # TODO: use .get with default value