from gamebook.tests.mock_scenes import scene1
from gamebook.tests.mock_nextscene import nextscene1

"""
    using mock Next_scene nextscene1:

    nextscene1:
        next_scene: scene1
        success_rate: 1.0 (default)
    
"""
def test_initialization():

    assert nextscene1.get_scene() == scene1
    assert nextscene1.get_scene_name() == scene1.get_name()
    assert nextscene1.get_success_rate() == 1.0

