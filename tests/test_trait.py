from gamebook.trait import Trait


def test_initialization():

    example_trait = Trait("example_trait", 6, amount=3)

    assert example_trait.get_name() == "example_trait"
    assert example_trait.get_min_value() == 6
    assert example_trait.get_amount() == 3


def test_get_value():

    example_trait = Trait("example_trait", 6, amount=3)

    """ example_trait's value is randomized but should be between 9 to 24"""
    result = example_trait.get_value() >= 9 and example_trait.get_value() <= 24

    assert result
