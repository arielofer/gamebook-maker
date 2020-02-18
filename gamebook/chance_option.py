import random
from gamebook.option import *

class ChanceOptions(Option):
    """an option which the player won't necessarily be succesful in preforming(depends on the decision's success rate)"""
    def DecisionDraw(self):
        wheights = []
        for i in range(len(self.decision)-1):
            wheights[i] = self.decision[i].get_success_rate()
        draw = random.choices(self.decision,wheights,k=1)
        return draw
