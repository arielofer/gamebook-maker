import temp_library
import random

class Decision(object):
    def __init__(self, next__scene, successRate=1.0):
        self.next_scene = next__scene
        self.successRate = successRate

    def GetScene(self):
        return self.next_scene

    def GetSceneName(self):
        return self.next_scene.getName()

    def GetSuccessRate(self):
        return self.successRate


class Scene(object):
    def __init__(self, name, desc, choice):
        self.name = name
        self.desc = desc
        self.choice = choice
        

    def GetName(self):
        return self.name

    def ShowDesc(self):
        return self.desc

    def ShowChoice(self):
        choice_list = "available options:\n"
        for options in range(len(self.choice)):
            choice_list += self.choice[options].ShowText()+" "+self.choice[options].ShowKeys()+" "+\
                          str(self.choice[options].GetDecision())+"\n"

        return choice_list


class Option(object):
    def __init__(self, text, key, decision):
        self.text = text
        self.key = key
        self.decision = decision

    def ShowText(self):
        return self.text

    def GetDecision(self):
        return self.decision.getDecisionName()

    def ShowKeys(self):
        key_list = "available keys: "
        for i in range(len(self.key)):
            key_list += self.key[i]
            if i + 1 <= len(self.key):
                key_list += ", "

        return key_list


class ChanceOption(Option):
    def DecisionDraw(self):
        wheights = []
        for i in range(len(self.decision)):
            wheights[i] = self.decision[i].getSuccessRate()
        draw = random.choices(self.decision,wheights,k=1)
        return draw


class IntroScene(Scene):
    desc = 'Hello from the intro'
    choice = [
        Option('Go left', key=['l', 'left'], decision=[Decision(NextScene1)]),
        Option('Go right', key=['r', 'right'], decision=[Decision(NextScene2)])
    ]


class NextScene1(Scene):
    desc='Hello from the next scene 1'
    choice=[
        ChanceOption('Fight', key=['fight'],
            decision=[
                Decision(LuckyScene, successRate=0.5),
                Decision(DeadScene, successRate=0.5)
            ]),
        ChanceOption('Flee', key=['flee'], 
            decision=[
                Decision(FleeScene, successRate= 0.5), 
                Decision(DeadScene, successRate=0.5)
            ])
    ]
