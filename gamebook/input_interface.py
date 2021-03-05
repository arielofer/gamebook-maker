class InputInterface(object):
    """
    declares operations common to all supported kinds of intput interfaces.
    the input uses this class to call the fuctions defined in the different
    output interfaces.
    """

    def input(self, prompt: str):
        raise NotImplementedError

    def ask_for_user_inputs(self, options: list):
        raise NotImplementedError
