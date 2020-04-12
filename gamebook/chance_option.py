import random
from gamebook.option import *

class ChanceOptions(Option):
    """an option which the player won't necessarily be succesful in preforming(depends on the nextscene's success rate)"""
    def Evaluate_decision(self):
        """
        wheights = []
        for i in self.nextscene:
            wheights.append(i.get_success_rate())
        """
        wheights = [i.get_success_rate() for i in self.nextscene]
        draw = random.choices(self.nextscene,wheights,k=1)
        return draw[0] # since random.choices returns a list and not the nextscene, we need to extract it.
