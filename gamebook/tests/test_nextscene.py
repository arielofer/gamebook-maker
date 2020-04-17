from gamebook.nextscene import NextScene
from gamebook.scene import Scene
from gamebook.option import Option

def test_get_scene_name():

    dead_scene = Scene("death_scene", "game over", [])
    
    scene1 = Scene("scene1", "At last your two-day hike is over.",
    [
        Option('Go left', user_input=['l', 'left'], next_scenes=[NextScene(dead_scene)]),
        Option('Go right', user_input=['r', 'right'], next_scenes=[NextScene(dead_scene)])
    ])

    nextscene1 = NextScene(scene1, 1.0)

    assert nextscene1.get_scene_name() == "scene1"