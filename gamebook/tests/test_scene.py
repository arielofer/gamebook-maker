from gamebook.scene import Scene
from gamebook.nextscene import NextScene
from gamebook.option import Option


def test_show_options():
    
    dead_scene = Scene("death scene", "game over", [])

    scene1 = Scene("scene1", "At last your two-day hike is over.",
    [
        Option('Go left', user_input=['l', 'left'], next_scenes=[NextScene(dead_scene)]),
        Option('Go right', user_input=['r', 'right'], next_scenes=[NextScene(dead_scene)])
    ])

    # the string is very long so i cut it to multiple sections

    result = "available options:\nGo left , available user_inputs: l, left , next scenes:death scene, 1.0\n\n"
    result += "Go right , available user_inputs: r, right , next scenes:death scene, 1.0\n\n"

    assert scene1.show_options() == result

def test_draw():
    
    scene1_name = "scene1"

    scene1 = Scene(scene1_name, "welcome", [])
    scene2 = Scene("scene2", "also welcome", [])
    nextscene1 = NextScene(scene1, success_rate = 1.0)
    nextscene2 = NextScene(scene2, success_rate = 0)
    option1 = Option("option no. 1",["n"],next_scenes=[nextscene1,nextscene2])
    option2 = Option("option no. 2",["m"],next_scenes = nextscene1)

    example_scene=Scene("exapmle scene","this is an example scene",options=[option1,option2])

    result = example_scene.next_scene_draw("n")#when next_scene is a list
    assert result.get_scene_name() == scene1_name
    
    result = example_scene.next_scene_draw("m")#when next_scene is not a list
    assert result.get_scene_name() == scene1_name

def test_draw_when_options_is_empty():

    scene1_name = "scene1"

    scene1 = Scene(scene1_name, "welcome", [])
    nextscene1 = NextScene(scene1, success_rate = 1.0)
    example_option = Option("option no. 1",["n"],next_scenes=nextscene1)
    example_scene = Scene("exapmle scene","this is an example scene",options=[])

    result = example_scene.next_scene_draw(example_option)
    assert result.get_scene_name == scene1_name

# TODO: test if options is empty
# TODO: test if option doesn't have next_scene

# cant think of a good idea for this tests