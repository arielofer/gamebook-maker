from gamebook.scene import *
from gamebook.option import *
from gamebook.nextscene import *
from gamebook.helpers import openscrn
from gamebook.options import Options


class FleeScene(Scene):
    def __init__(self, name, desc, options):
        super().__init__(
            name = "fleeing scene",
            desc='game over - you fled',
            options=[]
        )

class LuckyScene(Scene):
    def __init__(self, name, desc, options):
        super().__init__(
            name = "luck scene",
            desc='game over - you won',
            options=[]
        )

class DeadScene(Scene):
    def __init__(self, name, desc, options):
        super().__init__(
            name = "death scene",
            desc='game over - you died',
            options=[]
        )

class NextScene2(Scene):
    def __init__(self, name, desc, options):
        super().__init__(
            name = "scene2",
            desc='Hello from the next scene 2',
            options=[
                Option('Fight', user_input=['fight'],
                    next_scene=[
                        NextScene(LuckyScene, success_rate=0.5),
                        NextScene(DeadScene, success_rate=0.5)
                    ]),
                Option('Flee', user_input=['flee'], 
                    next_scene=[
                        NextScene(FleeScene, success_rate= 0.5), 
                        NextScene(DeadScene, success_rate=0.5)
                    ])
            ]
        )

class NextScene1(Scene):
    def __init__(self, name, desc, options):
        super().__init__(
            name = "scene1",
            desc='Hello from the next scene 1',
            options=[
                Option('Fight', user_input=['fight'],
                    next_scene=[
                        NextScene(LuckyScene, success_rate=0.5),
                        NextScene(DeadScene, success_rate=0.5)
                    ]),
                Option('Flee', user_input=['flee'], 
                    next_scene=[
                        NextScene(FleeScene, success_rate= 0.5), 
                        NextScene(DeadScene, success_rate=0.5)
                    ])
            ]
        )
    

class IntroScene(Scene):
    def __init__(self, name, desc, options):
        super().__init__(
            name = "intro",
            desc = "At last your two-day hike is over.\nYou unsheathe your sword",
            options = [
                Option('Go left', user_input=['l', 'left'], next_scene=[NextScene(NextScene1)]),
                Option('Go right', user_input=['r', 'right'], next_scene=[NextScene(NextScene2)])
            ]
        )

