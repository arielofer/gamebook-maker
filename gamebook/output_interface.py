class OutputInterface(object):
    """
    declares operations common to all supported kinds of output interfaces.
    the Output uses this class to call the fuctions defined in the different
    output interfaces.
    """

    def output(self, content: str):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def exit(self, exit_reason: str):
        raise NotImplementedError
