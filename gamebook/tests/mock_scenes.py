from gamebook.option import *
from gamebook.nextscene import *
from gamebook.scene import *

dead_scene = Scene("death scene", "game over", [])
    
scene1 = Scene("scene1", "welcome to scene no 1",
[
            Option('Go left', key=['l', 'left'], nextscene=[Next_scene(dead_scene)]),
            Option('Go right', key=['r', 'right'], nextscene=[Next_scene(dead_scene)])
        ] )