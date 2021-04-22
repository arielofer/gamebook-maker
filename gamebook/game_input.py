from gamebook.input_interface import InputInterface


class Input(object):

    def __init__(self, interface: InputInterface) -> None:
        self.interface = interface

    @property
    def interface(self) -> InputInterface:
        """ reference to the InputInterface object"""
        return self._interface

    @interface.setter
    def interface(self, new_interface: InputInterface) -> None:
        """replace the interface at runtime"""
        self._interface = new_interface

    def input(self, prompt: str):
        return self.interface.input(prompt)

    def ask_for_user_inputs(self, options: list):
        return self.interface.ask_for_user_inputs(options)
