from gamebook.output_interface import OutputInterface
import os
import sys


class TerminalOutput(OutputInterface):
    def output(self, content: str) -> None:
        if content:
            print(content)
        else:
            raise ValueError("no content recieved")

    def clear(self) -> None:
        """ clear the terminal window"""
        os.system("cls")

    def exit(self, exit_reason) -> None:
        self.output(exit_reason)
        sys.exit()
