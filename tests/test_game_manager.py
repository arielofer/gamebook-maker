from gamebook.game_manager import GameManager
from gamebook.scene import Scene
from gamebook.nextscene import NextScene
from gamebook.option import Option
import pytest


def test_run_scene(monkeypatch):
    scene1_name = "scene1"

    scene1 = Scene(scene1_name, "welcome", [])
    scene2 = Scene("scene2", "also welcome", [])

    nextscene1 = NextScene(scene1, success_rate=1.0)
    nextscene2 = NextScene(scene2, success_rate=0)

    option1 = Option("go left",
                     user_inputs=["l, left"],
                     next_scenes=[nextscene1, nextscene2])

    option2 = Option("go right",
                     user_inputs=["r, right"],
                     next_scenes=nextscene1)

    example_scene = Scene("example scene",
                          desc="this is an example scene",
                          options=[option1, option2])

    gm = GameManager(example_scene)

    path = 'gamebook.game_manager.GameManager.run_scene'
    monkeypatch.setattr(path, lambda self, options: "right")

    assert gm.run_scene() == scene1_name
