class NextScene(object):
    def __init__(self, next__scene, success_rate=1.0):
        self.next_scene = next__scene
        self.success_rate = success_rate

    def get_scene(self):
        return self.next_scene

    def get_scene_name(self):
        return self.next_scene.get_name() 

    def get_success_rate(self):
        return self.success_rate

