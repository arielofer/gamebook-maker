import temp_library


# class Decision:

class Scene(object):
    def __init__(self, desc, choice, decision):
        self.desc = desc
        self.choice = choice
        self.decision = decision

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
        return self.decision

    def ShowKeys(self):
        key_list = "available keys: "
        for i in range(len(self.key)):
            key_list += self.key[i]
            if i + 1 <= len(self.key):
                key_list += ", "

        return key_list


# class ChanceOption(Option):


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
        ChanceOption('Flee', key=['flee'], )
    ]
