from gamebook.tests.mock_nextscene import nextscene1
from gamebook.tests.mock_chance_option import option1

"""
using mock Next_scene nextscene1 and mock option option1

nextscene1:
    next_scene: scene1
    success_rate: not set (default is 1.0)

option1:
    text: hello world
    keys: h, next
    nextscene: nextscene1
"""

def test_initialization():
    
    assert option1.show_text() == 'hello world'
    assert option1.show_keys() == "available keys: h, next"
    assert option1.Evaluate_decision() == nextscene1