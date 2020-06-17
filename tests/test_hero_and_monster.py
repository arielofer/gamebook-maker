from gamebook.hero import Hero
from gamebook.monster import Monster
from gamebook.trait import Trait


def test_fight():
    skill = Trait("Skill", 6, 1)
    luck = Trait("Luck", 6, 1)
    stamina = Trait("Stamina", 12, 2)

    crono = Hero([skill, luck, stamina])

    monster_skill = Trait("Skill", 1, 1)
    monster_stamina = Trait("Stamina", 6, 2)

    imp = Monster("imp", [monster_skill, monster_stamina])

    assert crono.fight("Skill", "Stamina", imp)
