class ReachedTheEndException(Exception):
    """
    the end of the current plot line has been reached.
    the current scene has no 'options'
    """


class ExitRequested(Exception):
    """the user sent a request to exit the game"""


class OptionNotFoundError(Exception):
    """no option with the recieved user_input found"""


class TraitNotFoundError(Exception):
    """specified trait name couldn't be found in the trait list"""
    def __init__(self, trait_name):
        self.trait_name = trait_name


class NextSceneTypeError(TypeError):
    """the value of the next scene field in Scene isn't a NextScene object
       or a scene name"""
