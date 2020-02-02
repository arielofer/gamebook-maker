from scene import *
from option import *
from chance_option import *
from decision import *

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
