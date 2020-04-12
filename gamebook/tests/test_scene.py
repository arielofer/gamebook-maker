from gamebook.tests.mock_scenes import scene1, dead_scene

"""
using mock scenes scene1 and dead_scene

scene1:
    name: scene1
    desc: welcome to scene no 1
    choices:[
            Option('Go left', key=['l', 'left'], nextscene=[Next_scene(dead_scene)]),
            Option('Go right', key=['r', 'right'], nextscene=[Next_scene(dead_scene)])
            ]

dead_scene:
    name: death scene
    desc: game over
    choices:[]
"""

def test_initialization():

    assert scene1.get_name() == "scene1"
    assert scene1.show_desc() == "welcome to scene no 1"
    assert scene1.show_choices() == "available options:\nGo left , available keys: l, left , next scenes:death scene, 1.0\n\nGo right , available keys: r, right , next scenes:death scene, 1.0\n\n"

def test_recieving_next_scene():

    assert scene1.choices[0].nextscene[0].get_scene() == dead_scene

