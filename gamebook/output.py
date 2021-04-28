from gamebook.output_interface import OutputInterface


class Output(object):

    def __init__(self, interface: OutputInterface) -> None:
        self.interface = interface

    @property
    def interface(self) -> OutputInterface:
        """ reference to the OutputInterface object"""
        return self._interface

    @interface.setter
    def interface(self, new_interface: OutputInterface) -> None:
        """replace the interface at runtime"""
        self._interface = new_interface

    def output(self, content: str):
        self.interface.output(content)

    def clear(self) -> None:
        self.interface.clear()

    def exit(self, exit_reason) -> None:
        self.interface.exit(exit_reason)
