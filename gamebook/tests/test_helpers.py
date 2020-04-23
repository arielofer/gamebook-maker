from gamebook.trait import Trait
from gamebook.helpers import stats_display


def test_stats_display():

    display_data = ' ------------------------------\n'
    display_data += '|health: 6|luck: 2|strength: 1|\n'
    display_data += ' ------------------------------'

    trait1 = Trait("health", 6)
    trait2 = Trait("luck", 2)
    trait3 = Trait("strength", 1)
    display = stats_display(trait1, trait2, trait3)
    assert display_data == display
