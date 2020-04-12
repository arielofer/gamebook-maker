from gamebook.tests.mock_trait import trait1,trait2

"""
using mock scenes trait1 and trait2

trait1:
    name: trait1
    const: 6
    dice_num: not set - checking if default is 0

trait2:
    dice_num: 1
"""

def test_initialization():

    assert trait1.get_name() == "trait1"
    assert trait1.get_const() == 6
    assert trait1.get_dice_num() == 0
    assert trait2.get_dice_num() == 1
    # need to find a way to assert trait.value 