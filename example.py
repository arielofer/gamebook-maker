from gamebook.scene import Scene
from gamebook.trait import Trait
from gamebook.monster import Monster
from gamebook.fight_scene import FightScene
from gamebook.option import Option
from gamebook.nextscene import NextScene
from gamebook.game_manager import GameManager
import gamebook.constants

monster_skill = Trait(name=gamebook.constants.power_trait_name,
                      min_value=1, amount=1)
monster_stamina = Trait(name=gamebook.constants.health_trait_name,
                        min_value=6, amount=2)

imp = Monster(name="imp", traits=[monster_skill, monster_stamina])

trap_door_scene = Scene(
    name="trap door",
    desc='''you walk the path when suddenly the floor under you drops.
you crash to to ground and the walls around you are greatly tall and slippery.
you are stuck and unable to get out- game over''',
    options=[]
)

failed_to_escape = Scene(
    name="failed fleeing scene",
    desc='''you failed to flee the imp. he managed to grab you from behind and kill you.
game over - you died''',
    options=[]
)

flee_scene = Scene(
    name="fleeing scene",
    desc='game over - you fled',
    options=[]
)

fountain_scene = Scene(
    name="fountain scene",
    desc='''you feel your skin rejuvenated and more powerful then ever.
your journey is now completed.
game over - you won''',
    options=[]
)

dead_scene = Scene(
    name="death scene",
    desc='the imp defeated you.\ngame over - you died',
    options=[]
)

left_at_fork = Scene(
    name="left at fork",
    desc='''you keep walking the dark path, watching your steps.
then suddenly you witness a little spot of light. you walk towards it and
it grows as you get nearer it. it is an exit! you exit the maze and witness
your sought after treasure - the fountain of youth...
do you enter the water?''',
    options=[
        Option('enter the fountain', user_inputs=['enter'],
               next_scenes="fountain scene")
    ]
)

after_fight_scene = Scene(
    name="after fight with imp",
    desc='''congratulations, you defeated the imp.
you stare at the imp's corpse then at the wall infront of you.
you understand that you need to go back to the junction and take the other way''',
    options=[
        Option('go back and continue', user_inputs=['go back'],
               next_scenes="left path")
    ]
)

imp_fight_scene = FightScene(
    name="fight scene",
    desc="you fight the imp",
    next_scenes=[
        NextScene(after_fight_scene),
        NextScene(dead_scene)
    ],
    enemy=imp
)

right_at_intro = Scene(
    name="right at intro",
    desc='''you find yourself in a dead end facing a blue imp.
what do you do?''',
    options=[
        Option('Fight', user_inputs=['fight'],
               next_scenes=[
            NextScene(imp_fight_scene)
        ]),
        Option('Flee', user_inputs=['flee'],
               next_scenes=[
            NextScene(flee_scene, success_rate=0.5),
            NextScene(failed_to_escape, success_rate=0.5)
        ])
    ]
)

left_at_intro = Scene(
    name="left path",
    desc='''you are in a narrow corridor facing a three legged fork in the way.
only the middle one seems to be dimmly lit. which way do you pick?''',
    options=[
        Option('left', user_inputs=['left'],
               next_scenes=[
            NextScene(left_at_fork)
        ]),
        Option('middle', user_inputs=['middle'],
               next_scenes=[
            NextScene(trap_door_scene)
        ]),
        Option('right', user_inputs=['right'],
               next_scenes=[
            NextScene(trap_door_scene)
        ])
    ]
)

intro_scene = Scene(
    name="intro",
    desc="""At last your two-day hike is over. You unsheathe your sword
as you enter the maze. you walk the long straight path suddenly
you face a junction. choose to left or right""",
    options=[
        Option('Go left', user_inputs=['l', 'left'],
               next_scenes=NextScene(left_at_intro)),
        Option('Go right', user_inputs=['r', 'right'],
               next_scenes="right at intro")
    ]
)

scenes_list = [intro_scene, left_at_intro, right_at_intro, imp_fight_scene,
               after_fight_scene, dead_scene, fountain_scene, flee_scene,
               left_at_fork, failed_to_escape, trap_door_scene]


def main():
    gm = GameManager(scenes_list, "terminal")
    gm.start(intro_scene)


if __name__ == "__main__":
    main()
