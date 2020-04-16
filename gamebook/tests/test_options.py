from gamebook.options import Options
from gamebook.option import Option
from gamebook.nextscene import NextScene
from gamebook.scene import Scene

def test_draw():
    
    scene1_name = "scene1"

    scene1 = Scene("scene1", "welcome", [])
    scene2 = Scene("scene2", "also welcome", [])
    nextscene1 = NextScene(scene1, success_rate = 1.0)
    nextscene2 = NextScene(scene2, success_rate = 0)
    option1 = Option("option no. 1",["n"], next_scene = [nextscene1,nextscene2])
    option2 = Option("option no. 2",["m"], next_scene = nextscene1)

    options = Options([option1, option2])

    result = options.next_scene_draw(option1) # when next_scene is a list
    assert result.get_scene_name() == scene1_name
    
    result = options.next_scene_draw(option2)# when next_scene is not a list
    assert result.get_scene_name() == scene1_name


# TODO: test if options is empty
# TODO: test if option doesn't have next_scene

# cant think of a good idea for this tests