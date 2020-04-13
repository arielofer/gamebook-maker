from gamebook.scene import Scene
from gamebook.nextscene import NextScene
from gamebook.option import Option

dead_scene = Scene("death_scene", "game over", [])

scene1 = Scene("scene1", "At last your two-day hike is over.", [
                Option('Go left', key=['l', 'left'], next_scene=[NextScene(dead_scene)]),
                Option('Go right', key=['r', 'right'], next_scene=[NextScene(dead_scene)])
            ])

def test_show_options():
   
    # the string is very long so i cut it to multiple sections

    result = "available options:\nGo left , available keys: l, left , next scenes:death scene, 1.0\n\n"
    result += "Go right , available keys: r, right , next scenes:death scene, 1.0\n\n"

    assert scene1.show_options() == result

