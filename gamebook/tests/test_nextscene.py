from gamebook.nextscene import NextScene
from gamebook.scene import Scene
from gamebook.tests.test_scene import scene1

nextscene1 = NextScene(scene1, 1.0)

""" scene1: name = "scene1" """

def test_get_scene_name():
    assert nextscene1.get_scene_name == "scene1"