from gamebook.scene import Scene
from gamebook.nextscene import NextScene
from gamebook.option import Option


def test_show_options():
    
    dead_scene = Scene("death scene", "game over", [])

    scene1 = Scene("scene1", "At last your two-day hike is over.",
    [
        Option('Go left', user_input=['l', 'left'], next_scene=[NextScene(dead_scene)]),
        Option('Go right', user_input=['r', 'right'], next_scene=[NextScene(dead_scene)])
    ])


    # the string is very long so i cut it to multiple sections

    result = "available options:\nGo left , available user_inputs: l, left , next scenes:death scene, 1.0\n\n"
    result += "Go right , available user_inputs: r, right , next scenes:death scene, 1.0\n\n"

    assert scene1.show_options() == result

