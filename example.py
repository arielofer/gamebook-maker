from gamebook.scene import Scene
from gamebook.trait import Trait
from gamebook.monster import Monster
from gamebook.fight_scene import FightScene
from gamebook.option import Option
from gamebook.nextscene import NextScene
from gamebook.terminal_input import TerminalInput
from gamebook.terminal_output import TerminalOutput
from gamebook.game_manager import GameManager
import gamebook.important_strings

flee_scene = Scene(
            name="fleeing scene",
            desc='game over - you fled',
            options=[]
        )

lucky_scene = Scene(
            name="luck scene",
            desc='game over - you won',
            options=[]
        )

dead_scene = Scene(
            name="death scene",
            desc='game over - you died',
            options=[]
        )

monster_skill = Trait(name=gamebook.important_strings.power_trait_name,
                      min_value=1, amount=1)
monster_stamina = Trait(name=gamebook.important_strings.health_trait_name,
                        min_value=6, amount=2)

imp = Monster(name="imp", traits=[monster_skill, monster_stamina])

fight_scene = FightScene(
            name="fight scene",
            desc="you fight the monster",
            next_scenes=[
                        NextScene(lucky_scene),
                        NextScene(dead_scene)
                    ],
            enemy=imp
        )

next_scene2 = Scene(
            name="scene2",
            desc='Hello from the next scene 2',
            options=[
             Option('Fight', user_inputs=['fight'],
                    next_scenes=[
                    NextScene(lucky_scene, success_rate=0.5),
                    NextScene(dead_scene, success_rate=0.5)
                    ]),
             Option('Flee', user_inputs=['flee'],
                    next_scenes=[
                    NextScene(flee_scene, success_rate=0.5),
                    NextScene(dead_scene, success_rate=0.5)
                    ])
            ]
        )

next_scene1 = Scene(
            name="scene1",
            desc='Hello from the next scene 1',
            options=[
             Option('Fight', user_inputs=['fight'],
                    next_scenes=[
                    NextScene(fight_scene)
                    ]),
             Option('Flee', user_inputs=['flee'],
                    next_scenes=[
                    NextScene(flee_scene, success_rate=0.5),
                    NextScene(dead_scene, success_rate=0.5)
                    ])
            ]
        )

intro_scene = Scene(
            name="intro",
            desc="At last your two-day hike is over. You unsheathe your sword",
            options=[
             Option('Go left', user_inputs=['l', 'left'],
                    next_scenes=NextScene(next_scene1)),
             Option('Go right', user_inputs=['r', 'right'],
                    next_scenes=next_scene2)
            ]
        )

scenes_list = [intro_scene, next_scene1, next_scene2, fight_scene, dead_scene,
               lucky_scene, flee_scene]


def main():
    output_instance = TerminalOutput()
    input_instance = TerminalInput()

    gm = GameManager(scenes_list, output_instance, input_instance)
    gm.start(intro_scene)


if __name__ == "__main__":
    main()
