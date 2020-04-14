from gamebook.options import Options
from gamebook.option import Option
from gamebook.nextscene import NextScene
from gamebook.scene import Scene

def test_draw():
    
    option1_title = "option no. 1"

    scene1 = Scene("scene1", "welcome", [])
    scene2 = Scene("scene2", "also welcome", [])
    nextscene1 = NextScene(scene1, success_rate = 1.0)
    nextscene2 = NextScene(scene2, success_rate = 0)
    option1 = Option(option1_title,["n"], next_scene = nextscene1)
    option2 = Option("option no. 2",["m"], next_scene = nextscene2)

    options = Options([option1, option2])
    result = options.next_scene_draw()

    assert result.show_title() == option1_title

# TODO: test if options is empty
# TODO: test if option doesn't have next_scene