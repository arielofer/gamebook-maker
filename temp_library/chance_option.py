import random
from option import *

class ChanceOptions(Option):
    
    def DecisionDraw(self):
        wheights = []
        for i in range(len(self.decision)-1):
            wheights[i] = self.decision[i].get_success_rate()
        draw = random.choices(self.decision,wheights,k=1)
        return draw
