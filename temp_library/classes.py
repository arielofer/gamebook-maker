import temp_library
import random

class Decision(object):
    def __init__(self, next__scene, success_rate=1.0):
        self.next_scene = next__scene
        self.success_rate = success_rate

    def get_scene(self):
        return self.next_scene

    def get_scene_name(self):
        return self.next_scene.get_name()

    def get_success_rate(self):
        return self.success_rate


class Scene(object):
    def __init__(self, name, desc, choices):
        self.name = name
        self.desc = desc
        self.choices = choices
        

    def get_name(self):
        return self.name

    def show_desc(self):
        return self.desc

    def show_choices(self):
        choice_list = "available options:\n"
        for options in range(len(self.choices)-1):
            choice_list += self.choices[options].show_text()+" "+self.choices[options].show_keys()+" "+\
                          str(self.choices[options].get_decision())+"\n"

        return choice_list


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


class ChanceOptions(Option):
    def DecisionDraw(self):
        wheights = []
        for i in range(len(self.decision)-1):
            wheights[i] = self.decision[i].get_success_rate()
        draw = random.choices(self.decision,wheights,k=1)
        return draw


class IntroScene(Scene):
    desc = 'Hello from the intro'
    choices = [
        Option('Go left', key=['l', 'left'], decision=[Decision(NextScene1)]),
        Option('Go right', key=['r', 'right'], decision=[Decision(NextScene2)])
    ]


class NextScene1(Scene):
    desc='Hello from the next scene 1'
    choices=[
        ChanceOptions('Fight', key=['fight'],
            decision=[
                Decision(LuckyScene, success_rate=0.5),
                Decision(DeadScene, success_rate=0.5)
            ]),
        ChanceOptions('Flee', key=['flee'], 
            decision=[
                Decision(FleeScene, success_rate= 0.5), 
                Decision(DeadScene, success_rate=0.5)
            ])
    ]
