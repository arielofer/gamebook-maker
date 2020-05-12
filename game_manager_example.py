from gamebook.scene import Scene
from gamebook.option import Option
from gamebook.nextscene import NextScene
from gamebook.game_manager import GameManager


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

intro_scene = Scene(
            name="intro",
            desc="At last your two-day hike is over. You unsheathe your sword",
            options=[
                Option('Go left', user_inputs=['l', 'left'],
                       next_scenes=[NextScene(next_scene1)]),
                Option('Go right', user_inputs=['r', 'right'],
                       next_scenes=[NextScene(next_scene2)])
            ]
        )

scenes_list = [intro_scene, next_scene1, next_scene2, dead_scene, lucky_scene,
              flee_scene]


def main():
    gm = GameManager(scenes_list)
    gm.start(intro_scene)


if __name__ == "__main__":
    main()
