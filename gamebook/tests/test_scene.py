from gamebook.scene import Scene
from gamebook.nextscene import NextScene
from gamebook.option import Option
import pytest


def test_show_options():

    dead_scene = Scene("death scene", "game over", [])

    scene1 = Scene("scene1", "At last your two-day hike is over.",
                   [
                    Option('Go left',
                           user_inputs=['l', 'left'],
                           next_scenes=[NextScene(dead_scene)]),
                    Option('Go right',
                           user_inputs=['r', 'right'],
                           next_scenes=[NextScene(dead_scene)])
                   ])

    # the string is very long so i cut it to multiple sections

    result = """available options:
Go left , available user_inputs: l, left , next scenes:death scene, 1.0

Go right , available user_inputs: r, right , next scenes:death scene, 1.0

"""

    assert scene1.show_options() == result


def test_draw():

    scene1_name = "scene1"

    scene1 = Scene(scene1_name, "welcome", [])
    scene2 = Scene("scene2", "also welcome", [])

    nextscene1 = NextScene(scene1, success_rate=1.0)
    nextscene2 = NextScene(scene2, success_rate=0)

    option1 = Option("option no. 1",
                     user_inputs=["n"],
                     next_scenes=[nextscene1, nextscene2])

    option2 = Option("option no. 2",
                     user_inputs=["m"],
                     next_scenes=nextscene1)

    example_scene = Scene("exapmle scene",
                          desc="this is an example scene",
                          options=[option1, option2])

    result = example_scene.next_scene_draw("n")  # when next_scene is a list
    assert result.get_scene_name() == scene1_name

    result = example_scene.next_scene_draw("m")  # when next_scene is'nt a list
    assert result.get_scene_name() == scene1_name


def test_draw_when_options_is_empty():

    example_scene = Scene("exapmle scene",
                          desc="this is an example scene",
                          options=[])

    with pytest.raises(ValueError) as error_text:
        assert example_scene.next_scene_draw("n")
    assert str(error_text.value) == "options is empty"


def test_draw_when_option_doesnt_have_next_scene():

    example_option = Option("option no. 1",
                            user_inputs=["n"],
                            next_scenes=[])

    example_scene = Scene("exapmle scene",
                          desc="this is an example scene",
                          options=[example_option])

    with pytest.raises(ValueError) as error_text:
        assert example_scene.next_scene_draw("n")
    assert str(error_text.value) == "this option has no next_scene"

