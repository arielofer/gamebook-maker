from gamebook.trait import Trait

trait1 = Trait("trait1", 6, dice_num=3)

def test_initialization():

    assert trait1.get_name() == "trait1"
    assert trait1.get_const() == 6
    assert trait1.get_dice_num() == 3
    
def test_get_value():
    """ trait1's value is randomized but should be between 3 to 18"""
    result = trait1.get_value() >= 3 and trait1.get_value() <= 18

    assert result == True
