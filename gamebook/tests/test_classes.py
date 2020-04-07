from gamebook.decision import *
from gamebook.scene import *
from gamebook.option import *
from gamebook.chance_option import ChanceOptions

def test_decision():

    dead_scene = Scene("death scene", "game over", [])
    
    scene1 = Scene("scene1", "welcome to scene no 1",
    [
                Option('Go left', key=['l', 'left'], decision=[Decision(dead_scene)]),
                Option('Go right', key=['r', 'right'], decision=[Decision(dead_scene)])
            ] )

    decision1 = Decision(scene1)

    assert decision1.get_scene() == scene1
    assert decision1.get_scene_name() == scene1.get_name()
    assert decision1.get_success_rate() == 1.0


def test_chance_option():
    dead_scene = Scene("death scene", "game over", [])
    desicion1 = Decision(dead_scene)
    option1 = ChanceOptions('hello world', key=['h', 'next'], decision=[desicion1])
    
    assert option1.show_text() == 'hello world'
    # assert option1.show_decision() ==  "decisions:death scene, 1.0"
    assert option1.show_keys() == "available keys: h, next"
    assert option1.DecisionDraw() == desicion1