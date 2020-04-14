from gamebook.scene import *
from gamebook.option import *
from gamebook.decision import *
from gamebook.helpers import openscrn
from gamebook.chance_option import ChanceOptions


class FleeScene(Scene):
    def __init__(self, name, desc, choices):
        super().__init__(
            name = "fleeing scene",
            desc='game over - you fled',
            choices=[]
        )

class LuckyScene(Scene):
    def __init__(self, name, desc, choices):
        super().__init__(
            name = "luck scene",
            desc='game over - you won',
            choices=[]
        )

class DeadScene(Scene):
    def __init__(self, name, desc, choices):
        super().__init__(
            name = "death scene",
            desc='game over - you died',
            choices=[]
        )

class NextScene2(Scene):
    def __init__(self, name, desc, choices):
        super().__init__(
            name = "scene2",
            desc='Hello from the next scene 2',
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
        )

class NextScene1(Scene):
    def __init__(self, name, desc, choices):
        super().__init__(
            name = "scene1",
            desc='Hello from the next scene 1',
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
        )
    

class IntroScene(Scene):
    def __init__(self, name, desc, choices):
        super().__init__(
            name = "intro",
            desc = "At last your two-day hike is over.\nYou unsheathe your sword",
            choices = [
                Option('Go left', key=['l', 'left'], decision=[Decision(NextScene1)]),
                Option('Go right', key=['r', 'right'], decision=[Decision(NextScene2)])
            ]
        )

