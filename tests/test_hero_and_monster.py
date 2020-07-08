from gamebook.hero import Hero
from gamebook.monster import Monster
from gamebook.trait import Trait


def test_fight():
    skill = Trait(name="Skill", min_value=6, amount=1)
    luck = Trait(name="Luck", min_value=6, amount=1)
    stamina = Trait(name="Stamina", min_value=12, amount=2)

    crono = Hero(traits=[skill, luck, stamina])

    monster_skill = Trait(name="Skill", min_value=1, amount=1)
    monster_stamina = Trait(name="Stamina", min_value=6, amount=2)

    imp = Monster(name="imp", traits=[monster_skill, monster_stamina])

    assert crono.fight(attack_t_name="Skill", defence_t_name="Stamina",
                       monster=imp)
