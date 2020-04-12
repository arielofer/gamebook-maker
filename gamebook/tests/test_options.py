from gamebook.options import Options
from gamebook.option import Option
from gamebook.decision import Decision
from gamebook.scene import Scene

def test_draw():
    
    option1_title = "option no. 1"

    scene1 = Scene("scene1", "welcome", [])
    scene2 = Scene("scene2", "also welcome", [])
    nextscene1 = Decision(scene1, success_rate = 1.0)
    nextscene2 = Decision(scene2, success_rate = 0)
    option1 = Option(option1_title,["n"], decision = nextscene1)
    option2 = Option("option no. 2",["m"], decision = nextscene2)

    options = Options([option1, option2])
    result = options.decision_draw()

    assert result.show_text() == option1_title
