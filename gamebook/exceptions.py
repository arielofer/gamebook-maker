class ReachedTheEndException(Exception):
    """
    the end of the current plot line has been reached.
    the current scene has no 'options'
    """


class ExitRequested(Exception):
    """the user sent a request to exit the game"""


class OptionNotFoundError(Exception):
    """no option with the recieved user_input found"""
