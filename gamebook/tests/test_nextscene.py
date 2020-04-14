from gamebook.nextscene import NextScene
from gamebook.scene import Scene
from gamebook.tests.test_scene import scene1

def test_get_scene_name():
    nextscene1 = NextScene(scene1, 1.0)

    assert nextscene1.get_scene_name == "scene1"