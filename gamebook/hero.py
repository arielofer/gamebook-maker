from gamebook.creature import Creature


class Hero(Creature):
    def __init__(self, traits):
        self.traits = traits
        self.is_alive = True

    def fight(self, attack_t_name, defence_t_name, monster):
        """
            attack_t_name: the name of the trait that is used as the creature's
            power

            defence_t_name: the name of the trait that is used as the
            creature's health
        """

        while self.is_alive and monster.is_alive:
            if self.attack(attack_t_name) >= monster.attack(attack_t_name):
                monster.defend(defence_t_name, 2)
            else:
                self.defend(defence_t_name, 2)

        if self.is_alive:
            return True  # the hero won
        return False  # the hero lost
